---
page_id: 614
revision_id: 855
source_url: https://second-renaissance.fandom.com/wiki/Template%3ANumber_table_sorting/Qyes/0
raw_sha256: 3d9730644e2f3ef700292538a34df42d189202c017ab2b0fd773256ee3c20ccf
---

# Template:Number table sorting/Qyes/0

## Preserved source

```wikitext
<span style="{{{style|display:none}}}" class="sortkey">{{#ifeq:{{#expr:{{{1|0}}}}}|INF
   |9000000000000000000
   |{{#ifexpr:{{{1|0}}}=0
     |5000000000000000000
     |{{#expr:7000+{{{2|0}}}}}{{padleft:{{#iferror:{{#expr:{{#expr:floor({{{1|0}}}E(4-{{{2|0}}}))}}}}}}|5}}{{padleft:{{#expr:(floor({{{1|0}}}E(9-{{{2|0}}})))mod1E5}}|5}}{{padleft:{{#expr:(floor({{{1|0}}}E(14-{{{2|0}}})))mod1E5}}|5}}
   }}
}}♠</span>
```

## Provenance

Raw source: `bronze/pages/614/855.wikitext` · revision `855` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ANumber_table_sorting/Qyes/0)
