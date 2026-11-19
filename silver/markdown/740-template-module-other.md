---
page_id: 740
revision_id: 1012
source_url: https://second-renaissance.fandom.com/wiki/Template%3AModule_other
raw_sha256: 91b85bab754b66788c4bb2ebf1a4c16cb4d172b95f2ed1793292587a89d18e70
---

# Template:Module other

## Preserved source

```wikitext
{{#switch:
  <!--If no or empty "demospace" parameter then detect namespace-->
  {{#if:{{{demospace|}}}
  | {{lc: {{{demospace}}} }}    <!--Use lower case "demospace"-->
  | {{#ifeq:{{NAMESPACE}}|{{ns:Module}}
    | module
    | other
    }}
  }}
| module = {{{1|}}}
| other
| #default = {{{2|}}}
}}<!--End switch--><noinclude>

{{documentation}}
<!-- Add categories to the /doc subpage, not here! -->
</noinclude>
```

## Provenance

Raw source: `bronze/pages/740/1012.wikitext` · revision `1012` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AModule_other)
