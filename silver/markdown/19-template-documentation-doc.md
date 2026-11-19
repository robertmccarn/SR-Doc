---
page_id: 19
revision_id: 19
source_url: https://second-renaissance.fandom.com/wiki/Template%3ADocumentation/doc
raw_sha256: 8388b06ea6cbc2f58afb4493cacd5509627ea3d2391f2af9f485dff7dd50b32e
---

# Template:Documentation/doc

## Preserved source

```wikitext
# Description
This template is used to insert descriptions on template pages.

# Syntax
Add <code><nowiki><noinclude></nowiki>{{t|documentation}}<nowiki></noinclude></nowiki></code> at the end of the template page.

# Usage
## On the Template page
This is the normal format when used:

<pre>
TEMPLATE CODE<includeonly>Any categories to be inserted into articles by the template</includeonly><noinclude>
{{documentation}}</noinclude>
</pre>

''If your template is not a completed div or table, you may need to close the tags just before <code><nowiki>{{documentation}}</nowiki></code> is inserted (within the noinclude tags).''

''A line break right before <code><nowiki>{{documentation}}</nowiki></code> can also be useful as it helps prevent the documentation template "running into" previous code.''

## On the Template/doc page
Normally, you will want to write something like the following on the documentation page:

<pre>
# Description
This template is used to do something.

# Syntax
Type <code>{{t|templatename}}</code> somewhere.

# Samples
<code>&lt;nowiki>{{templatename|input}}&lt;/nowiki></code> 

results in...

{{templatename|input}}

<includeonly>Any categories for the template itself</includeonly><noinclude>[{{PAGENAME}}](18-category-template-documentation.md)</noinclude>
</pre>

Use any or all of the above description/syntax/sample output sections. You may also want to add "see also" or other sections.

Note that the above example also uses the [Template:T](40-template-t.md) and [Template:T/piece](41-template-t-piece.md) templates.

<includeonly>[{{PAGENAME}}](8-category-templates.md)</includeonly><noinclude>[{{PAGENAME}}](18-category-template-documentation.md)</noinclude>
```

## Provenance

Raw source: `bronze/pages/19/19.wikitext` · revision `19` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ADocumentation/doc)
