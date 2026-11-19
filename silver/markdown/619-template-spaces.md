---
page_id: 619
revision_id: 860
source_url: https://second-renaissance.fandom.com/wiki/Template%3ASpaces
raw_sha256: 9ee1ae3c8a1ea0377ccf9a4efc8eb54d49c88eb1cb730f1d22ea8f0692e0b7af
---

# Template:Spaces

## Preserved source

```wikitext
<span style="white-space:nowrap;">{{#iferror:{{#expr:{{{1|1}}}}}
  |{{#switch:{{{1}}}
     |fig=&#8199;
     |en=&ensp;
     |em=&emsp;
     |thin=&thinsp;
     |hair=&#8202;
     |&nbsp;
   }}
  |{{#invoke:String|rep|{{#switch:{{{2}}}
     |fig=&#8199;
     |en=&ensp;
     |em=&emsp;
     |thin=&thinsp;
     |hair=&#8202;
     |&nbsp;
   }}|{{{1|1}}}}}
}}</span><noinclude>
{{documentation}}
</noinclude>
```

## Provenance

Raw source: `bronze/pages/619/860.wikitext` · revision `860` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ASpaces)
