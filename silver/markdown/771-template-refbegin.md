---
page_id: 771
revision_id: 1044
source_url: https://second-renaissance.fandom.com/wiki/Template%3ARefbegin
raw_sha256: 918dd4dcfc23ebd368e67c742e97ce4ffb1842af9a77eb3beb92ab449c3a954a
---

# Template:Refbegin

## Preserved source

```wikitext
<includeonly><div class="refbegin <!--
 -->{{#if: {{{normalfont|}}}
    | refbegin-100 }} <!--
 -->{{#if: {{{1|}}}
    | columns {{#iferror: {{#ifexpr: {{{1|1}}} > 1 }}
      | references-column-width 
      | references-column-count references-column-count-{{#if:1|{{{1}}}}} }}
    | {{#if: {{{colwidth|}}}
      | references-column-width }} }}" style="<!--
 -->{{#if: {{{1|}}}
    | {{#iferror: {{#ifexpr: {{{1|1}}} > 1 }}
      | {{column-width|{{#if:1|{{{1}}}}}}}
      | {{column-count|{{#if:1|{{{1}}}}}}} }}
    | {{#if: {{{colwidth|}}}
      | {{column-width|{{{colwidth}}}}} }} }}"><!--
 -->{{#if: {{{indent|}}}
    | <dl style="text-indent: -{{{indentsize|3.2}}}em;">}}<!--
 -->{{#if: {{{normalfont|}}}
    | [Category:Pages using refbegin with normalfont parameter](https://second-renaissance.fandom.com/wiki/Category:Pages_using_refbegin_with_normalfont_parameter)}}</includeonly><noinclude>
{{Documentation}}
{{/TemplateData}}
</noinclude>
```

## Provenance

Raw source: `bronze/pages/771/1044.wikitext` · revision `1044` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ARefbegin)
