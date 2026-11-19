---
page_id: 146
revision_id: 200
source_url: https://second-renaissance.fandom.com/wiki/Template%3ANamespace_detect
raw_sha256: 10c6cf6ff0749d398eb3d80c969c8c2e41e9b247e5b4dfd6693f49e03aabdfa2
---

# Template:Namespace detect

## Preserved source

```wikitext
{{#switch:
  {{lc:               <!--Lower case the result-->
    <!--If no or empty "demospace" parameter then detect namespace-->
    {{#if:{{{demospace|}}} 
    | {{{demospace}}}
    | {{#if:{{{page|}}} 
      | <!--Detect the namespace in the "page" parameter-->
        {{#ifeq:{{NAMESPACE:{{{page}}} }}|{{TALKSPACE:{{{page}}} }}
        | talk
        | {{SUBJECTSPACE:{{{page}}} }} 
        }}
      | <!--No "demospace" or "page" parameters, so detect actual namespace-->
        {{#ifeq:{{NAMESPACE}}|{{TALKSPACE}}
        | talk
        | {{SUBJECTSPACE}} 
        }}
      }}
    }}
  }}
<!-- Only one of the lines below will be executed -->
<!-- Respecting empty parameters on purpose -->
| main        <!--"demospace=main" or {{SUBJECTSPACE}}={{ns:0}}=""-->
|           = {{{main| {{{other|}}} }}}
| talk      = {{{talk| {{{other|}}} }}}
| user      = {{{user| {{{other|}}} }}}
| wikipedia = {{{wikipedia| {{{other|}}} }}}
| file
| image     = {{{file| {{{image| {{{other|}}} }}} }}}
| mediawiki = {{{mediawiki| {{{other|}}} }}}
| template  = {{{template| {{{other|}}} }}}
| help      = {{{help| {{{other|}}} }}}
| category  = {{{category| {{{other|}}} }}}
| portal    = {{{portal| {{{other|}}} }}}
| book      = {{{book| {{{other|}}} }}}
| other
| #default  = {{{other|}}}   <!--"demospace=other" or a new namespace-->

}}<!--End switch--><noinclude>

{{documentation}}
</noinclude>
```

## Provenance

Raw source: `bronze/pages/146/200.wikitext` · revision `200` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ANamespace_detect)
