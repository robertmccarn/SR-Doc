---
page_id: 607
revision_id: 9442
source_url: https://second-renaissance.fandom.com/wiki/Template%3ACite_web
raw_sha256: ea8b5540e29184fb27b313a63d3de8281150929c81e73ea0ce2611f114493125
---

# Template:Cite web

## Preserved source

```wikitext
<includeonly>{{
#if: {{#if: {{{url|}}} | {{#if: {{{title|}}} |1}}}}
  ||Error on call to [Template:cite web](https://second-renaissance.fandom.com/wiki/Template:cite_web): Parameters '''url''' and '''title''' must be specified
}}{{
#if: {{{archiveurl|}}}{{{archivedate|}}} 
  | {{#if: {{#if: {{{archiveurl|}}}| {{#if: {{{archivedate|}}} |1}}}}
    ||Error on call to [template:cite web](https://second-renaissance.fandom.com/wiki/template:cite_web): Parameters '''archiveurl''' and '''archivedate''' must be both specified or both omitted
}}
}}{{#if: {{{author|}}}{{{last|}}}
  | {{#if: {{{authorlink|}}}
    | [{{#if: {{{last|}}}
      | {{{last}}}{{#if: {{{first|}}} | , {{{first}}} }}
      | {{{author}}}
    }}](https://second-renaissance.fandom.com/wiki/{{{authorlink}}})
    | {{#if: {{{last|}}}
      | {{{last}}}{{#if: {{{first|}}} | , {{{first}}} }}
      | {{{author}}}
    }}
  }}
}}{{#if: {{{author|}}}{{{last|}}}
  | {{#if: {{{coauthors|}}}| <nowiki>;</nowiki>&#32;{{{coauthors}}} }}
}}{{#if: {{{author|}}}{{{last|}}}|
    {{#if: {{{date|}}}
    | &#32;({{{date}}})
    | {{#if: {{{year|}}}
      | {{#if: {{{month|}}}
        | &#32;({{{month}}} {{{year}}})
        | &#32;({{{year}}})
      }}
    }}
  |}}
}}{{#if: {{{last|}}}{{{author|}}}
  | .&#32;}}{{
  #if: {{{editor|}}}
  | &#32;{{{editor}}}: 
}}{{#if: {{{archiveurl|}}}
    | {{#if: {{{archiveurl|}}} | {{#if: {{{title|}}} | [{{{archiveurl}}} {{{title}}}] }}}}
    | {{#if: {{{url|}}} | {{#if: {{{title|}}} | [{{{url}}} {{{title}}}] }}}}
}}{{#if: {{{language|}}} | &#32;<span style="font-size: 0.95em; font-weight: bold; color:#555; position: relative;">({{{language}}})</span> 
}}{{#if: {{{format|}}}
  | &#32;({{{format|}}})
}}{{#if: {{{work|}}}
  | .&#32;''{{{work}}}''
}}{{#if: {{{pages|}}}
  | &#32;{{{pages}}}
}}{{#if: {{{publisher|}}}
  | .&#32;{{{publisher}}}{{#if: {{{author|}}}{{{last|}}}
    | 
    | {{#if: {{{date|}}}{{{year|}}}{{{month|}}} || }}
  }}
}}{{#if: {{{author|}}}{{{last|}}}
  ||{{#if: {{{date|}}}
    | &#32;({{{date}}})
    | {{#if: {{{year|}}}
      | {{#if: {{{month|}}}
        | &#32;({{{month}}} {{{year}}})
        | &#32;({{{year}}})
      }}
    }}
  }}
}}.{{#if: {{{archivedate|}}}
  | &#32;Archived from [{{{url}}} the original] on {{#time:[F j](https://second-renaissance.fandom.com/wiki/F_j), [Y](https://second-renaissance.fandom.com/wiki/Y)|{{{archivedate}}}}}{{#if: {{{archiveyear|}}} | , [{{{archiveyear}}}](https://second-renaissance.fandom.com/wiki/{{{archiveyear}}}) }}.
}}{{#if: {{{accessdate|}}}
  | &#32;Retrieved on {{#time:[F j](https://second-renaissance.fandom.com/wiki/F_j), [Y](https://second-renaissance.fandom.com/wiki/Y)|{{{accessdate}}}}}.
}}{{#if: {{{quote|}}} 
  | &nbsp;"{{{quote}}}"
}}{{#if:{{{archiveurl|}}}
    |&#32;
    |{{#if:{{{nobackup|}}}
        |&#32;
        |{{#if:{{{url|}}}
            |{{#if:{{NAMESPACE}}
                |{{#ifeq:{{NAMESPACE}}|File||}}
                |}}
            |&#32;}}}}}}</includeonly>
<noinclude>
{{documentation}}
</noinclude>
```

## Provenance

Raw source: `bronze/pages/607/9442.wikitext` · revision `9442` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ACite_web)
