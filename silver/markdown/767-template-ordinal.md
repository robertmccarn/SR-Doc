---
page_id: 767
revision_id: 1040
source_url: https://second-renaissance.fandom.com/wiki/Template%3AOrdinal
raw_sha256: a0ba5ee16df915c21acb9749c546b423cd4fb41545d4d598a0273120c4b0bc61
---

# Template:Ordinal

## Preserved source

```wikitext
{{{1}}}{{{{{|safesubst:}}}#ifeq:{{{sup}}}|yes
 |<sup>
}}{{{{{|safesubst:}}}#switch:{{{{{|safesubst:}}}#expr:abs({{{1}}}) mod 100}}
  |11|12|13=th
  |{{{{{|safesubst:}}}#switch:{{{{{|safesubst:}}}#expr:abs{{{1}}} mod 10}}
   |1=st
   |2={{{{{|safesubst:}}}#ifeq:{{{2|}}}|d|d|nd}}
   |3={{{{{|safesubst:}}}#ifeq:{{{2|}}}|d|d|rd}}
   |th
  }}
 }}{{{{{|safesubst:}}}#ifeq:{{{sup}}}|yes
 |</sup>
}}<noinclude>
{{documentation}}
</noinclude>
```

## Provenance

Raw source: `bronze/pages/767/1040.wikitext` · revision `1040` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AOrdinal)
