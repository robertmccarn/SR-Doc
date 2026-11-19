---
page_id: 710
revision_id: 980
source_url: https://second-renaissance.fandom.com/wiki/Template%3AHidden_begin
raw_sha256: f325214ad9a87bed72a36820933b4fee9f46065f21e1a5bc52930775564cb549
---

# Template:Hidden begin

## Preserved source

```wikitext
<noinclude>{{hatnote|Templates {{noredirect|Template:Begin hidden|Begin hidden}}, {{noredirect|Template:Start hidden|Start hidden}} and {{noredirect|Template:Start hidden section|Start hidden section}} redirect here.}}</noinclude><!--
--><includeonly><!--
-->{{#ifeq:{{{showhide|}}}{{{toggle|}}}|left
    | <!------------------------------------------------------------------------
         showhide = left, so place [show/hide] link on lefthand side:
       -------------------------------------------------------------------------
       --><div class="NavFrame {{#if:{{{expanded|}}} | |collapsed}} {{{class|}}}" style="position:relative;width:100%;border:{{{border|none}}};{{{style|}}}"><!--
           --><div class="NavHead" style="position:absolute;width:3.2em<!--(to accommodate "[show]")-->;background:transparent;"></div><!--
           --><div style="font-size:100%;height:1.6em;background:transparent;padding-left:2.8em<!--(should place text just after [show/hide])-->;
                          text-align:{{{ta1|left}}};font-weight:bold;{{{extra1|}}}{{{titlestyle|{{{headercss|}}}}}}">&nbsp;&nbsp;<!--deprecated:-->{{{header|}}}<!---->{{{title|}}}</div><!--
           --><div class="NavContent" style="padding-left:0.3em;text-align:{{{ta2|left}}};{{{extra2|}}}{{{bodystyle|{{{contentstyle|{{{contentcss|}}}}}}}}}"><!--

 -->| <!------------------------------------------------------------------------
         showhide /= left, so place [show/hide] link on righthand side:
       -------------------------------------------------------------------------
       --><div class="NavFrame {{#if:{{{expanded|}}} | |collapsed}} {{{class|}}}" style="border:{{{border|none}}};{{{style|}}}"><!--
           --><div class="NavHead" style="background:{{{bg1|transparent}}};text-align:{{{ta1|left}}};{{{extra1|}}}{{{titlestyle|{{{headercss|}}}}}}"><!--
                    deprecated:-->{{{header|}}}<!---->{{{title|}}}&nbsp;</div><!--
           --><div class="NavContent" style="background:{{{bg2|transparent}}};text-align:{{{ta2|left}}};{{{extra2|}}}{{{bodystyle|{{{contentstyle|{{{contentcss|}}}}}}}}}"><!--

-->}}</includeonly><noinclude>{{Documentation}}</noinclude>
```

## Provenance

Raw source: `bronze/pages/710/980.wikitext` · revision `980` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AHidden_begin)
