---
page_id: 867
revision_id: 1186
source_url: https://second-renaissance.fandom.com/wiki/Template%3ADts/testcases/row
raw_sha256: 786959110480c1eb48584eadc4eab82fbdbd502bd08cd55db5713755503faa19
---

# Template:Dts/testcases/row

## Preserved source

```wikitext
<noinclude>{|class=wikitable
</noinclude>|-
{{#if:{{{a|}}}|
{{!}} style="vertical-align:top;" rowspan={{{span|1}}}{{!}}{{{a}}}{{!}}
}}{{#if:{{{b|}}}|
{{!}} style="vertical-align:top;" rowspan={{{span|1}}}{{!}}{{{b}}}{{!}}
}}|<code><nowiki>{{dts</nowiki>{{#if:{{{4|}}}
   |&#124;{{{1|}}}&#124;{{{2|}}}&#124;{{{3|}}}&#124;{{{4}}}
   |{{#if:{{{3|}}}
      |&#124;{{{1|}}}&#124;{{{2|}}}&#124;{{{3}}}
      |{{#if:{{{2|}}}
         |&#124;{{{1|}}}&#124;{{{2}}}
         |{{#if:{{{1|<noinclude>X</noinclude>}}}
            |&#124;{{{1|{{#time:j M Y}}}}}
          }}
       }}
    }}
 }}{{#if:{{{format|}}}
   |&#124;format={{{format|}}}
 }}{{#if:{{{abbr|}}}
   |&#124;abbr={{{abbr|}}}
 }}{{#if:{{{addkey|}}}
   |&#124;addkey={{{addkey|}}}
 }}}}</code>
{{#if:{{{test|}}}
   |{{dts/testcases/colour
      |{{dts
         |{{{1|<noinclude>{{#time:j M Y}}</noinclude>}}}|{{{2|}}}|{{{3|}}}|{{{4|}}}|debug=yes
         |abbr={{{abbr|}}}|addkey={{{addkey|}}}|format={{{format|}}}
       }}
      |{{dts/sandbox
         |{{{1|<noinclude>{{#time:j M Y}}</noinclude>}}}|{{{2|}}}|{{{3|}}}|{{{4|}}}|debug=yes
         |abbr={{{abbr|}}}|addkey={{{addkey|}}}|format={{{format|}}}
      }}
    }}
   |{{!}}{{dts
      |{{{1|<noinclude>{{#time:j M Y}}</noinclude>}}}|{{{2|}}}|{{{3|}}}|{{{4|}}}|debug=yes
      |abbr={{{abbr|}}}|addkey={{{addkey|}}}|format=hide
    }}{{!}}{{!}}{{dts
      |{{{1|<noinclude>{{#time:j M Y}}</noinclude>}}}|{{{2|}}}|{{{3|}}}|{{{4|}}}
      |abbr={{{abbr|}}}|addkey={{{addkey|}}}|format={{{format|}}}
    }}
 }}<noinclude>
|}</noinclude>
```

## Provenance

Raw source: `bronze/pages/867/1186.wikitext` · revision `1186` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ADts/testcases/row)
