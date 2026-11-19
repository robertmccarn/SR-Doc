---
page_id: 704
revision_id: 974
source_url: https://second-renaissance.fandom.com/wiki/Template%3ATag
raw_sha256: 59d4df4de51de30e62484193b1c1fadc78263740b0fff1ab48b75c4a7aaebdba
---

# Template:Tag

## Preserved source

```wikitext
<code class="{{#ifeq:{{{wrap|}}}|yes|wrap|nowrap}}" style="{{#ifeq:{{{style|}}}|plain|border:none;background:transparent;|{{{style|}}}}}"><!--
 Opening tag
-->{{#switch:{{{2|pair}}}
  |c|close =
  |s|single
  |o|open
  |p|pair = &lt;{{{1|tag}}}{{#if:{{{params|}}}|&#32;{{{params}}}}}
 }}<!--
 Content between tags
-->{{#switch:{{{2|pair}}}
  |c|close = {{{content|}}}
  |s|single = &#32;&#47;&gt;
  |o|open = &gt;{{{content|}}}
  |p|pair = {{#ifeq:{{{1|tag}}}|!--||&gt;}}{{{content|...}}}
 }}<!--
 Closing tag
-->{{#switch:{{{2|pair}}}
  |s|single
  |o|open =
  |c|close
  |p|pair = {{#ifeq:{{{1|tag}}}|!--|--&gt;|&lt;&#47;{{{1|tag}}}&gt;}}
 }}<!--
--></code><noinclude>
{{Documentation}}
</noinclude>
```

## Provenance

Raw source: `bronze/pages/704/974.wikitext` · revision `974` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ATag)
