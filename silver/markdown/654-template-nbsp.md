---
page_id: 654
revision_id: 915
source_url: https://second-renaissance.fandom.com/wiki/Template%3ANbsp
raw_sha256: 9ee1ae3c8a1ea0377ccf9a4efc8eb54d49c88eb1cb730f1d22ea8f0692e0b7af
---

# Template:Nbsp

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

Raw source: `bronze/pages/654/915.wikitext` · revision `915` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ANbsp)
