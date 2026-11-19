---
page_id: 143
revision_id: 197
source_url: https://second-renaissance.fandom.com/wiki/Template%3AStart_infobox_page/doc
raw_sha256: 657d78b741c288776ac172b0af2f842e39d4367726fad465523052077d66a496
---

# Template:Start infobox page/doc

## Preserved source

```wikitext
{{documentation subpage}}<!--
<!---
  PLEASE ADD METADATA WITHIN THE <includeonly> SECTION AT THE BOTTOM OF THIS PAGE
  --->
This template and its sister {{tl|end infobox page}} are intended to facilitate the presentation of an infobox template and its documentation on the infobox template's own page. The documentation should be prepared as a {{tl|documentation}} page. This template then assigns it the lefthand side of the infobox template's page, while the infobox template itself appears on the righthand side of the page, using this code:
<pre>
{| style="width:100%; background:transparent;"
|- style="vertical-align:top;"
| <!-----Lefthand side: documentation----->
{{documentation}}
| <!-------Righthand side: template------->
</pre>

This template should be placed between <nowiki><noinclude> and </noinclude></nowiki> tags at the very top of an infobox template page, immediately before the start of the infobox's code thus:

<code><nowiki><noinclude>{{start infobox page}}</noinclude><!--</nowiki></code><br/>
<code><nowiki>--></nowiki>''infobox code starts here''</code>

The start and end-comment markers ("<code><nowiki><!--</nowiki></code>" and "<code><nowiki>--></nowiki></code>") are important as they remove the possibility of a spurious space appearing. The {{tl|end infobox page}} template should then be placed within <nowiki><noinclude> and </noinclude></nowiki> tags on the first line after the end of the template code. For an example, see [http://en.wikipedia.org/w/index.php?title=Template:Infobox_Machinima&action=edit Infobox Machinima].
```

## Provenance

Raw source: `bronze/pages/143/197.wikitext` · revision `197` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AStart_infobox_page/doc)
