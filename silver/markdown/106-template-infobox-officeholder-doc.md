---
page_id: 106
revision_id: 121
source_url: https://second-renaissance.fandom.com/wiki/Template%3AInfobox_officeholder/doc
raw_sha256: c178b02516b47ae50720c9bcb554fee09f2d8aa2e85aabf24ae8964d265cc512
---

# Template:Infobox officeholder/doc

## Preserved source

```wikitext
{{Documentation subpage}}
{{Person infobox header}}
<includeonly>{{high-use|52,000+}}</includeonly>

{{tl|Infobox officeholder}} incorporates the following templates (i.e. all the templates listed <span class="plainlinks">[{{fullurl:Special:WhatLinksHere/Template:Infobox officeholder|namespace=10&limit=1000&hidetrans=1&hidelinks=1}} here]). Please use the most appropriate name when placing this template on a page.

{{refbegin|colwidth=20em}}
* {{Tl|Infobox AM}}
* {{Tl|Infobox ambassador}}
* {{Tl|Infobox Canadian MP}}
* {{Tl|Infobox Canadian senator}}
* {{Tl|Infobox candidate}}
* {{Tl|Infobox chancellor}}
* {{Tl|Infobox congressional candidate}}
* {{Tl|Infobox congressman}}
* {{Tl|Infobox defense minister}}
* {{Tl|Infobox deputy first minister}}
* {{Tl|Infobox deputy prime minister}}
* {{Tl|Infobox doge}}
* {{Tl|Infobox Eritrea cabinet official}}
* {{Tl|Infobox first lady}}
* {{Tl|Infobox first minister}}
* {{Tl|Infobox governor}}
* {{Tl|Infobox governor-elect}}
* {{Tl|Infobox governor general}}
* {{Tl|Infobox governor-general}}
* {{Tl|Infobox Indian politician}}
* {{Tl|Infobox judge}}
* {{Tl|Infobox lt governor}}
* {{Tl|Infobox mayor}}
* {{Tl|Infobox MEP}}
* {{Tl|Infobox minister}}
* {{Tl|Infobox MLA}}
* {{Tl|Infobox MP}}
* {{Tl|Infobox MSP}}
* {{Tl|Infobox PM}}
* {{Tl|Infobox politician}}
* {{Tl|Infobox politician (general)}}
* {{Tl|Infobox premier}}
* {{Tl|Infobox president}}
* {{Tl|Infobox president-elect}}
* {{Tl|Infobox prime minister}}
* {{Tl|Infobox prime minister-elect}}
* {{Tl|Infobox representative-elect}}
* {{Tl|Infobox SCC chief justice}}
* {{Tl|Infobox SCC puisne justice}}
* {{Tl|Infobox secretary-general}}
* {{Tl|Infobox senator}}
* {{Tl|Infobox senator-elect}}
* {{Tl|Infobox speaker}}
* {{Tl|Infobox state representative}}
* {{Tl|Infobox state SC associate justice}}
* {{Tl|Infobox state SC justice}}
* {{Tl|Infobox state senator}}
* {{Tl|Infobox US ambassador}}
* {{Tl|Infobox US associate justice}}
* {{Tl|Infobox US cabinet official}}
* {{Tl|Infobox US chief justice}}
* {{Tl|Infobox US territorial governor}}
* {{Tl|Infobox vice president}}
{{refend}}

# Usage
Paste the code for the relevant office and then add the [[#Personal data|personal data]] to the bottom. There are no required fields and some fields will not appear when others are in use. For instructions on how to implement multiple terms, see [this page](https://second-renaissance.fandom.com/wiki/Template:Infobox_officeholder/example). For advice on alt text, see ''[Wikipedia:Alternative text for images](https://second-renaissance.fandom.com/wiki/Wikipedia:Alternative_text_for_images)''.

The parameter {{para|order}} is used in conjunction with {{para|office}} to state that the officeholder is the ''n''th holder of the office, for example "2nd President of Mauritius". If {{para|order}} is not specified, the value of {{para|office}} can be [wikilinked](https://second-renaissance.fandom.com/wiki/Help:Link) in the usual way, for example, "<tt><nowiki>[Minister for Defence](https://second-renaissance.fandom.com/wiki/Ministry_of_Defence_(Singapore))</nowiki></tt>". However, if {{para|order}} is specified together with {{para|office}}, the value of {{para|office}} is automatically linked to a Wikipedia article of the same name, whether such an article exists or not. Wikilinking cannot be used to redirect the link elsewhere, but a [piped link](https://second-renaissance.fandom.com/wiki/Wikipedia:Piped_link) can be created like this: "<tt><nowiki>Ministry of Defence (Singapore){{!}}Minister for Defence</nowiki></tt>" (note that the double square brackets have been omitted).

When both a start and an end term are given, you can instead specify the complete term using using the parameters {{para|term}}, {{para|terms2}}, etc. This can be helpful with complicated terms that cannot be given as simple starting or ending dates, or if you prefer something other than the default term separator (an en dash, with spaces around it if the start or end is not a simple integer date).

# General office
{{For|examples of this code in use|Template:Infobox officeholder/example#General office}}
<pre style="overflow:auto;">
{{Infobox officeholder
|honorific-prefix   = 
|name               = 
|native_name        = 
|native_name_lang   = 
|honorific-suffix   = 
|image              = 
|imagesize          = 
|smallimage         = <!--If this is specified, "image" should not be.-->
|alt                = 
|caption            = 
|order              = 
|office             = 
|term_start         = 
|term_end           = 
|alongside          = <!--For two or more people serving in the same position from the same district.  (e.g. United States Senators.)-->
|vicepresident      = 
|viceprimeminister  = 
|deputy             = 
|lieutenant         = 
|monarch            = 
|president          = 
|primeminister      = 
|taoiseach          = 
|chancellor         = 
|governor           = 
|governor-general   = 
|governor_general   = 
|succeeding         = <!--For President-elect or equivalent-->
|predecessor        = 
|successor          = 
|constituency       = 
|majority           = 
|order2             =  <!--Can be repeated up to eight times by changing the number-->
|office2            =  <!--Can be repeated up to eight times by changing the number-->
|term_start2        =  <!--Can be repeated up to eight times by changing the number-->
|term_end2          =  <!--Can be repeated up to eight times by changing the number-->
|alongside2         =  <!--Can be repeated up to eight times by changing the number-->
|vicepresident2     =  <!--Can be repeated up to eight times by changing the number-->
|viceprimeminister2 =  <!--Can be repeated up to eight times by changing the number-->
|deputy2            =  <!--Can be repeated up to eight times by changing the number-->
|lieutenant2        =  <!--Can be repeated up to eight times by changing the number-->
|monarch2           =  <!--Can be repeated up to eight times by changing the number-->
|president2         =  <!--Can be repeated up to eight times by changing the number-->
|primeminister2     =  <!--Can be repeated up to eight times by changing the number-->
|governor2          =  <!--Can be repeated up to eight times by changing the number-->
|succeeding2        =  <!--Can be repeated up to eight times by changing the number-->
|predecessor2       =  <!--Can be repeated up to eight times by changing the number-->
|successor2         =  <!--Can be repeated up to eight times by changing the number-->
|constituency2      =  <!--Can be repeated up to eight times by changing the number-->
|majority2          =  <!--Can be repeated up to eight times by changing the number-->
</pre>
''add [[#Personal data|personal data]]''

# Ambassador
{{For|examples of this code in use|Template:Infobox officeholder/example#Ambassador}}
<pre style="overflow:auto;">
{{Infobox ambassador
|honorific-prefix = 
|name        = 
|honorific-suffix = 
|image       = 
|alt         = 
|order       =  <!--Can be repeated up to eight times by adding a number-->
|ambassador_from =  <!--Can be repeated up to eight times by adding a number-->
|country     =  <!--Can be repeated up to eight times by adding a number-->
|term_start  =  <!--Can be repeated up to eight times by adding a number-->
|term_end    =  <!--Can be repeated up to eight times by adding a number-->
|predecessor =  <!--Can be repeated up to eight times by adding a number-->
|successor   =  <!--Can be repeated up to eight times by adding a number-->
|president   =  <!--Can be repeated up to eight times by adding a number-->
</pre>
''add [[#Personal data|personal data]]''

# Assembly Member
{{For|examples of this code in use|Template:Infobox officeholder/example#Assembly Member}}
<pre style="overflow:auto;">
{{Infobox AM
|honorific-prefix = 
|name        = 
|honorific-suffix = 
|image       = 
|alt         = 
|caption     = 
|constituency_AM =  <!--Can be repeated up to eight times by adding a number-->
|assembly    =  <!--Can be repeated up to eight times by adding a number-->
|majority    =  <!--Can be repeated up to eight times by adding a number-->
|term_start  =  <!--Can be repeated up to eight times by adding a number-->
|term_end    =  <!--Can be repeated up to eight times by adding a number-->
|predecessor =  <!--Can be repeated up to eight times by adding a number-->
|successor   =  <!--Can be repeated up to eight times by adding a number-->
</pre>
''add [[#Personal data|personal data]]''

# Governor
{{For|examples of this code in use|Template:Infobox officeholder/example#Governor}}
<pre style="overflow:auto;">
{{Infobox governor
|honorific-prefix = 
|name        = 
|honorific-suffix = 
|image       = 
|alt         = 
|order       =  <!--Can be repeated up to eight times by adding a number-->
|office      =  <!--Can be repeated up to eight times by adding a number-->
|term_start  =  <!--Can be repeated up to eight times by adding a number-->
|term_end    =  <!--Can be repeated up to eight times by adding a number-->
|lieutenant  =  <!--Can be repeated up to eight times by adding a number-->
|predecessor =  <!--Can be repeated up to eight times by adding a number-->
|successor   =  <!--Can be repeated up to eight times by adding a number-->
</pre>
''add [[#Personal data|personal data]]''

If Governor was appointed by a President, add:
<pre style="overflow:auto;">
|president   =  <!--name of president-->
</pre>

If Governor appointed by other, add:
<pre style="overflow:auto;">
|appointed   =  <!--name of appointer-->
</pre>

# Judge
{{For|examples of this code in use|Template:Infobox officeholder/example#Judge}}
<pre style="overflow:auto;">
{{Infobox judge
|honorific-prefix = 
|name        = 
|honorific-suffix = 
|image       = 
|alt         = 
|caption     = 
|office      =  <!--Can be repeated up to eight times by changing the number-->
|term_start  =  <!--Can be repeated up to eight times by changing the number-->
|term_end    =  <!--Can be repeated up to eight times by changing the number-->
|nominator   =  <!--Can be repeated up to eight times by changing the number-->
|appointer   =  <!--Can be repeated up to eight times by changing the number-->
|predecessor =  <!--Can be repeated up to eight times by changing the number-->
|successor   =  <!--Can be repeated up to eight times by changing the number-->
</pre>
''add [[#Personal data|personal data]]''

# Nominee/Candidate
{{For|examples of this code in use|Template:Infobox officeholder/example#Nominee/Candidate}}
:'''''Do not add this section to pages of people who have held a previous office.'''''
<pre style="overflow:auto;">
{{Infobox candidate
|honorific-prefix = 
|name      = 
|honorific-suffix = 
|image     = 
|alt       = 
|caption   = 
|nominee   = 
|party_election = 
|election_date = 
|runningmate = 
|opponent  = 
|incumbent = 
</pre>

If a candidate, then instead of <code>nominee</code> use:
<pre style="overflow:auto;">
|candidate =
</pre>

''add [[#Personal data|personal data]]''

# Member of Parliament
{{For|examples of this code in use|Template:Infobox officeholder/example#Member of Parliament}}
<pre style="overflow:auto;">
{{Infobox MP
|honorific-prefix = 
|name        = 
|honorific-suffix = 
|image       = 
|alt         = 
|caption     = 
|constituency_MP =  <!--Can be repeated up to eight times by adding a number-->
|parliament  =  <!--Can be repeated up to eight times by adding a number-->
|majority    =  <!--Can be repeated up to eight times by adding a number-->
|term_start  =  <!--Can be repeated up to eight times by adding a number-->
|term_end    =  <!--Can be repeated up to eight times by adding a number-->
|predecessor =  <!--Can be repeated up to eight times by adding a number-->
|successor   =  <!--Can be repeated up to eight times by adding a number-->
</pre>
''add [[#Personal data|personal data]]''

# U.S. Representatives
## U.S. Congressman
{{For|examples of this code in use|Template:Infobox officeholder/example#US Congressman}}
<pre style="overflow:auto;">
{{Infobox Congressman
|honorific-prefix = 
|name        = 
|honorific-suffix = 
|image       = 
|alt         = 
|state       =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|district    =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|term_start  =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|term_end    =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|predecessor =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|successor   =  <!--Can be repeated up to seven times by adding a number, start at 3-->
</pre>
''add [[#Personal data|personal data]]''

If Congressman served as Speaker of the House add:
<pre style="overflow:auto;">
|speaker      =  <!--number of office holder-->
|term_start2  = 
|term_end2    = 
|predecessor2 = 
|successor2   = 
</pre>

If Congressman has been elected but not sworn in:
<pre style="overflow:auto;">
|succeeding   =  <!--the name of the incumbent congressman-->
</pre>

## State Representative
{{For|examples of this code in use|Template:Infobox officeholder/example#State Representative}}
<pre style="overflow:auto;">
{{Infobox state representative
|honorific-prefix = 
|name         = 
|honorific-suffix = 
|image        = 
|alt          = 
|state_house  =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|district     =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|term_start   =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|term_end     =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|predecessor  =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|successor    =  <!--Can be repeated up to seven times by adding a number, start at 3-->
</pre>
''add [[#Personal data|personal data]]''

For Representative from states that have an Assembly, instead of state_house use:
<pre style="overflow:auto;">
|state_assembly =  <!--Can be repeated up to seven times by adding a number, start at 3-->
</pre>

For Representative from states that have a House of Delegates, instead of state_house use:
<pre style="overflow:auto;">
|state_delegate =  <!--Can be repeated up to seven times by adding a number, start at 3-->
</pre>

For Representative from states that have a Legislature, instead of state_house use:
<pre style="overflow:auto;">
|state_legislature =  <!--Can be repeated up to seven times by adding a number, start at 3-->
</pre>

If Representative served as Speaker of the State House add:
<pre style="overflow:auto;">
|speaker      =  <!--number of office holder-->
|state_house  = 
|term_start2  = 
|term_end2    = 
|predecessor2 = 
|successor2   = 
</pre>

# U.S. Senators
## U.S. Senator
{{For|examples of this code in use|Template:Infobox officeholder/example#US Senator}}
<pre style="overflow:auto;">
{{Infobox senator
|honorific-prefix = 
|name        = 
|honorific-suffix = 
|image       = 
|imagesize   = 
|alt         = 
|jr/sr       =  <!--Can be repeated up to eight times by appending 2, 3, etc-->  This code has been disabled per Template talk:Infobox officeholder.
|state       =  <!--Can be repeated up to eight times by appending 2, 3, etc-->
|term_start  =  <!--Can be repeated up to eight times by appending 2, 3, etc-->
|term_end    =  <!--Can be repeated up to eight times by appending 2, 3, etc-->
|predecessor =  <!--Can be repeated up to eight times by appending 2, 3, etc-->
|successor   =  <!--Can be repeated up to eight times by appending 2, 3, etc-->
</pre>
''add [[#Personal data|personal data]]''

<pre style="overflow:auto;">
|alongside   =  <!--the name of fellow senator-->
</pre>

If Senator has just been elected and is a Senator-Elect:
<pre style="overflow:auto;">
|succeeding  =  <!--the name of the incumbent senator-->
</pre>

If Senator served as Senate Majority Leader add:
<pre style="overflow:auto;">
|majorityleader3 =  <!--number of office holder-->
|term_start3  =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|term_end3    =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|predecessor3 =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|successor3   =  <!--Can be repeated up to seven times by adding a number, start at 3-->
</pre>

If Senator served as Congressman add:
<pre style="overflow:auto;">
|state3       =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|district3    =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|term_start3  =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|term_end3    =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|predecessor3 =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|successor3   =  <!--Can be repeated up to seven times by adding a number, start at 3-->
</pre>

## State Senator
{{For|examples of this code in use|Template:Infobox officeholder/example#State Senator}}
<pre style="overflow:auto;">
{{Infobox State Senator
|honorific-prefix = 
|name         = 
|honorific-suffix = 
|image        = 
|alt          = 
|state_senate =  <!--Can be repeated up to eight times by appending 2, 3, etc-->
|district     =  <!--Can be repeated up to eight times by appending 2, 3, etc-->
|term_start   =  <!--Can be repeated up to eight times by appending 2, 3, etc-->
|term_end     =  <!--Can be repeated up to eight times by appending 2, 3, etc-->
|predecessor  =  <!--Can be repeated up to eight times by appending 2, 3, etc-->
|successor    =  <!--Can be repeated up to eight times by appending 2, 3, etc-->
</pre>
''add [[#Personal data|personal data]]''

If State Senator served as Majority Leader of the State Senate add:
<pre style="overflow:auto;">
|majority_leader3 =  <!--number of office holder-->
|term_start3  =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|term_end3    =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|predecessor3 =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|successor3   =  <!--Can be repeated up to seven times by adding a number, start at 3-->
</pre>


If State Senator served as Minority Leader of the State Senate add:
<pre style="overflow:auto;">
|minority_leader3 =  <!--number of office holder-->
|term_start3  =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|term_end3    =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|predecessor3 =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|successor3   =  <!--Can be repeated up to seven times by adding a number, start at 3-->
</pre>

If State Senator served as Majority Floor Leader of the State Senate add:
<pre style="overflow:auto;">
|majority_floor_leader3 =  <!--number of office holder-->
|term_start3  =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|term_end3    =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|predecessor3 =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|successor3   =  <!--Can be repeated up to seven times by adding a number, start at 3-->
</pre>

If State Senator served as Minority Floor Leader of the State Senate add:
<pre style="overflow:auto;">
|minority_floor_leader3 =  <!--number of office holder-->
|term_start3  =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|term_end3    =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|predecessor3 =  <!--Can be repeated up to seven times by adding a number, start at 3-->
|successor3   =  <!--Can be repeated up to seven times by adding a number, start at 3-->
</pre>

# Personal data
Place this underneath the template
<pre style="overflow:auto;">
|birth_date         = 
|birth_place        = 
|death_date         = 
|death_place        = 
|restingplace       = 
|restingplacecoordinates = 
|birthname          = 
|citizenship        = 
|nationality        = 
|party              = 
|otherparty         =  <!--For additional political affiliations-->
|spouse             = 
|partner            =  <!--For those with a domestic partner and not married-->
|relations          = 
|children           = 
|residence          = 
|alma_mater         = 
|occupation         = 
|profession         = 
|cabinet            = 
|committees         = 
|portfolio          = 
|religion           = 
|signature          = 
|signature_alt      = 
|website            = 
|footnotes          = 
|blank1             = 
|data1              = 
|blank2             = 
|data2              = 
|blank3             = 
|data3              = 
|blank4             = 
|data4              = 
|blank5             = 
|data5              = 
<!--Military service-->
|nickname           = 
|allegiance         = 
|branch             = 
|serviceyears       = 
|rank               = 
|unit               = 
|commands           = 
|battles            = 
|awards             = 
|military_blank1    = 
|military_data1     = 
|military_blank2    = 
|military_data2     = 
|military_blank3    = 
|military_data3     = 
|military_blank4    = 
|military_data4     = 
|military_blank5    = 
|military_data5     = 
}}
</pre><includeonly>

# Microformat
{{UF-hcard-person}}

<!--Categories-->
{{Basepage subpage|
[Officeholder](https://second-renaissance.fandom.com/wiki/Category:People_infobox_templates)
[Officeholder](https://second-renaissance.fandom.com/wiki/Category:Politics_and_government_infobox_templates)
}}
<!--Interwikis-->
[ar:قالب:معلومات صاحب منصب](https://second-renaissance.fandom.com/wiki/ar:قالب:معلومات_صاحب_منصب)
[ast:Plantilla:Info presidentes](https://second-renaissance.fandom.com/wiki/ast:Plantilla:Info_presidentes)
[az:Şablon:Dövlət xadimi](https://second-renaissance.fandom.com/wiki/az:Şablon:Dövlət_xadimi)
[be-x-old:Шаблён:Палітык](https://second-renaissance.fandom.com/wiki/be-x-old:Шаблён:Палітык)
[bg:Шаблон:Президент инфо](https://second-renaissance.fandom.com/wiki/bg:Шаблон:Президент_инфо)
[bs:Šablon:Infokutija predsjednik](https://second-renaissance.fandom.com/wiki/bs:Šablon:Infokutija_predsjednik)
[ca:Plantilla:Fitxa d'autoritat](https://second-renaissance.fandom.com/wiki/ca:Plantilla:Fitxa_d'autoritat)
[cy:Nodyn:Gwybodlen Gwleidydd](https://second-renaissance.fandom.com/wiki/cy:Nodyn:Gwybodlen_Gwleidydd)
[da:Skabelon:Infoboks leder](https://second-renaissance.fandom.com/wiki/da:Skabelon:Infoboks_leder)
[es:Plantilla:Ficha de autoridad](https://second-renaissance.fandom.com/wiki/es:Plantilla:Ficha_de_autoridad)
[fr:Modèle:Infobox Politicien](https://second-renaissance.fandom.com/wiki/fr:Modèle:Infobox_Politicien)
[ga:Teimpléad:Bosca Sonraí Uachtaráin](https://second-renaissance.fandom.com/wiki/ga:Teimpléad:Bosca_Sonraí_Uachtaráin)
[he:תבנית:נשיא ארצות הברית](https://second-renaissance.fandom.com/wiki/he:תבנית:נשיא_ארצות_הברית)
[hu:Sablon:Vezető infobox](https://second-renaissance.fandom.com/wiki/hu:Sablon:Vezető_infobox)
[hy:Կաղապար:Տեղեկաքարտ Պետական գործիչ](https://second-renaissance.fandom.com/wiki/hy:Կաղապար:Տեղեկաքարտ_Պետական_գործիչ)
[id:Templat:Infobox Officeholder](https://second-renaissance.fandom.com/wiki/id:Templat:Infobox_Officeholder)
[it:Template:Carica pubblica](https://second-renaissance.fandom.com/wiki/it:Template:Carica_pubblica)
[ja:Template:Infobox Officeholder](https://second-renaissance.fandom.com/wiki/ja:Template:Infobox_Officeholder)
[ka:თარგი:ინფოდაფა ლიდერი](https://second-renaissance.fandom.com/wiki/ka:თარგი:ინფოდაფა_ლიდერი)
[lb:Schabloun:Infobox Minister](https://second-renaissance.fandom.com/wiki/lb:Schabloun:Infobox_Minister)
[mk:Шаблон:Инфокутија Функционер](https://second-renaissance.fandom.com/wiki/mk:Шаблон:Инфокутија_Функционер)
[ms:Templat:Infobox officeholder](https://second-renaissance.fandom.com/wiki/ms:Templat:Infobox_officeholder)
[nn:Mal:Infoboks leiar](https://second-renaissance.fandom.com/wiki/nn:Mal:Infoboks_leiar)
[no:Mal:Infoboks_politiker](https://second-renaissance.fandom.com/wiki/no:Mal:Infoboks_politiker)
[oc:Modèl:Infobox Cap d'estat o govèrn](https://second-renaissance.fandom.com/wiki/oc:Modèl:Infobox_Cap_d'estat_o_govèrn)
[os:Шаблон:Паддзахадон архайæг](https://second-renaissance.fandom.com/wiki/os:Шаблон:Паддзахадон_архайæг)
[pl:Szablon:Polityk infobox](https://second-renaissance.fandom.com/wiki/pl:Szablon:Polityk_infobox)
[ro:Format:Infocaseta Funcţie oficială](https://second-renaissance.fandom.com/wiki/ro:Format:Infocaseta_Funcţie_oficială)
[ru:Шаблон:Государственный деятель](https://second-renaissance.fandom.com/wiki/ru:Шаблон:Государственный_деятель)
[si:සැකිල්ල:තොරතුරුකොටුව තනතුරුධාරි](https://second-renaissance.fandom.com/wiki/si:සැකිල්ල:තොරතුරුකොටුව_තනතුරුධාරි)
[simple:Template:Infobox Politician](https://second-renaissance.fandom.com/wiki/simple:Template:Infobox_Politician)
[sk:Šablóna:Infobox Politik](https://second-renaissance.fandom.com/wiki/sk:Šablóna:Infobox_Politik)
[sl:Predloga:Infopolje Funkcionar](https://second-renaissance.fandom.com/wiki/sl:Predloga:Infopolje_Funkcionar)
[sr:Шаблон:Председник](https://second-renaissance.fandom.com/wiki/sr:Шаблон:Председник)
[sv:Mall:Infobox politiker](https://second-renaissance.fandom.com/wiki/sv:Mall:Infobox_politiker)
[ta:வார்ப்புரு:தகவற்சட்டம் தலைவர்கள்](https://second-renaissance.fandom.com/wiki/ta:வார்ப்புரு:தகவற்சட்டம்_தலைவர்கள்)
[tr:Şablon:Makam sahibi bilgi kutusu](https://second-renaissance.fandom.com/wiki/tr:Şablon:Makam_sahibi_bilgi_kutusu)
[uk:Шаблон:Картка:Лідер](https://second-renaissance.fandom.com/wiki/uk:Шаблон:Картка:Лідер)
[ur:سانچہ:Infobox officeholder](https://second-renaissance.fandom.com/wiki/ur:سانچہ:Infobox_officeholder)
[vi:Tiêu bản:Tổng thống](https://second-renaissance.fandom.com/wiki/vi:Tiêu_bản:Tổng_thống)
[zh:Template:Infobox Officeholder](https://second-renaissance.fandom.com/wiki/zh:Template:Infobox_Officeholder)
</includeonly>
```

## Provenance

Raw source: `bronze/pages/106/121.wikitext` · revision `121` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AInfobox_officeholder/doc)
