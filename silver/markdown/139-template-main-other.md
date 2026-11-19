---
page_id: 139
revision_id: 188
source_url: https://second-renaissance.fandom.com/wiki/Template%3AMain_other
raw_sha256: 7f8aa77f4a064a31582c57adf7dca0a9973da94867aac7ea2d622822f4754a01
---

# Template:Main other

## Preserved source

```wikitext
{{#switch:
  <!--If no or empty "demospace" parameter then detect namespace-->
  {{#if:{{{demospace|}}} 
  | {{lc: {{{demospace}}} }}    <!--Use lower case "demospace"-->
  | {{#ifeq:{{NAMESPACE}}|{{ns:0}}
    | main
    | other
    }} 
  }}
| main     = {{{1|}}}
| other
| #default = {{{2|}}}
}}<noinclude>

{{documentation}}
<!-- Add categories and interwikis to the /doc subpage, not here! -->
</noinclude>
```

## Provenance

Raw source: `bronze/pages/139/188.wikitext` · revision `188` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AMain_other)
