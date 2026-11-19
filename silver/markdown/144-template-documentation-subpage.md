---
page_id: 144
revision_id: 1081
source_url: https://second-renaissance.fandom.com/wiki/Template%3ADocumentation_subpage
raw_sha256: 6962e6ed024eed63ac7222ab384aa0ab051cdfccf344b1e40918fc903f00d662
---

# Template:Documentation subpage

## Preserved source

```wikitext
<includeonly><!--
 -->{{#ifeq:{{lc:{{SUBPAGENAME}}}} |{{{override|doc}}}
     | <!--(this template has been transcluded on a /doc or /{{{override}}} page)-->
</includeonly><!--

      -->{{#ifeq:{{{doc-notice|show}}} |show
          | {{Mbox
             | type = notice
             | style = margin-bottom:1.0em;
             | image = [40px|alt=|link=](150-file-edit-copy-green-svg.md)
             | text =
'''This is a [documentation](https://second-renaissance.fandom.com/wiki/Wikipedia:Template_documentation) [subpage](https://second-renaissance.fandom.com/wiki/Wikipedia:Subpages) for {{{1|[:{{SUBJECTSPACE}}:{{BASEPAGENAME}}](https://second-renaissance.fandom.com/wiki/:{{SUBJECTSPACE}}:{{BASEPAGENAME}})}}}'''.<br />It contains usage information, [categories](https://second-renaissance.fandom.com/wiki/Wikipedia:Categorization) and other content that is not part of the original {{#if:{{{text2|}}} |{{{text2}}} |{{#if:{{{text1|}}} |{{{text1}}} |{{#ifeq:{{SUBJECTSPACE}} |{{ns:User}} |{{lc:{{SUBJECTSPACE}}}} template page |{{#if:{{SUBJECTSPACE}} |{{lc:{{SUBJECTSPACE}}}} page|article}}}}}}}}. 
            }}
         }}<!--

      -->{{DEFAULTSORT:{{{defaultsort|{{PAGENAME}}}}}}}<!--

      -->{{#if:{{{inhibit|}}} |<!--(don't categorize)-->
          |   <includeonly><!--
               -->{{#ifexist:{{NAMESPACE}}:{{BASEPAGENAME}}
                   | [Template=Template |Module=Module |User=User |#default=Wikipedia}} documentation pages](https://second-renaissance.fandom.com/wiki/Category:{{)
                   | [Category:Documentation subpages without corresponding pages](https://second-renaissance.fandom.com/wiki/Category:Documentation_subpages_without_corresponding_pages)
                  }}<!--
           --></includeonly>
         }}<!--

(completing initial #ifeq: at start of template:)
--><includeonly>
     | <!--(this template has not been transcluded on a /doc or /{{{override}}} page)-->
    }}<!--
--></includeonly><noinclude>{{Documentation}}</noinclude>
```

## Provenance

Raw source: `bronze/pages/144/1081.wikitext` · revision `1081` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ADocumentation_subpage)
