---
page_id: 303
revision_id: 453
source_url: https://second-renaissance.fandom.com/wiki/Template%3ACountry_showdata
raw_sha256: 98734622de8facaf270db4e66b0a42ea973e30bc66dae11e00590ec5bcb9d02c
---

# Template:Country showdata

## Preserved source

```wikitext
<includeonly>__NOEDITSECTION__
{{documentation|content=<code>Template:{{PAGENAME}}</code> is an internal data container not intended to be transcluded directly. It is used indirectly by templates such as <code>[flag](https://second-renaissance.fandom.com/wiki/Template:flag)</code>, <code>[flagicon](https://second-renaissance.fandom.com/wiki/Template:flagicon)</code>, and others.

{{ombox|text=This template is within the scope of '''[WikiProject Flag Template](https://second-renaissance.fandom.com/wiki/Wikipedia:WikiProject_Flag_Template)''', a collaborative effort to maintain flag templates on Wikipedia.  A more thorough discussion of the flag template system, including parameters not described here, can be found on the project page.}}

[Flag of None.svg}}}|thumb|{{#if:{{{flag link|}}} | See also: [[{{{flag link}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias) | {{#ifexist: Flag of {{{alias}}} | See also: [Flag of {{{alias}}}](https://second-renaissance.fandom.com/wiki/Flag_of_{{{alias}}}) | }} }}]]
## Standard parameters
<table class="wikitable">
<tr><th>Parameter name</th><th>Value</th><th>Meaning</th>
</tr><tr>
<td><code>alias</code></td>
<td>{{#if: {{{alias|}}} | <code>{{{alias}}}</code> | <span style="color:red">'''undefined!'''</span> }}
<td>Main article name ([{{{alias}}}](https://second-renaissance.fandom.com/wiki/{{{alias}}}))</td>
</tr>
{{#if: {{{shortname alias|}}} |
<tr>
<td><code>shortname alias</code></td>
<td><code>{{{shortname alias}}}</code></td>
<td>''(optional)'' Display name to be used for the wikilink, if <code>alias</code> is a disambiguated article name, for example</td>
</tr>
}}
<tr>
<td><code>flag alias</code></td>
<td>{{#if: {{{flag alias|}}} | <code>{{{flag alias}}}</code> | <span style="color:red">'''undefined!'''</span> }}</td>
<td>Image name ([:File:{{{flag alias}}}](https://second-renaissance.fandom.com/wiki/:File:{{{flag_alias}}}), shown on right)</td>
</tr></table>
{{#if: {{{var1|{{{flag alias-naval|}}}}}} |
## Flag variants
{{#if:{{{flag link|}}} | {{details|{{{flag link}}}}} | {{#ifexist: Flag of {{{alias}}} | {{details|Flag of {{{alias}}}}} | }} }}
<table class="wikitable">
<tr><th>Label</th><th>Flag image (40px)</th><th>Image name</th></tr>
{{#if: {{{var1|}}} | <tr><td><code>{{{var1}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var1}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var1}}}}}})</td><td><code>{{{flag alias-{{{var1}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var2|}}} | <tr><td><code>{{{var2}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var2}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var2}}}}}})</td><td><code>{{{flag alias-{{{var2}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var3|}}} | <tr><td><code>{{{var3}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var3}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var3}}}}}})</td><td><code>{{{flag alias-{{{var3}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var4|}}} | <tr><td><code>{{{var4}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var4}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var4}}}}}})</td><td><code>{{{flag alias-{{{var4}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var5|}}} | <tr><td><code>{{{var5}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var5}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var5}}}}}})</td><td><code>{{{flag alias-{{{var5}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var6|}}} | <tr><td><code>{{{var6}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var6}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var6}}}}}})</td><td><code>{{{flag alias-{{{var6}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var7|}}} | <tr><td><code>{{{var7}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var7}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var7}}}}}})</td><td><code>{{{flag alias-{{{var7}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var8|}}} | <tr><td><code>{{{var8}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var8}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var8}}}}}})</td><td><code>{{{flag alias-{{{var8}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var9|}}} | <tr><td><code>{{{var9}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var9}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var9}}}}}})</td><td><code>{{{flag alias-{{{var9}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var10|}}} | <tr><td><code>{{{var10}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var10}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var10}}}}}})</td><td><code>{{{flag alias-{{{var10}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var11|}}} | <tr><td><code>{{{var11}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var11}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var11}}}}}})</td><td><code>{{{flag alias-{{{var11}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var12|}}} | <tr><td><code>{{{var12}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var12}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var12}}}}}})</td><td><code>{{{flag alias-{{{var12}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var13|}}} | <tr><td><code>{{{var13}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var13}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var13}}}}}})</td><td><code>{{{flag alias-{{{var13}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var14|}}} | <tr><td><code>{{{var14}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var14}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var14}}}}}})</td><td><code>{{{flag alias-{{{var14}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var15|}}} | <tr><td><code>{{{var15}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var15}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var15}}}}}})</td><td><code>{{{flag alias-{{{var15}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var16|}}} | <tr><td><code>{{{var16}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var16}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var16}}}}}})</td><td><code>{{{flag alias-{{{var16}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var17|}}} | <tr><td><code>{{{var17}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var17}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var17}}}}}})</td><td><code>{{{flag alias-{{{var17}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var18|}}} | <tr><td><code>{{{var18}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var18}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var18}}}}}})</td><td><code>{{{flag alias-{{{var18}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var19|}}} | <tr><td><code>{{{var19}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var19}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var19}}}}}})</td><td><code>{{{flag alias-{{{var19}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var20|}}} | <tr><td><code>{{{var20}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var20}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var20}}}}}})</td><td><code>{{{flag alias-{{{var20}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var21|}}} | <tr><td><code>{{{var21}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var21}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var21}}}}}})</td><td><code>{{{flag alias-{{{var21}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var22|}}} | <tr><td><code>{{{var22}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var22}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var22}}}}}})</td><td><code>{{{flag alias-{{{var22}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var23|}}} | <tr><td><code>{{{var23}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var23}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var23}}}}}})</td><td><code>{{{flag alias-{{{var23}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var24|}}} | <tr><td><code>{{{var24}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var24}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var24}}}}}})</td><td><code>{{{flag alias-{{{var24}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var25|}}} | <tr><td><code>{{{var25}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var25}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var25}}}}}})</td><td><code>{{{flag alias-{{{var25}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var26|}}} | <tr><td><code>{{{var26}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var26}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var26}}}}}})</td><td><code>{{{flag alias-{{{var26}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var27|}}} | <tr><td><code>{{{var27}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var27}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var27}}}}}})</td><td><code>{{{flag alias-{{{var27}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var28|}}} | <tr><td><code>{{{var28}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var28}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var28}}}}}})</td><td><code>{{{flag alias-{{{var28}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var29|}}} | <tr><td><code>{{{var29}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var29}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var29}}}}}})</td><td><code>{{{flag alias-{{{var29}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var30|}}} | <tr><td><code>{{{var30}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var30}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var30}}}}}})</td><td><code>{{{flag alias-{{{var30}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var31|}}} | <tr><td><code>{{{var31}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var31}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var31}}}}}})</td><td><code>{{{flag alias-{{{var31}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var32|}}} | <tr><td><code>{{{var32}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var32}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var32}}}}}})</td><td><code>{{{flag alias-{{{var32}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var33|}}} | <tr><td><code>{{{var33}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var33}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var33}}}}}})</td><td><code>{{{flag alias-{{{var33}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var34|}}} | <tr><td><code>{{{var34}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var34}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var34}}}}}})</td><td><code>{{{flag alias-{{{var34}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var35|}}} | <tr><td><code>{{{var35}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var35}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var35}}}}}})</td><td><code>{{{flag alias-{{{var35}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var36|}}} | <tr><td><code>{{{var36}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var36}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var36}}}}}})</td><td><code>{{{flag alias-{{{var36}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var37|}}} | <tr><td><code>{{{var37}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var37}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var37}}}}}})</td><td><code>{{{flag alias-{{{var37}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var38|}}} | <tr><td><code>{{{var38}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var38}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var38}}}}}})</td><td><code>{{{flag alias-{{{var38}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var39|}}} | <tr><td><code>{{{var39}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var39}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var39}}}}}})</td><td><code>{{{flag alias-{{{var39}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{var40|}}} | <tr><td><code>{{{var40}}}</code></td><td style="text-align:center;">[40px|{{{border-{{{var40}}}|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-{{{var40}}}}}})</td><td><code>{{{flag alias-{{{var40}}}}}}</code></td></tr> }}<!--
-->{{#if: {{{flag alias-naval|}}} | <tr><td><code>naval</code></td><td style="text-align:center;">[40px|{{{border-naval|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-naval}}})</td><td><code>{{{flag alias-naval}}}</code></td></tr> }}<!--
-->{{#if: {{{flag alias-air force|}}} | <tr><td><code>air force</code></td><td style="text-align:center;">[40px|{{{border-air force|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-air_force}}})</td><td><code>{{{flag alias-air force}}}</code></td></tr> }}<!--
-->{{#if: {{{flag alias-army|}}} | <tr><td><code>army</code></td><td style="text-align:center;">[40px|{{{border-army|{{{border|border}}}}}}](https://second-renaissance.fandom.com/wiki/File:{{{flag_alias-army}}})</td><td><code>{{{flag alias-army}}}</code></td></tr> }}<!--
--></table>
}}
{{#if: {{{flag alias-naval|}}}{{{link alias-naval|}}}{{{flag alias-air force|}}}{{{link alias-air force|}}}{{{flag alias-army|}}}{{{link alias-army|}}} |
## Military ensigns
{{#if: {{{flag alias-naval|}}} |
This template includes a naval ensign flag variant that can be used with [Template:Navy](581-template-navy.md):
* <code><nowiki>{{navy|</nowiki>{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}<nowiki>}}</nowiki></code> → {{navy|{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}}}
* <code><nowiki>{{flagicon|</nowiki>{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}<nowiki>|naval}}</nowiki></code> → {{flagicon|{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}|naval}}
| {{#if: {{{link alias-naval|}}} |
This nation's naval ensign is the same as its national flag, so [Template:Navy](581-template-navy.md) produces the following:
* <code><nowiki>{{navy|</nowiki>{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}<nowiki>}}</nowiki></code> → {{navy|{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}}}
}}}}
{{#if: {{{flag alias-air force|}}} |
This template includes an air force ensign flag variant that can be used with [Template:Air force](https://second-renaissance.fandom.com/wiki/Template:Air_force):
* <code><nowiki>{{air force|</nowiki>{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}<nowiki>}}</nowiki></code> → {{air force|{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}}}
* <code><nowiki>{{flagicon|</nowiki>{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}<nowiki>|air force}}</nowiki></code> → {{flagicon|{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}|air force}}
| {{#if: {{{link alias-air force|}}} |
This nation's air force ensign is the same as its national flag, so [Template:Air force](https://second-renaissance.fandom.com/wiki/Template:Air_force) produces the following:
* <code><nowiki>{{air force|</nowiki>{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}<nowiki>}}</nowiki></code> → {{air force|{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}}}
}}}}
{{#if: {{{flag alias-army|}}} |
This template includes an army ensign flag variant that can be used with [Template:Army](https://second-renaissance.fandom.com/wiki/Template:Army):
* <code><nowiki>{{army|</nowiki>{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}<nowiki>}}</nowiki></code> → {{army|{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}}}
* <code><nowiki>{{flagicon|</nowiki>{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}<nowiki>|army}}</nowiki></code> → {{flagicon|{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}|army}}
| {{#if: {{{link alias-army|}}} |
This nation's army ensign is the same as its national flag, so [Template:Army](https://second-renaissance.fandom.com/wiki/Template:Army) produces the following:
* <code><nowiki>{{army|</nowiki>{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}<nowiki>}}</nowiki></code> → {{army|{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}}}
}}}} }}
{{#if: {{{redir1|}}} |
## Redirect aliases
This template can also be used via an ''alias'' name (implemented as a redirect to this template):<!--
--><table class="wikitable"><!--
--><tr><th>Alias name</th><th>{{tlx|flag|''alias''}} output</th><th>{{tlx|flagcountry|''alias''}} output</th></tr>
{{#if: {{{redir1|}}} | <tr><td><code>{{{redir1}}}</code> (<span class="plainlinks">[{{fullurl:Template:Country data {{{redir1}}}|redirect=no}} view]</span>)</td><td>{{flag|{{{redir1}}}}}</td><td>{{flagcountry|{{{redir1}}}}}</td></tr> }}<!--
-->{{#if: {{{redir2|}}} | <tr><td><code>{{{redir2}}}</code> (<span class="plainlinks">[{{fullurl:Template:Country data {{{redir2}}}|redirect=no}} view]</span>)</td><td>{{flag|{{{redir2}}}}}</td><td>{{flagcountry|{{{redir2}}}}}</td></tr> }}<!--
-->{{#if: {{{redir3|}}} | <tr><td><code>{{{redir3}}}</code> (<span class="plainlinks">[{{fullurl:Template:Country data {{{redir3}}}|redirect=no}} view]</span>)</td><td>{{flag|{{{redir3}}}}}</td><td>{{flagcountry|{{{redir3}}}}}</td></tr> }}<!--
-->{{#if: {{{redir4|}}} | <tr><td><code>{{{redir4}}}</code> (<span class="plainlinks">[{{fullurl:Template:Country data {{{redir4}}}|redirect=no}} view]</span>)</td><td>{{flag|{{{redir4}}}}}</td><td>{{flagcountry|{{{redir4}}}}}</td></tr> }}<!--
-->{{#if: {{{redir5|}}} | <tr><td><code>{{{redir5}}}</code> (<span class="plainlinks">[{{fullurl:Template:Country data {{{redir5}}}|redirect=no}} view]</span>)</td><td>{{flag|{{{redir5}}}}}</td><td>{{flagcountry|{{{redir5}}}}}</td></tr> }}<!--
--></table>
See [{{fullurl:Special:WhatLinksHere/{{FULLPAGENAMEE}}|hidelinks=1&hidetrans=1}} What links here] for a full list of redirects.
}}
## Example usage
* <code><nowiki>{{flag|</nowiki>{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}<nowiki>}}</nowiki></code> → {{flag|{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}}}
* <code><nowiki>{{flagicon|</nowiki>{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}<nowiki>}}</nowiki></code> → {{flagicon|{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}}}<!--
-->{{#if: {{{shortname alias|}}} |
* <code><nowiki>{{flagcountry|</nowiki>{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}<nowiki>}}</nowiki></code> → {{flagcountry|{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}}} }}
{{#if: {{{var1|}}} |
### Using a flag variant
* <code><nowiki>{{flag|</nowiki>{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}<nowiki>|</nowiki>{{{var1}}}<nowiki>}}</nowiki></code> → {{flag|{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}|{{{var1}}}}}
* <code><nowiki>{{flagicon|</nowiki>{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}<nowiki>|</nowiki>{{{var1}}}<nowiki>}}</nowiki></code> → {{flagicon|{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}|{{{var1}}}}}
}}
{{#if: {{{redir1|}}} |
### Using a redirect alias
* <code><nowiki>{{flagicon|</nowiki>{{{redir1}}}<nowiki>}}</nowiki></code> → {{flagicon|{{{redir1}}}}}
* <code><nowiki>{{flagcountry|</nowiki>{{{redir1}}}<nowiki>}}</nowiki></code> → {{flagcountry|{{{redir1}}}}}
* <code><nowiki>{{flag|</nowiki>{{{redir1}}}<nowiki>}}</nowiki></code> → {{flag|{{{redir1}}}}}
}}
{{#if: {{{related1|}}} |
## Related templates
Please see the following related <code>country_data</code> templates:
* [Template:Country data {{{related1}}}](https://second-renaissance.fandom.com/wiki/Template:Country_data_{{{related1}}})<span style="position:absolute; left:33em;">{{flag|{{{related1}}}<!-- {{#if:{{{related1param|}}}|{{!}}{{{related1param}}}}} -->}}</span><!--
-->{{#if: {{{related2|}}} |
* [Template:Country data {{{related2}}}](https://second-renaissance.fandom.com/wiki/Template:Country_data_{{{related2}}})<span style="position:absolute; left:33em;">{{flag|{{{related2}}}<!-- {{#if:{{{related2param|}}}|{{!}}{{{related2param}}}}} -->}}</span> }}<!--
-->{{#if: {{{related3|}}} |
* [Template:Country data {{{related3}}}](https://second-renaissance.fandom.com/wiki/Template:Country_data_{{{related3}}})<span style="position:absolute; left:33em;">{{flag|{{{related3}}}<!-- {{#if:{{{related3param|}}}|{{!}}{{{related3param}}}}} -->}}</span> }}<!--
-->{{#if: {{{related4|}}} |
* [Template:Country data {{{related4}}}](https://second-renaissance.fandom.com/wiki/Template:Country_data_{{{related4}}})<span style="position:absolute; left:33em;">{{flag|{{{related4}}}<!-- {{#if:{{{related4param|}}}|{{!}}{{{related4param}}}}} -->}}</span> }}<!--
-->{{#if: {{{related5|}}} |
* [Template:Country data {{{related5}}}](https://second-renaissance.fandom.com/wiki/Template:Country_data_{{{related5}}})<span style="position:absolute; left:33em;">{{flag|{{{related5}}}<!-- {{#if:{{{related5param|}}}|{{!}}{{{related5param}}}}} -->}}</span> }}<!--
-->{{#if: {{{related6|}}} |
* [Template:Country data {{{related6}}}](https://second-renaissance.fandom.com/wiki/Template:Country_data_{{{related6}}})<span style="position:absolute; left:33em;">{{flag|{{{related6}}}<!-- {{#if:{{{related6param|}}}|{{!}}{{{related6param}}}}} -->}}</span> }}<!--
-->}}
{{#ifexist:{{FULLPAGENAME}}/doc |
## Other information
{{{{FULLPAGENAME}}/doc|alias={{{alias|}}}|cat={{{cat|}}}}}
}}

## TemplateData
{{TemplateDataHeader}}
<templatedata>
{
  "description": "This template should not be used directly. It is used indirectly by flag templates such as Template:Flag and Template:Flagicon. See Category:Flag template system for a full list of flag templates and Wikipedia:WikiProject Flag Template for further documentation.",
  "params": {}
}
</templatedata>

{{#ifeq:{{NAMESPACE}}|{{ns:Template}}|<!--
  -->[{{{cat|{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}}}}](https://second-renaissance.fandom.com/wiki/Category:All_country_data_templates)<!--
  -->{{#if:{{{shortname alias|}}}|<!--
    -->[{{{cat|{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}}}}](https://second-renaissance.fandom.com/wiki/Category:Country_data_templates_with_distinct_shortname)<!--
  -->}}<!--
  -->{{#ifeq:{{PAGENAME}}|Country data {{{alias}}}||<!--
    -->{{#ifeq:{{PAGENAME}}|Country data {{{shortname alias}}}||<!--
      -->[{{{cat|{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}}}}](https://second-renaissance.fandom.com/wiki/Category:Country_data_templates_with_distinct_template_name)<!--
    -->}}<!--
  -->}}<!--
-->{{#ifeq:{{SUBPAGENAME}}|sandbox|<!--
  -->[{{{cat|{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}}}}](https://second-renaissance.fandom.com/wiki/Category:Country_data_template_sandboxes)|<!--
  -->{{#ifexist:{{FULLPAGENAME}}/doc|<!--
    -->[{{{cat|{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}}}}](https://second-renaissance.fandom.com/wiki/Category:Country_data_templates_with_documentation_subpage)|<!--
    -->[{{{cat|{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}}}}](https://second-renaissance.fandom.com/wiki/Category:Uncategorized_country_data_templates)<!--
    -->}}<!--
  -->{{#if:{{{size|}}}|[{{{cat|{{{templatename|{{Str right|{{BASEPAGENAME}}|13}}}}}}}}](https://second-renaissance.fandom.com/wiki/Category:Country_data_templates_with_distinct_default_size)<!--
    -->}}<!--
  -->}}<!--
-->}}<!--
-->{{#if:{{{templatename|}}}|[{{{cat|{{{templatename|}}}}}}](https://second-renaissance.fandom.com/wiki/Category:Country_data_templates_with_templatename_parameter)}}
|link box=This is the documentation for '''Template:{{PAGENAME}}'''. It is automatically generated by [Template:Country showdata](303-template-country-showdata.md).<br />Please {{purge|purge the cache}} after making any changes to this template.<!--
-->{{#ifexist:{{FULLPAGENAME}}/doc|<!--
  --><br />This template has a [/doc](https://second-renaissance.fandom.com/wiki/{{FULLPAGENAME}}/doc) subpage for the purposes of [categories](https://second-renaissance.fandom.com/wiki/WP:CAT) and documentation specific to this template.|<!--
  -->{{#switch:{{PROTECTIONLEVEL:edit}}|sysop|templateeditor=<!--
    --><br />This template is [{{#ifeq:{{PROTECTIONLEVEL:edit}}|sysop|fully protected|template-protected}}](https://second-renaissance.fandom.com/wiki/WP:PROTECT) and any [categories](https://second-renaissance.fandom.com/wiki/WP:CAT) should be added to the template's [{{fullurl:{{FULLPAGENAME}}/doc|action=edit&preload=Template:Category_interwiki/preload}} /doc] subpage, which is not protected.|#default=<!--
    --><br />Any [categories](https://second-renaissance.fandom.com/wiki/WP:CAT) should be added to the template's [{{fullurl:{{FULLPAGENAME}}/doc|action=edit&preload=Template:Category_interwiki/preload}} /doc] subpage, which does not exist yet.<!--
  -->}}<!--
-->}}
}}</includeonly><noinclude>
{{documentation}}
</noinclude>
```

## Provenance

Raw source: `bronze/pages/303/453.wikitext` · revision `453` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ACountry_showdata)
