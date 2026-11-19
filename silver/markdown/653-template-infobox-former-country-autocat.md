---
page_id: 653
revision_id: 914
source_url: https://second-renaissance.fandom.com/wiki/Template%3AInfobox_former_country/autocat
raw_sha256: 58c65234cbc523b7605219fd2493cfbef49e0a99acb0f1a20b96e5bed32ee8d2
---

# Template:Infobox former country/autocat

## Preserved source

```wikitext
<!-- Start common name check
-->{{#if:{{{common_name<includeonly>|</includeonly>}}}||
{{!}}- style="font-size: 85%;"
{{!}} colspan=2 {{!}} '''Warning''':  ''Value not specified for "[common_name](2822-template-infobox-former-country-doc.md)"''[N](https://second-renaissance.fandom.com/wiki/Category:Former_country_articles_requiring_maintenance)
}}<!-- Start Continent/Region Categories
-->{{#if:{{{continent|}}}|
 {{#switch:{{{region}}}
  |Italy = [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_countries_on_the_Italian_Peninsula)
  |Balkans = [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_countries_in_the_Balkans)
  |British Isles = [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_countries_in_the_British_Isles)
  |Low Countries |Netherlands = [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_polities_in_the_Netherlands)
  |Japan = [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_countries_in_Japanese_history)
  |Korea = [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_countries_in_Korean_history)
  |Malaysia = [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_countries_in_Malaysian_history)
  |China = [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_countries_in_Chinese_history)
  |Central Asia|South Asia|Southeast Asia|East Asia = [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_countries_in_{{{region}}})
  |the Middle East|Middle East = [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_countries_in_the_Middle_East)
  |#default = {{#switch:{{ucfirst:{{{country}}}}}
    |China|Japan|Korea|Malaysia = [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_countries_in_{{{country}}}_history)]
    |#default = {{#switch:{{{continent}}}
      |Africa|Asia|Europe|North America|South America = [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_countries_in_{{{continent}}})
      |Australia|Oceania = [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_countries_in_Oceania)
      |Asia, Europe|Eurasia = [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_countries_in_Europe)[{{{common_name}}}, {{{year_start}}}](3641-category-former-countries-in-asia.md)
      |Africa, Asia|Afroasia = [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_countries_in_Africa)[{{{common_name}}}, {{{year_start}}}](3641-category-former-countries-in-asia.md)
      |Africa, Europe|Afroeurope = [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_countries_in_Africa)[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_countries_in_Europe)
      |Africa, Asia, Europe|Afroeurasia = [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_countries_in_Europe)[{{{common_name}}}, {{{year_start}}}](3641-category-former-countries-in-asia.md)[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_countries_in_Africa)
      |Caribbean=<!-- No category yet -->
      |#default={{!}}- style="font-size: 85%;"
       {{!}} colspan=2 {{!}} '''Warning''': ''Value specified for "[continent](2822-template-infobox-former-country-doc.md)" [does not comply](2822-template-infobox-former-country-doc.md)''[C](https://second-renaissance.fandom.com/wiki/Category:Former_country_articles_requiring_maintenance)
  }}}}}}
 |<includeonly>{{!}}- style="font-size: 85%;"
  {{!}} colspan=2 {{!}} '''Warning''': ''Value not specified for "[continent](2822-template-infobox-former-country-doc.md)"''</includeonly>[C](https://second-renaissance.fandom.com/wiki/Category:Former_country_articles_requiring_maintenance)}}<!-- End Continent/Region Categories
--><!-- Start Status Categories
-->{{#if:{{{status|}}}| {{#switch:{{ucfirst:{{{status}}}}}
  |Empire = [{{{common_name}}}](https://second-renaissance.fandom.com/wiki/Category:Former_empires)
  |Federation |Federal = [{{{common_name}}}](https://second-renaissance.fandom.com/wiki/Category:Former_federations)
  |Confederation = [{{{common_name}}}](https://second-renaissance.fandom.com/wiki/Category:Former_confederations)
  |State union |State Union |Union = [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_state_unions)
  |Unrecognized |Unrecognised |Unrecognized state |Unrecognised state |Unrecognized State |Unrecognised State=[{{{common_name}}}](https://second-renaissance.fandom.com/wiki/Category:Former_unrecognized_countries)
  |City-state |City-State |City state |City State |City ={{#switch:{{{empire|}}}
    |Holy Roman Empire |HRE = [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:States_of_the_Holy_Roman_Empire)[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:City-states)[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Imperial_free_cities)
    |#default = [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:City-states)
  }}
  |Commonwealth realm |Commonwealth Realm = [{{{common_name}}}](https://second-renaissance.fandom.com/wiki/Category:Former_Commonwealth_realms)
  |League of Nations Mandate |League of Nations |Mandate = [{{{common_name}}}, {{{empire}}}](https://second-renaissance.fandom.com/wiki/Category:League_of_Nations_mandates)
  |United Nations Trust Territory| UN Trust Territory |Trust Territory=[{{{common_name}}}, {{{empire}}}](https://second-renaissance.fandom.com/wiki/Category:United_Nations_Trust_Territories)
  |Protectorate = [United Kingdom|UK|Britain=British}} protectorates|{{{common_name}}}, {{{empire}}}](https://second-renaissance.fandom.com/wiki/Category:Former_{{)
  |Client |Client state |Client State |Puppet |Puppet-state |Puppet state={{#switch:{{{empire|}}}
    |First French Empire | France = [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Client_states_of_the_Napoleonic_Wars)
    |#default =  [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_client_states)
  }}
  |Vassal |Fief |Abbey= {{#switch:{{{empire|}}}
    |Holy Roman Empire |HRE = [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:States_of_the_Holy_Roman_Empire)
    |#default =  [{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:Former_vassal_states)
  }}
  |Satellite |Satellite State | Satellite state =[{{{common_name}}}](https://second-renaissance.fandom.com/wiki/Category:Soviet_satellite_states)
  |Colony={{#switch:{{ucfirst:{{{empire}}}}}
    |United Kingdom |UK |British Empire |Britain=[{{{common_name}}}, {{{empire}}}](https://second-renaissance.fandom.com/wiki/Category:Former_British_colonies)
    |England=[{{{common_name}}}, {{{empire}}}](https://second-renaissance.fandom.com/wiki/Category:Former_English_colonies)
    |France |First French Empire| French Empire=[{{{common_name}}}, {{{empire}}}](https://second-renaissance.fandom.com/wiki/Category:Former_French_colonies)
    |NL |Netherlands |The Netherlands=[{{{common_name}}}, {{{empire}}}](https://second-renaissance.fandom.com/wiki/Category:Former_Dutch_colonies)
    |Belgium=[{{{common_name}}}, {{{empire}}}](https://second-renaissance.fandom.com/wiki/Category:Former_Belgian_colonies)
    |Spain |Spanish Empire=[{{{common_name}}}, {{{empire}}}](https://second-renaissance.fandom.com/wiki/Category:Former_Spanish_colonies)
    |Portugal=[{{{common_name}}}, {{{empire}}}](https://second-renaissance.fandom.com/wiki/Category:Former_Portuguese_colonies)
    |Germany |German Empire=[{{{common_name}}}, {{{empire}}}](https://second-renaissance.fandom.com/wiki/Category:Former_German_colonies)
    |Italy=[{{{common_name}}}, {{{empire}}}](https://second-renaissance.fandom.com/wiki/Category:Former_Italian_colonies)
    |Sweden=[{{{common_name}}}, {{{empire}}}](https://second-renaissance.fandom.com/wiki/Category:Former_Swedish_colonies)
    |Denmark=[{{{common_name}}}, {{{empire}}}](https://second-renaissance.fandom.com/wiki/Category:Former_Danish_colonies)
    |Norway=[{{{common_name}}}, {{{empire}}}](https://second-renaissance.fandom.com/wiki/Category:Former_Norwegian_colonies)
    |Japan=[{{{common_name}}}, {{{empire}}}](https://second-renaissance.fandom.com/wiki/Category:Former_Japanese_colonies)
    |#default = [{{{common_name}}}, {{{empire}}}](https://second-renaissance.fandom.com/wiki/Category:Former_colonies)
  }}
  |Exile |Exiled Government = [{{{common_name}}}](https://second-renaissance.fandom.com/wiki/Category:Governments_in_exile)
  |Provisional |Provisional Government |Provisional government = [{{{common_name}}}](https://second-renaissance.fandom.com/wiki/Category:Provisional_governments)
  |Special |Special territory |Military occupation |Rump state= 
  |#default=[S](https://second-renaissance.fandom.com/wiki/Category:Former_country_articles_requiring_maintenance)
}}}}<!-- End Status Categories
--><!-- Start Established Categories
-->{{#if:{{{year_start|}}}<!--
-->|{{#ifexist:Category:States and territories established in the {{{year_start}}}<!--
    -->|[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:States_and_territories_established_in_the_{{{year_start}}})<!--
    -->|{{#ifexist:Category:States and territories established in {{{year_start}}}<!--
       -->|[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:States_and_territories_established_in_{{{year_start}}})<!--
       -->|{{#ifeq:{{Str find| {{{year_start}}} |BC}}|-1<!--
          -->|{{#ifexist:Category:States and territories established in the {{#expr: {{{year_start}}}-{{{year_start}}}mod10}}s<!--
             -->|[{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:States_and_territories_established_in_the_{{)<!--
             -->|{{#ifexist:Category:States and territories established in the {{Ordinal|{{#expr: ({{{year_start}}}-{{{year_start}}}mod100)/100+1}}}} century<!--
                -->|[{{#expr: ({{{year_start}}}-{{{year_start}}}mod100)/100+1}}}} century|{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:States_and_territories_established_in_the_{{Ordinal)<!--
                -->|[Y1](https://second-renaissance.fandom.com/wiki/Category:Former_country_articles_requiring_maintenance)<!--
                -->}}<!--
             -->}}<!--
          -->|{{#ifexist:Category:States and territories established in the {{#expr: {{Str mid| {{{year_start}}}||{{#expr: {{Str find|{{{year_start}}} |BC}}-1}} }}-{{Str mid| {{{year_start}}}||{{#expr: {{Str find|{{{year_start}}} |BC}}-1}} }}mod10}}s BC<!--
             -->|[{{{year_start}}}||{{#expr: {{Str find|{{{year_start}}} |BC}}-1}} }}-{{Str mid| {{{year_start}}}||{{#expr: {{Str find|{{{year_start}}} |BC}}-1}} }}mod10}}s BC|{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:States_and_territories_established_in_the_{{)<!--
             -->|{{#ifexist:Category:States and territories established in the {{Ordinal| {{#expr: ({{Str mid| {{{year_start}}}||{{#expr: {{Str find|{{{year_start}}} |BC}}-1}} }} - {{Str mid| {{{year_start}}}||{{#expr: {{Str find|{{{year_start}}} |BC}}-1}} }}mod100)/100+1}}}} century BC<!--
                -->|[{{#expr: ({{Str mid| {{{year_start}}}||{{#expr: {{Str find|{{{year_start}}} |BC}}-1}} }} - {{Str mid| {{{year_start}}}||{{#expr: {{Str find|{{{year_start}}} |BC}}-1}} }}mod100)/100+1}}}} century BC|{{{common_name}}}, {{{year_start}}}](https://second-renaissance.fandom.com/wiki/Category:States_and_territories_established_in_the_{{Ordinal)<!--
                -->|[Y1](https://second-renaissance.fandom.com/wiki/Category:Former_country_articles_requiring_maintenance)<!--
                -->}}<!--
             -->}}<!--
          -->}}<!--
     -->}}<!--
  -->}}<!--
-->|[D1](https://second-renaissance.fandom.com/wiki/Category:Former_country_articles_requiring_maintenance)<!--
-->}}<!-- End Established Categories
--><!-- Start Disestablished Categories
-->{{#if:{{{year_end|}}}<!--
-->|{{#ifexist:Category:States and territories disestablished in the {{{year_end}}}<!--
    -->|[{{{common_name}}}, {{{year_end}}}](https://second-renaissance.fandom.com/wiki/Category:States_and_territories_disestablished_in_the_{{{year_end}}})<!--
    -->|{{#ifexist:Category:States and territories disestablished in {{{year_end}}}<!--
       -->|[{{{common_name}}}, {{{year_end}}}](https://second-renaissance.fandom.com/wiki/Category:States_and_territories_disestablished_in_{{{year_end}}})<!--
       -->|{{#ifeq:{{Str find| {{{year_end}}} |BC}}|-1<!--
          -->|{{#ifexist:Category:States and territories disestablished in the {{#expr: {{{year_end}}}-{{{year_end}}}mod10}}s<!--
             -->|[{{{common_name}}}, {{{year_end}}}](https://second-renaissance.fandom.com/wiki/Category:States_and_territories_disestablished_in_the_{{)<!--
             -->|{{#ifexist:Category:States and territories disestablished in the {{Ordinal|{{#expr: ({{{year_end}}}-{{{year_end}}}mod100)/100+1}}}} century<!--
                -->|[{{#expr: ({{{year_end}}}-{{{year_end}}}mod100)/100+1}}}} century|{{{common_name}}}, {{{year_end}}}](https://second-renaissance.fandom.com/wiki/Category:States_and_territories_disestablished_in_the_{{Ordinal)<!--
                -->|[Y2](https://second-renaissance.fandom.com/wiki/Category:Former_country_articles_requiring_maintenance)<!--
                -->}}<!--
             -->}}<!--
          -->|{{#ifexist:Category:States and territories disestablished in the {{#expr: {{Str mid| {{{year_end}}}||{{#expr: {{Str find|{{{year_end}}} |BC}}-1}} }}-{{Str mid| {{{year_end}}}||{{#expr: {{Str find|{{{year_end}}} |BC}}-1}} }}mod10}}s BC<!--
             -->|[{{{year_end}}}||{{#expr: {{Str find|{{{year_end}}} |BC}}-1}} }}-{{Str mid| {{{year_end}}}||{{#expr: {{Str find|{{{year_end}}} |BC}}-1}} }}mod10}}s BC|{{{common_name}}}, {{{year_end}}}](https://second-renaissance.fandom.com/wiki/Category:States_and_territories_disestablished_in_the_{{)<!--
             -->|{{#ifexist:Category:States and territories disestablished in the {{Ordinal|{{#expr: ({{Str mid| {{{year_end}}}||{{#expr: {{Str find|{{{year_end}}} |BC}}-1}} }} - {{Str mid| {{{year_end}}}||{{#expr: {{Str find|{{{year_end}}} |BC}}-1}} }}mod100)/100+1}}}} century BC<!--
                -->|[{{#expr: ({{Str mid| {{{year_end}}}||{{#expr: {{Str find|{{{year_end}}} |BC}}-1}} }} - {{Str mid| {{{year_end}}}||{{#expr: {{Str find|{{{year_end}}} |BC}}-1}} }}mod100)/100+1}}}} century BC|{{{common_name}}}, {{{year_end}}}](https://second-renaissance.fandom.com/wiki/Category:States_and_territories_disestablished_in_the_{{Ordinal)<!--
                -->|[Y2](https://second-renaissance.fandom.com/wiki/Category:Former_country_articles_requiring_maintenance)<!--
                -->}}<!--
             -->}}<!--
          -->}}<!--
     -->}}<!--
  -->}}<!--
-->|[D2](https://second-renaissance.fandom.com/wiki/Category:Former_country_articles_requiring_maintenance)<!--
-->}}<!-- End Disestablished Categories
--><noinclude>
{{Documentation|content=
This subtemplate of {{tl|Infobox country}} is used to automatically add categories to articles which transclude this template.  It should not be used directly

## Establishment dates
*First the template tests to see if "Category:States and territories established in the {{{year_start}}}" exists.  If so, it is added.
*If not, the template tests to see if "Category:States and territories established in {{{year_start}}}" exists.  If so, it is added.
*If not, the template tests to see if "Category:States and territories established in the DECADEs" where DECADE is the decade containing {{{year_start}}} (ie {{cl|States and territories established in the 120s BC}}).  If so, it is added.
*If not, the template tests to see if "Category:States and territories established in the Nth century" where N is the century containing {{{year_start}}} (ie {{cl|States and territories established in the 1st century BC}}).  If so, it is added.

The reason for the first case is in case an imprecise date is imputed, such as "the 820s" or "the 18th century", before trying exact dates like "1820".

## Disestablishment dates
*First the template tests to see if "Category:States and territories disestablished in the {{{year_start}}}" exists.  If so, it is added.
*If not, the template tests to see if "Category:States and territories disestablished in {{{year_start}}}" exists.  If so, it is added.
*If not, the template tests to see if "Category:States and territories disestablished in the DECADEs" where DECADE is the decade containing {{{year_start}}} (ie {{cl|States and territories disestablished in the 120s BC}}).  If so, it is added.
*If not, the template tests to see if "Category:States and territories disestablished in the Nth century" where N is the century containing {{{year_start}}} (ie {{cl|States and territories disestablished in the 1st century BC}}).  If so, it is added.

The reason for the first case is in case an imprecise date is imputed, such as "the 820s" or "the 18th century", before trying exact dates like "1820".
}}
</noinclude>
```

## Provenance

Raw source: `bronze/pages/653/914.wikitext` · revision `914` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AInfobox_former_country/autocat)
