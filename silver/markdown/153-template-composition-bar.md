---
page_id: 153
revision_id: 208
source_url: https://second-renaissance.fandom.com/wiki/Template%3AComposition_bar
raw_sha256: 9485c088078618d46c3c311ee9bcfb4dc65be0240182ef6019cc5a7c14ae6965
---

# Template:Composition bar

## Preserved source

```wikitext
<div style="border: {{{border-width|1px}}} solid {{{border-color|#c0c0c0}}}; background-color: {{{background-color|#f0f0f0}}}; width: {{{width|100}}}px; height: 1.5em;"><div style="position: absolute; background-color:{{#if:{{both|{{{4|}}}|{{{5|}}}}}
    |rgb({{#expr:255*{{{3|255}}}}},{{#expr:255*{{{4|0}}}}},{{#expr:255*{{{5|0}}}}})
    |{{{hex|{{{3|#CCCCCC}}}}}} }}; width: {{#expr:floor({{{width|100}}}*{{{1|{{#expr:{{{width|100}}}/2}}}}}/{{{2|{{{width|100}}}}}})}}px; height: 1.5em;"></div><div style="position: absolute; font-weight: bold; width: {{{width|100}}}px; height: 1.5em; text-align: center; z-index: 5; color: {{{color|#000}}};">{{formatnum:{{{1|50}}}}}&nbsp;/&nbsp;{{formatnum:{{{2|100}}}}}{{#if:{{{per|}}}|&nbsp;&nbsp;&nbsp;({{#expr:(({{{1|50}}}/{{{2|100}}})*100)round 0}}%)}}</div></div><noinclude>
{{Documentation}}
</noinclude>
```

## Provenance

Raw source: `bronze/pages/153/208.wikitext` · revision `208` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AComposition_bar)
