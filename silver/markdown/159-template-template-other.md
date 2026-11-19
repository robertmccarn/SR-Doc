---
page_id: 159
revision_id: 215
source_url: https://second-renaissance.fandom.com/wiki/Template%3ATemplate_other
raw_sha256: f7beeb2d6a618aae1f005317c7a3d87669b79d17b584a4283efcf5ee89ecb1be
---

# Template:Template other

## Preserved source

```wikitext
{{#switch:
  <!--If no or empty "demospace" parameter then detect namespace-->
  {{#if:{{{demospace|}}}
  | {{lc: {{{demospace}}} }}    <!--Use lower case "demospace"-->
  | {{#ifeq:{{NAMESPACE}}|{{ns:Template}}
    | template
    | other
    }}
  }}
| template = {{{1|}}}
| other
| #default = {{{2|}}}
}}<!--End switch--><noinclude>

{{documentation}}
<!-- Add categories and interwikis to the /doc subpage, not here! -->
</noinclude>
```

## Provenance

Raw source: `bronze/pages/159/215.wikitext` · revision `215` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ATemplate_other)
