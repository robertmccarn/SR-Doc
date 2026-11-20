#!/usr/bin/env python3
"""Extract conservative semantic edges from recognized raw-Wikitext infoboxes."""
import argparse,json,re,zipfile,collections
MAPPINGS={
"Infobox officeholder":{"predecessor":"SUCCEEDED","successor":"PRECEDED_BY","party":"MEMBER_OF","office":"HOLDS_OFFICE_IN","country":"ASSOCIATED_WITH_STATE","leader":"LEADS","president":"LEADS","prime minister":"LEADS","primeminister":"LEADS","governor":"LEADS"},
"Infobox Military Conflict":{"partof":"PART_OF_CONFLICT","place":"TAKES_PLACE_IN","causes":"HAS_STATED_CAUSE","result":"HAS_STATED_RESULT","combatant1":"HAS_COMBATANT","combatant2":"HAS_COMBATANT","combatant3":"HAS_COMBATANT","commander1":"HAS_COMMANDER","commander2":"HAS_COMMANDER","commander3":"HAS_COMMANDER"},
"Infobox country":{"capital":"HAS_CAPITAL","largest_city":"HAS_LARGEST_CITY","leader_name":"LED_BY","currency":"USES_CURRENCY","official_language":"USES_LANGUAGE"},
"Infobox former country":{"capital":"HAS_CAPITAL","largest_city":"HAS_LARGEST_CITY","leader_name":"LED_BY","currency":"USES_CURRENCY","official_language":"USES_LANGUAGE"},
"Infobox political party":{"leader":"LED_BY","founder":"FOUNDED_BY","ideology":"HAS_IDEOLOGY","headquarters":"HEADQUARTERED_IN"}}
NON_ENTITY_NS={"file","image","category","special","wikipedia","template","module"}
def split_top(s,sep="|"):
 out=[];start=0;tpl=link=i=0
 while i<len(s):
  if s.startswith("{{",i):tpl+=1;i+=2;continue
  if s.startswith("}}",i) and tpl:tpl-=1;i+=2;continue
  if s.startswith("[[",i):link+=1;i+=2;continue
  if s.startswith("]]",i) and link:link-=1;i+=2;continue
  if s[i]==sep and tpl==0 and link==0:out.append(s[start:i]);start=i+1
  i+=1
 out.append(s[start:]);return out
def templates(s):
 i=0; known={x.casefold() for x in MAPPINGS}
 while i<len(s)-1:
  if not s.startswith("{{",i):i+=1;continue
  st=i;d=1;j=i+2
  while j<len(s)-1 and d:
   if s.startswith("{{",j):d+=1;j+=2
   elif s.startswith("}}",j):d-=1;j+=2
   else:j+=1
  if d:return
  body=s[st+2:j-2];name=split_top(body)[0].strip()
  if name.casefold() in known:yield name,body
  i=st+2
def params(body):
 out={}
 for part in split_top(body)[1:]:
  pair=split_top(part,"=")
  if len(pair)>1:out[pair[0].strip().casefold()]="=".join(pair[1:]).strip()
 return out
def links(v):
 for m in re.finditer(r"\[\[([^\]]+)\]\]",v):yield m.group(1).split("|",1)[0].split("#",1)[0].strip()
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--archive",required=True);ap.add_argument("--graph",required=True);ap.add_argument("--out",required=True);a=ap.parse_args()
 graph=json.load(open(a.graph,encoding="utf-8"))
 with zipfile.ZipFile(a.archive) as z:
  pages=[json.loads(x) for x in z.read("silver/pages.jsonl").decode().splitlines() if x.strip()]
  title={p["title"].replace("_"," ").strip().casefold():p for p in pages}
  entities={n["page_id"]:n["id"] for n in graph["nodes"] if n.get("page_id") is not None}
  existing={(e["source"],e["predicate"],e["target"],e.get("evidence",{}).get("field")) for e in graph["edges"] if e["predicate"] not in ("WIKI_LINKS_TO","MENTIONS_YEAR")}
  additions=[];counts=collections.Counter();excluded=collections.Counter()
  for p in pages:
   if p["namespace"]!=0:continue
   raw=z.read(p["raw_path"]).decode("utf-8",errors="replace")
   for name,body in templates(raw):
    mapping=next(v for k,v in MAPPINGS.items() if k.casefold()==name.casefold())
    for field,pred in mapping.items():
     value=params(body).get(field)
     if not value:continue
     for ix,target in enumerate(links(value)):
      if target.split(":",1)[0].casefold() in NON_ENTITY_NS:excluded["non_entity_namespace"]+=1;continue
      tp=title.get(target.replace("_"," ").strip().casefold())
      if not tp:excluded["unresolved_title"]+=1;continue
      src=entities.get(p["page_id"]);dst=entities.get(tp["page_id"])
      if not src or not dst:excluded["no_entity_node"]+=1;continue
      key=(src,pred,dst,field)
      if key in existing:excluded["already_present"]+=1;continue
      eid=f"infobox-v2:{p['page_id']}:{field}:{ix}:{tp['page_id']}"
      inv={"SUCCEEDED":"PRECEDED_BY","PRECEDED_BY":"SUCCEEDED"}.get(pred,f"INVERSE_OF_{pred}")
      additions.append({"id":eid,"source":src,"predicate":pred,"target":dst,"bidirectional":False,"inverse_predicate":inv,"temporal_scope":None,"certainty":"explicit_infobox_field","evidence_strength":"structured_source_claim","evidence":{"source_path":p["raw_path"],"source_page_id":p["page_id"],"source_title":p["title"],"revision_id":p["revision_id"],"template":name,"field":field,"raw_value":value,"target_title":target,"target_page_id":tp["page_id"],"target_source_path":tp["raw_path"]},"weight":0.9})
      existing.add(key);counts[pred]+=1
 graph["edges"].extend(additions);graph["edges"].sort(key=lambda e:e["id"]);ids={n["id"] for n in graph["nodes"]}
 report={"new_edges":len(additions),"by_predicate":dict(counts),"excluded":dict(excluded),"nodes":len(graph["nodes"]),"edges":len(graph["edges"]),"semantic_infobox_edges":sum(e["predicate"] not in ("WIKI_LINKS_TO","MENTIONS_YEAR") for e in graph["edges"]),"unique_edge_ids":len({e["id"] for e in graph["edges"]})==len(graph["edges"]),"all_endpoints_resolve":all(e["source"] in ids and e["target"] in ids for e in graph["edges"])}
 json.dump(graph,open(a.out,"w",encoding="utf-8"),ensure_ascii=False,indent=2);print(json.dumps(report,indent=2))
 if not report["unique_edge_ids"] or not report["all_endpoints_resolve"]:raise SystemExit(1)
if __name__=="__main__":main()
