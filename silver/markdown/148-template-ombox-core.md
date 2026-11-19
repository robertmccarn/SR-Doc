---
page_id: 148
revision_id: 202
source_url: https://second-renaissance.fandom.com/wiki/Template%3AOmbox/core
raw_sha256: 3e895864ca01f61c6f4fe49550d42b445073fc0fc1d452ef6a23ccf7b108e79d
---

# Template:Ombox/core

## Preserved source

```wikitext
<table class="plainlinks ombox {{#ifeq:{{{small}}}|yes|mbox-small}} 
{{#switch:{{{type|}}}
| speedy     = ombox-speedy
| delete     = ombox-delete
| content    = ombox-content
| style      = ombox-style
| move       = ombox-move
| protection = ombox-protection
| notice          <!-- notice = default -->
| #default   = ombox-notice
}}" style="{{{style|}}}">
<tr>
{{#ifeq:{{{image|}}}|none
| <!-- No image. Cell with some width or padding necessary for text cell to have 100% width. --><td class="mbox-empty-cell"></td>
| <td class="mbox-image">
  {{#if:{{{image|}}}
  | {{{image}}}
  | [}}}
    | speedy     = Imbox speedy deletion.png
    | delete     = Imbox deletion.png
    | content    = Imbox content.png
    | style      = Edit-clear.svg
    | move       = Imbox move.png
    | protection = Imbox protection.png
    | notice          <!-- notice = default -->
    | #default   = Imbox notice.png
    }} | {{#ifeq:{{{small|}}}|yes
    | 30x30px
    | 40x40px
    }}|link=|alt=](https://second-renaissance.fandom.com/wiki/Image:{{)
  }}</td>
}}
<td class="mbox-text" style="{{{textstyle|}}}"> {{{text}}} </td>
{{#if:{{{imageright|}}}
| {{#ifeq:{{{imageright|}}}|none
  | <!-- No image. -->
  | <td class="mbox-imageright"> {{{imageright}}} </td>
  }}
}}
</tr>
</table><!-- Detect and report usage with faulty "type" parameter:
-->{{#switch:{{{type|}}}
|   <!-- No type fed, is also valid input -->
| speedy
| delete
| content
| style
| move
| protection
| notice     =    <!-- Do nothing, valid "type" -->
| #default   = <div style="text-align: center;">This message box is using an invalid "type={{{type|}}}" parameter and needs fixing.</div>[{{main other|Main:}}{{FULLPAGENAME}}](https://second-renaissance.fandom.com/wiki/Category:Wikipedia_message_box_parameter_needs_fixing)<!-- Sort on namespace -->
}}<noinclude>
```

## Provenance

Raw source: `bronze/pages/148/202.wikitext` · revision `202` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AOmbox/core)
