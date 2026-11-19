---
page_id: 764
revision_id: 1037
source_url: https://second-renaissance.fandom.com/wiki/Template%3AEfn
raw_sha256: 1dd5a77d76604d41bea42e241617835cea24493c4b67b7176d00f0feaf832456
---

# Template:Efn

## Preserved source

```wikitext
<includeonly>{{#if:{{{name|}}}
 |{{#tag:ref|{{{1|{{{reference|}}}}}}|name={{{name|}}}|group={{#switch: {{{group|}}}
    | note
    | upper-alpha
    | upper-roman
    | lower-alpha
    | lower-greek
    | lower-roman = {{{group|}}}
    | #default = lower-alpha
   }}
 }}
 |{{#tag:ref|{{{1|{{{reference|}}}}}}|group={{#switch: {{{group|}}}
    | note
    | upper-alpha
    | upper-roman
    | lower-alpha
    | lower-greek
    | lower-roman = {{{group|}}}
    | #default = lower-alpha
   }}
 }}
}}</includeonly><noinclude>
{{documentation}}
</noinclude>
```

## Provenance

Raw source: `bronze/pages/764/1037.wikitext` · revision `1037` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AEfn)
