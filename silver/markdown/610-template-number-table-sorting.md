---
page_id: 610
revision_id: 851
source_url: https://second-renaissance.fandom.com/wiki/Template%3ANumber_table_sorting
raw_sha256: 687db0a3ef0b6208a5c2dce42048ba400d11a7321255b8fdabddda7aa69d72e7
---

# Template:Number table sorting

## Preserved source

```wikitext
{{number table sorting/{{#iferror:{{#expr:+{{formatnum:{{{1|}}}|R}}}}
      |error
      |Q{{{quiet|no/F{{{format|yes}}}/S{{{scinote|no}}}}}}/{{#expr:{{formatnum:{{{1}}}|R}}<0}}
    }}
   |{{formatnum:{{{1|}}}|R}}|style={{#ifeq:{{{debug}}}|yes
      |border:1px solid
      |display:none
    }}
   |{{#expr:floor((ln(abs({{formatnum:{{{1}}}|R}}))/ln10)+1E-14)}}|prefix={{{prefix|}}}
   |{{{hideerror|off}}}
}}<noinclude>
{{documentation}}
<!-- Add cats and interwikis to the /doc subpage, not here! -->
</noinclude>
```

## Provenance

Raw source: `bronze/pages/610/851.wikitext` · revision `851` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ANumber_table_sorting)
