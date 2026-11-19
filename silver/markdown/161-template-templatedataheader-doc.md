---
page_id: 161
revision_id: 217
source_url: https://second-renaissance.fandom.com/wiki/Template%3ATemplateDataHeader/doc
raw_sha256: cb27f769160624f4c9af2bc984716838ebe038b536e53b6a00b5b1b0cde21a7c
---

# Template:TemplateDataHeader/doc

## Preserved source

```wikitext
{{Documentation subpage}}
<!-- Categories go at the bottom of this page and interwikis go in Wikidata. -->

Inserts a brief header for the template data section. Adds the page to [:Category:TemplateData documentation](https://second-renaissance.fandom.com/wiki/:Category:TemplateData_documentation).

# Usage
<pre>
# TemplateData== or ==Parameters== or ==Usage
{{TemplateDataHeader}}
<templatedata>{
...
}</templatedata>
</pre>

Use <code><nowiki>{{TemplateDataHeader|Template name}}</nowiki></code> if you want an alternative name for the template to be displayed.

# Parameters
{{TemplateDataHeader}}
<templatedata>{
  "description": "Inserts a brief header for the template data section. Adds the page to [Category:TemplateData documentation](https://second-renaissance.fandom.com/wiki/Category:TemplateData_documentation)",
  "params": {
    "1": {
      "label": "Template name",
      "description": "The name of the template to display. Default is {{BASEPAGENAME}}.",
      "type": "string",
      "required": false
    }
  }
}</templatedata>

# See also
<includeonly>
<!-- Categories go here, and interwikis go in Wikidata -->

</includeonly>
```

## Provenance

Raw source: `bronze/pages/161/217.wikitext` · revision `217` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ATemplateDataHeader/doc)
