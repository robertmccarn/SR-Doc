---
page_id: 685
revision_id: 953
source_url: https://second-renaissance.fandom.com/wiki/Template%3ATransclude
raw_sha256: 33e85c1109a2a897e0088642d4fa3d7a4384ad0b0a91179f6ea54d2e5e101bd2
---

# Template:Transclude

## Preserved source

```wikitext
{{#switch: {{NAMESPACE: {{{1}}} }}
 |#default = {{FULLPAGENAME: {{{1}}} }} <!-- eg "User:Foo" -->
 |{{ns:0}} = 
    {{#ifeq: {{NAMESPACE: {{{1}}} }} | {{NAMESPACE: Template{{{1}}} }}
      | Template:{{{1}}}            <!-- no leading colon, eg "Foo" -->
      | {{PAGENAME: {{{1}}} }}      <!-- leading colon, eg ":Foo", so we want the article -->
    }}
}}<noinclude>
{{documentation}}
</noinclude>
```

## Provenance

Raw source: `bronze/pages/685/953.wikitext` · revision `953` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ATransclude)
