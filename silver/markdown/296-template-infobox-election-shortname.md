---
page_id: 296
revision_id: 445
source_url: https://second-renaissance.fandom.com/wiki/Template%3AInfobox_election/shortname
raw_sha256: cdc3040c7530e4d212db8c7594dc81372016557d51bdcd4af96e870596da1041
---

# Template:Infobox election/shortname

## Preserved source

```wikitext
{{#if:{{{name|}}}
  |{{#ifeq:{{{link}}}|no
     |{{{name}}}
     |{{#ifexist:Template:{{{name}}}/meta/shortname
       |[{{Template: {{{name}}}/meta/shortname}}](https://second-renaissance.fandom.com/wiki/{{{name}}})
       |{{{name}}}
      }}
   }}
}}<noinclude>
{{documentation|content=
This is a subtemplate of {{tl|Infobox election}}, it should not be used directly.

# Purpose
This subtemplate takes two inputs, <code>name</code> and <code>link</code>.  If link is set to <code>no</code>, then it returns the value of <code>name</code> verbatim.  Otherwise, if the corresponding {{tld|{{{name}}}/meta/shortname}} template exists, it returns <code><nowiki>[shortname](https://second-renaissance.fandom.com/wiki/{{{name}}})</nowiki></code> where <code>shortname</code> is the output of the {{tld|{{{name}}}/meta/shortname}} template.  If this template does not exist, it returns the value of <code>name</code> verbatim. 
}}</noinclude>
```

## Provenance

Raw source: `bronze/pages/296/445.wikitext` · revision `445` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AInfobox_election/shortname)
