---
page_id: 1621
revision_id: 3873
source_url: https://second-renaissance.fandom.com/wiki/Template%3AFossil_range/marker
raw_sha256: 64ef02a991a8d9c22f97d1a072467712060f984f0615f6186f27deb093a349c7
---

# Template:Fossil range/marker

## Preserved source

```wikitext
<includeonly><onlyinclude>{{#ifexpr:{{{1}}}-{{{2}}}>5|
<div style="position:absolute; height:8px; left:{{#expr:(650-{{{1}}})/650*220}}px; width:{{#expr:({{{1}}}-{{{2}}})*220/650}}px; background-color:#360; opacity:{{#if:{{{3|}}}|0.{{{3}}}|1}}; "><!--range-border--></div>
{{#if:{{{3|}}}||<div style="position:absolute; height:6px; top:1px; left:{{#expr:((650-{{{1}}})/650*220)+1}}px; width:{{#expr:(({{{1}}}-{{{2}}})*220/650)-2}}px; background-color:#6c3;"><!--range-marker--></div>}}
|<!--else-->
{{#if:{{{3|}}}||<div style="position:absolute; left:{{#expr:(650-{{{1}}})/650*220}}px; font-size:50%"><!--contains arrow--><div style="position:relative; left:-0.42em"><!--nudges back left-->&darr;</div></div>}}
}}</onlyinclude></includeonly><noinclude>
{{pp-template|small=yes}}
[Category:Template implementation details](https://second-renaissance.fandom.com/wiki/Category:Template_implementation_details)
[ar:قالب:Fossil range/marker](https://second-renaissance.fandom.com/wiki/ar:قالب:Fossil_range/marker)
[id:Templat:Rentang fosil/marka](https://second-renaissance.fandom.com/wiki/id:Templat:Rentang_fosil/marka)
[la:Formula:Fossil range/marker](https://second-renaissance.fandom.com/wiki/la:Formula:Fossil_range/marker)
[pl:Szablon:Okres istnienia grupy organizmów 2/znacznik](https://second-renaissance.fandom.com/wiki/pl:Szablon:Okres_istnienia_grupy_organizmów_2/znacznik)
</noinclude>
```

## Provenance

Raw source: `bronze/pages/1621/3873.wikitext` · revision `3873` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AFossil_range/marker)
