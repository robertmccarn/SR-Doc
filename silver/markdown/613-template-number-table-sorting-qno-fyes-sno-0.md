---
page_id: 613
revision_id: 854
source_url: https://second-renaissance.fandom.com/wiki/Template%3ANumber_table_sorting/Qno/Fyes/Sno/0
raw_sha256: 759b738b102d26bc42f5c744ad875f4f2c2fbd2d0d5e84e50b4c0c25089134df
---

# Template:Number table sorting/Qno/Fyes/Sno/0

## Preserved source

```wikitext
<span style="{{{style|display:none}}}" class="sortkey">{{#ifeq:{{#expr:{{{1|0}}}}}|INF
   |9000000000000000000
   |{{#ifexpr:{{{1|0}}}=0
     |5000000000000000000
     |{{#expr:7000+{{{2|0}}}}}{{padleft:{{#iferror:{{#expr:{{#expr:floor({{{1|0}}}E(4-{{{2|0}}}))}}}}}}|5}}{{padleft:{{#expr:(floor({{{1|0}}}E(9-{{{2|0}}})))mod1E5}}|5}}{{padleft:{{#expr:(floor({{{1|0}}}E(14-{{{2|0}}})))mod1E5}}|5}}
   }}
}}♠</span>{{{prefix|}}}{{formatnum:{{#if:{{#titleparts:{{{1|0}}}|1|2}}
     |{{number table sorting/frac|{{{1|0}}}|{{#titleparts:{{{1|0}}}|1|1}}|{{#titleparts:{{{1|0}}}|1|2}}|pos}}
     |{{#switch:{{#expr:{{{1|}}}400}}
        |0|INF={{#iferror:{{#expr:1/{{#expr:{{{1|0}}}}}}}
           |{{{1|0}}}
           |{{#expr:{{{1}}}E-{{{2|0}}}}}<span style="margin-left:0.2em">×<span style="margin-left:0.1em">10</span></span><s style="display:none">^</s><sup>{{#ifexpr:{{{2|0}}}<0|−{{#expr:-{{{2|0}}}}}|{{{2|0}}}}}</sup>
         }}
        |{{{1|0}}}
      }}
   }}
}}
```

## Provenance

Raw source: `bronze/pages/613/854.wikitext` · revision `854` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ANumber_table_sorting/Qno/Fyes/Sno/0)
