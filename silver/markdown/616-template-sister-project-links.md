---
page_id: 616
revision_id: 857
source_url: https://second-renaissance.fandom.com/wiki/Template%3ASister_project_links
raw_sha256: bd0be28f2a62beb247871a8f8dd81d6dfad3b75dd01996d8113ce2febc7eee1a
---

# Template:Sister project links

## Preserved source

```wikitext
<includeonly>{| class="metadata plainlinks mbox-small{{#ifeq:{{lc:{{{position|}}}}}|left|-left}} {{#if:{{{collapsible|}}}|mw-collapsible {{#ifeq:{{{collapsible|}}}|collapsed |mw-collapsed}}}}" style="padding:0.25em 0.5em 0.5em 0.75em;border:1px solid #aaa;background:#f9f9f9;{{{style|}}}"
|-
|colspan="2" style="padding-bottom:0.75em;border-bottom:1px solid #aaa;text-align:center;"| <div style="clear:both;">Find more about<br/>'''{{{display|{{{1|{{PAGENAME}}}}}}}}'''<br />at Wikipedia's [sister projects](https://second-renaissance.fandom.com/wiki/Wikipedia:Wikimedia_sister_projects) </div>
|- style="height:25px;"
{{#ifeq:{{{wikt|}}}|no |
 | {{!}}style="padding-top:0.75em;"{{!}} [25x25px|link={{fullurl:wikt:{{{wikt|Special:Search/{{{1|{{PAGENAME}}}}}}}}}}|Search Wiktionary](https://second-renaissance.fandom.com/wiki/File:Wiktionary-logo-en.svg)
   {{!}}style="padding-top:0.75em;"{{!}} [Special:Search/{{{1|{{PAGENAME}}}}}}}}|Definitions](https://second-renaissance.fandom.com/wiki/wikt:{{{wikt) from Wiktionary
}}
|- style="height:25px;"
{{#ifeq:{{{c|{{{commons|}}}}}}|no |
 | {{#ifeq:{{{commonscat|no}}}|yes
    | {{!}} [25x25px|link={{fullurl:c:Special:Search/Category:{{{c|{{{commons|{{{1|{{PAGENAME}}}}}}}}}}}}}|Search Commons](https://second-renaissance.fandom.com/wiki/File:Commons-logo.svg)
      {{!}} [{{{commons|{{{1|{{PAGENAME}}}}}}}}}}}|Media](https://second-renaissance.fandom.com/wiki/c:Special:Search/Category:{{{c) from Commons
    | {{!}} [25x25px|link={{fullurl:c:{{{c|{{{commons|Special:Search/{{{1|{{PAGENAME}}}}}}}}}}}}}|Search Commons](https://second-renaissance.fandom.com/wiki/File:Commons-logo.svg)
      {{!}} [{{{commons|Special:Search/{{{1|{{PAGENAME}}}}}}}}}}}|Media](https://second-renaissance.fandom.com/wiki/c:{{{c) from Commons
   }}
}}
|- style="height:25px;"
{{#ifeq:{{{n|}}}|no |
 | {{!}} [25x25px|link={{fullurl:n:Special:Search/{{{1|{{PAGENAME}}}}}}}|Search Wikinews](https://second-renaissance.fandom.com/wiki/File:Wikinews-logo.svg)
   {{!}} [{{PAGENAME}}}}}|News stories](https://second-renaissance.fandom.com/wiki/n:Special:Search/{{{1) from Wikinews
}}
|- style="height:25px;"
{{#ifeq:{{{q|}}}|no |
 | {{!}} [25x25px|link={{fullurl:q:{{{q|Special:Search/{{{1|{{PAGENAME}}}}}}}}}}|Search Wikiquote](https://second-renaissance.fandom.com/wiki/File:Wikiquote-logo.svg)
   {{!}} [Special:Search/{{{1|{{PAGENAME}}}}}}}}|Quotations](https://second-renaissance.fandom.com/wiki/q:{{{q) from Wikiquote
}}
|- style="height:25px;"
{{#ifeq:{{{s|}}}|no |
 | {{#ifeq:{{{author|no}}}|yes
    | {{!}} [25x25px|link={{fullurl:s:Special:Search/Author:{{{s|{{{1|{{PAGENAME}}}}}}}}}}|Search Wikisource](https://second-renaissance.fandom.com/wiki/File:Wikisource-logo.svg)
      {{!}} [{{{1|{{PAGENAME}}}}}}}}|Source texts](https://second-renaissance.fandom.com/wiki/s:Special:Search/Author:{{{s) from Wikisource
    | {{!}} [25x25px|link={{fullurl:s:{{{s|Special:Search/{{{1|{{PAGENAME}}}}}}}}}}|Search Wikisource](https://second-renaissance.fandom.com/wiki/File:Wikisource-logo.svg)
      {{!}} [Special:Search/{{{1|{{PAGENAME}}}}}}}}|Source texts](https://second-renaissance.fandom.com/wiki/s:{{{s) from Wikisource
   }}
}}
|- style="height:25px;"
{{#ifeq:{{{b|}}}|no |
 | {{!}} [25x25px|link={{fullurl:b:{{{b|Special:Search/{{{1|{{PAGENAME}}}}}}}}}}|Search Wikibooks](https://second-renaissance.fandom.com/wiki/File:Wikibooks-logo.svg)
   {{!}} [Special:Search/{{{1|{{PAGENAME}}}}}}}}|Textbooks](https://second-renaissance.fandom.com/wiki/b:{{{b) from Wikibooks
}}
|- style="height:25px;"
{{#ifeq:
   <!-- Show Wikivoyage if the "voy" parameter is anything other than blank, empty or "no" -->
   {{#switch: {{{voy|<noinclude>yes</noinclude>}}}
    | | no     = false
    | #default = true
   }}
 | true
 | {{!}} [25x25px|link={{fullurl:voy:{{{voy|Special:Search/{{{1|{{PAGENAME}}}}}}}}}}|Search Wikivoyage](https://second-renaissance.fandom.com/wiki/File:Wikivoyage-Logo-v3-icon.svg)
   {{!}} [Special:Search/{{{1|{{PAGENAME}}}}}}}}|Travel {{#if: {{{voy|}}}| guide| information}}](https://second-renaissance.fandom.com/wiki/voy:{{{voy) from Wikivoyage
}}
|- style="height:25px;"
{{#ifeq:{{{v|}}}|no |
 | {{!}} [25x25px|link={{fullurl:v:{{{v|Special:Search/{{{1|{{PAGENAME}}}}}}}}}}|Search Wikiversity](https://second-renaissance.fandom.com/wiki/File:Wikiversity-logo-Snorky.svg)
   {{!}} [Special:Search/{{{1|{{PAGENAME}}}}}}}}|Learning resources](https://second-renaissance.fandom.com/wiki/v:{{{v) from Wikiversity
}}
|- style="height:25px;"
{{#ifeq:{{{d|no}}}|no |
 | {{!}} [25x25px|link={{fullurl:d:{{{d<noinclude>|Special:ItemByTitle/enwiki/{{{1|{{PAGENAME}}}}}</noinclude>}}}}}|Search Wikidata](https://second-renaissance.fandom.com/wiki/File:Wikidata-logo.svg)
   {{!}} [{{{1|Special:ItemByTitle/enwiki/{{PAGENAME}}}}}</noinclude>}}}|Database entry {{ucfirst:{{{d<noinclude>|</noinclude>}}}}}](https://second-renaissance.fandom.com/wiki/d:{{{d<noinclude>) on Wikidata
}}
|- style="height:25px;"
{{#ifeq:{{{species|no}}}|no |
 | {{!}} [25x25px|link={{fullurl:species:{{{species<noinclude>|Special:Search/{{{1|{{PAGENAME}}}}}</noinclude>}}}}}|Search Wikispecies](https://second-renaissance.fandom.com/wiki/File:Wikispecies-logo.svg)
   {{!}} [Special:Search/{{{1|{{PAGENAME}}}}}</noinclude>}}}|Taxonomy of {{{species<noinclude>|</noinclude>}}}](https://second-renaissance.fandom.com/wiki/species:{{{species<noinclude>) from Wikispecies
}}
|- style="height:25px;"
{{#ifeq:{{{species_author|no}}}|no |
 | {{!}} [25x25px|link={{fullurl:species:{{{species_author<noinclude>|Special:Search/{{{1|{{PAGENAME}}}}}</noinclude>}}}}}|Search Wikispecies](https://second-renaissance.fandom.com/wiki/File:Wikispecies-logo.svg)
   {{!}} [Special:Search/{{{1|{{PAGENAME}}}}}</noinclude>}}}|Species author{{{species_author<noinclude>|</noinclude>}}}](https://second-renaissance.fandom.com/wiki/species:{{{species_author<noinclude>) on Wikispecies
}}
|- style="height:25px;"
{{#if:{{{m|}}}|
 {{#switch:{{lc:{{{m}}}}}
   |yes = {{!}}<noinclude>|</noinclude> [25x25px|link={{fullurl:n:Special:Search/{{{1|{{PAGENAME}}}}}}}|Search Meta-Wiki](https://second-renaissance.fandom.com/wiki/File:Wikimedia_Community_Logo.svg)
   {{!}}<noinclude>|</noinclude> [{{PAGENAME}}}}}|Discussion](https://second-renaissance.fandom.com/wiki/m:Special:Search/{{{1) from Meta-Wiki
   |no =
   |{{!}} [25x25px|link={{fullurl:m:{{{m}}}}}|Search Meta-Wiki](https://second-renaissance.fandom.com/wiki/File:Wikimedia_Community_Logo.svg)
   {{!}} [Discussion](https://second-renaissance.fandom.com/wiki/m:{{{m}}}) from Meta-Wiki
 }}
}}
|- style="height:25px;"
{{#ifeq:{{{mw|no}}}|no |
 | {{!}} [25x25px|link={{fullurl:mw:{{{mw<noinclude>|Special:Search/{{{1|{{PAGENAME}}}}}</noinclude>}}}}}|Search MediaWiki](https://second-renaissance.fandom.com/wiki/File:MediaWiki-logo.svg)
   {{!}} [Special:Search/{{{1|{{PAGENAME}}}}}</noinclude>}}}|Documentation on {{{mw<noinclude>|</noinclude>}}}](https://second-renaissance.fandom.com/wiki/mw:{{{mw<noinclude>) from MediaWiki
}}
|}</includeonly><noinclude>
{{Documentation}}
</noinclude>
```

## Provenance

Raw source: `bronze/pages/616/857.wikitext` · revision `857` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ASister_project_links)
