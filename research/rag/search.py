#!/usr/bin/env python3
"""Search SR-Doc FTS5 and emit a provenance-bearing evidence packet."""
import argparse, json, sqlite3

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('query',nargs='?',default='')
    ap.add_argument('--db',default='srdoc_fts5.sqlite')
    ap.add_argument('-k',type=int,default=8)
    ap.add_argument('--json',action='store_true')
    ap.add_argument('--page-id')
    a=ap.parse_args()
    terms=[x for x in a.query.replace('"',' ').split() if x]
    if not a.page_id and not terms: raise SystemExit('Provide query terms or --page-id')
    match=' OR '.join('"'+t.replace('"','')+'"' for t in terms)
    db=sqlite3.connect(a.db); db.row_factory=sqlite3.Row
    try:
        if a.page_id:
            rows=db.execute('SELECT *, 0.0 AS rank FROM chunks WHERE page_id=? ORDER BY char_start LIMIT ?', (str(a.page_id),max(1,min(a.k,200)))).fetchall()
            page=db.execute('SELECT * FROM pages WHERE page_id=?',(str(a.page_id),)).fetchone()
        else:
            rows=db.execute('''SELECT c.*, bm25(chunk_fts, 0.0, 2.0, 1.0, 1.0) AS rank
              FROM chunk_fts JOIN chunks c ON c.chunk_id=chunk_fts.chunk_id
              WHERE chunk_fts MATCH ? ORDER BY rank LIMIT ?''',(match,max(1,min(a.k,50)))).fetchall()
            page=None
    except sqlite3.OperationalError as e: raise SystemExit(f'FTS query error: {e}')
    evidence=[]
    for i,r in enumerate(rows,1):
        evidence.append({'evidence_id':f'E{i:02d}','source_class':r['source_class'],'page_id':r['page_id'],'title':r['title'],'namespace':r['namespace'],'revision_id':r['revision_id'],'source_path':r['source_path'],'capture_id':r['capture_id'],'content_sha256':r['source_sha256'],'section_path':[r['section_path']],'text':r['text'],'locator':f"chars {r['char_start']}–{r['char_end']}",'chunk_id':r['chunk_id'],'source_url':r['source_url'],'retrieval_rank':r['rank']})
    packet={'schema_version':'1.0','question':a.query or f'Fetch page ID {a.page_id}','resolved_entities':[dict(page)] if page else [],'retrieval':{'indexes_searched':['sqlite-fts5'] if not a.page_id else ['page-id lookup'],'corpus_snapshot':evidence[0]['capture_id'] if evidence else None,'warnings':[] if evidence else ['No matching passages found; this is not proof the information is absent.'],'query_mode':'OR lexical token match' if not a.page_id else 'exact page ID'},'evidence':evidence,'candidate_relationships':[],'contradiction_candidates':[],'unresolved_questions':[]}
    if a.json: print(json.dumps(packet,ensure_ascii=False,indent=2))
    else:
        print(f"{len(evidence)} passages retrieved")
        for e in evidence:
            print(f"\n[{e['evidence_id']}] {e['title']} (page_id={e['page_id']}, ns={e['namespace']}, rev={e['revision_id']})")
            print(f"Section: {e['section_path'][0]} | {e['locator']} | {e['source_path']}")
            print(e['text'][:1200])
    db.close()
if __name__=='__main__': main()
