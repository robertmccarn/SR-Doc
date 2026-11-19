---
page_id: 2364
revision_id: 6849
source_url: https://second-renaissance.fandom.com/wiki/Template%3AInfobox_Former_International_Organization
raw_sha256: 1440a2a95c1fae8428dffccf8222e034af04a35e4f95587e02d0b40338d8baa0
---

# Template:Infobox Former International Organization

## Preserved source

```wikitext
<noinclude>{{being deleted|2016 December 23|Template:Infobox former country|merge=Template:Infobox country}}
</noinclude>{| class="infobox geography vcard vevent" style="width:{{{width|290px}}};"
|- class="mergedtoprow"
<!-----------------
  Headings (names)
 ------------------>
|colspan="3" class="fn org summary" style="text-align:center; line-height:1.2em; font-size:135%; font-weight:bold;"| <!--
 -->{{#if:{{{conventional_long_name<includeonly>|</includeonly>}}}
        | {{{conventional_long_name}}}
        | {{#if:{{{native_name|}}}
           | {{{native_name}}}
           | ''Error: No name(s) given'' {{#if:{{{_noautocat|<noinclude>yes</noinclude>}}}||[N](https://second-renaissance.fandom.com/wiki/Category:Former_country_articles_requiring_maintenance)}}
          }}
       }}
|- class="mergedbottomrow"
{{#if:{{both|{{{conventional_long_name<includeonly>|</includeonly>}}}|{{{native_name<includeonly>|</includeonly>}}}}}|{{!}}colspan="3" class="fn org summary"  style="text-align:center; line-height:1.2em; font-size:115%; font-weight:bold;"{{!}} {{{native_name}}} }}
|-
<!---------------
  Status as a dependency, colony, vassal etc.
  Categorisation of this entry is handled in [Template:Infobox former country/autocat](653-template-infobox-former-country-autocat.md). This section here is just what will be displayed in the infobox. This has been split up to make the code look clearer. Also, not all statuses need to be displayed (although the optional status_text field will work, regardless of status)
 ---------------->
{{#if:{{{status<includeonly>|</includeonly>}}}
 | {{#if:{{{status_text|}}}{{{empire|}}}
    |{{!}}colspan="3" style="vertical-align:middle; text-align:center; font-size:115%;"{{!}}
    |{{#switch:{{ucfirst:{{{status|}}}}}
      <!----Values for "status" given in the first line of this #switch will not display the status bar IF nothing is given for "status_text" OR "empire":---->
      |Empire |Federation |Federal |Confederation |State union |State Union |Union |City-state |City state |City State |City=
      |#default={{!}}colspan="3" style="vertical-align:middle; text-align:center; font-size:115%;"{{!}} <!--
  -->}}<!--
-->}}<!--
   Display contents of status bar. Values placed in the first line of the above switch should have their values commented out (within the status_text check):
-->{{#if:{{{status_text|}}} |{{{status_text}}} |{{#switch:{{ucfirst:{{{status|}}}}}
    |Empire=<!--Empire-->
    |Nomadic empire|Nomadic Empire=[Nomadic empire](https://second-renaissance.fandom.com/wiki/Nomadic_empire)
    |Ancient Chinese state |Ancient Chinese State=[Ancient Chinese state](https://second-renaissance.fandom.com/wiki/Ancient_Chinese_state)
    |Federation |Federal=<!--Federation-->
    |Confederation=<!--Confederation-->
    |State union |State Union |Union=<!--State union-->
    |Special |Special territory=<!--Special territory-->
    |Unrecognized state |Unrecognised state |Unrecognized State |Unrecognised State
    |Unrecognized |Unrecognised=[Unrecognized state](https://second-renaissance.fandom.com/wiki/List_of_states_with_limited_recognition)
    |City-state |City-State |City state |City State
    |City={{#if:{{{empire|}}}
              | {{#switch:{{{empire|}}} |Holy Roman Empire |HRE=[Free Imperial City](https://second-renaissance.fandom.com/wiki/Free_Imperial_City) of the [Holy Roman Empire](https://second-renaissance.fandom.com/wiki/Holy_Roman_Empire) {{#if:{{{year_end|}}}|{{#ifexpr:{{{year_end}}}>1806|<br/><small>(until 1806)</small>}}|}} |#default=City-state {{#if:{{{empire|}}}|of [{{{empire}}}](https://second-renaissance.fandom.com/wiki/{{{empire}}})|}} }}
              |<!--City-state-->
             }}
    |Commonwealth realm |Commonwealth Realm=[Commonwealth Realm](https://second-renaissance.fandom.com/wiki/Commonwealth_Realm)
    |League of Nations Mandate |League of Nations
    |Mandate={{#if:{{{empire|}}}
                 | [Mandate](https://second-renaissance.fandom.com/wiki/League_of_Nations_mandate) of&nbsp;{{#switch:{{{empire}}} |United Kingdom |UK=the [United Kingdom](https://second-renaissance.fandom.com/wiki/United_Kingdom) |#default={{#ifexist:{{{empire}}}|[{{{empire}}}](https://second-renaissance.fandom.com/wiki/{{{empire}}})|{{{empire}}}}} }}
                 | [League of Nations mandate](https://second-renaissance.fandom.com/wiki/League_of_Nations_mandate)
                }}
    |United Nations Trust Territory| UN Trust Territory
    |Trust Territory=[Trust Territory](https://second-renaissance.fandom.com/wiki/United_Nations_Trust_Territories)<!--
                          -->{{#if:{{{empire|}}} |&nbsp;of&nbsp;{{#switch:{{{empire}}} |United Kingdom |UK=the [United Kingdom](https://second-renaissance.fandom.com/wiki/United_Kingdom) |United States |US |USA=the [United States](806-united-states.md) |#default={{#ifexist:{{{empire}}}|[{{{empire}}}](https://second-renaissance.fandom.com/wiki/{{{empire}}})|{{{empire}}}}} }} }}
    |Protectorate=Protectorate of&nbsp;<!--
                     -->{{#if:{{{empire|}}}
                         |{{#switch:{{{empire}}} 
                            |United Kingdom |UK=the [United Kingdom](https://second-renaissance.fandom.com/wiki/United_Kingdom) 
                            |United States |US |USA=the [United States](806-united-states.md) |#default={{#ifexist:{{{empire}}}|[{{{empire}}}](https://second-renaissance.fandom.com/wiki/{{{empire}}})|{{{empire}}}}} 
                            }}
                         |whom? {{#if:{{{_noautocat|<noinclude>yes</noinclude>}}}||[S](https://second-renaissance.fandom.com/wiki/Category:Former_country_articles_requiring_maintenance)}}
                        }}
    |Client |Client state |Client State |Puppet |Puppet-state
    |Puppet state={{#if:{{{empire|}}}
                      | {{#switch:{{{empire}}} |First French Empire |France=[Client](https://second-renaissance.fandom.com/wiki/French_client_republic) of the [First French Empire](https://second-renaissance.fandom.com/wiki/First_French_Empire) |#default=[Puppet state](https://second-renaissance.fandom.com/wiki/Puppet_state) of {{#ifexist:{{{empire}}}|[{{{empire}}}](https://second-renaissance.fandom.com/wiki/{{{empire}}})|{{{empire}}}}} }}
                      | Puppet state ''of whom?'' {{#if:{{{_noautocat|<noinclude>yes</noinclude>}}}||[S](https://second-renaissance.fandom.com/wiki/Category:Former_country_articles_requiring_maintenance)}}
                     }}
    |Vassal={{#switch:{{{empire|}}} |Holy Roman Empire |HRE=[State](https://second-renaissance.fandom.com/wiki/States_of_the_Holy_Roman_Empire) of the [Holy Roman Empire](https://second-renaissance.fandom.com/wiki/Holy_Roman_Empire) {{#if:{{{year_end|}}}|{{#ifexpr:{{{year_end}}}>1806|<small>(until 1806)</small>}}|}} |#default=Vassal{{#if:{{{empire|}}}|&nbsp;of&nbsp;{{{empire}}}|&nbsp;''of whom?'' {{#if:{{{_noautocat|<noinclude>yes</noinclude>}}}||[S](https://second-renaissance.fandom.com/wiki/Category:Former_country_articles_requiring_maintenance)}}}} }}
    |Fief={{#switch:{{{empire|}}} |#default=Fief{{#if:{{{empire|}}}|&nbsp;of&nbsp;{{{empire}}}|&nbsp;''of whom?'' {{#if:{{{_noautocat|<noinclude>yes</noinclude>}}}||[S](https://second-renaissance.fandom.com/wiki/Category:Former_country_articles_requiring_maintenance)}}}} }}
    |Abbey={{#switch:{{{empire|}}} |Holy Roman Empire |HRE=[Imperial Abbey](https://second-renaissance.fandom.com/wiki/Imperial_Abbey) of the [Holy Roman Empire](https://second-renaissance.fandom.com/wiki/Holy_Roman_Empire) {{Main other|[{{{common_name}}}](https://second-renaissance.fandom.com/wiki/Category:Imperial_abbeys)}} |#default=Abbey{{#if:{{{empire|}}}|&nbsp;of&nbsp;{{{empire}}}|&nbsp;''of whom?'' {{#if:{{{_noautocat|<noinclude>yes</noinclude>}}}||[S](https://second-renaissance.fandom.com/wiki/Category:Former_country_articles_requiring_maintenance)}}}} }}
    |Satellite state |Satellite State
    |Satellite= Satellite state of the [Soviet Union](https://second-renaissance.fandom.com/wiki/Soviet_Union)
    |Colony={{#switch:{{ucfirst:{{{empire}}}}}
             |United Kingdom |UK |British Empire |Britain=[British colony](https://second-renaissance.fandom.com/wiki/Territorial_evolution_of_the_British_Empire)
             |England=[English colony](https://second-renaissance.fandom.com/wiki/English_overseas_possessions)
             |France |First French Empire| French Empire=[French colony](https://second-renaissance.fandom.com/wiki/French_colonial_empire)
             |NL |Netherlands |The Netherlands=[Dutch colony](https://second-renaissance.fandom.com/wiki/Dutch_Empire)
             |Belgium=[Belgian colony](https://second-renaissance.fandom.com/wiki/Belgian_colonial_empire)
             |Spain |Spanish Empire=[Spanish colony](2362-spanish-empire.md)
             |Portugal=[Portuguese colony](https://second-renaissance.fandom.com/wiki/Portuguese_Empire)
             |Germany |German Empire=[German colony](https://second-renaissance.fandom.com/wiki/German_colonial_empire)
             |Italy=[Italian colony](https://second-renaissance.fandom.com/wiki/Italian_Empire)
             |Sweden=[Swedish colony](https://second-renaissance.fandom.com/wiki/Swedish_overseas_colonies)
             |Denmark=[Danish colony](https://second-renaissance.fandom.com/wiki/Danish_colonial_empire)
             |Norway=[Norwegian colony](https://second-renaissance.fandom.com/wiki/Norwegian_Empire)
             |Russia=[Russian colony](https://second-renaissance.fandom.com/wiki/Russian_Empire)
             |Japan=[Japanese colony](https://second-renaissance.fandom.com/wiki/Empire_of_Japan)
             |#default=Colony ({{#if:{{{empire|}}} |{{{empire}}}) |''of whom?'') {{#if:{{{_noautocat|<noinclude>yes</noinclude>}}}||[S](https://second-renaissance.fandom.com/wiki/Category:Former_country_articles_requiring_maintenance)}} }}
            }}
    |Provisional Government |Provisional government
    |Provisional=[Provisional government](https://second-renaissance.fandom.com/wiki/Provisional_government)
    |Exiled Government |Exiled government
    |Exile={{#if:{{{year_exile_start|}}}
            | [In exile](https://second-renaissance.fandom.com/wiki/Government_in_exile) {{#if:{{{year_exile_end|}}} |({{{year_exile_start}}}{{spaced ndash}}{{{year_exile_end}}}) |since {{{year_exile_start}}} }}
            | [Government in exile](https://second-renaissance.fandom.com/wiki/Government_in_exile)
           }}
    |#default={{{status}}}
   }} }}{{#if:{{{status_text|}}}|{{#ifeq:{{ucfirst:{{{status|}}}}}|Colony|{{main other|[Category:Former country articles using status text with Colony or Exile](https://second-renaissance.fandom.com/wiki/Category:Former_country_articles_using_status_text_with_Colony_or_Exile)}}|{{#ifeq:{{ucfirst:{{{status|}}}}}|Exile|{{main other|[Category:Former country articles using status text with Colony or Exile](https://second-renaissance.fandom.com/wiki/Category:Former_country_articles_using_status_text_with_Colony_or_Exile)}}}}}}}}

}}
|-
<!---------------
  Start and end dates of the subdivision plus icons of preceding and succeeding entities (if "successorflags" parameter is used)
  For the preceding and succeeding entities, give as input the name the territory. If there is already flag at "Image:Flag of _.svg" no address to that image needs to be provided.
 ---------------->
|colspan="3" style="vertical-align:middle; text-align:center; border-top:solid 1px #aaa; padding:0.2em 0em 0.2em 0em;"|
    {| style="width:100%; text-align:center; margin:0 auto; background:transparent;"
     |-
     | style="width:50px; border:0; vertical-align:middle; font-size:30%; line-height:105%;"| {{#ifeq:{{{successorflags|}}}|yes|{{#if:{{{p1|}}}|[<span style="font-size:300%;">←</span>](https://second-renaissance.fandom.com/wiki/{{{p1}}}) {{#if:{{{flag_p1|}}}|[30px{{#ifeq:{{{border_p1}}}|no||{{!}}border}}|link={{{p1}}}|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_p1}}})|{{#if:{{{image_p1|}}}|{{{image_p1}}}|[30px{{#ifeq:{{{border_p1}}}|no||{{!}}border}}|link={{{p1}}}|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}<br/>}}{{#if:{{{p2|}}}|&nbsp;<br/>[<span style="font-size:300%;">←</span>](https://second-renaissance.fandom.com/wiki/{{{p2}}}) {{#if:{{{flag_p2|}}}|[30px{{#ifeq:{{{border_p2}}}|no||{{!}}border}}|link={{{p2}}}|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_p2}}})|{{#if:{{{image_p2|}}}|{{{image_p2}}}|[30px{{#ifeq:{{{border_p2}}}|no||{{!}}border}}|link={{{p2}}}|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}<br/>}}{{#if:{{{p3|}}}|&nbsp;<br/>[<span style="font-size:300%;">←</span>](https://second-renaissance.fandom.com/wiki/{{{p3}}}) {{#if:{{{flag_p3|}}}|[30px{{#ifeq:{{{border_p3}}}|no||{{!}}border}}|link={{{p3}}}|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_p3}}})|{{#if:{{{image_p3|}}}|{{{image_p3}}}|[30px{{#ifeq:{{{border_p3}}}|no||{{!}}border}}|link={{{p3}}}|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}<br/>}}{{#if:{{{p4|}}}|&nbsp;<br/>[<span style="font-size:300%;">←</span>](https://second-renaissance.fandom.com/wiki/{{{p4}}}) {{#if:{{{flag_p4|}}}|[30px{{#ifeq:{{{border_p4}}}|no||{{!}}border}}|link={{{p4}}}|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_p4}}})|{{#if:{{{image_p4|}}}|{{{image_p4}}}|[30px{{#ifeq:{{{border_p4}}}|no||{{!}}border}}|link={{{p4}}}|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}<br/>}}{{#if:{{{p5|}}}|&nbsp;<br/>[<span style="font-size:300%;">←</span>](https://second-renaissance.fandom.com/wiki/{{{p5}}}) {{#if:{{{flag_p5|}}}|[30px{{#ifeq:{{{border_p5}}}|no||{{!}}border}}|link={{{p5}}}|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_p5}}})|{{#if:{{{image_p5|}}}|{{{image_p5}}}|[30px{{#ifeq:{{{border_p5}}}|no||{{!}}border}}|link={{{p5}}}|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}<br/>}}}}
     |style="vertical-align:middle; text-align:center; font-size:115%; border:0;" | {{#if:{{{year_end|}}}| {{#if:{{{life_span|}}}|'''{{{life_span}}}''' |'''{{#ifeq:{{{year_start|}}}|{{{year_end}}}|{{{year_start}}}|{{#if:{{{year_start|}}}|{{{year_start}}}–}}{{{year_end}}}}}'''}} |'''Life span?''' }}
     | style="width:50px; border:0; vertical-align:middle; text-align:right; line-height:105%; font-size:30%;"| {{#ifeq:{{{successorflags|}}}|yes|{{#if:{{{s1|}}}|{{#if:{{{flag_s1|}}}|[30px{{#ifeq:{{{border_s1}}}|no||{{!}}border}}|link={{{s1}}}|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_s1}}})|{{#if:{{{image_s1|}}}|{{{image_s1}}}|[30px{{#ifeq:{{{border_s1}}}|no||{{!}}border}}|link={{{s1}}}|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}} [<span style="font-size:300%;">→</span>](https://second-renaissance.fandom.com/wiki/{{{s1}}})<br/>}}{{#if:{{{s2|}}}|&nbsp;<br/>{{#if:{{{flag_s2|}}}|[30px{{#ifeq:{{{border_s2}}}|no||{{!}}border}}|link={{{s2}}}|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_s2}}})|{{#if:{{{image_s2|}}}|{{{image_s2}}}|[30px{{#ifeq:{{{border_s2}}}|no||{{!}}border}}|link={{{s2}}}|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}} [<span style="font-size:300%;">→</span>](https://second-renaissance.fandom.com/wiki/{{{s2}}})<br/>}} {{#if:{{{s3|}}}|&nbsp;<br/>{{#if:{{{flag_s3|}}}|[30px{{#ifeq:{{{border_s3}}}|no||{{!}}border}}|link={{{s3}}}|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_s3}}})|{{#if:{{{image_s3|}}}|{{{image_s3}}}|[30px{{#ifeq:{{{border_s3}}}|no||{{!}}border}}|link={{{s3}}}|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}} [<span style="font-size:300%;">→</span>](https://second-renaissance.fandom.com/wiki/{{{s3}}})<br/>}}{{#if:{{{s4|}}}|&nbsp;<br/>{{#if:{{{flag_s4|}}}|[30px{{#ifeq:{{{border_s4}}}|no||{{!}}border}}|link={{{s4}}}|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_s4}}})|{{#if:{{{image_s4|}}}|{{{image_s4}}}|[30px{{#ifeq:{{{border_s4}}}|no||{{!}}border}}|link={{{s4}}}|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}} [<span style="font-size:300%;">→</span>](https://second-renaissance.fandom.com/wiki/{{{s4}}})<br/>}}{{#if:{{{s5|}}}|&nbsp;<br/>{{#if:{{{flag_s5|}}}|[30px{{#ifeq:{{{border_s5}}}|no||{{!}}border}}|link={{{s5}}}|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_s5}}})|{{#if:{{{image_s5|}}}|{{{image_s5}}}|[30px{{#ifeq:{{{border_s5}}}|no||{{!}}border}}|link={{{s5}}}|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}} [<span style="font-size:300%;">→</span>](https://second-renaissance.fandom.com/wiki/{{{s5}}})<br/>}}}}
    |}
|-
<!----------------------
  Flag and coat of arms
 ----------------------->
{{#if:{{{image_coat<includeonly>|</includeonly>}}}{{{image_symbol|}}}{{{image_flag<includeonly>|</includeonly>}}}{{{image_flag2|}}}|
{{!}} colspan="3" style="vertical-align:middle; text-align:center; border-top:solid 1px #aaa; padding:0.2em 0em 0.2em 0em;" {{!}}
{{infobox country/imagetable
    |image1a = {{#invoke:InfoboxImage|InfoboxImage|suppressplaceholder={{main other||no}}|image={{{image_flag|<noinclude>Sin bandera.svg</noinclude>}}}|sizedefault=125px|size={{{flag_size|}}}|maxsize=250|border={{yesno |{{{flag_border|}}}|yes=yes|blank=yes}}|alt={{{flag_alt|{{{alt_flag|}}}}}}|title=Flag}}
    |image1b = {{#invoke:InfoboxImage|InfoboxImage|suppressplaceholder={{main other||no}}|image={{{image_flag2|}}}|sizedefault=125px|size={{{flag_size|}}}|maxsize=250|border={{yesno |{{{flag2_border|}}}|yes=yes|blank=yes}}|alt={{{flag_alt2|{{{alt_flag2|}}}}}} }}
    |caption1= {{if empty | {{{flag_caption|}}} | {{#ifexist:Flag of {{{linking_name|{{{common_name}}}}}} |[{{{common_name}}}}}}|{{if empty|{{{flag_type|}}}|Flag}}](https://second-renaissance.fandom.com/wiki/Flag_of_{{{linking_name) |{{#ifexist:Flag of the {{{linking_name|{{{common_name}}}}}} |[{{{common_name}}}}}}|{{if empty|{{{flag_type|}}}|Flag}}](https://second-renaissance.fandom.com/wiki/Flag_of_the_{{{linking_name) | {{if empty|{{{flag_type|}}}|Flag}} }} }} }}
    |image2  = {{#invoke:InfoboxImage|InfoboxImage|suppressplaceholder={{main other||no}}|image={{if empty|{{{image_coat|<noinclude>Sin escudo.svg</noinclude>}}}|{{{image_symbol|}}}}} |size={{#if:{{{image_coat|}}}|{{{coa_size|}}}|{{{symbol_width|}}}}}|sizedefault=85px|alt={{#if:{{{image_coat|}}}|{{{alt_coat|}}}|{{{alt_symbol|}}}}}|title={{if empty|{{{symbol_type|}}}|Coat of arms}}}}
    |caption2= {{if empty | {{{symbol_caption|}}} | {{#ifexist:{{{symbol_type_article|{{if empty|{{{symbol_type|}}}|Coat of arms}} of {{{linking_name|{{{common_name}}}}}}}}} |[{{if empty|{{{symbol_type|}}}|Coat of arms}} of {{{linking_name|{{{common_name}}}}}}}}} | {{if empty|{{{symbol_type|}}}|Coat of arms}}](https://second-renaissance.fandom.com/wiki/{{{symbol_type_article) | {{#ifexist:{{{symbol_type_article|{{if empty|{{{symbol_type|}}}|Coat of arms}} of the {{{linking_name|{{{common_name}}}}}}}}} |[{{if empty|{{{symbol_type|}}}|Coat of arms}} of the {{{linking_name|{{{common_name}}}}}}}}} | {{if empty|{{{symbol_type|}}}|Coat of arms}}](https://second-renaissance.fandom.com/wiki/{{{symbol_type_article) | {{if empty|{{{symbol_type|}}}|Coat of arms}} }} }} }}
    }} }}
|-
<!---------------
  Motto
 ---------------->
{{#if:{{{national_motto<includeonly>|</includeonly>}}} |
{{!}}colspan="3" style="vertical-align:top; text-align:center; font-size:95%;"{{!}} '''Motto'''<br/>{{{national_motto}}}
}}
|-
<!---------------
  Anthem
 ---------------->
{{#if:{{{national_anthem<includeonly>|</includeonly>}}} |
{{!}}colspan="3" style="vertical-align:top; text-align:center; font-size:95%;"{{!}} '''Anthem'''<br/>{{#ifexist:{{{national_anthem}}} |[{{{national_anthem}}}](https://second-renaissance.fandom.com/wiki/{{{national_anthem}}}) |{{{national_anthem}}} }}
}}
|-
<!---------------
  Map/s
 ---------------->
{{#if:{{{image_map<includeonly>|</includeonly>}}}
 |{{!}}colspan="3" style="text-align:center; font-size:95%; padding:0.6em 0em 0.6em 0em;"{{!}}<!--
   -->[<noinclude>Missing map.svg</noinclude>}}}|{{{image_map_size|250px}}}|center|alt={{{image_map_alt|}}}|Location of {{{common_name}}}](https://second-renaissance.fandom.com/wiki/File:{{{image_map)<!--
   -->{{#if:{{{image_map_caption<includeonly>|</includeonly>}}} |<div style="padding:0.5em 0.5em 0;line-height:1.25em;">{{{image_map_caption}}}</div>}}
 | {{#if:{{{location_map|}}}
    |{{!}}colspan="3" style="text-align:center; font-size:95%; padding:0.6em 0em 0.6em 0em;"{{!}} {{{location_map}}}
   }}
}}
{{#if:{{{image_map2|}}} |
{{!}}- class="mergedtoprow"
{{!}}colspan="3" style="text-align:center; padding:0.6em 0em;"{{!}}<!--
  -->[{{{image_map2_size|280px}}}|center|alt={{{image_map2_alt|}}}|Location of {{{common_name}}}](https://second-renaissance.fandom.com/wiki/File:{{{image_map2}}})<!--
  -->{{#if:{{{image_map2_caption|}}} |<div style="padding-top:0.5em;line-height:1.25em;font-size:90%;">{{{image_map2_caption}}}</div>}}</small>
}}
<!---------------
  Capital
 ---------------->
|- {{#if:{{{capital_exile|}}} |class="mergedtoprow"}}
{{#ifeq:{{{capital|}}}|omitted | |
{{!}}colspan="2"{{!}} '''Capital'''
<!----Width of column 3 (of 3) specified here:---->
{{!}}style="width:50%;"{{!}} {{#if:{{{capital|}}} |{{#ifeq:{{{capital}}}|Unknown |''Unknown'' |{{#ifexist:{{{capital}}} |[}}}](https://second-renaissance.fandom.com/wiki/{{{capital) |{{{capital|}}} }} }} |''Not specified''}}
}}
|- {{#ifeq:{{{capital|}}}|omitted | |class="mergedbottomrow"}}
<!-----Capital-in-exile----->
{{#if:{{{capital_exile|}}} |
{{!}}colspan="2"{{!}} '''Capital-in-exile'''
{{!}} {{#ifexist:{{{capital_exile}}} |[}}}](https://second-renaissance.fandom.com/wiki/{{{capital_exile) |{{{capital_exile|}}} }}
}}
|-
<!-----------------
  Common languages
 ------------------>
{{#if:{{{common_languages<includeonly>|</includeonly>}}} |
{{!}}colspan="2"{{!}} '''Languages'''
{{!}} {{#ifexist:{{{common_languages}}} language |[{{{common_languages}}}](https://second-renaissance.fandom.com/wiki/{{{common_languages}}}_language) |{{#ifexist:{{{common_languages}}} |[{{{common_languages}}}](https://second-renaissance.fandom.com/wiki/{{{common_languages}}}) |{{{common_languages}}} }} }}
}}
|-
<!---------------
  Religion
 ---------------->
{{#if: {{{religion<includeonly>|</includeonly>}}}|
{{!}}colspan="2"{{!}} '''Religion'''
{{!}} {{#ifexist:{{{religion}}}|[{{{religion}}}](https://second-renaissance.fandom.com/wiki/{{{religion}}})|{{{religion}}}}}
}}
|-
<!---------------
  Demonym
 ---------------->
{{#if: {{{demonym<includeonly>|</includeonly>}}}|
{{!}}colspan="2"{{!}} '''[Demonym](1021-demonym.md)'''
{{!}} {{#ifexist:{{{demonym}}} people|[{{{demonym}}}](https://second-renaissance.fandom.com/wiki/{{{demonym}}}_people)|{{{demonym}}}}}
}}
<!-----------------------
  Government and leaders
 ------------------------>
|- {{#if:{{{title_leader|}}}{{{title_deputy|}}}{{{title_representative|}}} |class="mergedtoprow"}}
|colspan="2"| '''{{#if:{{{government_type|}}}
                  | Government
                  | {{#if:{{{status|}}} |Political structure |Government}}
                 }}'''
| {{#if:{{{government_type|}}}
   | {{#switch:{{ucfirst:{{{government_type}}}}}
      |Constitutional monarchy |Constitutional Monarchy|Elective monarchy|Elective Monarchy |Absolute Monarchy |Absolute monarchy
      |Monarchy=[{{{government_type}}}](https://second-renaissance.fandom.com/wiki/{{{government_type}}}) <!--
       -->{{#if:{{{_noautocat|<noinclude>yes</noinclude>}}} |
           |{{Main other|{{#switch:{{{continent}}}
             |Europe=[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_monarchies_of_Europe)
             |Asia=[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_monarchies_of_Asia)
             |North America=[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_monarchies_of_North_America)
             |South America=[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_monarchies_of_South_America)
             |Africa=[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_monarchies_of_Africa)
             |Oceania=[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_monarchies_of_Oceania)
             |Eurasia=[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_monarchies_of_Europe)[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_monarchies_of_Asia)
             |Afroasia=[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_monarchies_of_Africa)[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_monarchies_of_Asia)
             |Afroeurasia=[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_monarchies_of_Europe)[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_monarchies_of_Asia)[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_monarchies_of_Africa)|[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_monarchies)
            }} }}
          }}
      |Republic|Federal Republic|Federal republic=[Republic](974-republic.md) {{#if:{{{_noautocat|<noinclude>yes</noinclude>}}} | |{{Main other|[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_republics)}} }}
      |Principality=
         {{#switch:{{{empire}}}
          |Holy Roman Empire|HRE=[Principality](https://second-renaissance.fandom.com/wiki/Princes_of_the_Holy_Roman_Empire)
          |#default=[Principality](https://second-renaissance.fandom.com/wiki/Principality)
         }}
         {{#if:{{{_noautocat|<noinclude>yes</noinclude>}}} | |{{Main other|[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_principalities)}} }}
      |Emirate=[Emirate](https://second-renaissance.fandom.com/wiki/Emirate) {{#if:{{{_noautocat|<noinclude>yes</noinclude>}}} | |{{Main other|[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_emirates)}} }}
      |Socialist republic |Socialist Republic |Socialist State
      |Socialist state=[Socialist republic](https://second-renaissance.fandom.com/wiki/Socialist_state) {{#if:{{{_noautocat|<noinclude>yes</noinclude>}}} | |{{Main other|[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_socialist_republics)}} }}
      |Military dictatorship |Military Dictatorship |Dictatorship=[Dictatorship](https://second-renaissance.fandom.com/wiki/Dictatorship)
      |Theocracy=[Theocracy](https://second-renaissance.fandom.com/wiki/Theocracy) {{#if:{{{_noautocat|<noinclude>yes</noinclude>}}} | |{{Main other|[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_theocracies)}} }}
      |Unknown=''Unknown''
      |Various=
      |#default={{#ifexist:{{{government_type}}} |[{{{government_type}}}](https://second-renaissance.fandom.com/wiki/{{{government_type}}}) |{{{government_type}}} }}<!----''Value specified for "government_type" [does not comply](2822-template-infobox-former-country-doc.md)''---->{{ns0|[G](https://second-renaissance.fandom.com/wiki/Category:Former_country_articles_requiring_maintenance)}}
     }}
   | {{#if:{{{status|}}}
      | {{#ifexist:{{{status}}} |[{{{status}}}](https://second-renaissance.fandom.com/wiki/{{{status}}}) |{{{status}}} }}
      | ''Not specified''
     }}
  }}
|- class="{{#if:{{{year_leader1<includeonly>|</includeonly>}}}{{{leader2|}}}{{{deputy1|}}}{{{representative1|}}} |mergedrow|mergedbottomrow}}"
<!-----
 Head of state ("leader" parameters).
 For colonies and dependant territories, this is still the head of the ruling entity (e.g. the head of state of a British colony is the British monarch).
 ------>
{{#if:{{{leader1<includeonly>|</includeonly>}}}
 |{{!}}colspan="2"{{!}} <!--
        -->'''{{#if:{{{title_leader<includeonly>|</includeonly>}}}
               | {{{title_leader}}}
               | {{#switch:{{{government_type}}}
                  |Constitutional monarchy
                  |Monarchy={{#ifexist:King of {{{common_name}}}
                             |[King of {{{common_name}}}{{!}}King](https://second-renaissance.fandom.com/wiki/King_of_{{{common_name}}}{{!}}King)
                             |{{#ifexist:King of the {{{common_name}}} |[King of the {{{common_name}}}{{!}}King](https://second-renaissance.fandom.com/wiki/King_of_the_{{{common_name}}}{{!}}King) |King}}
                            }}
                  | {{#ifexist:President of {{{common_name}}}
                     |[President of {{{common_name}}}{{!}}President](https://second-renaissance.fandom.com/wiki/President_of_{{{common_name}}}{{!}}President)
                     |{{#ifexist:President of the {{{common_name}}} |[President of the {{{common_name}}}{{!}}President](https://second-renaissance.fandom.com/wiki/President_of_the_{{{common_name}}}{{!}}President) |President}}
                    }}
                 }}<!--
           -->}}''' {{#if:{{{year_leader1<includeonly>|</includeonly>}}}
                     |{{!!}}
                     |{{!!}}style="vertical-align:bottom;"{{!}} {{#ifexist:{{{leader1}}} |[{{{leader1}}}](https://second-renaissance.fandom.com/wiki/{{{leader1}}}) |{{{leader1}}}}}<!--
                 -->}}
{{!}}- class="{{#if:{{{leader2|}}}{{{representative1<includeonly>|</includeonly>}}}{{{deputy1|}}} |mergedrow|mergedbottomrow}}"
  {{#if:{{{year_leader1<includeonly>|</includeonly>}}}
<!-----
 Width of first column (for the dashes before names, events, etc) first defined here:
 ------>
   |{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}}&nbsp;•&nbsp;
    {{!}}style="padding-left:0;text-align:left;"{{!}} {{{year_leader1}}}
    {{!}} {{#ifexist:{{{leader1}}}|[{{{leader1}}}](https://second-renaissance.fandom.com/wiki/{{{leader1}}})|{{{leader1}}}}}
  }}
}}
{{!}}- class="{{#if:{{{leader3|}}}{{{representative1<includeonly>|</includeonly>}}}{{{deputy1|}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{leader2|}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} {{#if:{{{year_leader2|}}} |&nbsp;•&nbsp;{{!!}}style="padding-left:0;text-align:left;"{{!}}{{{year_leader2}}} |{{!!}} }}
{{!}} {{#ifexist:{{{leader2}}} |[{{{leader2}}}](https://second-renaissance.fandom.com/wiki/{{{leader2}}}) |{{{leader2}}} }}
}}
{{!}}- class="{{#if:{{{leader4|}}}{{{representative1<includeonly>|</includeonly>}}}{{{deputy1|}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{leader3|}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} {{#if:{{{year_leader3|}}} |&nbsp;•&nbsp;{{!!}}style="padding-left:0;text-align:left;"{{!}}{{{year_leader3}}} |{{!!}} }}
{{!}} {{#ifexist:{{{leader3}}} |[{{{leader3}}}](https://second-renaissance.fandom.com/wiki/{{{leader3}}}) |{{{leader3}}} }}
}}
{{!}}- class="{{#if:{{{leader5|}}}{{{representative1<includeonly>|</includeonly>}}}{{{deputy1|}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{leader4|}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} {{#if:{{{year_leader4|}}} |&nbsp;•&nbsp;{{!!}}style="padding-left:0;text-align:left;"{{!}}{{{year_leader4}}} |{{!!}} }}
{{!}} {{#ifexist:{{{leader4}}} |[{{{leader4}}}](https://second-renaissance.fandom.com/wiki/{{{leader4}}}) |{{{leader4}}} }}
}}
{{!}}- class="{{#if:{{{leader6|}}}{{{representative1<includeonly>|</includeonly>}}}{{{deputy1|}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{leader5|}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} {{#if:{{{year_leader5|}}} |&nbsp;•&nbsp;{{!!}}style="padding-left:0;text-align:left;"{{!}}{{{year_leader5}}} |{{!!}} }}
{{!}} {{#ifexist:{{{leader5}}} |[{{{leader5}}}](https://second-renaissance.fandom.com/wiki/{{{leader5}}}) |{{{leader5}}} }}
}}
{{!}}- class="{{#if:{{{leader7|}}}{{{representative1<includeonly>|</includeonly>}}}{{{deputy1|}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{leader6|}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} {{#if:{{{year_leader6|}}} |&nbsp;•&nbsp;{{!!}}style="padding-left:0;text-align:left;"{{!}}{{{year_leader6}}} |{{!!}} }}
{{!}} {{#ifexist:{{{leader6}}} |[{{{leader6}}}](https://second-renaissance.fandom.com/wiki/{{{leader6}}}) |{{{leader6}}} }}
}}
{{!}}- class="{{#if:{{{leader8|}}}{{{representative1<includeonly>|</includeonly>}}}{{{deputy1|}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{leader7|}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} {{#if:{{{year_leader7|}}} |&nbsp;•&nbsp;{{!!}}style="padding-left:0;text-align:left;"{{!}}{{{year_leader7}}} |{{!!}} }}
{{!}} {{#ifexist:{{{leader7}}} |[{{{leader7}}}](https://second-renaissance.fandom.com/wiki/{{{leader7}}}) |{{{leader7}}} }}
}}
{{!}}- class="{{#if:{{{leader9<includeonly>|</includeonly>}}}{{{representative1|}}}{{{deputy1|}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{leader8|}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} {{#if:{{{year_leader8|}}} |&nbsp;•&nbsp;{{!!}}style="padding-left:0;text-align:left;"{{!}}{{{year_leader8}}} |{{!!}} }}
{{!}} {{#ifexist:{{{leader8}}} |[{{{leader8}}}](https://second-renaissance.fandom.com/wiki/{{{leader8}}}) |{{{leader8}}} }}
}}
{{!}}- class="{{#if:{{{deputy1<includeonly>|</includeonly>}}}{{{representative1|}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{leader9<includeonly>|</includeonly>}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} {{#if:{{{year_leader9<includeonly>|</includeonly>}}} |&nbsp;•&nbsp;{{!!}}style="padding-left:0;text-align:left;"{{!}}{{{year_leader9}}} |{{!!}} }}
{{!}} {{#ifexist:{{{leader9}}} |[{{{leader9}}}](https://second-renaissance.fandom.com/wiki/{{{leader9}}}) |{{{leader9}}} }}
}}
<!-----
 Representative of head of state (eg. colony governors)
 ------>
|- class="{{#if:{{{year_representative1<includeonly>|</includeonly>}}}{{{representative2|}}}{{{deputy1|}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{representative1<includeonly>|</includeonly>}}}
 |{{!}}colspan="2"{{!}} <!--
  -->'''{{#if:{{{title_representative<includeonly>|</includeonly>}}}
         | {{{title_representative}}}
         | {{#ifexist:Governor of {{{common_name}}}
            | [Governor of {{{common_name}}}{{!}}Governor](https://second-renaissance.fandom.com/wiki/Governor_of_{{{common_name}}}{{!}}Governor)
            | {{#ifexist:Governor of the {{{common_name}}}
               | [Governor of the {{{common_name}}}{{!}}Governor](https://second-renaissance.fandom.com/wiki/Governor_of_the_{{{common_name}}}{{!}}Governor)
               | Governor}} }}
        }}'''
  {{#if:{{{year_representative1<includeonly>|</includeonly>}}}
   |{{!}} 
   |{{!}}style="vertical-align:bottom;"{{!}} {{#ifexist:{{{representative1}}}|[{{{representative1}}}](https://second-renaissance.fandom.com/wiki/{{{representative1}}})|{{{representative1}}} }}
  }}
  {{!}}- class="{{#if:{{{representative2|}}}{{{deputy1<includeonly>|</includeonly>}}} |mergedrow|mergedbottomrow}}"
  {{#if:{{{year_representative1<includeonly>|</includeonly>}}}
   |{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}}&nbsp;•&nbsp;{{!!}}style="padding-left:0;text-align:left;"{{!}}{{{year_representative1}}}{{!!}} {{#ifexist:{{{representative1}}} |[{{{representative1}}}](https://second-renaissance.fandom.com/wiki/{{{representative1}}}) |{{{representative1}}} }}
  }}
}}
{{!}}- class="{{#if:{{{representative3|}}}{{{deputy1<includeonly>|</includeonly>}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{representative2|}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} {{#if:{{{year_representative2|}}} |&nbsp;•&nbsp;{{!!}}style="padding-left:0;text-align:left;"{{!}}{{{year_representative2}}} |{{!!}} }}
{{!!}} {{#ifexist:{{{representative2}}} |[{{{representative2}}}](https://second-renaissance.fandom.com/wiki/{{{representative2}}}) |{{{representative2}}} }}
}}
{{!}}- class="{{#if:{{{representative3|}}}{{{deputy1<includeonly>|</includeonly>}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{representative3|}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} {{#if:{{{year_representative3|}}} |&nbsp;•&nbsp;{{!!}}style="padding-left:0;text-align:left;"{{!}}{{{year_representative3}}} |{{!!}} }}
{{!!}} {{#ifexist:{{{representative3}}} |[{{{representative3}}}](https://second-renaissance.fandom.com/wiki/{{{representative3}}}) |{{{representative3}}} }}
}}
{{!}}- class="{{#if:{{{representative5<includeonly>|</includeonly>}}}{{{deputy1|}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{representative4|}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} {{#if:{{{year_representative4|}}} |&nbsp;•&nbsp;{{!!}}style="padding-left:0;text-align:left;"{{!}}{{{year_representative4}}} |{{!!}} }}
{{!!}}{{#ifexist:{{{representative4}}} |[{{{representative4}}}](https://second-renaissance.fandom.com/wiki/{{{representative4}}}) |{{{representative4}}} }}
}}
{{!}}- class="{{#if:{{{deputy1<includeonly>|</includeonly>}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{representative5<includeonly>|</includeonly>}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} {{#if:{{{year_representative5<includeonly>|</includeonly>}}} |&nbsp;•&nbsp;{{!!}}style="padding-left:0;text-align:left;"{{!}}{{{year_representative5}}} |{{!!}} }}
{{!!}} {{#ifexist:{{{representative5}}} |[{{{representative5}}}](https://second-renaissance.fandom.com/wiki/{{{representative5}}}) |{{{representative5}}} }}
}}
<!-----
 Head of government (if different from head of state) or second-in-charge, etc.
 ("deputy" parameters)
 ------>
|- class="{{#if:{{{year_deputy1<includeonly>|</includeonly>}}}{{{deputy2|}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{deputy1<includeonly>|</includeonly>}}}
 |{{!}}colspan="2"{{!}} <!--
    -->'''{{#if:{{{title_deputy<includeonly>|</includeonly>}}}
           | {{{title_deputy}}}
           | {{#ifexist:Prime Minister of {{{common_name}}}
              | [Prime Minister of {{{common_name}}}{{!}}Prime Minister](https://second-renaissance.fandom.com/wiki/Prime_Minister_of_{{{common_name}}}{{!}}Prime_Minister)
              | {{#ifexist:Prime Minister of the {{{common_name}}}
                 | [Prime Minister of the {{{common_name}}}{{!}}Prime Minister](https://second-renaissance.fandom.com/wiki/Prime_Minister_of_the_{{{common_name}}}{{!}}Prime_Minister)
                 |Prime Minister}} }}
          }}'''
  {{#if:{{{year_deputy1<includeonly>|</includeonly>}}}
   |{{!}}
   |{{!}}style="vertical-align:bottom;"{{!}} {{#ifexist:{{{deputy1}}} |[{{{deputy1}}}](https://second-renaissance.fandom.com/wiki/{{{deputy1}}}) |{{{deputy1}}} }}
  }}
{{!}}- class="{{#if:{{{deputy2<includeonly>|</includeonly>}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{year_deputy1<includeonly>|</includeonly>}}} | 
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}}&nbsp;•&nbsp;{{!!}}style="padding-left:0;text-align:left;"{{!}}{{{year_deputy1}}}
{{!}} {{#ifexist:{{{deputy1}}} |[{{{deputy1}}}](https://second-renaissance.fandom.com/wiki/{{{deputy1}}}) |{{{deputy1}}} }}
}}
}}
{{!}}- class="{{#if:{{{deputy3|}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{deputy2|}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} {{#if:{{{year_deputy2|}}} |&nbsp;•&nbsp;{{!!}}style="padding-left:0;text-align:left;"{{!}}{{{year_deputy2}}} |{{!!}} }}
{{!!}} {{#ifexist:{{{deputy2}}} |[{{{deputy2}}}](https://second-renaissance.fandom.com/wiki/{{{deputy2}}}) |{{{deputy2}}} }}
}}
{{!}}- class="{{#if:{{{deputy4|}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{deputy3|}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} {{#if:{{{year_deputy3|}}} |&nbsp;•&nbsp;{{!!}}style="padding-left:0;text-align:left;"{{!}}{{{year_deputy3}}} |{{!!}} }}
{{!!}} {{#ifexist:{{{deputy3}}} |[{{{deputy3}}}](https://second-renaissance.fandom.com/wiki/{{{deputy3}}}) |{{{deputy3}}} }}
}}
{{!}}- class="{{#if:{{{deputy5|}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{deputy4|}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} {{#if:{{{year_deputy4|}}} |&nbsp;•&nbsp;{{!!}}style="padding-left:0;text-align:left;"{{!}}{{{year_deputy4}}} |{{!!}} }}
{{!!}} {{#ifexist:{{{deputy4}}} |[{{{deputy4}}}](https://second-renaissance.fandom.com/wiki/{{{deputy4}}}) |{{{deputy4}}} }}
}}
{{!}}- class="{{#if:{{{deputy6<includeonly>|</includeonly>}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{deputy5|}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} {{#if:{{{year_deputy5|}}} |&nbsp;•&nbsp;{{!!}}style="padding-left:0;text-align:left;"{{!}}{{{year_deputy5}}} |{{!!}} }}
{{!!}} {{#ifexist:{{{deputy5}}} |[{{{deputy5}}}](https://second-renaissance.fandom.com/wiki/{{{deputy5}}}) |{{{deputy5}}} }}
}}
{{!}}- class="mergedbottomrow"
{{#if:{{{deputy6<includeonly>|</includeonly>}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} {{#if:{{{year_deputy6<includeonly>|</includeonly>}}} |&nbsp;•&nbsp;{{!!}}style="padding-left:0;text-align:left;"{{!}}{{{year_deputy6}}} |{{!!}} }}
{{!!}} {{#ifexist:{{{deputy6}}} |[{{{deputy6}}}](https://second-renaissance.fandom.com/wiki/{{{deputy6}}}) |{{{deputy6}}} }}
}}
|-
<!---------------
  Legislature
 ---------------->
{{#if:{{{legislature<includeonly>|</includeonly>}}} |
{{!}}- {{#if:{{{house1|}}}{{{house2|}}} |class="mergedtoprow"}}
{{!}}colspan="2"{{!}} '''Legislature'''
{{!}} {{#ifexist:{{{legislature}}} |[{{{legislature}}}](https://second-renaissance.fandom.com/wiki/{{{legislature}}}) |{{{legislature}}} }}
{{#if:{{{house1|}}} | 
{{!}}- class="{{#if:{{{house2|}}} |mergedrow|mergedbottomrow}}"
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}}&nbsp;•&nbsp;{{!!}}style="padding-left:0;text-align:left;"{{!}} {{#if:{{{type_house1|}}} |{{{type_house1}}} |Upper house}}
{{!}} {{#ifexist:{{{house1}}} |[{{{house1}}}](https://second-renaissance.fandom.com/wiki/{{{house1}}}) |{{{house1}}} }}
}}
{{#if:{{{house2|}}} | 
{{!}}- class="mergedbottomrow"
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}}&nbsp;•&nbsp;{{!!}}style="padding-left:0;text-align:left;"{{!}} {{#if:{{{type_house2|}}} |{{{type_house2}}} |Lower house}}
{{!}} {{#ifexist:{{{house2}}}|[{{{house2}}}](https://second-renaissance.fandom.com/wiki/{{{house2}}})|{{{house2}}} }}
}}
}}
<!---------------
  Events
 ---------------->
|- class="mergedtoprow"
|colspan="2"| {{#if:{{{era|}}} |'''Historical era''' |'''History'''}}
| {{#if:{{{era|}}} |{{#ifexist:{{{era|}}}|[{{{era}}}](https://second-renaissance.fandom.com/wiki/{{{era}}})|{{{era}}}}} {{#if:{{{_noautocat|<noinclude>yes</noinclude>}}}||{{Main other|{{#switch:{{{era}}}
  |Cold War=[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_polities_of_the_Cold_War)
  |Interwar period=[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_polities_of_the_interwar_period)
  }} }} }} }}
|- class="mergedrow"
{{#if:{{{event_pre<includeonly>|</includeonly>}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}}&nbsp;•&nbsp;{{!!}}style="padding-left:0em;text-align:left;"{{!}}{{{event_pre}}}
{{!}}style="vertical-align: bottom;"{{!}}{{#if:{{{date_pre<includeonly>|</includeonly>}}}|{{{date_pre}}}}}{{#ifeq:{{#time: F j |{{#if:{{{date_pre<includeonly>|</includeonly>}}}|{{{date_pre}}}}}}}|{{#if:{{{date_pre<includeonly>|</includeonly>}}}|{{{date_pre}}}}}|,}}
}}
|- class="mergedrow"
|style="width:1.0em; padding:0 0 0 0.6em;"| &nbsp;•&nbsp; ||style="padding-left:0em;text-align:left;"| {{#if:{{{event_start|}}} |{{{event_start}}} |Established}}
|style="vertical-align: bottom;"| {{#if:{{{date_start|}}} |{{{date_start}}}}}{{#ifeq:{{#time: F j |{{#if:{{{date_start|}}}|{{{date_start}}}}}}}|{{#if:{{{date_start|}}}|{{{date_start}}}}}|,}} {{#if:{{{year_start|}}}|{{{year_start}}}|''Enter start year''}}
|- class="mergedrow"
{{#if:{{{event1<includeonly>|</includeonly>}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}}&nbsp;•&nbsp;{{!!}}style="padding-left:0em;text-align:left;"{{!}}{{{event1}}}
{{!}}style="vertical-align: bottom;"{{!}}{{#if:{{{date_event1<includeonly>|</includeonly>}}}|{{{date_event1}}}}}{{#ifeq:{{#time: F j |{{#if:{{{date_event1<includeonly>|</includeonly>}}}|{{{date_event1}}}}}}}|{{#if:{{{date_event1<includeonly>|</includeonly>}}}|{{{date_event1}}}}}|,}}
}}
|- class="mergedrow"
{{#if:{{{event2|}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}}&nbsp;•&nbsp;{{!!}}style="padding-left:0em;text-align:left;"{{!}}{{{event2}}}
{{!}}style="vertical-align: bottom;"{{!}}{{#if:{{{date_event2|}}}|{{{date_event2}}}}}{{#ifeq:{{#time: F j |{{#if:{{{date_event2|}}}|{{{date_event2}}}}}}}|{{#if:{{{date_event2|}}}|{{{date_event2}}}}}|,}}
}}
|- class="mergedrow"
{{#if:{{{event3|}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}}&nbsp;•&nbsp;{{!!}}style="padding-left:0em;text-align:left;"{{!}}{{{event3}}}
{{!}}style="vertical-align: bottom;"{{!}}{{#if:{{{date_event3|}}}|{{{date_event3}}}}}{{#ifeq:{{#time: F j |{{#if:{{{date_event3|}}}|{{{date_event3}}}}}}}|{{#if:{{{date_event3|}}}|{{{date_event3}}}}}|,}}
}}
|- class="mergedrow"
{{#if:{{{event4|}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}}&nbsp;•&nbsp;{{!!}}style="padding-left:0em;text-align:left;"{{!}}{{{event4}}}
{{!}}style="vertical-align: bottom;"{{!}}{{#if:{{{date_event4|}}}|{{{date_event4}}}}}{{#ifeq:{{#time: F j |{{#if:{{{date_event4|}}}|{{{date_event4}}}}}}}|{{#if:{{{date_event4|}}}|{{{date_event4}}}}}|,}}
}}
|- class="mergedrow"
{{#if:{{{event5<includeonly>|</includeonly>}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}}&nbsp;•&nbsp;{{!!}}style="padding-left:0em;text-align:left;"{{!}}{{{event5}}}
{{!}}style="vertical-align: bottom;"{{!}}{{#if:{{{date_event5<includeonly>|</includeonly>}}}|{{{date_event5}}}}}{{#ifeq:{{#time: F j |{{#if:{{{date_event5<includeonly>|</includeonly>}}}|{{{date_event5}}}}}}}|{{#if:{{{date_event5<includeonly>|</includeonly>}}}|{{{date_event5}}}}}|,}}
}}
|- class="mergedrow"
{{#if:{{{event6<includeonly>|</includeonly>}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}}&nbsp;•&nbsp;{{!!}}style="padding-left:0em;text-align:left;"{{!}}{{{event6}}}
{{!}}style="vertical-align: bottom;"{{!}}{{#if:{{{date_event6<includeonly>|</includeonly>}}}|{{{date_event6}}}}}{{#ifeq:{{#time: F j |{{#if:{{{date_event6<includeonly>|</includeonly>}}}|{{{date_event6}}}}}}}|{{#if:{{{date_event6<includeonly>|</includeonly>}}}|{{{date_event6}}}}}|,}}
}}
|- class="{{#if:{{{event_post<includeonly>|</includeonly>}}} |mergedrow|mergedbottomrow}}"
|style="width:1.0em; padding:0 0 0 0.6em;"| &nbsp;•&nbsp; ||style="padding-left:0em;text-align:left;"| {{#if:{{{event_end|}}} |{{{event_end}}} |Disestablished}}
|style="vertical-align: bottom;"| {{#if:{{{date_end|}}}|{{{date_end}}}}}{{#ifeq:{{#time: F j |{{#if:{{{date_end|}}}|{{{date_end}}}}}}}|{{#if:{{{date_end|}}}|{{{date_end}}}}}|,}} {{#if:{{{year_end|}}}|{{{year_end}}}|''Enter end year''}}
|- class="mergedbottomrow"
{{#if:{{{event_post<includeonly>|</includeonly>}}} |
{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}}&nbsp;•&nbsp;{{!!}}style="padding-left:0em;text-align:left;"{{!}}{{{event_post}}}
{{!}}style="vertical-align: bottom;"{{!}}{{#if:{{{date_post<includeonly>|</includeonly>}}}|{{{date_post}}}}}{{#ifeq:{{#time: F j |{{#if:{{{date_post<includeonly>|</includeonly>}}}|{{{date_post}}}}}}}|{{#if:{{{date_post<includeonly>|</includeonly>}}}|{{{date_post}}}}}|,}}
}}
<!---------------
  Area
 ---------------->
|- {{#if:{{{stat_year1<includeonly>|</includeonly>}}} | |class="mergedtoprow"}}
{{#if:{{{stat_year1<includeonly>|</includeonly>}}}
 | {{#if:{{{stat_area1<includeonly>|</includeonly>}}}{{{stat_area2|}}}{{{stat_area3|}}}{{{stat_area4|}}}{{{stat_area5|}}}
    |{{!}}colspan="3"{{!}} '''[Area](https://second-renaissance.fandom.com/wiki/List_of_countries_and_dependencies_by_area)'''
   }}
<!----Area: 1st year---->
   {{!}}- class="{{#if:{{{stat_area2|}}}{{{stat_area3|}}}{{{stat_area4|}}}{{{stat_area5<includeonly>|</includeonly>}}} |mergedrow|mergedbottomrow}}"
   {{#if:{{{stat_area1<includeonly>|</includeonly>}}}
    |{{!}} {{#if:{{{stat_year1<includeonly>|</includeonly>}}}
            |style="width:1.0em; padding:0 0 0 0.6em;"{{!}} &nbsp;•&nbsp; {{!!}}style="padding-left:0;text-align:left;"{{!}} {{{stat_year1}}} {{#if:{{{ref_area1|}}}|{{{ref_area1}}}}}
            |{{!!}}
           }}
     {{!}} {{convinfobox|{{{stat_area1|}}}|km2||sqmi}}
   }}
<!----Area: 2nd year---->
   {{!}}- class="{{#if:{{{stat_area3|}}}{{{stat_area4|}}}{{{stat_area5<includeonly>|</includeonly>}}} |mergedrow|mergedbottomrow}}"
   {{#if:{{{stat_area2|}}}
    | {{#ifeq:{{{stat_area2|}}}|{{{stat_area1|}}}
       |
       |{{!}} {{#if:{{{stat_year2|}}}
               |style="width:1.0em; padding:0 0 0 0.6em;"{{!}} &nbsp;•&nbsp; {{!!}}style="padding-left:0;text-align:left;"{{!}} {{{stat_year2}}} {{#if:{{{ref_area2|}}}|{{{ref_area2}}}}}
               |{{!!}}
              }}
        {{!}} {{convinfobox|{{{stat_area2|}}}|km2||sqmi}}
      }}
   }}
<!----Area: 3rd year---->
   {{!}}- class="{{#if:{{{stat_area4|}}}{{{stat_area5<includeonly>|</includeonly>}}} |mergedrow|mergedbottomrow}}"
   {{#if:{{{stat_area3|}}}
    | {{#ifeq:{{{stat_area3|}}}|{{{stat_area2|}}}
       |
       |{{!}} {{#if:{{{stat_year3|}}}
               |style="width:1.0em; padding:0 0 0 0.6em;"{{!}} &nbsp;•&nbsp; {{!!}}style="padding-left:0;text-align:left;"{{!}} {{{stat_year3}}} {{#if:{{{ref_area3|}}}|{{{ref_area3}}}}}
               |{{!!}}
              }}
        {{!}} {{convinfobox|{{{stat_area3|}}}|km2||sqmi}}
      }}
   }}
<!----Area: 4th year---->
   {{!}}- class="{{#if:{{{stat_area5<includeonly>|</includeonly>}}} |mergedrow|mergedbottomrow}}"
   {{#if:{{{stat_area4|}}}
    | {{#ifeq:{{{stat_area4|}}}|{{{stat_area3|}}}
       |
       |{{!}} {{#if:{{{stat_year4|}}}
               |style="width:1.0em; padding:0 0 0 0.6em;"{{!}} &nbsp;•&nbsp; {{!!}}style="padding-left:0;text-align:left;"{{!}} {{{stat_year4}}} {{#if:{{{ref_area4|}}}|{{{ref_area4}}}}}
               |{{!!}}
              }}
        {{!}} {{convinfobox|{{{stat_area4|}}}|km2||sqmi}}
      }}
   }}
<!----Area: 5th year---->
   {{!}}- class="mergedbottomrow"
   {{#if:{{{stat_area5<includeonly>|</includeonly>}}}
    | {{#ifeq:{{{stat_area5<includeonly>|</includeonly>}}}|{{{stat_area4<includeonly>|</includeonly>}}}
       |
       |{{!}} {{#if:{{{stat_year5<includeonly>|</includeonly>}}} |style="width:1.0em; padding:0 0 0 0.6em;"{{!}} &nbsp;•&nbsp; {{!!}}style="padding:0em 1em 0.2em 0;vertical-align:top;text-align:left;"{{!}} {{{stat_year5}}}
               |{{!!}}
              }}
        {{!}} {{convinfobox|{{{stat_area5|}}}|km2||sqmi}}
      }}
   }}
<!----Area: Alternative if stat_year1 not provided---->
 | {{#if:{{{stat_area1|}}}
    |{{!}}colspan="2"{{!}} '''[Area](https://second-renaissance.fandom.com/wiki/List_of_countries_and_outlying_territories_by_area)'''
     {{!}} {{convinfobox|{{{stat_area1|}}}|km2||sqmi}}
   }}
}}
<!---------------
  Population
 ---------------->
|- class="mergedtoprow"
{{#if:{{{stat_pop1<includeonly>|</includeonly>}}}{{{stat_pop2|}}}{{{stat_pop3|}}}{{{stat_pop4|}}}{{{stat_pop5|}}}
 |{{!}}colspan="3"{{!}} '''[Population](2953-list-of-countries-by-population.md)'''
}}
<!----Population: 1st year---->
|- class="{{#if:{{{stat_area1<includeonly>|</includeonly>}}}{{{stat_pop2|}}}{{{stat_pop3|}}}{{{stat_pop4|}}}{{{stat_pop5|}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{stat_pop1<includeonly>|</includeonly>}}}
 |{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} &nbsp;•&nbsp;
  {{!}}style="padding-left:0;text-align:left;"{{!}} {{#if:{{{stat_year1<includeonly>|</includeonly>}}}|{{{stat_year1}}}}} est.{{#if:{{{ref_pop1|}}}|{{{ref_pop1}}}}}
  {{!}} {{formatnum:{{{stat_pop1<includeonly>|</includeonly>}}}}}&nbsp;
  {{!}}- class="{{#if:{{{stat_pop2|}}}{{{stat_pop3|}}}{{{stat_pop4|}}}{{{stat_pop5<includeonly>|</includeonly>}}} |mergedrow|mergedbottomrow}}"
  {{#if:{{{stat_area1<includeonly>|</includeonly>}}}
   |{{!}}colspan="2"{{!}} {{nbsp|5}}Density
    {{!}}style="white-space:nowrap;"{{!}} {{convinfobox|<includeonly>{{#expr:{{{stat_pop1}}} div {{{stat_area1}}}}}</includeonly>|/km2||/sqmi|0|adj=ri0}}
  }}
}}
<!----Population: 2nd year---->
|- class="{{#if:{{{stat_area2|}}}{{{stat_pop3|}}}{{{stat_pop4|}}}{{{stat_pop5<includeonly>|</includeonly>}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{stat_pop2|}}}
 |{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} &nbsp;•&nbsp;
  {{!}}style="padding-left:0;text-align:left;"{{!}} {{{stat_year2}}} est.{{#if:{{{ref_pop2|}}}|{{{ref_pop2}}}}}
  {{!}} {{formatnum:{{{stat_pop2|}}}}}&nbsp;
  {{!}}- class="{{#if:{{{stat_pop3|}}}{{{stat_pop4|}}}{{{stat_pop5|}}} |mergedrow|mergedbottomrow}}"
  {{#if:{{{stat_area2|}}}
   |{{!}}colspan="2"{{!}} {{nbsp|5}}Density
    {{!}}style="white-space:nowrap;"{{!}} {{convinfobox|<includeonly>{{#expr:{{{stat_pop2}}} div {{{stat_area2}}}}}</includeonly>|/km2||/sqmi|0|adj=ri0}}
  }}
}}
<!----Population: 3rd year---->
|- class="{{#if:{{{stat_area3|}}}{{{stat_pop4|}}}{{{stat_pop5<includeonly>|</includeonly>}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{stat_pop3|}}}
 |{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} &nbsp;•&nbsp;
  {{!}}style="padding-left:0;text-align:left;"{{!}} {{{stat_year3}}} est.{{#if:{{{ref_pop3|}}}|{{{ref_pop3}}}}}
  {{!}} {{formatnum:{{{stat_pop3|}}}}}&nbsp;
  {{!}}- class="{{#if:{{{stat_pop4|}}}{{{stat_pop5|}}} |mergedrow|mergedbottomrow}}"
  {{#if:{{{stat_area3|}}}
   |{{!}}colspan="2"{{!}} {{nbsp|5}}Density
    {{!}}style="white-space:nowrap;"{{!}} {{convinfobox|<includeonly>{{#expr:{{{stat_pop3}}} div {{{stat_area3}}}}}</includeonly>|/km2||/sqmi|0|adj=ri0}}
  }}
}}
<!----Population: 4th year---->
|- class="{{#if:{{{stat_area4|}}}{{{stat_pop5<includeonly>|</includeonly>}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{stat_pop4|}}}
 |{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} &nbsp;•&nbsp;
  {{!}}style="padding-left:0;text-align:left;"{{!}} {{{stat_year4}}} est.{{#if:{{{ref_pop4|}}}|{{{ref_pop4}}}}}
  {{!}} {{formatnum:{{{stat_pop4|}}}}}&nbsp;
  {{!}}- class="{{#if:{{{stat_pop5<includeonly>|</includeonly>}}} |mergedrow|mergedbottomrow}}"
  {{#if:{{{stat_area4|}}}
   |{{!}}colspan="2"{{!}} {{nbsp|5}}Density
    {{!}}style="white-space:nowrap;"{{!}} {{convinfobox|<includeonly>{{#expr:{{{stat_pop4}}} div {{{stat_area4}}}}}</includeonly>|/km2||/sqmi|0|adj=ri0}}
  }}
}}
<!----Population: 5th year---->
|- class="{{#if:{{{stat_area5<includeonly>|</includeonly>}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{stat_pop5<includeonly>|</includeonly>}}}
 |{{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} &nbsp;•&nbsp;
  {{!}}style="padding-left:0;text-align:left;"{{!}} {{{stat_year5}}} est.{{#if:{{{ref_pop5|}}}|{{{ref_pop5}}}}}
  {{!}} {{formatnum:{{{stat_pop5<includeonly>|</includeonly>}}}}}&nbsp;
  {{!}}- class="mergedbottomrow"
  {{#if:{{{stat_area5<includeonly>|</includeonly>}}}
   |{{!}}colspan="2"{{!}} {{nbsp|5}}Density
    {{!}}style="white-space:nowrap;"{{!}} {{convinfobox|<includeonly>{{#expr:{{{stat_pop5}}} div {{{stat_area5}}}}}</includeonly>|/km2||/sqmi|0|adj=ri0}}
  }}
}}
|-
<!------------------------------
  Currency, cctld, calling code
 ------------------------------->
{{#if: {{{currency<includeonly>|</includeonly>}}} |
{{!}}colspan="2"{{!}} '''Currency'''
{{!}} {{#ifexist:{{{currency}}}|[{{{currency}}}](https://second-renaissance.fandom.com/wiki/{{{currency}}})|{{{currency}}}}}
}}
|-
{{#if:{{{cctld|}}}
 |{{!}}colspan="2"{{!}} '''[Internet TLD](993-country-code-top-level-domain.md)'''
  {{!}} {{{cctld}}}
}}
|-
{{#if:{{{calling_code|}}}
 |{{!}}colspan="2"{{!}} '''[Calling code](https://second-renaissance.fandom.com/wiki/List_of_country_calling_codes)'''
  {{!}} [+{{{calling_code}}}](https://second-renaissance.fandom.com/wiki/+{{{calling_code}}})
        {{#ifexist:{{{calling_code_note|}}} |{{!}} {{{calling_code_note}}} }}
}}
<!------------------------
  Preceding and succeding entities (unless listed in flag-only format at the top)
 ------------------------->
|-
{{#ifeq:{{#expr:{{#expr:{{#if:{{{p1|}}}|1|0}}+{{#if:{{{s1|}}}|1|0}}}} > 0}} | 1 |{{#ifeq:{{{successorflags|}}}|yes||
{{!}}colspan="3"{{!}} <!--start subtable:-->
{{{!}} style="width:95%; background: transparent; text-align:center; margin:0 auto;"
{{!}}-
{{!}} style="text-align:center; border:0; padding-bottom:0"{{!}}<div id="before-after"></div> {{#if:{{{p1|}}}|'''Preceded by'''}} {{!}}{{!}} style="text-align:center;border:0; padding-bottom:0;"{{!}} {{#if:{{{s1|}}}|'''Succeeded by'''}}
{{!}}-
{{!}} style="vertical-align:top; text-align:center; border:0;"{{!}} {{#if:{{{p1|}}} | <!--start subtable:-->{{{!}} style="width:100%; background: transparent; text-align:center; margin:0 auto;  border:0;"
{{!}}-
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_p1|}}}|[20px{{#ifeq:{{{border_p1}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_p1}}})|{{#if:{{{image_p1|}}}|{{{image_p1}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:left;"{{!}} [{{{p1}}}](https://second-renaissance.fandom.com/wiki/{{{p1}}})
{{!}}-
{{#if:{{{p2|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_p2|}}}|[20px{{#ifeq:{{{border_p2}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_p2}}})|{{#if:{{{image_p2|}}}|{{{image_p2}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:left;"{{!}} [{{{p2}}}](https://second-renaissance.fandom.com/wiki/{{{p2}}})}}
{{!}}-
{{#if:{{{p3|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_p3|}}}|[20px{{#ifeq:{{{border_p3}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_p3}}})|{{#if:{{{image_p3|}}}|{{{image_p3}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:left;"{{!}} [{{{p3}}}](https://second-renaissance.fandom.com/wiki/{{{p3}}})}}
{{!}}-
{{#if:{{{p4|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_p4|}}}|[20px{{#ifeq:{{{border_p4}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_p4}}})|{{#if:{{{image_p4|}}}|{{{image_p4}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:left;"{{!}} [{{{p4}}}](https://second-renaissance.fandom.com/wiki/{{{p4}}})}}
{{!}}-
{{#if:{{{p5|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_p5|}}}|[20px{{#ifeq:{{{border_p5}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_p5}}})|{{#if:{{{image_p5|}}}|{{{image_p5}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:left;"{{!}} [{{{p5}}}](https://second-renaissance.fandom.com/wiki/{{{p5}}})}}
{{!}}-
{{#if:{{{p6|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_p6|}}}|[20px{{#ifeq:{{{border_p6}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_p6}}})|{{#if:{{{image_p6|}}}|{{{image_p6}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:left;"{{!}} [{{{p6}}}](https://second-renaissance.fandom.com/wiki/{{{p6}}})}}
{{!}}-
{{#if:{{{p7|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_p7|}}}|[20px{{#ifeq:{{{border_p7}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_p7}}})|{{#if:{{{image_p7|}}}|{{{image_p7}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:left;"{{!}} [{{{p7}}}](https://second-renaissance.fandom.com/wiki/{{{p7}}})}}
{{!}}-
{{#if:{{{p8|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_p8|}}}|[20px{{#ifeq:{{{border_p8}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_p8}}})|{{#if:{{{image_p8|}}}|{{{image_p8}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:left;"{{!}} [{{{p8}}}](https://second-renaissance.fandom.com/wiki/{{{p8}}})}}
{{!}}-
{{#if:{{{p9|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_p9|}}}|[20px{{#ifeq:{{{border_p9}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_p9}}})|{{#if:{{{image_p9|}}}|{{{image_p9}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:left;"{{!}} [{{{p9}}}](https://second-renaissance.fandom.com/wiki/{{{p9}}})}}
{{!}}-
{{#if:{{{p10|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_p10|}}}|[20px{{#ifeq:{{{border_p10}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_p10}}})|{{#if:{{{image_p10|}}}|{{{image_p10}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:left;"{{!}} [{{{p10}}}](https://second-renaissance.fandom.com/wiki/{{{p10}}})}}
{{!}}-
{{#if:{{{p11|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_p11|}}}|[20px{{#ifeq:{{{border_p11}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_p11}}})|{{#if:{{{image_p11|}}}|{{{image_p11}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:left;"{{!}} [{{{p11}}}](https://second-renaissance.fandom.com/wiki/{{{p11}}})}}
{{!}}-
{{#if:{{{p12|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_p12|}}}|[20px{{#ifeq:{{{border_p12}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_p12}}})|{{#if:{{{image_p12|}}}|{{{image_p12}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:left;"{{!}} [{{{p12}}}](https://second-renaissance.fandom.com/wiki/{{{p12}}})}}
{{!}}-
{{#if:{{{p13|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_p13|}}}|[20px{{#ifeq:{{{border_p13}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_p13}}})|{{#if:{{{image_p13|}}}|{{{image_p13}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:left;"{{!}} [{{{p13}}}](https://second-renaissance.fandom.com/wiki/{{{p13}}})}}
{{!}}-
{{#if:{{{p14|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_p14|}}}|[20px{{#ifeq:{{{border_p14}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_p14}}})|{{#if:{{{image_p14|}}}|{{{image_p14}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:left;"{{!}} [{{{p14}}}](https://second-renaissance.fandom.com/wiki/{{{p14}}})}}
{{!}}-
{{#if:{{{p15|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_p15|}}}|[20px{{#ifeq:{{{border_p15}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_p15}}})|{{#if:{{{image_p15|}}}|{{{image_p15}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:left;"{{!}} [{{{p15}}}](https://second-renaissance.fandom.com/wiki/{{{p15}}})}}
<!--end subtable:-->
{{!}}}
}}
{{!}} style="vertical-align:top; text-align:center;border:0;"{{!}} {{#if:{{{s1|}}} | <!--start subtable:-->{{{!}} style="width:92%; background:transparent; text-align:center; margin:0 auto; border:0;"
{{!}}-
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:right;"{{!}} [{{{s1}}}](https://second-renaissance.fandom.com/wiki/{{{s1}}})
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_s1|}}}|[20px{{#ifeq:{{{border_s1}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_s1}}})|{{#if:{{{image_s1|}}}|{{{image_s1}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}
{{!}}-
{{#if:{{{s2|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:right;"{{!}} [{{{s2}}}](https://second-renaissance.fandom.com/wiki/{{{s2}}})
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_s2|}}}|[20px{{#ifeq:{{{border_s2}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_s2}}})|{{#if:{{{image_s2|}}}|{{{image_s2}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}}}
{{!}}-
{{#if:{{{s3|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:right;"{{!}} [{{{s3}}}](https://second-renaissance.fandom.com/wiki/{{{s3}}})
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_s3|}}}|[20px{{#ifeq:{{{border_s3}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_s3}}})|{{#if:{{{image_s3|}}}|{{{image_s3}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}}}
{{!}}-
{{#if:{{{s4|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:right;"{{!}} [{{{s4}}}](https://second-renaissance.fandom.com/wiki/{{{s4}}})
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_s4|}}}|[20px{{#ifeq:{{{border_s4}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_s4}}})|{{#if:{{{image_s4|}}}|{{{image_s4}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}}}
{{!}}-
{{#if:{{{s5|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:right;"{{!}} [{{{s5}}}](https://second-renaissance.fandom.com/wiki/{{{s5}}})
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_s5|}}}|[20px{{#ifeq:{{{border_s5}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_s5}}})|{{#if:{{{image_s5|}}}|{{{image_s5}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}}}
{{!}}-
{{#if:{{{s6|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:right;"{{!}} [{{{s6}}}](https://second-renaissance.fandom.com/wiki/{{{s6}}})
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_s6|}}}|[20px{{#ifeq:{{{border_s6}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_s6}}})|{{#if:{{{image_s6|}}}|{{{image_s6}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}}}
{{!}}-
{{#if:{{{s7|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:right;"{{!}} [{{{s7}}}](https://second-renaissance.fandom.com/wiki/{{{s7}}})
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_s7|}}}|[20px{{#ifeq:{{{border_s7}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_s7}}})|{{#if:{{{image_s7|}}}|{{{image_s7}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}}}
{{!}}-
{{#if:{{{s8|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:right;"{{!}} [{{{s8}}}](https://second-renaissance.fandom.com/wiki/{{{s8}}})
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_s8|}}}|[20px{{#ifeq:{{{border_s8}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_s8}}})|{{#if:{{{image_s8|}}}|{{{image_s8}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}}}
{{!}}-
{{#if:{{{s9|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:right;"{{!}} [{{{s9}}}](https://second-renaissance.fandom.com/wiki/{{{s9}}})
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_s9|}}}|[20px{{#ifeq:{{{border_s9}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_s9}}})|{{#if:{{{image_s9|}}}|{{{image_s9}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}}}
{{!}}-
{{#if:{{{s10|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:right;"{{!}} [{{{s10}}}](https://second-renaissance.fandom.com/wiki/{{{s10}}})
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_s10|}}}|[20px{{#ifeq:{{{border_s10}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_s10}}})|{{#if:{{{image_s10|}}}|{{{image_s10}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}}}
{{!}}-
{{#if:{{{s11|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:right;"{{!}} [{{{s11}}}](https://second-renaissance.fandom.com/wiki/{{{s11}}})
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_s11|}}}|[20px{{#ifeq:{{{border_s11}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_s11}}})|{{#if:{{{image_s11|}}}|{{{image_s11}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}}}
{{!}}-
{{#if:{{{s12|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:right;"{{!}} [{{{s12}}}](https://second-renaissance.fandom.com/wiki/{{{s12}}})
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_s12|}}}|[20px{{#ifeq:{{{border_s12}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_s12}}})|{{#if:{{{image_s12|}}}|{{{image_s12}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}}}
{{!}}-
{{#if:{{{s13|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:right;"{{!}} [{{{s13}}}](https://second-renaissance.fandom.com/wiki/{{{s13}}})
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_s13|}}}|[20px{{#ifeq:{{{border_s13}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_s13}}})|{{#if:{{{image_s13|}}}|{{{image_s13}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}}}
{{!}}-
{{#if:{{{s14|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:right;"{{!}} [{{{s14}}}](https://second-renaissance.fandom.com/wiki/{{{s14}}})
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_s14|}}}|[20px{{#ifeq:{{{border_s14}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_s14}}})|{{#if:{{{image_s14|}}}|{{{image_s14}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}}}
{{!}}-
{{#if:{{{s15|}}} |
{{!}}style="border:0; padding:0; vertical-align:middle; text-align:right;"{{!}} [{{{s15}}}](https://second-renaissance.fandom.com/wiki/{{{s15}}})
{{!}}style="border:0; padding:0; vertical-align:middle;"{{!}} {{#if:{{{flag_s15|}}}|[20px{{#ifeq:{{{border_s15}}}|no||{{!}}border}}|link=|alt=](https://second-renaissance.fandom.com/wiki/File:{{{flag_s15}}})|{{#if:{{{image_s15|}}}|{{{image_s15}}}|[22px|link=|alt=](https://second-renaissance.fandom.com/wiki/File:Blank.png)}}}}}}
<!--end subtable:-->
{{!}}}
}}
<!--end subtable:-->
{{!}}}
}}}}
<!-------------
 Today part of
 -------------->
|-
{{#if: {{{today<includeonly>|</includeonly>}}}
 |{{!}}colspan="2"{{!}} '''Today part of'''
  {{!}} {{{today}}}
}}
<!---------
 Footnotes
 ---------->
<!-----Lettered footnotes----->
|- style="font-size:85%;"
{{#if:{{{footnote_a<includeonly>|</includeonly>}}}
 | {{!}}style="width:1.0em; padding:0.4em 0 0 0.6em;"{{!}} a. {{!!}}colspan="2" style="padding-left:0;text-align:left;"{{!}} {{{footnote_a}}}
}}
|- style="font-size:85%;" class="{{#if:{{{footnote_c|}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{footnote_b|}}}
 | {{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} b. {{!!}}colspan="2" style="padding-left:0;text-align:left;"{{!}} {{{footnote_b}}}
}}
|- style="font-size:85%;" class="{{#if:{{{footnote_d|}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{footnote_c|}}}
 | {{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} c. {{!!}}colspan="2" style="padding-left:0;text-align:left;"{{!}} {{{footnote_c}}}
}}
|- style="font-size:85%;" class="{{#if:{{{footnote_e|}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{footnote_d|}}}
 | {{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} d. {{!!}}colspan="2" style="padding-left:0;text-align:left;"{{!}} {{{footnote_d}}}
}}
|- style="font-size:85%;" class="{{#if:{{{footnote_f|}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{footnote_e|}}}
 | {{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} e. {{!!}}colspan="2" style="padding-left:0;text-align:left;"{{!}} {{{footnote_e}}}
}}
|- style="font-size:85%;" class="{{#if:{{{footnote_g|}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{footnote_f|}}}
 | {{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} f. {{!!}}colspan="2" style="padding-left:0;text-align:left;"{{!}} {{{footnote_f}}}
}}
|- style="font-size:85%;" class="{{#if:{{{footnote_h|}}} |mergedrow|mergedbottomrow}}"
{{#if:{{{footnote_g|}}}
 | {{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} g. {{!!}}colspan="2" style="padding-left:0;text-align:left;"{{!}} {{{footnote_g}}}
}}
|- style="font-size:85%;" class="mergedbottomrow"
{{#if:{{{footnote_h<includeonly>|</includeonly>}}}
 | {{!}}style="width:1.0em; padding:0 0 0 0.6em;"{{!}} h. {{!!}}colspan="2" style="padding-left:0;text-align:left;"{{!}} {{{footnote_h}}}
}}
|-
<!-----footnotes (non-specific)----->
{{#if:{{{footnotes<includeonly>|</includeonly>}}}
 | {{!}}colspan="3"{{!}} <small>{{{footnotes}}}</small>
}}
|-
<!-----footnotes2----->
{{#if:{{{footnotes2<includeonly>|</includeonly>}}}
 | {{!}}colspan="3"{{!}} <small>{{{footnotes2}}}</small>
}}
|-
{{#if:{{{_noautocat|<noinclude>yes</noinclude>}}} |
 | {{ns0|{{Infobox former country/autocat|continent={{{continent|}}} |empire={{{empire|}}} |region={{{region|}}} |status={{{status|}}} |year_start={{{year_start|}}} |common_name={{{common_name|}}} |year_end={{{year_end|}}} }} }}
}}
|}{{#invoke:Check for unknown parameters|check|unknown={{main other|[_VALUE_{{PAGENAME}}](https://second-renaissance.fandom.com/wiki/Category:Pages_using_infobox_former_country_with_unknown_parameters)}}|preview=Page using [Template:Infobox former country](650-template-infobox-former-country.md) with unknown parameter "_VALUE_"|ignoreblank=y| _noautocat | border_p1 | border_p10 | border_p11 | border_p12 | border_p13 | border_p14 | border_p15 | border_p2 | border_p3 | border_p4 | border_p5 | border_p6 | border_p7 | border_p8 | border_p9 | border_s1 | border_s10 | border_s11 | border_s12 | border_s13 | border_s14 | border_s15 | border_s2 | border_s3 | border_s4 | border_s5 | border_s6 | border_s7 | border_s8 | border_s9 | calling_code | calling_code_note | capital | capital_exile | cctld | coa_size | coat_alt | common_languages | common_name | continent | conventional_long_name | currency | date_end | date_event1 | date_event2 | date_event3 | date_event4 | date_event5 | date_event6 | date_post | date_pre | date_start | demonym | deputy1 | deputy2 | deputy3 | deputy4 | deputy5 | deputy6 | empire | era | event_end | event_post | event_pre | event_start | event1 | event2 | event3 | event4 | event5 | event6 | flag | flag_alt | flag_alt2 | flag_border | flag_caption | flag_p1 | flag_p10 | flag_p11 | flag_p12 | flag_p13 | flag_p14 | flag_p15 | flag_p2 | flag_p3 | flag_p4 | flag_p5 | flag_p6 | flag_p7 | flag_p8 | flag_p9 | flag_s1 | flag_s10 | flag_s11 | flag_s12 | flag_s13 | flag_s14 | flag_s15 | flag_s2 | flag_s3 | flag_s4 | flag_s5 | flag_s6 | flag_s7 | flag_s8 | flag_s9 | flag_size | flag_type | footnote_a | footnote_b | footnote_c | footnote_d | footnote_e | footnote_f | footnote_g | footnote_h | footnotes | footnotes2 | government_type | house1 | house2 | image_coat | image_flag | image_flag2 | image_map | image_map_alt | image_map_caption | image_map_size | image_map2 | image_map2_alt | image_map2_caption | image_map2_size | image_p1 | image_p10 | image_p11 | image_p12 | image_p13 | image_p14 | image_p15 | image_p2 | image_p3 | image_p4 | image_p5 | image_p6 | image_p7 | image_p8 | image_p9 | image_s1 | image_s10 | image_s11 | image_s12 | image_s13 | image_s14 | image_s15 | image_s2 | image_s3 | image_s4 | image_s5 | image_s6 | image_s7 | image_s8 | image_s9 | leader1 | leader2 | leader3 | leader4 | leader5 | leader6 | leader7 | leader8 | leader9 | legislature | life_span | location_map | national_anthem | national_motto | native_name | p1 | p10 | p11 | p12 | p13 | p14 | p15 | p2 | p3 | p4 | p5 | p6 | p7 | p8 | p9 | ref_area1 | ref_area2 | ref_area3 | ref_area4 | ref_pop1 | ref_pop2 | ref_pop3 | ref_pop4 | ref_pop5 | region | religion | representative1 | representative2 | representative3 | representative4 | representative5 | s1 | s10 | s11 | s12 | s13 | s14 | s15 | s2 | s3 | s4 | s5 | s6 | s7 | s8 | s9 | stat_area1 | stat_area2 | stat_area3 | stat_area4 | stat_area5 | stat_pop1 | stat_pop2 | stat_pop3 | stat_pop4 | stat_pop5 | stat_year1 | stat_year2 | stat_year3 | stat_year4 | stat_year5 | status | status_text | successorflags | symbol_type_article | symbol_caption | symbol_type | title_deputy | title_leader | title_representative | today | type_house1 | type_house2 | width | year_deputy1 | year_deputy2 | year_deputy3 | year_deputy4 | year_deputy5 | year_deputy6 | year_end | year_exile_end | year_exile_start | year_leader1 | year_leader2 | year_leader3 | year_leader4 | year_leader5 | year_leader6 | year_leader7 | year_leader8 | year_leader9 | year_representative1 | year_representative2 | year_representative3 | year_representative4 | year_representative5 | year_start 
}}{{main other|{{#if:{{{flag_type|}}}|[T{{PAGENAME}}](https://second-renaissance.fandom.com/wiki/Category:Pages_using_infobox_country_or_infobox_former_country_with_the_flag_caption_or_type_parameters)
}}{{#if:{{{flag_caption|}}}|[C{{PAGENAME}}](https://second-renaissance.fandom.com/wiki/Category:Pages_using_infobox_country_or_infobox_former_country_with_the_flag_caption_or_type_parameters)
}}{{#if:{{{symbol_type|}}}|[T{{PAGENAME}}](https://second-renaissance.fandom.com/wiki/Category:Pages_using_infobox_country_or_infobox_former_country_with_the_symbol_caption_or_type_parameters)
}}{{#if:{{{symbol_caption|}}}|[C{{PAGENAME}}](https://second-renaissance.fandom.com/wiki/Category:Pages_using_infobox_country_or_infobox_former_country_with_the_symbol_caption_or_type_parameters)
}}}}<noinclude>
{{documentation}}
</noinclude>
```

## Provenance

Raw source: `bronze/pages/2364/6849.wikitext` · revision `6849` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AInfobox_Former_International_Organization)
