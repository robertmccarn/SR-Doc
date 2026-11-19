---
page_id: 207
revision_id: 265
source_url: https://second-renaissance.fandom.com/wiki/Template%3ABartable
raw_sha256: 21546144a83eeeca5ae1f2f815b6fc49ac0ee9111d868cd6b1de3f724a591c5b
---

# Template:Bartable

## Preserved source

```wikitext
<includeonly>{{#if:{{{2|}}} | {{#if:{{#titleparts:{{{2}}}|1|2}}|{{#if:{{#titleparts:{{{2}}}|1|1}}|{{{1}}}{{{2}}}|{{convert|{{{1}}}|{{#titleparts:{{{2}}}|1|2}}|{{#titleparts:{{{2}}}|1|3}}|{{#titleparts:{{{2}}}|1|4}}|abbr=on}} }}|{{{1}}}{{{2}}} }} | {{{1|&mdash;}}} }} {{#ifexpr:{{#if:{{{3|}}}|{{{3}}}|0}}<0 | {{!}}{{!}} {{#ifexpr:{{formatnum:{{{1|0}}}|R}}<0 | align="right" {{!}} <div style="width:{{#expr:-abs({{#if:{{{3|}}}|{{{3}}}|1}})*{{formatnum:{{{1}}}|R}} }}px;height:{{#if:{{{4|}}}|{{{4}}}|2ex}};background:#aaa;{{{5|}}}">&nbsp;</div>|}} | }}
| {{#ifexpr:{{formatnum:{{{1|0}}}|R}}>0 | align="left" {{!}} <span style="display:none;">{{#expr:{{formatnum:{{{1}}}|R}} }}</span><div style="width:{{#expr:abs({{#if:{{{3|}}}|{{{3}}}|1}})*{{formatnum:{{{1}}}|R}} }}px;height:{{#if:{{{4|}}}|{{{4}}}|2ex}};background:#aaa;{{{5|}}}">&nbsp;</div>|}}</includeonly><noinclude>{{Documentation}}</noinclude>
```

## Provenance

Raw source: `bronze/pages/207/265.wikitext` · revision `265` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ABartable)
