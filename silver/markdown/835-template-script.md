---
page_id: 835
revision_id: 1148
source_url: https://second-renaissance.fandom.com/wiki/Template%3AScript
raw_sha256: 5fbd0eb18f4f2486793a5c6b80802bb38d946c96fa3650d0167d2686b3cd174d
---

# Template:Script

## Preserved source

```wikitext
{{#switch: {{{1|}}}
<!--scripts with dedicated templates-->
|Arab = {{script/Arabic|1={{{2}}}}}
|fa-Arab|ps-Arab|ur-Arab = {{script/Nastaliq|1={{{2}}}}}
|Bali = {{script/Bali|1={{{2}}}}}
|Bamu = {{script/Bamum|1={{{2}}}}}
|Brah = {{script/Brahmi|1={{{2}}}}}
|Bugi = {{script/Lontara|2={{{2}}}}}
|Buhd = {{script/Buhid|1={{{2}}}}}
|Copt = {{script/Coptic|1={{{2}}}}}
|Cham = {{script/Cham|1={{{2}}}}}
|Cyrs = {{script/Slavonic|1={{{2}}}}}
|Geok = {{script/Khutsuri|1={{{2}}}}}
|Grek = {{script/Greek|1={{{2}}}}}
|Hebr = {{script/Hebrew|1={{{2}}}}}
|Java = {{script/Java|1={{{2}}}}}
|Kali = {{script/Kayah Li|1={{{2}}}}}
|Khmr = {{script/Khmer|1={{{2}}}}}
|Latg = {{script/Gaelic|1={{{2}}}}}
|Latn = {{script/Latin|1={{{2}}}}}
|Lana = {{script/Tai Tham|1={{{2}}}}}
|Lisu|Fraser = {{script/Lisu|1={{{2}}}}}
|Mymr = {{script/Mymr|1={{{2}}}}}
|Nkoo|Nko = {{script/Nko|1={{{2}}}}}
|Orkh = {{script/Orkhon|1={{{2}}}}}
|Osma = {{script/Osmanya|1={{{2}}}}}
|Phnx = {{script/Phoenician|1={{{2}}}}}
|Rjng = {{script/Rejang|1={{{2}}}}}
|Runr = {{script/Runic|1={{{2}}}}}
|Syre = {{script/Strng|1={{{2}}}}}
|Syrj = {{script/Serto|1={{{2}}}}}
|Syrn = {{script/Mdnh|1={{{2}}}}}
|Tagb = {{script/Tagbanwa|1={{{2}}}}}
|Talu = {{script/New Tai Lue|1={{{2}}}}}
|Tavt = {{script/Tai Viet|1={{{2}}}}}
|Tglg = {{script/Baybayin|1={{{2}}}}}
|Tfng = {{script/Tifinagh|1={{{2}}}}}
|Vaii|Vai = {{script/Vai|1={{{2}}}}}
|Xsux = {{script/Cuneiform|1={{{2}}}}}
|Yiii|Yi = {{script/Yi|1={{{2}}}}}
<!--other scripts use standard language spans-->
|#default = <span {{#switch: {{{1}}}
  <!--tweaks which should be moved to global CSS classes, with fonts supported in the Universal Language Selector-->
  |Cprt = style="font-size:125%;font-family:'Noto Sans Cypriot', Code2001;"<!--SMP, rarely supported, state font explicltly-->
  |Goth = style="font-size:125%;"
  |Latf = style="font-size:125%;font-family:'Breitkopf Fraktur',UnifrakturCook,UniFrakturMaguntia;"
  |Linb = style="font-size:125%;"
  |Ugar = style="font-size:125%;font-family:Aegean"
  |Xpeo = style="font-size:125%;font-family:Artaxerxes,Xerxes,Aegean;"<!--Use Xerxes for Old Persian-->
  |#default = class="Unicode"<!--BMP, use generic "unicode" CSS class for all other scripts, including "Latn" for IPA-->
 }}>{{{2}}}</span>
}}<noinclude>
{{template doc}}<!-- Add categories, documentation, and interwiki links to the /doc subpage, not here! -->
</noinclude>
```

## Provenance

Raw source: `bronze/pages/835/1148.wikitext` · revision `1148` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AScript)
