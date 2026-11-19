---
page_id: 141
revision_id: 269
source_url: https://second-renaissance.fandom.com/wiki/Template%3AInfobox_political_party/doc
raw_sha256: 237412cf120f330a1ab3f428ce28227698fff839623464d388fbd505489c50ed
---

# Template:Infobox political party/doc

## Preserved source

```wikitext
{{Documentation subpage}}
{{lua|Module:Check for unknown parameters}}
{{Intricate template}}
{{high-use|6300}}
<!--Categories where indicated at the bottom of this page, please; interwikis at Wikidata (see [Wikipedia:Wikidata](https://second-renaissance.fandom.com/wiki/Wikipedia:Wikidata))-->

# Usage
## Basic
{{Generic template demo
|name 
|logo 
|colorcode=red 
|leader 
|president 
|chairman 
|general_secretary 
|first_secretary 
|secretary_general 
|presidium 
|secretary 
|spokesperson 
|foundation 
|ideology 
|country  
|headquarters 
|international 
|website 
|country
}}
<pre style="overflow:auto;">
{{Infobox political party
| name = 
| logo = 
| colorcode =     <!-- HTML color code (e.g. "red", "#FF0000" or Party metadata color template) otherwise "transparent" -->
| leader = 
| president = 
| chairman = 
| general_secretary = 
| first_secretary = 
| secretary_general = 
| presidium = 
| secretary = 
| spokesperson = 
| foundation =    <!-- {{start date|YYYY|MM|DD}} -->
| ideology = 
| headquarters = 
| international = 
| website = 
| country = 
}}
</pre>
<br clear="right" />

## Full
{{Generic template demo
 |name |native_name 
|native_name_lang |lang1 |name_lang1 |lang2 |name_lang2 |lang3 |name_lang3 |lang4 |name_lang4 |logo |caption |colorcode=red |abbreviation
 |leader |president |chairperson={{{chairperson}}} or {{{chairman}}} |general_secretary |first_secretary |secretary_general |presidium |secretary |spokesperson |founder
 |leader1_title |leader1_name |leader2_title |leader2_name |leader3_title |leader3_name |leader4_title |leader4_name |leader5_title |leader5_name
 |slogan |founded |legalised |dissolved |merger |split |predecessor |merged |successor |headquarters |newspaper |think_tank |student_wing |youth_wing |wing1_title |wing1 |wing2_title |wing2 |wing3_title |wing3
 |membership_year=[''year''] |membership |ideology |position |religion |national |international |european |europarl |affiliation1_title |affiliation1 |colors |anthem
 |blank1_title |blank1 |blank2_title |blank2 |blank3_title |blank3 |blank4_title |blank4
 |seats1_title |seats1 |seats2_title |seats2 |seats3_title |seats3 |seats4_title |seats4
 |symbol |flag  |website |country |country2 |footnotes 
}}
<pre style="overflow:auto;">
{{Infobox political party
| name = 
| native_name = 
| native_name_lang =
| lang1 = 
| name_lang1 = 
| lang2 = 
| name_lang2 = 
| lang3 = 
| name_lang3 = 
| lang4 = 
| name_lang4 = 
| logo = 
| caption =
| colorcode =       <!-- HTML color code (e.g. "red", "#FF0000" or Party metadata color template) otherwise "transparent" -->
| abbreviation =    <!-- official abbreviation -->
| leader = 
| president = 
| chairperson =     <!-- or: | chairman = -->
| general_secretary =
| first_secretary =
| secretary_general = 
| presidium =
| secretary =
| spokesperson = 
| founder = 
| leader1_title = 
| leader1_name = 
| leader2_title = 
| leader2_name = 
| leader3_title = 
| leader3_name = 
| leader4_title = 
| leader4_name = 
| leader5_title = 
| leader5_name = 
| slogan = 
| founded =         <!-- {{start date|YYYY|MM|DD}} -->
| legalised =       <!-- or |legalized= -->
| dissolved =       <!-- {{end date|YYYY|MM|DD}} -->
| merger = 
| split = 
| predecessor = 
| merged = 
| successor = 
| headquarters = 
| newspaper = 
| think_tank = 
| student_wing = 
| youth_wing = 
| wing1_title = 
| wing1 = 
| wing2_title = 
| wing2 = 
| wing3_title = 
| wing3 = 
| membership_year = 
| membership = 
| ideology = 
| position =
| religion = 
| national = 
| international = 
| european = 
| europarl = 
| affiliation1_title = 
| affiliation1 = 
| colors =          <!-- or: | colours = -->
| anthem = 
| blank1_title = 
| blank1 = 
| blank2_title = 
| blank2 = 
| blank3_title = 
| blank3 = 
| blank4_title = 
| blank4 = 
| seats1_title = 
| seats1 =          <!-- {{Infobox political party/seats|seats_won|total_seats|hex=#ff0000}} -->
| seats2_title = 
| seats2 = 
| seats3_title = 
| seats3 = 
| seats4_title = 
| seats4 =          <!-- up to |seats11= -->
| symbol = 
| flag = 
| website = 
| state =           <!-- or country -->
| country =         <!-- or state -->
| country_dab1 = 
| parties_dab1 = 
| elections_dab1 = 
| country2 = 
| country_dab2 = 
| parties_dab2 = 
| elections_dab2 = 
| footnotes = 
}}
</pre>
<br clear="right" />

# Microformat
{{UF-hcard-org}}

# TemplateData
{{TemplateDataHeader}}
<templatedata>{
  "description": "An infobox for political party.",
  "params": {
  "name": {
      "label": "Name",
      "description": "The name of the party.",
      "type": "string",
      "default": "",
      "required": false
    },
  "logo": {
      "label": "Logo",
      "description": "The logo of the party.",
      "type": "string",
      "default": "",
      "required": false
    },
  "colorcode": {
      "label": "Color code",
      "description": "The color code of the party. HTML color code (e.g. red, #FF0000 or Party metadata color template) or transparent for no coloring.",
      "type": "string",
      "default": "",
      "required": false
    },
  "leader": {
      "label": "Leader",
      "description": "The leader of the party.",
      "type": "string",
      "default": "",
      "required": false
    },
  "president": {
      "label": "President",
      "description": "The president of the party.",
      "type": "string",
      "default": "",
      "required": false
    },
  "chairman":{
    "label": "Chairman",
    "description":
    "The chairman of the party.",
    "type": "string",
    "default": "",
    "required": false
  },
  "general_secretary":{
    "label": "General secretary",
    "description":
    "The general secretary of the party.",
    "type": "string",
    "default": "",
    "required": false
  },
  "first_secretary":{
    "label": "First secretary",
    "description":
    "The first secretary of the party.",
    "type": "string",
    "default": "",
    "required": false
  },
  "secretary_general":{
    "label": "Secretary-general",
    "description":
    "The secretary-general of the party.",
    "type": "string",
    "default": "",
    "required": false
  },
  "presidium":{
    "label": "Presidium",
    "description":
    "The presidium of the party.",
    "type": "string",
    "default": "",
    "required": false
  },
  "secretary":{
    "label": "Secretary",
    "description":
    "The secretary of the party.",
    "type": "string",
    "default": "",
    "required": false
  },
  "spokesperson":{
    "label": "Spokesperson",
    "description":
    "The spokesperson of the party.",
    "type": "string",
    "default": "",
    "required": false
  },
  "foundation":{
    "label": "Foundation",
    "description":
    "The foundation date of the party. Insert as {{Start date|YYYY|MM|DD}}.",
    "type": "string",
    "default": "",
    "required": false
  },
  "ideology":{
    "label": "Ideology",
    "description":
    "The ideology of the party.",
    "type": "string",
    "default": "",
    "required": false
  },
  "headquarters":{
    "label": "Headquarters",
    "description":
    "The headquarters of the party.",
    "type": "string",
    "default": "",
    "required": false
  },
  "international":{
    "label": "International",
    "description":
    "The international of the party.",
    "type": "string",
    "default": "",
    "required": false
  },
  "website":{
    "label": "Website",
    "description":
    "The website of the party.",
    "type": "string",
    "default": "",
    "required": false
  },
  "country":{
    "label": "Country",
    "description":
    "The country of the party.",
    "type": "string",
    "default": "",
    "required": false
  }
 } 
}</templatedata>

# See also
* {{tl|Composition bar}}, used to display a statistic such as the number of seats held by a political party.

; Hidden tracking/maintenance category
* [:Category:Political party articles using deprecated parameters](https://second-renaissance.fandom.com/wiki/:Category:Political_party_articles_using_deprecated_parameters) (via [Module:Check for unknown parameters](722-module-check-for-unknown-parameters.md))

<br/>{{Organization infoboxes}}

<includeonly>{{#ifeq:{{SUBPAGENAME}}|sandbox | |
<!--Categories below this line, please; interwikis at Wikidata-->
[Political Party](https://second-renaissance.fandom.com/wiki/Category:Organization_infobox_templates)
[](https://second-renaissance.fandom.com/wiki/Category:Political_party_infobox_templates)
[Category:Templates that add a tracking category](https://second-renaissance.fandom.com/wiki/Category:Templates_that_add_a_tracking_category)
}}</includeonly>
```

## Provenance

Raw source: `bronze/pages/141/269.wikitext` · revision `269` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AInfobox_political_party/doc)
