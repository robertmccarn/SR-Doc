---
page_id: 324
revision_id: 513
source_url: https://second-renaissance.fandom.com/wiki/Template%3AMONTHNUMBER
raw_sha256: d092129e0b2f397c871df1d6976a5eef5e36e035cc1b47400c9c5484cf77fe08
---

# Template:MONTHNUMBER

## Preserved source

```wikitext
<includeonly>{{#if:{{{1|}}}
 |{{#switch:{{lc:{{{1}}}}}
  |january|jan=1
  |february|feb=2
  |march|mar=3
  |apr|april=4
  |may=5
  |june|jun=6
  |july|jul=7
  |august|aug=8
  |september|sep|sept=9
  |october|oct=10
  |november|nov=11
  |december|dec=12
  |{{#ifexpr:{{{1}}}<0
   |{{#ifexpr:(({{{1}}})round 0)!=({{{1}}})
    |{{#expr:12-(((0.5-({{{1}}}))round 0)mod 12)}}
    |{{#expr:12-(((11.5-({{{1}}}))round 0)mod 12)}}
   }}
  |{{#expr:(((10.5+{{{1}}})round 0)mod 12)+1}}
  }}
 }}
 |Missing required parameter 1=''month''!
}}</includeonly><noinclude>
{{Documentation}}
<!-- Add categories and interwikis to the /doc subpage, not here! -->
</noinclude>
```

## Provenance

Raw source: `bronze/pages/324/513.wikitext` · revision `513` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AMONTHNUMBER)
