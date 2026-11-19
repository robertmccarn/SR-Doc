---
page_id: 227
revision_id: 304
source_url: https://second-renaissance.fandom.com/wiki/Template%3ACss_Image_Crop
raw_sha256: 1c4aa4c6fa70550c79277a06cc27d5b0e2d6af788aa2e8675ff261be41d7ea44
---

# Template:Css Image Crop

## Preserved source

```wikitext
<includeonly><div class="{{#if:{{{Description|}}}|thumb <!--
-->{{#switch:{{{Location|}}}
 | none | tnone = tnone
 | left | tleft = tleft
 | right | tright = tright
 | center = center
 | #default = tright }}|<!-- if no description:
-->{{#switch:{{{Location|}}}
 | none = floatnone
 | left = floatleft
 | right = floatright
 | center = center }}}}">
{{#if:{{{Description|}}}|<div class="thumbinner" style="width: {{{cWidth}}}px;">}}
<div style="width: {{{cWidth}}}px; height: {{{cHeight}}}px; overflow: hidden;">
<div style="position: relative; top: -{{{oTop}}}px; left: -{{{oLeft}}}px; width: {{{bSize}}}px"><!--
-->[{{{bSize}}}px|alt={{{Alt|{{{Description|{{{Image}}}}}}}}}{{#if:{{{Link|}}}|{{!}}link={{{Link}}}}}{{#if:{{{Page|}}}|{{!}}page={{{Page}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{Image}}})<!--
--></div>
{{#if:{{{Description|}}}|</div>
<div class="thumbcaption">
<div class="magnify">[}}}|{{{magnify-link}}}|File:{{{Image}}}}}](https://second-renaissance.fandom.com/wiki/:{{)</div>{{{Description}}}
</div>}}
</div>
</div>{{#ifeq:1|{{ifnumber|{{{cWidth|}}}{{{cHeight|}}}{{{oTop|}}}{{{oLeft|}}}{{{bSize|}}}}}||[Category:CSS image crop using invalid parameters](https://second-renaissance.fandom.com/wiki/Category:CSS_image_crop_using_invalid_parameters)}}</includeonly><noinclude>
{{documentation}}
</noinclude>
```

## Provenance

Raw source: `bronze/pages/227/304.wikitext` · revision `304` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ACss_Image_Crop)
