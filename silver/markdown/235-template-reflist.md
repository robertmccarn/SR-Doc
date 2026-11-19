---
page_id: 235
revision_id: 314
source_url: https://second-renaissance.fandom.com/wiki/Template%3AReflist
raw_sha256: 03cf5e9f06a797c5c5e18028b1d2fcf62d9f905430355adf155b72ab22d31d69
---

# Template:Reflist

## Preserved source

```wikitext
<div class="reflist <!--
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
      | {{column-width|{{{colwidth}}}}} }} }} list-style-type: <!--
 -->{{{liststyle|{{#switch: {{{group|}}}
    | upper-alpha
    | upper-roman
    | lower-alpha
    | lower-greek
    | lower-roman = {{{group}}}
    | #default = decimal}}}}};">
{{#tag:references|{{{refs|}}}|group={{{group|}}}}}</div><noinclude>
{{Documentation}}
</noinclude>
```

## Provenance

Raw source: `bronze/pages/235/314.wikitext` · revision `314` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AReflist)
