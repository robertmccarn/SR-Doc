#!/usr/bin/env python3
"""Build a provenance-preserving SR-Doc chunk JSONL and SQLite FTS5 index."""
from __future__ import annotations
import argparse, hashlib, json, re, sqlite3, zipfile
from pathlib import PurePosixPath
from pathlib import Path

ARCHIVE_HASH = 'd1af0775d69def6ef442b66393e3ad84db66cb6b9ecf9138170573fdfe0a02c8'
CHUNK_TARGET = 1800
CHUNK_OVERLAP = 180

def norm(p): return str(PurePosixPath(str(p).replace('\\','/'))).lstrip('./')
def sha(b): return hashlib.sha256(b).hexdigest()
def load_jsonl(z, path):
    return [json.loads(x) for x in z.read(path.replace('/','\\')).splitlines() if x.strip()]
def heading_text(s):
    return re.sub(r"'{2,5}", '', re.sub(r'\[\[([^]|]+)(?:\|([^]]+))?\]\]', lambda m:m.group(2) or m.group(1), s)).strip()
def split_section(text, start, end, heading, base_meta):
    raw=text[start:end]
    if not raw.strip(): return []
    parts=[]; cursor=0
    while cursor < len(raw):
        hard=min(len(raw), cursor+CHUNK_TARGET)
        if hard < len(raw):
            cut=raw.rfind('\n\n', cursor+CHUNK_TARGET//2, hard)
            if cut <= cursor: cut=raw.rfind('\n', cursor+CHUNK_TARGET//2, hard)
            if cut <= cursor: cut=hard
        else: cut=len(raw)
        piece=raw[cursor:cut]
        if piece.strip():
            parts.append({**base_meta,'section_path':heading,'text':piece.strip(),'char_start':start+cursor,'char_end':start+cut})
        if cut>=len(raw): break
        cursor=max(cursor+1,cut-CHUNK_OVERLAP)
    return parts

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('archive'); ap.add_argument('--chunks',default='chunks.jsonl'); ap.add_argument('--db',default='srdoc_fts5.sqlite')
    ap.add_argument('--report',default='chunk-build-report.json'); ap.add_argument('--allow-unpinned-archive',action='store_true')
    a=ap.parse_args(); archive=Path(a.archive); archive_hash=sha(archive.read_bytes())
    if archive_hash != ARCHIVE_HASH and not a.allow_unpinned_archive: raise SystemExit(f'Archive hash mismatch: {archive_hash}')
    with zipfile.ZipFile(archive) as z:
        pages=json.loads(z.read('bronze\\manifests\\pages.json'))
        silver={str(x['page_id']):x for x in load_jsonl(z,'silver/pages.jsonl')}
        infos={norm(i.filename):i.filename for i in z.infolist()}
        chunks=[]; seen=set(); errors=[]
        for p in pages:
            pid=str(p['page_id']); s=silver.get(pid)
            if not s: errors.append(f'missing Silver page record {pid}'); continue
            path=norm(p['raw_path'])
            if path not in infos: errors.append(f'missing source {path}'); continue
            raw=z.read(infos[path]); actual=sha(raw)
            if actual != p.get('raw_sha256'): errors.append(f'hash mismatch {path}'); continue
            try: text=raw.decode('utf-8')
            except UnicodeDecodeError: errors.append(f'utf8 decode failure {path}'); continue
            headings=sorted(s.get('headings',[]),key=lambda h:int(h.get('offset',0)))
            starts=[(0,'(lead)')]
            for h in headings:
                off=int(h.get('offset',0))
                if 0 <= off < len(text): starts.append((off,heading_text(h.get('title','(untitled)'))))
            compact=[]
            for item in starts:
                if compact and compact[-1][0]==item[0]: compact[-1]=item
                else: compact.append(item)
            ns=p.get('namespace')
            cls='primary' if ns==0 else ('community' if ns in (1,2,3,1200,1201) else 'context')
            base={'page_id':pid,'title':p['title'],'namespace':ns,'revision_id':p.get('revision_id'),'parent_revision_id':p.get('parent_revision_id'),'timestamp':p.get('timestamp'),'source_path':path,'source_sha256':actual,'source_url':p.get('source_url'),'source_class':cls,'capture_id':archive_hash}
            for i,(start,heading) in enumerate(compact):
                end=compact[i+1][0] if i+1<len(compact) else len(text)
                for part in split_section(text,start,end,heading,base):
                    identity=f"{archive_hash}:{pid}:{part['char_start']}:{part['char_end']}"
                    part['chunk_id']=hashlib.sha256(identity.encode()).hexdigest()[:24]
                    if part['chunk_id'] in seen: errors.append(f'duplicate chunk id {part["chunk_id"]}')
                    seen.add(part['chunk_id']); chunks.append(part)
        if errors: raise SystemExit('Build failed:\n'+'\n'.join(errors[:30]))
    with open(a.chunks,'w',encoding='utf-8',newline='\n') as f:
        for row in chunks: f.write(json.dumps(row,ensure_ascii=False)+'\n')
    db=sqlite3.connect(a.db); db.execute('PRAGMA journal_mode=DELETE')
    db.executescript('DROP TABLE IF EXISTS pages; DROP TABLE IF EXISTS chunks; DROP TABLE IF EXISTS chunk_fts; CREATE TABLE pages(page_id TEXT PRIMARY KEY,title TEXT,namespace INTEGER,revision_id TEXT,parent_revision_id TEXT,timestamp TEXT,source_path TEXT,source_sha256 TEXT,source_url TEXT,redirect INTEGER,source_class TEXT); CREATE TABLE chunks(chunk_id TEXT PRIMARY KEY,page_id TEXT,title TEXT,namespace INTEGER,revision_id TEXT,timestamp TEXT,source_path TEXT,source_sha256 TEXT,source_url TEXT,source_class TEXT,capture_id TEXT,section_path TEXT,char_start INTEGER,char_end INTEGER,text TEXT); CREATE VIRTUAL TABLE chunk_fts USING fts5(chunk_id UNINDEXED,title,section_path,text, tokenize="unicode61 remove_diacritics 2");')
    page_rows=[]
    for p in pages:
        ns=p.get('namespace'); cls='primary' if ns==0 else ('community' if ns in (1,2,3,1200,1201) else 'context')
        page_rows.append((str(p['page_id']),p['title'],ns,str(p.get('revision_id')),str(p.get('parent_revision_id')),p.get('timestamp'),norm(p.get('raw_path','')),p.get('raw_sha256'),p.get('source_url'),int(bool(p.get('redirect'))),cls))
    db.executemany('INSERT INTO pages VALUES (?,?,?,?,?,?,?,?,?,?,?)',page_rows)
    rows=[(c['chunk_id'],c['page_id'],c['title'],c['namespace'],str(c['revision_id']),c['timestamp'],c['source_path'],c['source_sha256'],c['source_url'],c['source_class'],c['capture_id'],c['section_path'],c['char_start'],c['char_end'],c['text']) for c in chunks]
    db.executemany('INSERT INTO chunks VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',rows)
    db.executemany('INSERT INTO chunk_fts(chunk_id,title,section_path,text) VALUES (?,?,?,?)',[(c['chunk_id'],c['title'],c['section_path'],c['text']) for c in chunks])
    db.commit(); db.close()
    page_ids={c['page_id'] for c in chunks}
    report={'status':'PASS','archive_sha256':archive_hash,'page_records':len(pages),'silver_page_records':len(silver),'chunks':len(chunks),'unique_chunk_ids':len(seen),'pages_in_metadata_table':len(pages),'pages_with_text_chunks':len(page_ids),'pages_without_text_chunks_count':sum(str(p['page_id']) not in page_ids for p in pages),'main_namespace_pages_without_text_chunks':[{'page_id':str(p['page_id']),'title':p['title']} for p in pages if p.get('namespace')==0 and str(p['page_id']) not in page_ids],'namespace_counts':{},'fts5':'built','errors':[],'chunk_target_chars':CHUNK_TARGET,'chunk_overlap_chars':CHUNK_OVERLAP}
    for c in chunks: report['namespace_counts'][str(c['namespace'])]=report['namespace_counts'].get(str(c['namespace']),0)+1
    Path(a.report).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
if __name__=='__main__': main()
