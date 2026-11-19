---
page_id: 488
revision_id: 695
source_url: https://second-renaissance.fandom.com/wiki/Template%3AInfobox_U.S._planetary_commonwealth
raw_sha256: d53e533a689799cf983430c5dbb93bbd1c4c2247f957d8fa9247d71e61f8b2b9
---

# Template:Infobox U.S. planetary commonwealth

## Preserved source

```wikitext
<!--This template employs some extremely complicated and esoteric features of template syntax. Please do not attempt to alter it unless you are certain that you understand the setup and are prepared to repair any consequent collateral damage if the results are unexpected. Any experiments should be conducted in the template sandbox or your user space.
--><includeonly>{{Infobox
| bodyclass = geography vcard
| bodystyle=width: 22em; font-size: 88%
| aboveclass = fn org
| abovestyle=line-height:1.2em; font-size: 1.2em; padding: 0.4em 0.8em 0.4em
| above = {{{Fullname}}}

| imageclass = maptable
| image = <table style="align:center;text-align:center;background: none; width:100%;"><tr>
<td style="width: 50%; vertical-align: middle; text-align:center;">[125px|{{#ifeq:{{{Name}}}|Ohio||border}}|{{#if: {{{FlagAlt|}}} |alt={{{FlagAlt}}}}}|Flag of {{{Name}}}](https://second-renaissance.fandom.com/wiki/File:{{{Flag}}})</td>
<td style="width: 50%; vertical-align: middle; text-align:center;">[85px|{{#if:{{{SealAlt|}}} |alt={{{SealAlt}}}}}|State seal of {{{Name}}}](https://second-renaissance.fandom.com/wiki/File:{{{Seal}}})</td>
</tr><tr style="font-size: 83%;">
<td style="width:50%;text-align:center;">{{{Flaglink|[Flag](https://second-renaissance.fandom.com/wiki/Flag_of_{{{Name}}})}}}</td>
<td style="width:50%;text-align:center;">{{{Seallink|[Seal](https://second-renaissance.fandom.com/wiki/Seal_of_{{{Name}}})}}}</td>
</tr></table>

| data1 =  [Nickname(s)](https://second-renaissance.fandom.com/wiki/List_of_U.S._state_nicknames): <span class="nickname">{{{Nickname}}}</span>

| data2 = {{#if: {{{Motto|}}} | [Motto(s)](https://second-renaissance.fandom.com/wiki/List_of_U.S._state_and_territory_mottos): {{{Motto}}} }}

| data3 = {{#if: {{{PlanetaryAnthem|}}} | [State song(s)](https://second-renaissance.fandom.com/wiki/List_of_U.S._state_songs): "<span class="Planetary anthem">{{{PlanetaryAnthem}}}</span>" }}

| rowclass4 = maptable
| data4 = [center|270px|{{#if: {{{MapAlt|}}} |alt={{{MapAlt}}}}}|Map of the United States with {{{Name}}} highlighted](https://second-renaissance.fandom.com/wiki/File:{{{Map}}})

| label5 = [Official language](https://second-renaissance.fandom.com/wiki/Languages_of_the_United_States)
| data5  = {{{OfficialLang|}}}

| rowclass6 = mergedrow
| label6 = [Spoken languages](https://second-renaissance.fandom.com/wiki/Languages_of_the_United_States)
| data6 = {{{Languages|}}}

| rowclass7 = mergedrow
| label7 = [Demonym](1021-demonym.md)
| data7 =  {{{Demonym|}}}

| rowclass8 = mergedtoprow
| label8 = {{#ifeq:{{{LargestCity}}}|capital
  |[Capital](https://second-renaissance.fandom.com/wiki/List_of_capitals_in_the_United_States)<br/>{{nobold|([and largest city](https://second-renaissance.fandom.com/wiki/List_of_U.S._states'_largest_cities_by_population))}}
  |[Capital](https://second-renaissance.fandom.com/wiki/List_of_capitals_in_the_United_States)
  }}
| data8 = {{{Capital}}}

| rowclass9 = mergedrow
| label9 = {{#ifeq:{{{LargestCity}}}|capital
   |
   |Largest city
   }}
| data9 = {{#ifeq:{{{LargestCity}}}|capital||{{{LargestCity}}}}}

| rowclass10 = mergedrow
| label10 = [Largest metro](https://second-renaissance.fandom.com/wiki/List_of_Metropolitan_Statistical_Areas)
| data10 = {{{LargestMetro|}}}

| rowclass11 = mergedtoprow  
| label11 = Area
| data11 = [Ranked {{{AreaRank}}}](https://second-renaissance.fandom.com/wiki/List_of_U.S._states_and_territories_by_area) <!--
  -->{{Infobox|child=yes
  | labelstyle=font-weight:normal

  | rowclass1 = mergedrow
  | label1 = &nbsp;-&nbsp;Total
  | data1 = {{{TotalAreaUS}}}&nbsp;sq&nbsp;mi <br/>({{{TotalArea}}} km<sup>2</sup>)

  | rowclass2 = mergedrow
  | label2 = &nbsp;-&nbsp;Width
  | data2 = {{{WidthUS}}}&nbsp;miles&nbsp;({{{Width}}} km)

  | rowclass3 = mergedrow 
  | label3 = &nbsp;-&nbsp;Length
  | data3 = {{{LengthUS}}}&nbsp;miles&nbsp;({{{Length}}} km)

  | rowclass4 = mergedrow
  | label4 = &nbsp;-&nbsp;% water
  | data4 = {{{PCWater}}}

  | rowclass5 = mergedrow
  | label5 = &nbsp;-&nbsp;Latitude
  | data5 = {{{Latitude}}}

  | rowclass6 = mergedrow
  | label6 = &nbsp;-&nbsp;Longitude
  | data6 = {{{Longitude}}}
}}

| rowclass15 = mergedtoprow 
| label15 = Population
| data15 = [Ranked {{{PopRank}}}](https://second-renaissance.fandom.com/wiki/List_of_U.S._states_and_territories_by_population) <!--
  -->{{Infobox|child=yes
  | labelstyle=font-weight:normal

  | rowclass1 = mergedrow
  | label1 = &nbsp;-&nbsp;Total
  | data1 = {{{2010Pop|{{{2000Pop}}}}}}

  | rowclass2 = {{#if:{{{MedianHouseholdIncome|}}}|mergedrow|mergedbottomrow}}
  | label2 = &nbsp;-&nbsp;[Density](https://second-renaissance.fandom.com/wiki/List_of_U.S._states_by_population_density)
  | data2 = {{{2010DensityUS|{{{2000DensityUS}}}}}}/sq&nbsp;mi&nbsp; ({{{2010Density|{{{2000Density}}}}}}/km<sup>2</sup>)<br />[Ranked {{{DensityRank}}}](https://second-renaissance.fandom.com/wiki/List_of_U.S._states_by_population_density)

  | rowclass3 = mergedbottomrow
  | label3 = &nbsp;-&nbsp;[Median household income](https://second-renaissance.fandom.com/wiki/Household_income_in_the_United_States)
  | data3 = {{#if:{{{MedianHouseholdIncome|}}}|{{{MedianHouseholdIncome}}} ({{{IncomeRank}}}) }}
  }}

| rowclass20 = mergedtoprow
| label20 = [Elevation](https://second-renaissance.fandom.com/wiki/List_of_U.S._states_by_elevation)
| data20 = <!--
 -->{{Infobox|child=yes
  | labelstyle=font-weight:normal

  | rowclass1 = mergedrow
  | label1 = &nbsp;-&nbsp;Highest point
  | data1 = {{{HighestPoint}}}<br/>{{{HighestElevUS}}}&nbsp;ft&#32;({{{HighestElev}}} m)

  | rowclass2 = mergedrow
  | label2 = &nbsp;-&nbsp;Mean
  | data2 = {{{MeanElevUS}}}&nbsp;ft&nbsp; ({{{MeanElev}}} m)

  | rowclass3 = mergedbottomrow
  | label3 = &nbsp;-&nbsp;Lowest point
  | data3 = {{#if: {{{LowestPoint|}}} |{{{LowestPoint}}}<br/>}} {{#ifeq:{{{LowestElev}}}|0|sea level|{{{LowestElevUS}}}&nbsp;ft&#32;({{{LowestElev}}} m)}}
}}
| rowclass25 = mergedtoprow
| label25 = Before statehood
| data25 = {{#ifexist:{{{Former|}}}|[}}}](https://second-renaissance.fandom.com/wiki/{{{Former)|{{{Former|}}}}}

| rowclass26 = {{#if:{{{Former|}}}|mergedbottomrow}}
| label26 = [Admission to Union](https://second-renaissance.fandom.com/wiki/Admission_to_the_Union)
| data26 = {{{AdmittanceDate}}} ({{{AdmittanceOrder}}})

| rowclass27 = mergedtoprow
| label27 = [Governor](https://second-renaissance.fandom.com/wiki/Governor_of_{{{Name}}})
| data27 = {{{Governor}}}

| rowclass28 = mergedrow
| label28 = [{{{Lieutenant Governor_alt|Lieutenant Governor}}}](https://second-renaissance.fandom.com/wiki/Lieutenant_Governor_of_{{{Name}}})
| data28 = {{{Lieutenant Governor}}}

| rowclass29 = mergedtoprow 
| label29 = [Legislature](https://second-renaissance.fandom.com/wiki/Legislature)
| data29 = {{{Legislature}}} <!--
 -->{{infobox|child=yes
  | labelstyle=font-weight:normal

  | rowclass1 = mergedrow
  | label1 = &nbsp;-&nbsp;[Upper house](1019-upper-house.md)
  | data1 = {{{Upperhouse}}}

  | rowclass2 = mergedrow
  | label2 = &nbsp;-&nbsp;[Lower house](1033-lower-house.md)
  | data2 = {{{Lowerhouse}}}
  }}

| rowclass35 = mergedtoprow 
| label35 = [U.S. Senators](https://second-renaissance.fandom.com/wiki/List_of_United_States_Senators_from_{{{Name}}})
| data35 = {{{Senators}}}

| rowclass36 = mergedbottomrow
| label36 = [U.S. House delegation](https://second-renaissance.fandom.com/wiki/United_States_House_of_Representatives) 
| data36 = {{#if:{{{Representative|}}}
  | {{{Representative}}} ([list](https://second-renaissance.fandom.com/wiki/United_States_congressional_delegations_from_{{{Name}}})) 
  | [List](https://second-renaissance.fandom.com/wiki/United_States_congressional_delegations_from_{{{Name}}})
  }}

| rowclass37 = mergedtoprow
| label37 = [Time zone{{#if: {{{TimeZone2|}}}|s}}](https://second-renaissance.fandom.com/wiki/List_of_time_offsets_by_U.S._state)
| data37 = {{#if: {{{TimeZone2|}}} 
  | {{{TZDesc|&nbsp;}}} <!--
  -->{{infobox|child = yes
    | labelstyle=font-weight:normal

    | rowclass1 = mergedrow
    | label1 = &nbsp;- {{{TZ1Where}}}
    | data1 = {{{TimeZone}}}

    | rowclass2 = mergedrow
    | label2 = &nbsp;- {{{TZ2Where}}}
    | data2 = {{{TimeZone2}}}
    }}
  | {{{TimeZone}}} 
  }}

| label38 = [ISO 3166](https://second-renaissance.fandom.com/wiki/ISO_3166)
| data38 = {{#if:{{{ISOCode| }}}| [{{{ISOCode}}}](https://second-renaissance.fandom.com/wiki/ISO_3166-2:US) }}

| label39 = Abbreviations
| data39 = [{{{PostalAbbreviation| }}}](https://second-renaissance.fandom.com/wiki/List_of_U.S._state_abbreviations), [{{{TradAbbreviation| }}}](https://second-renaissance.fandom.com/wiki/List_of_U.S._state_abbreviations)

| rowclass40 = mergedtoprow
| label40 = Website
| data40 = {{#if:{{{Website|}}}| {{URL|1={{{Website}}}}} }}

| rowclass41 = mergedtoprow
| data41 = {{#if: {{{Footnotes|}}}| '''Footnotes:''' {{{Footnotes}}} }}

}}</includeonly><noinclude>{{Documentation}}</noinclude>
```

## Provenance

Raw source: `bronze/pages/488/695.wikitext` · revision `695` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AInfobox_U.S._planetary_commonwealth)
