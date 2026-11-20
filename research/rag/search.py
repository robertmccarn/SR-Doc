#!/usr/bin/env python3
"""Search SR-Doc FTS5 and emit provenance-bearing evidence packets."""
import argparse, json, re, sqlite3

DATE_RE = re.compile(
    r"(?<!\d)(?:(?:1[0-9]{3}|20[0-9]{2}|21[0-9]{2})(?:\s*[-–—]\s*(?:1[0-9]{3}|20[0-9]{2}|21[0-9]{2}))?|(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+(?:1[0-9]{3}|20[0-9]{2}|21[0-9]{2}))"
)
def title_key(value):
    return re.sub(r"\s+", " ", value.replace("_", " ").strip()).casefold()
def date_signals(text):
    found=[]
    for m in DATE_RE.finditer(text):
        value=re.sub(r"\s+", "", m.group(0)).replace("—","-").replace("–","-")
        if value not in found: found.append(value)
    return found
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("query",nargs="?",default="")
    ap.add_argument("--db",default="srdoc_fts5.sqlite")
    ap.add_argument("-k",type=int,default=8)
    ap.add_argument("--json",action="store_true")
    ap.add_argument("--page-id")
    ap.add_argument("--title")
    ap.add_argument("--include-context",action="store_true")
    ap.add_argument("--contrast",action="store_true",help="retrieve diversified date-bearing comparison candidates; does not adjudicate contradictions")
    a=ap.parse_args()
    if a.page_id and a.title: raise SystemExit("Use only one of --page-id or --title")
    if a.contrast and (a.page_id or a.title): raise SystemExit("--contrast is available with lexical queries only")
    terms=[x for x in a.query.replace('"'," ").split() if x]
    if not a.page_id and not a.title and not terms: raise SystemExit("Provide query terms, --page-id, or --title")
    match=" OR ".join('"'+t.replace('"',"")+'"' for t in terms)
    db=sqlite3.connect(a.db); db.row_factory=sqlite3.Row
    resolved=[]; warnings=[]; mode="OR lexical token match"; contradiction_candidates=[]
    try:
        if a.page_id:
            page=db.execute("SELECT * FROM pages WHERE page_id=?",(str(a.page_id),)).fetchone()
            rows=db.execute("SELECT *,0.0 AS rank FROM chunks WHERE page_id=? ORDER BY char_start LIMIT ?",(str(a.page_id),max(1,min(a.k,200)))).fetchall()
            mode="exact page ID"
            if page: resolved=[{"page_id":page["page_id"],"title":page["title"],"resolution_status":"exact"}]
            else: warnings.append("Page ID not present in the indexed snapshot.")
        elif a.title:
            matches=db.execute("SELECT * FROM title_keys WHERE title_key=? ORDER BY page_id",(title_key(a.title),)).fetchall()
            unique={r["page_id"]:r for r in matches}; rows=[]
            if len(unique)>1:
                warnings.append("Title is ambiguous in the captured corpus; no page was selected.")
                resolved=[{"page_id":r["page_id"],"title":r["title"],"resolution_status":"ambiguous_exact_title"} for r in unique.values()]
                mode="exact title lookup (ambiguous)"
            elif len(unique)==1:
                alias=next(iter(unique.values()))
                if alias["target_page_id"]:
                    target=db.execute("SELECT * FROM pages WHERE page_id=?",(alias["target_page_id"],)).fetchone()
                    if target:
                        rows=db.execute("SELECT *,0.0 AS rank FROM chunks WHERE page_id=? ORDER BY char_start LIMIT ?",(target["page_id"],max(1,min(a.k,200)))).fetchall()
                        resolved=[{"page_id":target["page_id"],"title":target["title"],"resolution_status":"redirect_target","via_page_id":alias["page_id"],"via_title":alias["title"],"redirect_target_title":alias["redirect_target_title"]}]
                        mode="title lookup via captured redirect"
                        if target["namespace"] != 0: warnings.append("Resolved page is outside the main namespace; treat it as context/metadata, not automatic lore evidence.")
                    else: warnings.append("Redirect target page ID is absent; no canonical substitution made.")
                else:
                    rows=db.execute("SELECT *,0.0 AS rank FROM chunks WHERE page_id=? ORDER BY char_start LIMIT ?",(alias["page_id"],max(1,min(a.k,200)))).fetchall()
                    resolved=[{"page_id":alias["page_id"],"title":alias["title"],"resolution_status":"exact_title"}]
                    mode="exact title lookup"
                    if alias["is_redirect"]: warnings.append("Page is marked as redirect, but its target syntax could not be resolved; original page identity retained.")
                    if alias["namespace"] != 0: warnings.append("Resolved page is outside the main namespace; treat it as context/metadata, not automatic lore evidence.")
            else:
                warnings.append("No exact title or captured redirect alias matched. No fuzzy identity merge is performed.")
                mode="exact title lookup (not found)"
        else:
            limit=max(50,min(a.k*12,240)) if a.contrast else max(1,min(a.k,50))
            rows=db.execute("""SELECT c.*,bm25(chunk_fts,0.0,2.0,1.0,1.0) AS rank FROM chunk_fts JOIN chunks c ON c.chunk_id=chunk_fts.chunk_id WHERE chunk_fts MATCH ? AND (? OR c.namespace=0) ORDER BY rank LIMIT ?""",(match,int(a.include_context),limit)).fetchall()
            if a.contrast: mode="contrast candidate retrieval (diversified lexical OR)"
        if a.contrast:
            selected=[]; seen_chunks=set(); seen_pages=set()
            for r in rows:
                if r["page_id"] not in seen_pages:
                    selected.append(r); seen_pages.add(r["page_id"]); seen_chunks.add(r["chunk_id"])
            for r in rows:
                if r["chunk_id"] not in seen_chunks and date_signals(r["text"]):
                    selected.append(r); seen_chunks.add(r["chunk_id"])
                if len(selected)>=max(1,min(a.k,40)): break
            rows=selected[:max(1,min(a.k,40))]
        evidence=[]
        for i,r in enumerate(rows,1):
            evidence.append({"evidence_id":f"E{i:02d}","source_class":r["source_class"],"page_id":r["page_id"],"title":r["title"],"namespace":r["namespace"],"revision_id":r["revision_id"],"source_path":r["source_path"],"capture_id":r["capture_id"],"content_sha256":r["source_sha256"],"section_path":[r["section_path"]],"text":r["text"],"locator":f"chars {r['char_start']}–{r['char_end']}","chunk_id":r["chunk_id"],"source_url":r["source_url"],"retrieval_rank":r["rank"],"date_signals":date_signals(r["text"])})
        if not evidence and not warnings: warnings.append("No matching passages found; this is not proof the information is absent.")
        if a.contrast:
            dated=[e for e in evidence if e["date_signals"]]
            for e in dated:
                ranges=[d for d in e["date_signals"] if re.fullmatch(r"(?:1[0-9]{3}|20[0-9]{2}|21[0-9]{2})-(?:1[0-9]{3}|20[0-9]{2}|21[0-9]{2})",d)]
                if len(ranges)>1:
                    contradiction_candidates.append({"candidate_id":f"CC{len(contradiction_candidates)+1:02d}","evidence_ids":[e["evidence_id"]],"page_id":e["page_id"],"title":e["title"],"date_signals":ranges,"comparison_status":"multiple_date_ranges_single_passage","reason":"One passage contains multiple distinct year ranges; inspect labels and context before classifying them as incompatible."})
            by_page={}
            for e in dated: by_page.setdefault(e["page_id"],[]).append(e)
            for pid,items in by_page.items():
                signals=sorted({d for e in items for d in e["date_signals"]})
                if len(items)>1 and len(signals)>1:
                    contradiction_candidates.append({"candidate_id":f"CC{len(contradiction_candidates)+1:02d}","evidence_ids":[e["evidence_id"] for e in items],"page_id":pid,"title":items[0]["title"],"date_signals":signals,"comparison_status":"intra_page_date_variance","reason":"Multiple date-bearing passages from one captured page; inspect context and field semantics before classifying."})
            warnings.append("Contrast mode retrieves date-bearing comparison candidates only. It does not determine whether claims are semantically incompatible or which source is correct.")
        indexes=["title/redirect index","page/chunk index"] if a.title else (["page-id lookup"] if a.page_id else (["sqlite-fts5-all-namespaces"] if a.include_context else ["sqlite-fts5-main-namespace"]))
        packet={"schema_version":"1.0","question":a.query or (f"Fetch page ID {a.page_id}" if a.page_id else f"Resolve title {a.title}"),"resolved_entities":resolved,"retrieval":{"indexes_searched":indexes,"corpus_snapshot":evidence[0]["capture_id"] if evidence else None,"warnings":warnings,"query_mode":mode},"evidence":evidence,"candidate_relationships":[],"contradiction_candidates":contradiction_candidates,"unresolved_questions":[]}
        if a.json: print(json.dumps(packet,ensure_ascii=False,indent=2))
        else:
            print(f"{len(evidence)} passages retrieved; {mode}")
            for x in resolved: print("Resolved:",x)
            for x in warnings: print("Warning:",x)
            for e in evidence: print(f"\n[{e['evidence_id']}] {e['title']} (page_id={e['page_id']}, ns={e['namespace']}) | {e['section_path'][0]} | dates={e['date_signals']}\n{e['text'][:1200]}")
            if contradiction_candidates: print("\nComparison candidates:",json.dumps(contradiction_candidates,ensure_ascii=False,indent=2))
    except sqlite3.OperationalError as e: raise SystemExit(f"Index/query error: {e}")
    finally: db.close()
if __name__=="__main__": main()
