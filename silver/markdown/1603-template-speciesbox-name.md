---
page_id: 1603
revision_id: 3855
source_url: https://second-renaissance.fandom.com/wiki/Template%3ASpeciesbox/name
raw_sha256: d0b4ac46edf063bfd5f83b36036732ead4b2c8d8e29f76c2313e5c19a33f8127
---

# Template:Speciesbox/name

## Preserved source

```wikitext
<noinclude>{{pp-template|small=yes}}</noinclude><noinclude><!--Parameters: 1=name, 2=taxon, 3=genus, 4=species, 5=PAGENAMEBASE, 6=italic_title (obey no)
--></noinclude><includeonly>{{#switch:{{{5}}}
|{{{2|}}}
|{{Str letter/trim|{{{3|}}}}} {{{4|}}}
|{{Str letter/trim|{{{2|}}}}}
|{{Str letter/trim|{{{3|}}}}}={{#ifeq:{{{6|yes}}}|no||{{italic title}}}}{{#if:{{{1|}}}|{{{1}}}|''{{{5}}}''}}
|#default={{#if:{{{1|}}}|{{{1}}}|{{#if:{{{2|}}}{{{3|}}}|{{Speciesbox/hybrid name|{{{5}}}}}|{{#ifeq:{{{6|yes}}}|no||{{italic title}}}}''{{{5}}}''}}}}
}}</includeonly><noinclude>{{documentation}}</noinclude>
```

## Provenance

Raw source: `bronze/pages/1603/3855.wikitext` · revision `3855` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ASpeciesbox/name)
