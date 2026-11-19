---
page_id: 157
revision_id: 213
source_url: https://second-renaissance.fandom.com/wiki/Template%3ACollapsible_option
raw_sha256: 98610bfbc0c89887a54fbb0a927e213f652dc85fc3b45932a4e16883addf7f21
---

# Template:Collapsible option

## Preserved source

```wikitext
'''How to manage this template's initial visibility'''<br />
To manage this template's visibility when it first appears, [add the parameter](https://second-renaissance.fandom.com/wiki/Help:Template):
:{{para|state|collapsed}} to show the template in its collapsed state, i.e. hidden apart from its titlebar&nbsp;– e.g. <code><nowiki>{{</nowiki><includeonly>{{</includeonly>BASEPAGENAME<includeonly>}}</includeonly><nowiki> |state=collapsed}}</nowiki></code>
:{{para|state|expanded}} to show the template in its expanded state, i.e. fully visible&nbsp;– e.g. <code><nowiki>{{</nowiki><includeonly>{{</includeonly>BASEPAGENAME<includeonly>}}</includeonly><nowiki> |state=expanded}}</nowiki></code>
:{{para|state|autocollapse}} to show the template in its collapsed state ''but only if'' there is another template of the same type on the page&nbsp;– e.g. <code><nowiki>{{</nowiki><includeonly>{{</includeonly>BASEPAGENAME<includeonly>}}</includeonly><nowiki> |state=autocollapse}}</nowiki></code>

Unless set otherwise (see the {{para|state}} parameter in the template's code), the template's default state is <code>{{#switch:{{{default|}}}|collapsed=collapsed|expanded=expanded|autocollapse|#default=autocollapse}}</code>.<!--
-->{{#if:{{{align|}}}|
:{{para|align|''value''}} is also available; where ''value'' can be either <code>right</code> or <code>left</code>. The default is <code>center</code>
}}{{#if:{{{title-background|}}}|:{{para|title-background|''value''}} is also available; where ''value'' can be either <code>navbox</code> or a <code>color</code>. The default is <code>none</code> and <code>navbox</code> defaults to the default navbox color.
}}{{#if:{{{width|}}}|
:{{para|width|''value''}} is also available; where ''value'' can be either <code>N [em/%/px]</code> or <code>auto</code>. The default is <code>100%</code>
}}<!--
Add {{pp-template}} if template page where this template is transcluded is protected:
-->{{template other
    | {{#if:{{PROTECTIONLEVEL:edit}} |{{pp-template|docusage=yes}}
       | {{#if:{{PROTECTIONLEVEL:move}} |{{pp-move|docusage=yes|small=yes}} }}
   }} }}<noinclude>
{{Documentation}}
</noinclude>
```

## Provenance

Raw source: `bronze/pages/157/213.wikitext` · revision `213` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ACollapsible_option)
