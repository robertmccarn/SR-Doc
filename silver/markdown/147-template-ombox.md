---
page_id: 147
revision_id: 201
source_url: https://second-renaissance.fandom.com/wiki/Template%3AOmbox
raw_sha256: d1f6a23589dfb02b0434204ad1c907b791f8a7ac55eaff8d3d2b0cdcccea9a95
---

# Template:Ombox

## Preserved source

```wikitext
{{#ifeq:{{{small|}}}|yes
| {{ombox/core
  | small = yes
  | type  = {{{type|}}}
  | image = {{#if:{{{smallimage|}}}| {{{smallimage}}} | {{{image|}}} }}
  | imageright = {{#if:{{{smallimageright|}}} | {{{smallimageright}}} | {{{imageright|}}} }}
  | style = {{{style|}}}
  | textstyle = {{{textstyle|}}}
  | text  = {{#if:{{{smalltext|}}}| {{{smalltext}}} | {{{text}}} }}
  }}
| {{ombox/core
  | type  = {{{type|}}}
  | image = {{{image|}}}
  | imageright = {{{imageright|}}} 
  | style = {{{style|}}}
  | textstyle = {{{textstyle|}}}
  | text  = {{{text}}}
  }}
}}<noinclude>
```

## Provenance

Raw source: `bronze/pages/147/201.wikitext` · revision `201` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AOmbox)
