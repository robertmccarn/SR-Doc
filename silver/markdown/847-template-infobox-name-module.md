---
page_id: 847
revision_id: 1160
source_url: https://second-renaissance.fandom.com/wiki/Template%3AInfobox_name_module
raw_sha256: 8be96645623e4d34e7f26673bb507a29936b3ff27b952498989973d2dcaa32e5
---

# Template:Infobox name module

## Preserved source

```wikitext
{{ infobox
| child     = yes
| decat     = yes <!-- remove from template:infobox tracking categories -->
| title     = 

| label1    = Original title
|  data1    = {{#if: {{{original|}}}|''{{{original|}}}''}}

| label2    = [Traditional](https://second-renaissance.fandom.com/wiki/Traditional_Chinese_characters)
|  data2    = {{#if:{{{traditional|{{{fanti|}}}}}}|<big>{{{traditional|{{{fanti|}}}}}}</big>}}
| label3    = [Simplified](https://second-renaissance.fandom.com/wiki/Simplified_Chinese_characters)
|  data3    = {{#if:{{{simplified|{{{jianti|}}}}}}|<big>{{{simplified|{{{jianti|}}}}}}</big>}}
| label4    = [Chinese](https://second-renaissance.fandom.com/wiki/Chinese_characters)
|  data4    = {{#if:{{{chinese|{{{Chinese|}}}}}}|<big>{{{chinese|{{{Chinese|}}}}}}</big>}}
| label5    = [Mandarin](https://second-renaissance.fandom.com/wiki/Pinyin)
|  data5    = {{{pinyin|}}}
| label6    = [Cantonese](https://second-renaissance.fandom.com/wiki/Jyutping)
|  data6    = {{{jyutping|}}}
| label7    = [Hokkien](https://second-renaissance.fandom.com/wiki/Pe̍h-ōe-jī)
|  data7    = {{{poj|}}}

| label8    = [Japanese](https://second-renaissance.fandom.com/wiki/Japanese_language)
|  data8    = {{#if: {{{kanji|}}}|<span class="t_nihongo_kanji" lang="ja">{{{kanji|}}}</span>}}{{#if: {{{kana|}}}|<span class="t_nihongo_kanji" lang="ja">{{{kana|}}}</span>}}
| label9    = [Hepburn](https://second-renaissance.fandom.com/wiki/Hepburn_romanization)
|  data9    = {{#if: {{{romaji|}}}|''{{{romaji|}}}''}}

| label10   = {{#switch: {{lc:{{{context|}}}}}|n|nk|north|dprk=[Chos&#335;n'g&#365;l](https://second-renaissance.fandom.com/wiki/Hangul)|#default=[Hangul](https://second-renaissance.fandom.com/wiki/Hangul)}}
|  data10   = {{#if: {{{hangul|}}}|{{lang|ko-Hang|{{{hangul}}} }} }}
| label11   = {{#switch: {{lc:{{{context|}}}}}|n|nk|north|dprk=[Hancha](https://second-renaissance.fandom.com/wiki/Hanja)|#default=[Hanja](https://second-renaissance.fandom.com/wiki/Hanja)}}
|  data11   = {{#if: {{{hanja|}}}|{{#ifeq: {{{hanja|}}}|!|<noinclude>!</noinclude>|{{lang|ko-Hani|{{{hanja}}} }} }} }}
| label12   = {{#switch: {{lc:{{{context|}}}}}|n|nk|north|dprk=[McCune–Reischauer](https://second-renaissance.fandom.com/wiki/McCune–Reischauer)|#default=[Revised Romanization](https://second-renaissance.fandom.com/wiki/Revised_Romanization_of_Korean)}}
|  data12   = {{#if: {{#switch: {{lc:{{{context|}}}}}|n|nk|north|dprk={{{mr|}}}|#default={{{rr|}}} }}|''{{transl|ko|{{#switch: {{lc:{{{context|}}}}}|n|nk|north|dprk={{{mr}}}|#default={{{rr}}} }} }}''}}
| label13   = {{#switch: {{lc:{{{context|}}}}}|n|nk|north|dprk=[Revised Romanization](https://second-renaissance.fandom.com/wiki/Revised_Romanization_of_Korean)|#default=[McCune–Reischauer](https://second-renaissance.fandom.com/wiki/McCune–Reischauer)}}
|  data13   = {{#if: {{#switch: {{lc:{{{context|}}}}}|n|nk|north|dprk={{{rr|}}}|#default={{{mr|}}} }}|''{{transl|ko|{{#switch: {{lc:{{{context|}}}}}|n|nk|north|dprk={{{rr}}}|#default={{{mr}}} }} }}''}}


| label14   = Literally
|  data14   = {{#if: {{{translation|}}}|''{{{translation|}}}''}}
}}<noinclude>{{documentation}}

<!-- Add cats and interwikis to the /doc subpage -->

</noinclude>
```

## Provenance

Raw source: `bronze/pages/847/1160.wikitext` · revision `1160` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AInfobox_name_module)
