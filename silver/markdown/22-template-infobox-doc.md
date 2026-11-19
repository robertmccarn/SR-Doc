---
page_id: 22
revision_id: 22
source_url: https://second-renaissance.fandom.com/wiki/Template%3AInfobox/doc
raw_sha256: ec73ae9cb7faf6f5cca41c832385e319c3ece4916aa6933efa9b389a2c71871d
---

# Template:Infobox/doc

## Preserved source

```wikitext
# Description
This template is a sample infobox, to aid in the creation of new infoboxes.

Recommended usage: copy the template code to a new template page, and edit it there.

## Infobox and template background
See [Help:Templates](https://second-renaissance.fandom.com/wiki/Help:Templates), [Help:Infobox](https://second-renaissance.fandom.com/wiki/Help:Infobox) and [Help:Tables](https://second-renaissance.fandom.com/wiki/Help:Tables) for some background on how templates and infoboxes work.

## Building blocks
The infobox is made of the following basic building blocks:

* Overall table class: <code>class="wikia-infobox"</code>
* Table heading cell class: <code>class="wikia-infobox-header"</code>
* Use row header marks ("<code>!</code>") for row title cells ''(and "<code>|</code>" for normal cells)''
* Section separator line: give the header below it a wrapping <code>div</code> with <code>class="wikia-infobox-section-header"</code>
* Image cell class: <code>class="wikia-infobox-image"</code>
* Image caption cell class: <code>class="wikia-infobox-caption"</code>

## Other notes
* The Title, First, Second, and Third rows show ''"Unknown"'' if their values are not specified.
* The Image, Imagecaption, Fourth, Fifth, and Sixth rows won't show up if their values are not specified: they are each completely enclosed in an 'if' statement.

# Syntax
<pre>
{{infobox
 | title         = 
 | image         = [e.g. "Example.jpg"]
 | imagewidth    = [e.g. "150"] [default: 210 pixels]
 | imagecaption  = 
 | first         =
 | second        =
 | third         =
 | fourth        =
 | fifth         =
 | sixth         =
}}
</pre>

# Samples
<pre>
{{infobox
 | title         = A pretty flower
 | image         = Example.jpg
 | imagewidth    = 100
 | imagecaption  = Floweris flowerum
 | first         = Pink and green
 | second        = Outdoors
 | fourth        = Annual
}}
</pre>

Results in...

{{infobox
 | title         = A pretty flower
 | image         = Example.jpg
 | imagewidth    = 100
 | imagecaption  = Floweris flowerum
 | first         = Pink and green
 | second        = Outdoors
 | fourth        = Annual
}}

<includeonly>[{{PAGENAME}}](8-category-templates.md)</includeonly><noinclude>[{{PAGENAME}}](18-category-template-documentation.md)</noinclude>
```

## Provenance

Raw source: `bronze/pages/22/22.wikitext` · revision `22` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AInfobox/doc)
