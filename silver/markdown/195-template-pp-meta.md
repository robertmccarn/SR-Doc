---
page_id: 195
revision_id: 253
source_url: https://second-renaissance.fandom.com/wiki/Template%3APp-meta
raw_sha256: dbc78def243b26b126a48c190df750b8a62c3705b547dfc76e7dec174e6cd341
---

# Template:Pp-meta

## Preserved source

```wikitext
{{#ifeq:{{#switch:{{lc:{{{type}}}}}
  |move=<!--
 -->{{#ifeq:
      {{#switch:{{lc:{{{demolevel|undefined}}}}}
        |semi |autoconfirmed           = autoconfirmed
        |administrator |full |sysop    = sysop
        |undefined                     = {{PROTECTIONLEVEL:move}}
        |#default                      = <!--fallback value: null
   -->}}
      |sysop|yes|no
    }}
  |create=<!--
 -->{{#if:
      {{#switch:{{lc:{{{demolevel|undefined}}}}}
        |semi |autoconfirmed           = autoconfirmed
        |administrator |full |sysop    = sysop
        |undefined                     = {{PROTECTIONLEVEL:create}}
        |#default                      = <!--fallback value: null
   -->}}
      |yes|no
    }}
  |template=<!--
 -->{{#if:
      {{#switch:{{lc:{{{demolevel|undefined}}}}}
        |templateeditor |template      = templateeditor
        |administrator |full |sysop    = sysop
        |undefined                     = {{PROTECTIONLEVEL:edit}}
        |#default                      = <!--fallback value: null
   -->}}
      |yes|no
    }}
  |pc1 =<!--
 -->{{#ifeq:
      {{#switch:{{lc:{{{demolevel|undefined}}}}}
        |pc1                           = autoconfirmed <!-- this is the value that the PENDINGCHANGELEVEL magic word returns for pc1 -->
        |undefined                     = {{PENDINGCHANGELEVEL}}
        |#default                      = <!--fallback value: null
   -->}}
      |autoconfirmed
      |yes|no
    }}
  |pc2 =<!--
 -->{{#ifeq:
      {{#switch:{{lc:{{{demolevel|undefined}}}}}
        |pc2                           = review <!-- this is the value that the PENDINGCHANGELEVEL magic word returns for pc2 -->
        |undefined                     = {{PENDINGCHANGELEVEL}}
        |#default                      = <!--fallback value: null
   -->}}
      |review
      |yes|no
    }}
|#default<!--includes all other types-->=<!--
 -->{{#if:
      {{#switch:{{lc:{{{demolevel|undefined}}}}}
        |semi |autoconfirmed           = autoconfirmed
        |administrator |full |sysop    = sysop
        |undefined                     = {{PROTECTIONLEVEL:edit}}
        |#default                      = <!--fallback value: null
   -->}}
      |{{#ifeq:{{#switch:{{lc:{{{disallowlevel|}}}}}
                 |semi |autoconfirmed           = autoconfirmed
                 |administrator |full |sysop    = sysop
                 |#default                      = <!--fallback value: null-->}}
         |{{#switch:{{lc:{{{demolevel|undefined}}}}}
            |semi |autoconfirmed           = autoconfirmed
            |administrator |full |sysop    = sysop
            |undefined                     = {{PROTECTIONLEVEL:edit}}
            |#default                      = <!--fallback value: null
       -->}}
         |no|yes
       }}
   |no}}
}}|yes|{{#ifeq:{{lc:{{{small|}}}}}|yes|
<div class="metadata topicon nopopups" id="protected-icon" style="display:none; right:{{#if:{{{right|}}}|{{{right}}}|55px}};">[{{#switch:{{lc:{{{type}}}}}
 |full=Padlock.svg
 |semi=Padlock-silver.svg
 |template=Padlock-pink.svg
 |pc1=Padlock-silver-light.svg
 |pc2=Padlock-orange.svg
 |move=Padlock-olive.svg
 |indef=Padlock-red.svg
 |office=Padlock-black.svg
 |create=Padlock-skyblue.svg
 |#default=Transparent.gif
}}}}}|20px|link={{{icon-link|Wikipedia:Protection policy#{{lc:{{{type}}}}}}}}|{{{icon-text|{{#switch:{{lc:{{{type}}}}}
|pc1 = All edits by unregistered and new users are subject to review
|pc2 = All edits by users who are not reviewers or administrators are subject to review
|template = This is a permanently protected {{pp-meta/pagetype}}
|#default = This {{pp-meta/pagetype}} is {{#switch:{{lc:{{{type}}}}}
  |semi=semi-
  |move=move-
  |indef=permanently<nowiki> </nowiki>
  |create=creation-
  |office=<!--null, but should this have a special tag?-->
  |full
  |#default=<!--null-->
  }}protected
}}{{#ifeq:{{lc:{{{type}}}}}|indef||{{#if:{{{expiry|}}}|<nowiki> </nowiki>until {{#time:F j, Y|{{{expiry}}}}}{{#if:{{{icon-reason|}}}|,}}}}}}{{#if:{{{icon-reason|}}}|<nowiki> </nowiki>{{{icon-reason}}}}}.}}}|alt={{#ifeq:{{lc:{{{type}}}}}|template
 |{{#switch:{{NAMESPACENUMBER}}
   |10|828=Permanently protected {{pp-meta/pagetype}}
   |#default=Page permanently protected
  }}
 |Page {{#switch:{{lc:{{{type}}}}}
          |pc1=protected with pending changes level 1
          |pc2=protected with pending changes level 2
          |semi=semi-protected
          |move=move-protected
          |indef=permanently protected
          |create=creation-protected
          |office=<!--null, but should this have a special tag?-->
          |full
          |#default=protected
       }}
}}](https://second-renaissance.fandom.com/wiki/Image:{{{image)</div>
|<!-- else, not small -->
{{mbox 
| name = {{{name|Pp-meta}}}
| subst = {{{subst|}}}
| demospace = {{{demospace|}}}
| type = protection
| image = [{{#switch:{{lc:{{{type}}}}}
 |full=Padlock.svg
 |semi=Padlock-silver.svg
 |pc1=Padlock-silver-light.svg
 |pc2=Padlock-orange.svg
 |move=Padlock-olive.svg
 |template=Padlock-pink.svg
 |indef=Padlock-red.svg
 |office=Padlock-black.svg
 |create=Padlock-skyblue.svg
 |#default=Transparent.gif
}}}}}|40px|{{{icon-text|{{#ifeq:{{lc:{{{type}}}}}|template
                         |{{#switch:{{NAMESPACENUMBER}}
                           |10|828=This is a permanently protected {{pp-meta/pagetype}}
                           |#default=This page is permanently protected
                          }}
                         |This page is {{#switch:{{lc:{{{type}}}}}
                                        |pc1=protected with pending changes level 1
                                        |pc2=protected with pending changes level 2
                                        |semi=semi-protected
                                        |move=move-protected
                                        |indef=permanently protected
                                        |create=creation-protected
                                        |office=protected<!--should this have a special tag?-->
                                        |full
                                        |#default=protected
                                       }}
                        }}.}}}](https://second-renaissance.fandom.com/wiki/Image:{{{image)
| text = '''{{{reason-text|{{#switch:{{lc:{{{type}}}}}
 |full=This {{pp-meta/pagetype}} is currently [protected](https://second-renaissance.fandom.com/wiki/Help:Protection) from editing
 |semi=Editing of this {{pp-meta/pagetype}} by [new](https://second-renaissance.fandom.com/wiki/Wikipedia:User_access_levels) or [unregistered](https://second-renaissance.fandom.com/wiki/Wikipedia:User_access_levels) users is currently [disabled](https://second-renaissance.fandom.com/wiki/Help:Protection)
 |pc1=All edits made to this {{pp-meta/pagetype}} by [new](https://second-renaissance.fandom.com/wiki/Wikipedia:User_access_levels) or [unregistered](https://second-renaissance.fandom.com/wiki/Wikipedia:User_access_levels) users are currently [subject to review](https://second-renaissance.fandom.com/wiki/Wikipedia:Pending_changes)
 |pc2=All edits made to this {{pp-meta/pagetype}} by users who are not [reviewers](https://second-renaissance.fandom.com/wiki/Wikipedia:Reviewing) or [administrators](https://second-renaissance.fandom.com/wiki/Wikipedia:Administrators) are currently [subject to review](https://second-renaissance.fandom.com/wiki/Wikipedia:Pending_changes)
 |move=This {{pp-meta/pagetype}} is currently [protected](https://second-renaissance.fandom.com/wiki/Help:Protection) from [page moves](https://second-renaissance.fandom.com/wiki/Help:Moving_a_page)
 |template=This is a permanently [protected](https://second-renaissance.fandom.com/wiki/Help:Protection) {{pp-meta/pagetype}}, as it is [high-risk](https://second-renaissance.fandom.com/wiki/Wikipedia:High-risk_templates)
 |indef=This page is [protected](https://second-renaissance.fandom.com/wiki/Help:Protection) from editing ''indefinitely''
 |office=This {{pp-meta/pagetype}} is currently [protected](https://second-renaissance.fandom.com/wiki/Help:Protection) from editing
 |create=[Recreation](https://second-renaissance.fandom.com/wiki/Help:Starting_a_new_page) of this {{pp-meta/pagetype}} [has been disabled](https://second-renaissance.fandom.com/wiki/Help:Protection)
}}{{#ifeq:{{lc:{{{type}}}}}|indef||{{#if:{{{expiry|}}}|&#32;until {{#time:F j, Y|{{{expiry}}}}}{{#if:{{{reason|}}}|,}}}}}}{{{reason<includeonly>|</includeonly>}}}.}}}'''<br /> {{{explanation-text|{{#ifeq:{{lc:{{{dispute}}}}}|yes|This protection is '''not''' an endorsement of the {{#ifeq:{{{type}}}|move|[{{fullurl:Special:Log|type=move&page={{FULLPAGENAMEE}}}} current title]|[{{fullurl:{{FULLPAGENAMEE}}|action=history}} current version]}}.}} See the [protection policy](https://second-renaissance.fandom.com/wiki/Wikipedia:Protection_policy) and [{{fullurl:Special:Log|type={{#switch:{{lc:{{{type}}}}} | pc1 | pc2 = stable | #default = protect }}&page={{FULLPAGENAMEE}}}} {{#switch:{{lc:{{{type}}}}} | pc1 | pc2 = pending changes | #default = protection }} log] for more details. {{#switch:{{lc:{{{type}}}}}
 |full|indef=Please discuss any changes on the [}}}|{{{section}}}|top}}|talk page](https://second-renaissance.fandom.com/wiki/{{TALKPAGENAME}}); you may {{Submit an edit request/link|display=submit a request}} to ask an [administrator](https://second-renaissance.fandom.com/wiki/Wikipedia:Administrators) to make an edit if it is [uncontroversial](https://second-renaissance.fandom.com/wiki/Help:Minor_edit) or supported by [consensus](https://second-renaissance.fandom.com/wiki/Wikipedia:Consensus). {{#ifeq:{{NAMESPACE}}|{{ns:8}}<!--MediaWiki-->||You may also [request](https://second-renaissance.fandom.com/wiki/Wikipedia:Requests_for_page_protection) that this page be unprotected.}}
 |semi=If you cannot edit this {{pp-meta/pagetype}} and you wish to make a change, you can {{#ifeq:{{NAMESPACE}}|{{TALKSPACE}}||{{submit an edit request/link|type=semi|display=request an edit}}, [discuss changes on the talk page](https://second-renaissance.fandom.com/wiki/{{TALKPAGENAME}}),}} [request unprotection](https://second-renaissance.fandom.com/wiki/Wikipedia:Requests_for_page_protection), [log in](https://second-renaissance.fandom.com/wiki/Special:Userlogin), or [create an account](https://second-renaissance.fandom.com/wiki/Special:UserLogin/signup).
 |move=The page may still be edited but cannot be moved until unprotected. Please discuss any suggested moves on the [talk page](https://second-renaissance.fandom.com/wiki/{{TALKPAGENAME}}) or at [Wikipedia:Requested moves](https://second-renaissance.fandom.com/wiki/Wikipedia:Requested_moves).  You can also [request](https://second-renaissance.fandom.com/wiki/Wikipedia:Requests_for_page_protection) that the page be unprotected.  
 |template=Please discuss any changes on the [}}}|{{{section}}}|top}}|talk page](https://second-renaissance.fandom.com/wiki/{{TALKPAGENAME}}); you may {{Submit an edit request/link|type=template|display=submit a request}} to ask an [administrator](https://second-renaissance.fandom.com/wiki/Wikipedia:Administrators) or [template editor](https://second-renaissance.fandom.com/wiki/Wikipedia:Template_editor) to make an edit if it is [uncontroversial](https://second-renaissance.fandom.com/wiki/Help:Minor_edit) or supported by [consensus](https://second-renaissance.fandom.com/wiki/Wikipedia:Consensus). {{#ifeq:{{NAMESPACE}}|{{ns:8}}<!--MediaWiki-->||You may also [request](https://second-renaissance.fandom.com/wiki/Wikipedia:Requests_for_page_protection) that this page be unprotected.}}
 |office=If you can edit this page, please discuss all changes and additions on the [talk page](https://second-renaissance.fandom.com/wiki/{{TALKPAGENAME}}) first. '''Do not remove protection from this page unless you are authorized by the Wikimedia Foundation to do so.'''
 |create=Please see the {{#if:{{{xfd|}}}|'''[deletion discussion](https://second-renaissance.fandom.com/wiki/{{{xfd}}})''' or the}} [{{fullurl:Special:Log|type=delete&page={{FULLPAGENAMEE}}}} deletion log] for details of why this page was deleted. If you would like to create a page at this title, you must first [request](https://second-renaissance.fandom.com/wiki/Wikipedia:Requests_for_page_protection) for it to be unprotected, or contact the administrator who deleted the page for the deleted material to be restored. If unsuccessful, you can use [deletion review](https://second-renaissance.fandom.com/wiki/Wikipedia:Deletion_review).
}}}}}
}}
}}|{{#ifeq:{{FULLPAGENAME}}|Template:Pp-meta|<!--nothing-->|[Category:Wikipedia pages with incorrect protection templates](https://second-renaissance.fandom.com/wiki/Category:Wikipedia_pages_with_incorrect_protection_templates)}}}}<!--End if small--><includeonly>{{#ifeq:{{PROTECTIONLEVEL:edit}}{{lc:{{{demolevel|undefined}}}}}|templateeditorundefined|{{#switch:{{NAMESPACE}}|Template|Module=|[Category:Wikipedia template-protected pages other than templates and modules](https://second-renaissance.fandom.com/wiki/Category:Wikipedia_template-protected_pages_other_than_templates_and_modules)}}}}{{#ifeq:{{lc:{{{categories|no}}}}}|no||{{{categories|}}}}}</includeonly><noinclude>

{{documentation}}
<!-- Add categories and interwikis to the /doc subpage, not here! -->
</noinclude>
```

## Provenance

Raw source: `bronze/pages/195/253.wikitext` · revision `253` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3APp-meta)
