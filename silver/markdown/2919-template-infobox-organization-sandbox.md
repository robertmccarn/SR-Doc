---
page_id: 2919
revision_id: 8507
source_url: https://second-renaissance.fandom.com/wiki/Template%3AInfobox_Organization/sandbox
raw_sha256: e5c910f1f0e2e04345f5ce26711c2401d9e58e3446beee0b40a0f478fe07147b
---

# Template:Infobox Organization/sandbox

## Preserved source

```wikitext
{{Infobox
| bodyclass = vcard

| titleclass = fn org
| titlestyle = background:{{If empty|{{{bgcolor|}}} |none}}; color:{{Use first nonempty |{{{fgcolor|}}} |#000}}; padding-bottom:0.15em;<!--(to ensure title doesn't touch infobox's border)-->
| title = {{{name|{{{organization_name|{{{Non-profit_name|<includeonly>{{PAGENAME}}</includeonly>}}}}}}}}}

| subheader = {{{native name|{{{native_name|}}}}}}

| image1 = {{#invoke:InfoboxImage|InfoboxImage |image={{{image|{{{logo|{{{organization_logo|{{{Non-profit_logo|}}}}}}}}}}}} |size={{{image_size|{{{imagesize|{{{size|}}}}}}}}} |sizedefault=frameless |alt={{{image_alt|{{{alt|}}}}}} }}
| caption1 = {{{caption|}}}

| image2 = {{#invoke:InfoboxImage|InfoboxImage |image={{{map|}}} |size={{{map_size|{{{msize|}}}}}} |sizedefault=250px |alt={{{map_alt|{{{malt|}}}}}} }}
| caption2 = {{{map_caption|{{{mcaption|}}}}}}

| image3 = {{#invoke:InfoboxImage|InfoboxImage |image={{{map2|}}} |size={{{map2_size|}}} |sizedefault=250px |alt={{{map2_alt|}}} }}
| caption3 = {{{map2_caption|}}}

| labelstyle = padding-right:0.6em;<!--(to ensure some gap between any (long/unwrapped) labels and subsequent data on same line)-->

| label1  = Abbreviation
| class1  = nickname
|  data1  = {{{abbreviation|}}}

| label2  = Motto
| class2  = note
|  data2  = {{{motto|{{{organization_motto|{{{pledge|}}}}}}}}}

| label3  = Predecessor
|  data3  = {{{predecessor|}}}

| label4  = Merged&nbsp;into
|  data4  = {{{merged|}}}

| label5  = Successor
|  data5  = {{{successor|}}}

| label6  = {{#if:{{{formation|}}} |Formation |{{#if:{{{founded_date|{{{founded|}}}}}}|Founded|Established}} }}
| class6  = note
|  data6  = {{If empty|{{{formation|}}} |{{{established|}}} |{{{founded_date|{{{founded|}}}}}} }}

| label7  = Founder{{#if:{{{founders|}}}|s}}
|  data7  = {{#if:{{{founders|}}} |{{{founders}}} |{{{founder|}}} }}

| label8  = {{#if:{{{extinction|}}} |Extinction |[Dissolved](https://second-renaissance.fandom.com/wiki/Dissolution_(law))}}
|  data8  = {{#if:{{{extinction|}}} |{{{extinction}}} |{{{dissolved|}}} }}

| label9  = Merger&nbsp;of
|  data9  = {{{merger|}}}

| label10 = Type
|  data10 = {{{type|{{{organization_type|{{{Non-profit_type|}}}}}}}}}

| label11 = {{longitem |{{#if:{{{vat_id|}}} |[VAT ID no.](https://second-renaissance.fandom.com/wiki/VAT_identification_number) |[Tax ID no.](https://second-renaissance.fandom.com/wiki/Taxpayer_Identification_Number)}} }}
|  data11 = {{#if:{{{vat_id|}}} |{{{vat_id}}} |{{{tax_id|}}} }}

| label12 = Registration&nbsp;no.
|  data12 = {{{registration_id|}}}

| label13 = Legal status
|  data13 = {{{status|}}}

| label14 = {{#if:{{{focus|}}} |Focus |Purpose}}
|  data14 = {{#if:{{{focus|}}} |{{{focus}}} |{{{purpose|}}} }}

| label15 = {{longitem|Professional title}}
|  data15 = {{{professional_title|}}}

| label16 = Headquarters
|  data16 = {{{headquarters|}}}

| label17 = Location
| class17 = label
|  data17 = {{Unbulleted list
             | 1 = {{Comma separated entries
                    | 1 = {{#if:{{{location_city|}}}    |<span class="locality">{{{location_city}}}</span>}}
                    | 2 = {{#if:{{{location_country|}}} |<span class="country-name">{{{location_country}}}</span>}}
                   }}
             | 2 = {{{location|}}}
             | 3 = {{Comma separated entries
                    | 1 = {{#if:{{{location_city2|}}}    |<span class="locality">{{{location_city2}}}</span>}}
                    | 2 = {{#if:{{{location_country2|}}} |<span class="country-name">{{{location_country2}}}</span>}}
                   }}
             | 4 = {{{location2|}}}
            }}

| label18 = Locations
| class18 = label
|  data18 = {{Unbulleted list
             | 1 = {{Comma separated entries
                    | 1 = {{#if:{{{addnl_location_city|}}}    |<span class="locality">{{{addnl_location_city}}}</span>}}
                    | 2 = {{#if:{{{addnl_location_country|}}} |<span class="country-name">{{{addnl_location_country}}}</span>}}
                   }}
             | 2 = {{{addnl_location|{{{additional_location|}}}}}}
             | 3 = {{Comma separated entries
                    | 1 = {{#if:{{{addnl_location_city2|}}}    |<span class="locality">{{{addnl_location_city2}}}</span>}}
                    | 2 = {{#if:{{{addnl_location_country2|}}} |<span class="country-name">{{{addnl_location_country2}}}</span>}}
                   }}
             | 4 = {{{addnl_location2|{{{additional_location2|}}}}}}
            }}

| label19 = Coordinates
|  data19 = {{{coordinates|{{{coords|}}}}}}

| label20 = Map
| data20 = {{{location_map|}}}

| label21 = {{longitem |{{#if:{{{area_served|}}} |Area served |Region {{#if:{{{region_served|}}}|served}} }} }}
|  data21 = {{If empty|{{{area_served|}}} |{{{region_served|}}} |{{{region|}}} }}

| label22 = Product{{#if:{{{products|}}}|s}}
|  data22 = {{#if:{{{products|}}} |{{{products}}} |{{{product|}}} }}

| label23 = Services
| class23 = note
|  data23 = {{{services|}}}

| label24 = Method{{#if:{{{methods|}}}|s}}
|  data24 = {{#if:{{{methods|}}} |{{{methods}}} |{{{method|}}} }}

| label25 = Field{{#if:{{{fields|}}}|s}}
|  data25 = {{#if:{{{fields|}}} |{{{fields}}} |{{{field|}}} }}

| label26 = {{longitem |Members{{#if:{{{num_members|{{{members|}}}}}}||hip}} {{#if:{{{num_members_year|}}} |{{nobold|({{{num_members_year}}})}} }} }}
|  data26 = {{#if:{{{num_members|{{{members|}}}}}} |{{{num_members|{{{members}}}}}} |{{{membership|}}} }}

| label27 = {{longitem |Official language{{#if:{{{languages|}}}|s}} }}
|  data27 = {{#if:{{{languages|}}} |{{{languages}}} |{{{language|}}} }}

| label28 = Owner{{#if:{{{owners|}}}|s}}
|  data28 = {{#if:{{{owners|}}} |{{{owners}}} |{{{owner|}}} }}

| label29 = {{longitem|Secretary General}}
|  data29 = {{#if:{{{general|}}} |{{{general}}} |{{{sec_gen|}}} }}

| label30 = {{#if:{{{leader_title|}}} |{{longitem|{{{leader_title}}}}} |Leader}}
|  data30 = {{{leader_name|}}}

| label31 = {{longitem|{{{leader_title2}}}}}
|  data31 = {{#if:{{{leader_title2|}}} |{{{leader_name2|}}} }}

| label32 = {{longitem|{{{leader_title3}}}}}
|  data32 = {{#if:{{{leader_title3|}}} |{{{leader_name3|}}} }}

| label33 = {{longitem|{{{leader_title4}}}}}
|  data33 = {{#if:{{{leader_title4|}}} |{{{leader_name4|}}} }}

| label34 = {{longitem|[{{allow wrap|Board&nbsp;of directors}}](https://second-renaissance.fandom.com/wiki/Board_of_directors)}}
|  data34 = {{{board_of_directors|}}}

| label35 = {{longitem|Key people}}
|  data35 = {{{key_people|}}}

| label36 = {{#if:{{{main_organ|}}} |{{longitem|Main organ}} |Publication}}
|  data36 = {{#if:{{{main_organ|}}} |{{{main_organ}}} |{{{publication|}}} }}

| label37 = {{longitem|Parent organi{{#if:{{{parent_organisation|}}}|s|z}}ation}}
|  data37 = {{#if:{{{parent_organisation|}}} |{{{parent_organisation}}} |{{{parent_organization|}}} }}

| label38 = [Subsidiaries](https://second-renaissance.fandom.com/wiki/Subsidiary)
|  data38 = {{#if:{{{subsidiaries|}}} |{{{subsidiaries}}} |{{{subsid|}}} }}

| label39 = Secessions
|  data39 = {{{secessions|}}}

| label40 = Affiliations
|  data40 = {{{affiliations|}}}

| label41 = {{longitem |Budget {{#if:{{{budget_year|}}} |{{nobold|({{{budget_year}}})}} }} }}
|  data41 = {{{budget|}}}

| label42 = {{longitem |Revenue {{#if:{{{revenue_year|{{{income_year|}}}}}} |{{nobold|({{{revenue_year|{{{income_year|}}}}}})}} }} }}
|  data42 = {{{revenue|{{{income|}}}}}}

| label43 = Disbursements
|  data43 = {{{disbursed|{{{disbursements|{{{disbursement|}}}}}}}}}

| label44 = Expenses
|  data44 = {{{expenses|{{{spent|{{{expense|}}}}}}}}}

| label45 = [Endowment](https://second-renaissance.fandom.com/wiki/Financial_endowment)
|  data45 = {{{endowment|}}}

| label46 = {{longitem |{{#if:{{{num_staff|}}}{{{staff|}}} |Staff |Employees}} {{#if:{{{num_staff_year|{{{num_employees_year|}}}}}} |{{nobold|({{{num_staff_year|{{{num_employees_year|}}}}}})}} }} }}
|  data46 = {{If empty|{{{num_staff|}}} |{{{staff|}}} |{{{num_employees|}}} |{{{employees|}}} }}

| label47 = {{longitem |Volunteers {{#if:{{{num_volunteers_year|}}} |{{nobold|({{{num_volunteers_year}}})}} }} }}
|  data47 = {{#if:{{{num_volunteers|}}} |{{{num_volunteers}}} |{{{volunteers|}}} }}

| label48 = [Slogan](https://second-renaissance.fandom.com/wiki/Slogan)
|  data48 = {{{slogan|{{{Non-profit_slogan|{{{non-profit_slogan|}}}}}}}}}

| label49 = [Mission](https://second-renaissance.fandom.com/wiki/Mission_statement)
|  data49 = {{{mission|}}}

| label50 = Website
|  data50 = {{{website|{{{homepage|}}}}}}

| label51 = Remarks
|  data51 = {{{remarks|}}}

| label52 = {{longitem|Formerly called}}
| class52 = nickname
|  data52 = {{If empty|{{{former name|}}} |{{{former_name|}}} |{{{former|}}} |{{{formerly|}}} }}

| belowstyle = border-top:#aaa 1px solid;
| below = {{{footnotes|}}}

}}<!-- Tracking categories:
-->{{#if:{{{named_after|}}}  |[n{{PAGENAME}}](https://second-renaissance.fandom.com/wiki/Category:Pages_using_infobox_organization_with_unsupported_parameters)}}<!--
-->{{#if:{{{founding_location|}}} |[f{{PAGENAME}}](https://second-renaissance.fandom.com/wiki/Category:Pages_using_infobox_organization_with_unsupported_parameters)}}<!--
-->{{#if:{{{ethnicity|}}}    |[e{{PAGENAME}}](https://second-renaissance.fandom.com/wiki/Category:Pages_using_infobox_organization_with_unsupported_parameters)}}<!--
-->{{#if:{{{rivals|}}}       |[r{{PAGENAME}}](https://second-renaissance.fandom.com/wiki/Category:Pages_using_infobox_organization_with_unsupported_parameters)}}<!--

--><noinclude>
{{Documentation}}
</noinclude>
```

## Provenance

Raw source: `bronze/pages/2919/8507.wikitext` · revision `8507` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AInfobox_Organization/sandbox)
