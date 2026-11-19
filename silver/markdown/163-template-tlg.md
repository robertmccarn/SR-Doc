---
page_id: 163
revision_id: 219
source_url: https://second-renaissance.fandom.com/wiki/Template%3ATlg
raw_sha256: 1f255fe9484712139aa5f680ad898c063356398190bf177197d59b9415d3fe43
---

# Template:Tlg

## Preserved source

```wikitext
<includeonly><!--
 -->{{#if:{{{nowrap|}}}        |<span class="nowrap">}}<!--
 -->{{#if:{{{code|{{{tt|}}}}}} |<code> |{{#if:{{{plaincode|}}}|<code style="border:none;background:transparent;">}} }}<!--
 -->{{#if:{{{braceinside|}}}   | |<nowiki>{{</nowiki>}}<!--
 -->{{#if:{{{subst|}}}         |[subst](https://second-renaissance.fandom.com/wiki/Help:Substitution):}}<!--

 -->{{#if:{{{bold|{{{boldlink|{{{boldname|}}}}}}}}} |'''}}<!--
 -->{{#if:{{{nolink|}}} |<!--then omit template link, else:
  -->| {{#if:{{{braceinside|}}} |<nowiki>{</nowiki>}}<!--
       -->{{!((}}:<!--(start building link with "[1|{{{1}}}}}|: <!--i.e. if {{{1}}}'s first character is a colon,
              then:--> |{{FULLPAGENAME:{{{1}}}}}<!--
              else:--> |{{#switch:{{NAMESPACE:{{#if:{{{1|}}}|{{{1}}}|{{FULLPAGENAME}}}}}}
                         | {{ns:0}} = {{ns:10}}:{{#if:{{{1|}}}|{{PAGENAME:{{{1}}}}}|{{PAGENAME}}}}
                         | #default = {{#if:{{{1|}}}|{{FULLPAGENAME:{{{1}}}}}|{{FULLPAGENAME}}}}
                      }}}}<!--
       -->{{!}}<!--(pipe between link and label, i.e. [[:link|label](https://second-renaissance.fandom.com/wiki/:")
___________________-->{{))
 -->}}<!--
 -->{{#if:{{{braceinside|}}} |<nowiki>{</nowiki>}}<!--
 label / template name:
 -->{{{alttext|{{#if:{{{1|}}}|{{{1}}}|{{#ifeq:{{NAMESPACE}}|{{ns:Template}}|{{PAGENAME}}|{{FULLPAGENAME}}}}}}}}}<!--
 -->{{#if:{{{braceinside|}}} |<nowiki>}</nowiki>}}<!--
 -->{{#if:{{{nolink|}}} | |<!--
       -->{{!))}}<!--(end link)
    -->{{#if:{{{braceinside|}}} |<nowiki>}</nowiki>}}<!-- 
 -->}}<!--
 -->{{#if:{{{bold|{{{boldlink|{{{boldname|}}}}}}}}} |'''}}<!--

 -->{{#if:{{{italic|{{{italics|}}}}}} |<span style="font-style:italic;">}}<!--
 -->{{#ifeq:{{{2|¬}}}|¬ | |&#124;{{#tag:nowiki|{{{2}}}}}}}<!--
 -->{{#ifeq:{{{3|¬}}}|¬ | |&#124;{{#tag:nowiki|{{{3}}}}}}}<!--
 -->{{#ifeq:{{{4|¬}}}|¬ | |&#124;{{#tag:nowiki|{{{4}}}}}}}<!--
 -->{{#ifeq:{{{5|¬}}}|¬ | |&#124;{{#tag:nowiki|{{{5}}}}}}}<!--
 -->{{#ifeq:{{{6|¬}}}|¬ | |&#124;{{#tag:nowiki|{{{6}}}}}}}<!--
 -->{{#ifeq:{{{7|¬}}}|¬ | |&#124;{{#tag:nowiki|{{{7}}}}}}}<!--
 -->{{#ifeq:{{{8|¬}}}|¬ | |&#124;{{#tag:nowiki|{{{8}}}}}}}<!--
 -->{{#ifeq:{{{9|¬}}}|¬ | |&#124;{{#tag:nowiki|{{{9}}}}}}}<!--
 -->{{#ifeq:{{{10|¬}}}|¬ | |&#124;{{#tag:nowiki|{{{10}}}}}}}<!--
 -->{{#ifeq:{{{11|¬}}}|¬ | |&#124;{{#tag:nowiki|{{{11}}}}}}}<!--
 -->{{#if:{{{12|}}} |&#124;…}}<!--
 -->{{#if:{{{italic|{{{italics|}}}}}} |</span>}}<!--

 -->{{#if:{{{braceinside|}}} | |<nowiki>}}</nowiki>}}<!--
 -->{{#if:{{{code|{{{tt|}}}}}}{{{plaincode|}}} |</code>}}<!--
 -->{{#if:{{{nowrap|}}} |</span>}}<!--
--></includeonly><noinclude>
{{Documentation}}
</noinclude>
```

## Provenance

Raw source: `bronze/pages/163/219.wikitext` · revision `219` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ATlg)
