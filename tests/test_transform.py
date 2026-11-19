from sr_doc.transform import slug
from sr_doc.wiki import shell

def test_slug_is_stable():
    assert slug("A State of Merit") == "a-state-of-merit"


def test_root_wiki_shell_uses_root_assets():
    document = shell("Home", "content")
    assert 'href="assets/wiki.css"' in document
    assert 'href="index.html"' in document
