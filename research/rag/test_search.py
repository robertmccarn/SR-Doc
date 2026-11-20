#!/usr/bin/env python3
"""Regression tests for SR-Doc lexical, title, and contrast retrieval."""
import json, subprocess, sys
SEARCH, DB = sys.argv[1], sys.argv[2]
def run(*args):
    p=subprocess.run([sys.executable, SEARCH, *args, "--db", DB, "--json"],capture_output=True,text=True)
    assert p.returncode == 0, p.stderr
    return json.loads(p.stdout)
p=run("--title","Second Chinese Civil War")
assert p["resolved_entities"][0]["page_id"] == "1413"
assert any("2027-2048" in e["date_signals"] and "2105-2111" in e["date_signals"] for e in p["evidence"])
p=run("Second Chinese Civil War 2027 2048 2105 2111","--contrast","-k","16")
assert any(e["page_id"] == "1413" for e in p["evidence"])
assert any(c["page_id"] == "1413" and c["comparison_status"] == "multiple_date_ranges_single_passage" for c in p["contradiction_candidates"])
assert any("does not determine" in w for w in p["retrieval"]["warnings"])
p=run("Talk Third Chinese Civil War")
assert all(e["namespace"] == 0 for e in p["evidence"])
p=run("Talk Third Chinese Civil War","--include-context")
assert any(e["namespace"] != 0 for e in p["evidence"])
print(json.dumps({"status":"PASS","tests":4,"checks":["exact title/page identity","intra-page date-range candidate","main namespace default","explicit context opt-in"]},indent=2))
