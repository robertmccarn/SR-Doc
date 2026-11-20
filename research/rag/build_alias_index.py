#!/usr/bin/env python3
"""Add exact-title and explicit Wikitext redirect mappings to an existing SR-Doc index."""
import argparse, json, re, sqlite3, zipfile
from pathlib import PurePosixPath

def title_key(value):
    return re.sub(r"\\s+", " ", value.replace("_", " ").strip()).casefold()

def archive_key(value):
    return str(PurePosixPath(str(value).replace("\\\\", "/"))).lstrip("./")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("archive")
    ap.add_argument("--db", default="srdoc_fts5.sqlite")
    a=ap.parse_args()
    db=sqlite3.connect(a.db); db.row_factory=sqlite3.Row
    try:
        if not db.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='pages'").fetchone():
            raise SystemExit("Index has no pages table; build the base FTS5 index first.")
        pages={r["page_id"]:dict(r) for r in db.execute("SELECT * FROM pages")}
        with zipfile.ZipFile(a.archive) as z:
            manifest=json.loads(z.read("bronze\\\\manifests\\\\pages.json"))
            raw_by_id={str(x["page_id"]):x for x in manifest}
            infos={archive_key(i.filename):i.filename for i in z.infolist()}
            title_to_ids={}
            for p in pages.values():
                title_to_ids.setdefault(title_key(p["title"]),[]).append(p["page_id"])
            rows=[]
            for pid,p in pages.items():
                redirect=bool(p["redirect"])
                target_title=None; target_id=None; status="exact_title"
                if redirect:
                    record=raw_by_id.get(pid)
                    if record:
                        source=infos.get(archive_key(record["raw_path"]))
                        if source:
                            raw=z.read(source).decode("utf-8","replace")
                            hit=re.search(r"^\\s*#redirect\\s*\\[\\[([^]|]+)(?:\\|[^]]*)?\\]\\]",raw,re.I|re.M)
                            if hit:
                                target_title=hit.group(1).strip()
                                ids=title_to_ids.get(title_key(target_title),[])
                                if len(ids)==1:
                                    target_id=ids[0]; status="resolved_redirect"
                                elif len(ids)>1: status="ambiguous_redirect_target"
                                else: status="unresolved_redirect_target"
                            else: status="redirect_syntax_not_parsed"
                        else: status="redirect_source_missing"
                    else: status="redirect_manifest_record_missing"
                rows.append((title_key(p["title"]),p["title"],pid,p["title"],p["namespace"],int(redirect),target_title,target_id,status))
        db.executescript("DROP TABLE IF EXISTS title_keys; CREATE TABLE title_keys(title_key TEXT NOT NULL, alias_title TEXT NOT NULL, page_id TEXT NOT NULL, title TEXT NOT NULL, namespace INTEGER, is_redirect INTEGER NOT NULL, redirect_target_title TEXT, target_page_id TEXT, resolution_status TEXT NOT NULL, PRIMARY KEY(title_key,page_id)); CREATE INDEX title_keys_page_id ON title_keys(page_id);")
        db.executemany("INSERT INTO title_keys VALUES (?,?,?,?,?,?,?,?,?)",rows)
        db.commit()
        stats={r["resolution_status"]:r["n"] for r in db.execute("SELECT resolution_status,COUNT(*) n FROM title_keys GROUP BY resolution_status")}
        print(json.dumps({"status":"PASS","title_key_rows":len(rows),"distinct_normalized_titles":len(set(r[0] for r in rows)),"redirect_status_counts":stats},indent=2))
    finally: db.close()
if __name__=="__main__": main()
