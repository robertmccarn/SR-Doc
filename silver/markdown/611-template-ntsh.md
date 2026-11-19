---
page_id: 611
revision_id: 852
source_url: https://second-renaissance.fandom.com/wiki/Template%3ANtsh
raw_sha256: 6fd9627446d175011dc241a3fd39bba61410c8ab83991c440f328a0f1a642b86
---

# Template:Ntsh

## Preserved source

```wikitext
{{number table sorting/{{#iferror:{{#expr:+{{formatnum:{{{1|}}}|R}}}}
      |error
      |Qyes/{{#expr:{{formatnum:{{{1}}}|R}}<0}}
    }}
   |{{formatnum:{{{1|}}}|R}}|style={{#ifeq:{{{debug}}}|yes
      |border:1px solid;display:inline;
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

Raw source: `bronze/pages/611/852.wikitext` · revision `852` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ANtsh)
