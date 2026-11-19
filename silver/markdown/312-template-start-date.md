---
page_id: 312
revision_id: 483
source_url: https://second-renaissance.fandom.com/wiki/Template%3AStart_date
raw_sha256: 1522a188b959c97d6169deb6e9900223ddb952729e251e39d59974aaedf2309b
---

# Template:Start date

## Preserved source

```wikitext
<includeonly>{{#if: {{{4|}}}
  |{{#if: {{{5|}}}
     |{{padleft:{{{4}}}|2|0}}:{{padleft:{{{5}}}|2|0}}{{#if: {{{6|}}}
                                                   |&#58;{{padleft:{{{6}}}|2|0}} }},&#32;}} }}<!--ABOVE FOR TIME; BELOW FOR DATE
-->{{#if: {{{1|}}}
     |{{#if: {{{2|}}}
        |{{#if: {{{3|}}}
           |{{#if: {{{df|}}}|{{#expr:{{{3}}}}}&nbsp;{{MONTHNAME|{{{2}}}}}|{{MONTHNAME|{{{2}}}}}&nbsp;{{#expr:{{{3}}}}},}}&nbsp;{{{1}}}|{{MONTHNAME|{{{2}}}}}&nbsp;{{{1}}}}}|{{{1}}}}}}}{{#if: {{{7|}}}
              |&#32;({{#ifeq: {{{7}}}|Z|UTC|{{{7}}}}})}}<!-- BELOW FOR hCalendar
--><span style="display:none">&#160;(<span class="bday dtstart published updated">{{#if: {{{1|}}}
  | {{{1}}}{{#if: {{{2|}}}
     | -{{padleft:{{{2}}}|2|0}}{{#if: {{{3|}}}
        | -{{padleft:{{{3}}}|2|0}} }} }}<!--
-->{{#if: {{{4|}}}
     | T{{padleft:{{{4}}}|2|0}}{{#if: {{{5|}}}
        | &#58;{{padleft:{{{5}}}|2|0}}{{#if: {{{6|}}}
           | &#58;{{padleft:{{{6}}}|2|0}} }} }} }} }}{{{7|}}}</span>)</span></includeonly><noinclude>
{{documentation}}
</noinclude>
```

## Provenance

Raw source: `bronze/pages/312/483.wikitext` · revision `483` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AStart_date)
