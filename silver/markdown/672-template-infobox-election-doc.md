---
page_id: 672
revision_id: 1073
source_url: https://second-renaissance.fandom.com/wiki/Template%3AInfobox_election/doc
raw_sha256: 8bc8f317db9f140e2660f26172b67746dd6bce5b3dc46fa42005c86f39b4a769
---

# Template:Infobox election/doc

## Preserved source

```wikitext
{{Documentation subpage}}
{{Intricate template}}
<!-- Please place categories where indicated at the bottom of this page and interwikis at Wikidata (see [Wikipedia:Wikidata](https://second-renaissance.fandom.com/wiki/Wikipedia:Wikidata)) -->

This infobox describes a presidential, legislative or parliamentary election.

# Usage
Remove fields for different types of election.

<pre style="overflow:auto;">
{{Infobox election
| election_name     = 
| country           = 
| flag_year         = 
| flag_image        = 
| type              = <!-- presidential, legislative, or parliamentary -->
| vote_type         = Popular <!-- default -->
| ongoing           = 
| party_colour      = 
| party_name        = 
| alliance_name     = 
| previous_election = 
| previous_year     = 
| previous_mps      = 
| election_date     = <!-- {{Start date|YYYY|MM|DD}} -->
| elected_mps       = 
| next_election     = <!-- link to file. If red link, then it will not be linked-->
| next_year         = 
| next_mps          = 
| votes_for_election= 
| needed_votes      = 
| seats_for_election= 
| majority_seats    = 
| opinion_polls     = 
| registered        = 
| turnout           = 
<!--        person 1        -->
| image1            = 
| colour1           = 
| nominee1          = <!-- presidential only, when appropriate, candidate1 can be used instead -->
| candidate1        = <!-- any type of election -->
| leader1           = <!-- legislative or parliamentary only-->
| party1            = 
| alliance1         = 
<!-- presidential -->
| home_state1       = 
| running_mate1     = 
| electoral_vote1   = 
| delegate_count1   = 
| states_carried1   = 
| districts_won1    = 
<!-- legislative or parliamentary -->
| leader_since1     = 
| leaders_seat1     = 
| last_election1    = 
| seats_before1     = 
| seats_needed1     = 
| seats1            = 
| seats_after1      = 
| seat_change1      = 
<!-- any -->
| popular_vote1     = 
| percentage1       = 
| swing1            = <!-- legislative or parliamentary only-->
<!--        person 2        -->
| image2            = 
| colour2           = 
| nominee2          = <!-- presidential only, when appropriate, candidate2 can be used instead -->
| candidate2        = <!-- any type of election -->
| leader2           = <!-- legislative or parliamentary only-->
| party2            = 
| alliance2         = 
<!-- presidential -->
| home_state2       = 
| running_mate2     = 
| electoral_vote2   = 
| delegate_count2   = 
| states_carried2   = 
| districts_won2    = 
<!-- legislative or parliamentary -->
| leader_since2     = 
| leaders_seat2     = 
| last_election2    = 
| seats_before2     = 
| seats_needed2     = 
| seats2            = 
| seats_after2      = 
| seat_change2      = 
<!-- any -->
| popular_vote2     = 
| percentage2       = 
| swing2            = <!-- legislative or parliamentary only-->
<!-- polls -->
| poll1_date        = 
| poll1_source      = 
| poll1_nominee1    = <!-- presidential only, when appropriate, poll1_candidate1 can be used instead -->
| poll1_party1      = <!-- legislative or parliamentary only-->
| poll1_nominee2    = <!-- presidential only, when appropriate, poll1_candidate2 can be used instead -->
| poll1_party2      = <!-- legislative or parliamentary only-->
| poll2_date        = 
| poll2_source      = 
| poll2_nominee1    = <!-- presidential only, when appropriate, poll2_candidate1 can be used instead -->
| poll2_party1      = <!-- legislative or parliamentary only-->
| poll2_nominee2    = <!-- presidential only, when appropriate, poll2_candidate2 can be used instead -->
| poll2_party2      = <!-- legislative or parliamentary only-->
<!-- auxiliary rows -->
| 1blank            = 
| 1data1            = 
| 1data2            = 
| 2blank            = 
| 2data1            = 
| 2data2            = 
<!-- map -->
| map_image         = 
| map_size          = 
| map_alt           = 
| map               = 
| map_caption       = 
<!-- bottom -->
| title             = 
| before_election   = 
| before_party      = 
| posttitle         = 
| after_election    = 
| after_party       = 
}}
</pre>

: *Non-optional fields.
: &dagger; only displayed if the election is yet to take place.
: &Dagger; only displayed if the election has finished.

{| class="wikitable" cellpadding=2
! Field !! Type !! Description
|-
| '''election_name'''
|*
| Name given to the election. If this field is left empty the page name is displayed
|-
| '''country'''
|
| Country where the election took place.
|-
| '''flag_year'''
|
| For historical elections when an older flag design was in effect, enter the year the flag came into effect (not the election year).  Default is to use the current flag.
|-
| '''flag_image'''
|
| For non-country elections, specify the full name of the flag, coat-of-arms, or seal image to display.
|-
| '''type'''
|*
| The type of election. Must be one of four: presidential, legislative, parliamentary or by-election. Legislative after the election will display majority and minority party, rather than first and second party.
|-
| '''vote_type'''
|
| The type of votes recorded at popular_vote''n''. Defaults to "Popular".
|-
| '''ongoing'''
|*
| Must be either yes or no, whether the election is yet to take place, or completed.  Fields marked with a &dagger; are only displayed if the election is yet to take place. Fields marked with a &Dagger; are only displayed if the election has finished. (Default no.)
|-
| '''party_colour'''
|
| Also spelled '''party_color'''. To turn off the party colours enter 'no'.
|-
| '''party_name'''
|
| To turn off linking to the parties enter 'no'.
|-
| '''alliance_name'''
|
| To turn off linking to the alliances enter 'no'.
|-
| '''previous_election'''
|
| The page name of the last election of this type.
|-
| '''previous_year'''
|
| The year the last election of this type took place.
|-
| '''previous_mps'''
| ''legislative''<br>''parliamentary''
|  Also spelled '''previous_MPs''' or '''previous_members''', page name for the members elected in the last election.
|-
| '''election_date'''
| 
| Date of election - use {{tl|Start date}}
|-
| '''elected_mps'''
| ''legislative''<br>''parliamentary''
| Wikilink to the MPs elected in this election.
|-
| '''next_election'''
|
| The page name of the next election of this type.   If red link (it doesn't exist), then it will appear unlinked.
|-
| '''next_year'''
|
| The year the next election of this type took place.
|-
| '''next_mps'''
| ''legislative''<br>''parliamentary''
| Also spelled '''next_MPs''' or '''next_members''', page name for the members elected in the next election.
|-
| '''votes_for_election'''
| ''presidential''
| The number of votes for election and the system of voting (e.g. Electoral College).
|-
| '''needed_votes'''
| ''presidential''
| The number of votes required to win. If there is an even number of votes, use the number that is said by the media.
|-
| '''seats_for_election'''
| ''legislative''<br>''parliamentary''<br>''by-election''
| The number of seats for election and the house or chamber the seats are for.
|-
| '''majority_seats'''
| ''legislative''<br>''parliamentary''
| The number of seats required for a [majority government](https://second-renaissance.fandom.com/wiki/majority_government). If there is an even number of seats in the house or chamber, use the number that is said by the media.
|-
| '''opinion_polls'''
| 
| Pagename or section anchor of [opinion poll](https://second-renaissance.fandom.com/wiki/opinion_poll)s.
|-
| '''registered'''
| 
| Number of [registered voters](https://second-renaissance.fandom.com/wiki/Voter_registration) for this election.
|-
| '''turnout'''
| 
| [Voter turnout](https://second-renaissance.fandom.com/wiki/Voter_turnout) for this election.
|-
| '''image1'''
| 
| Image of Nominee, head of Party list or Party Leader. The number can be changed up to nine to display different Nominees, heads of Party list or Leaders at the same time. In order to work, colour1 or party1 must be entered.
|-
| '''colour1'''
| 
| Also spelt '''color1'''. Enter a hex colour code (without the <nowiki>#</nowiki>) to override the border colour of image1. The number can be changed up to nine to display different Nominees, heads of Party list or Leaders at the same time.
|-
| '''nominee1'''
| ''presidential''<br>''by-election''
| Name of Nominee. When appropriate, candidate1 can be used instead. The number can be changed up to nine to display different Nominees or Candidates at the same time.
|-
| '''candidate1'''
| 
| Name of Candidate. The number can be changed up to nine to display different Candidates at the same time.
|-
| '''leader1'''
| ''legislative''<br>''parliamentary''
| Name of head of Party list or Party Leader. The number can be changed up to nine to display different Parties at the same time.
|-
| '''party1'''
| 
| Political Party using [Political party shortname templates](https://second-renaissance.fandom.com/wiki/:Category:Political_party_shortname_templates). The number can be changed up to nine to display different Parties at the same time.
|-
| '''alliance1'''
| 
| Political alliance in elections where coalition politics is common. 
|-
| '''home_state1'''
| ''presidential''
| The state the Nominee or Candidate represents. The number can be changed up to nine to display different Nominees at the same time.
|-
| '''running_mate1'''
| ''presidential''
| The Nominee's [Running mate](https://second-renaissance.fandom.com/wiki/Running_mate). The number can be changed up to nine to display different Nominees at the same time.
|-
| '''electoral_vote1'''
| ''presidential''<br>&Dagger;
| The [electoral vote](https://second-renaissance.fandom.com/wiki/electoral_vote)s obtained by the Nominee. The number can be changed up to nine to display different Nominees at the same time.
|-
| '''delegate_count1'''
| ''presidential''
| The aggregate number of [delegate](https://second-renaissance.fandom.com/wiki/delegate)s obtained by the candidate. The number can be changed up to nine to display different candidates at the same time. Intended for use in pre-election processes such as selection of delegates to [United States presidential nominating convention](https://second-renaissance.fandom.com/wiki/United_States_presidential_nominating_convention)s. Intended to be used instead of electoral_vote1 for these cases.
|-
| '''states_carried1'''
| ''presidential''<br>&Dagger;
| The states carried or won by the Nominee. The number can be changed up to nine to display different Nominees at the same time.
|-
| '''districs_won1'''
| ''presidential''<br>&Dagger;
| The number of districts won by the Nominee. The number can be changed up to nine to display different Nominees at the same time.
|-
| '''leader_since1'''
| ''legislative''<br>''parliamentary''
| The date the Leader took office. The number can be changed up to nine to display different Parties at the same time.
|-
| '''leaders_seat1'''
| ''legislative''<br>''parliamentary''
| The seat the Leader represents. The number can be changed up to nine to display different Parties at the same time.
|-
| '''last_election1'''
| ''legislative''<br>''parliamentary''
| The seat count and percentage of the vote received at the previous election. The number can be changed up to nine to display different Parties at the same time.
|-
| '''seats_before1'''
| ''legislative''<br>''parliamentary''
| The seat count before the election, labeled 'current seats' if the election is yet to take place. The number can be changed up to nine to display different Parties at the same time.
|-
| '''seats_needed1'''
| ''legislative''<br>''parliamentary''<br>&dagger;
| The seats required to gain an overall majority. The number can be changed up to nine to display different Parties at the same time.
|-
| '''seats1'''
| ''legislative''<br>''parliamentary''<br>&Dagger;
| The seats won at the election. The number can be changed up to nine to display different Parties at the same time.
|-
| '''seats_after1'''
| ''legislative''<br>''parliamentary''<br>&Dagger;
| The seat count after the election. The number can be changed up to nine to display different Parties at the same time.
|-
| '''seat_change1'''
| ''legislative''<br>''parliamentary''<br>&Dagger;
| The change in the number of seats won at the election compared to the previous election. The number can be changed up to nine to display different Parties at the same time.
|-
| '''popular_vote1'''
| &Dagger;
| The number of votes obtained by the Nominee or Party. The number can be changed up to nine to display different Nominees or Parties at the same time.
|-
| '''percentage1'''
| &Dagger;
| The percentage of the popular vote obtained by the Nominee or Party. The number can be changed up to nine to display different Nominees or Parties at the same time.
|-
| '''swing1'''
| ''legislative''<br>''parliamentary''<br>&Dagger;
| The [swing](https://second-renaissance.fandom.com/wiki/Swing_(politics)) or change in popular vote at the election compared to the previous election. The number can be changed up to nine to display different Parties at the same time.
|-
| '''poll1_date'''
| &dagger;
| The date of an opinion poll. The number can be changed up to five to display different polls at the same time.
|-
| '''poll1_source'''
| &dagger;
| The source or URL of the opinion poll. The number can be changed up to five to display different polls at the same time.
poll1_nominee1
|-
| '''poll1_nominee1'''
| ''presidential''<br>&dagger;
| The percentage poll 1 gave to nominee 1. When appropriate, '''poll1_candidate1''' can be used instead. The poll number can be changed up to five to display different polls at the same time. The nominee or candidate number can be changed up to nine to display different Nominees or Candidates at the same time.
|-
| '''poll1_party1'''
| ''legislative''<br>''parliamentary''<br>&dagger;
| The percentage poll 1 gave to party 1. The poll number can be changed up to five to display different polls at the same time. The party number can be changed up to nine to display different Nominees at the same time.
|-
| '''1blank'''
|
| Title of an auxiliary row. The number can be changed up to six to display six extra rows.
|-
| '''1data1'''
|
| Data 1 for nominee or party 1. The first number can be changed up to six to display six extra rows. The second number can be changed up to nine to display different Nominees or Parties at the same time.
|-
| '''map_image'''
|
| Page name for the election map file.
|-
| '''map_size'''
|
| Size of image of the election map to be displayed. (Default 300px).
|-
| '''map_alt'''
|
| [Alt text](https://second-renaissance.fandom.com/wiki/WP:Alternative_text_for_images) for the election map.
|-
| '''map'''
|
| A freeform replacement for the above, which can be used to insert [extension:ImageMap](https://second-renaissance.fandom.com/wiki/mw:extension:ImageMap)s or templates instead of images.
|-
| '''map_caption'''
|
| Caption on image of the election map to be displayed.
|-
| '''title'''
|
| Title of the leader before the election. (President, Speaker, Government, Prime Minister...)
|-
| '''before_election'''
|
| The leader in power before the election, labeled [incumbent](https://second-renaissance.fandom.com/wiki/incumbent) if the election is yet to take place.
|-
| '''before_party'''
|
| The party in power before the election. This can be set to "Acting (law)" (which will display as "[Acting](https://second-renaissance.fandom.com/wiki/Acting_(law))") if necessary.
|-
| '''posttitle'''
| &Dagger;
| Title of the victor of the election (President-elect, Prime Minister-designate...), only if different than before.
|-
| '''after_election'''
| &Dagger;
| The leader in power as a result of the election.
|-
| '''after_party'''
| &Dagger;
| The party in power as a result of the election.
|}

# Notes
The template can display up to nine parties or nominees at the same time, three per row. If exactly four are needed, use the first two on the top and bottom lines. This is done by only using the numbers 1, 2, 4 and 5 on the fields that require a number.

All the fields that work for Legislative will also work for Parliamentary. The only difference between the two is the titles above the images.

The template uses the party fields to display the party colour in the background of the images and some text. To turn this function off, input:
 | party_colour      = no
To override the calling of the party short name templates, input:
 | party_name        = no
To override the calling of the alliance short name templates, input:
 | alliance_name     = no
To override the colour for party1 or nominee1, input:
 | colour1           = [HEX OF COLOUR, MINUS #]
The hex number must be entered without the hash for the field to work. The number (colour'''1''') can be changed up to nine for different parties or Nominees. The fields work with both spellings of the word 'color'.

# Examples
## Presidential
{{Infobox election
| election_name     = United States presidential election, 2004
| country           = United States
| type              = presidential
| previous_election = United States presidential election, 2000
| previous_year     = 2000
| election_date     = {{Start date|2004|11|02}}
| next_election     = United States presidential election, 2008
| next_year         = 2008
| votes_for_election= All [538 electoral votes](https://second-renaissance.fandom.com/wiki/List_of_United_States_presidential_electors,_2004) of the [Electoral College](https://second-renaissance.fandom.com/wiki/Electoral_College_(United_States))
| needed_votes      = 270 electoral
<!-- George W. Bush -->
| image1            = [160x150px](243-file-george-w-bush-jpeg.md)
| nominee1          = [George W. Bush](https://second-renaissance.fandom.com/wiki/Wikipedia:George_W._Bush)
| party1            = Republican Party (United States)
| home_state1       = [Texas](1001-texas.md)
| running_mate1     = [Richard B. Cheney](https://second-renaissance.fandom.com/wiki/Wikipedia:Dick_Cheney)
| electoral_vote1   = 286
| states_carried1   = 31
| popular_vote1     = 62,040,610
| percentage1       = 50.7%
<!-- John Kerry -->
| image2            = [160x150px](797-file-john-kerry-headshot-with-us-flag-jpg.md)
| nominee2          = [John Kerry](https://second-renaissance.fandom.com/wiki/Wikipedia:John_Kerry)
| party2            = Democratic Party (United States)
| home_state2       = [Massachusetts](https://second-renaissance.fandom.com/wiki/Massachusetts)
| running_mate2     = [John Edwards](https://second-renaissance.fandom.com/wiki/Wikipedia:John_Edwards)
| electoral_vote2   = 251
| states_carried2   = 19 + [DC](679-washington-d-c.md)
| popular_vote2     = 59,028,444
| percentage2       = 48.3%
<!-- map -->
| map_image         = ElectoralCollege2004.svg
| map_size          = 270px
| map_caption       = Presidential election results map
<!-- bottom -->
| title             = President
| before_election   = [George W. Bush](https://second-renaissance.fandom.com/wiki/Wikipedia:George_W._Bush)
| before_party      = Republican Party (United States)
| after_election    = [George W. Bush](https://second-renaissance.fandom.com/wiki/Wikipedia:George_W._Bush)
| after_party       = Republican Party (United States)
}}
<pre style="overflow: auto">
{{Infobox election
| election_name     = United States presidential election, 2004
| country           = United States
| type              = presidential
| previous_election = United States presidential election, 2000
| previous_year     = 2000
| election_date     = {{Start date|2004|11|02}}
| next_election     = United States presidential election, 2008
| next_year         = 2008
| votes_for_election= All [538 electoral votes](https://second-renaissance.fandom.com/wiki/List_of_United_States_presidential_electors,_2004) of the [Electoral College](https://second-renaissance.fandom.com/wiki/Electoral_College_(United_States))
| needed_votes      = 270 electoral
<!-- George W. Bush -->
| image1            = [160x150px](243-file-george-w-bush-jpeg.md)
| nominee1          = [George W. Bush](https://second-renaissance.fandom.com/wiki/Wikipedia:George_W._Bush)
| party1            = Republican Party (United States)
| home_state1       = [Texas](1001-texas.md)
| running_mate1     = [Richard B. Cheney](https://second-renaissance.fandom.com/wiki/Dick_Cheney)
| electoral_vote1   = 286
| states_carried1   = 31
| popular_vote1     = 62,040,610
| percentage1       = 50.7%
<!-- John Kerry -->
| image2            = [160x150px](797-file-john-kerry-headshot-with-us-flag-jpg.md)
| nominee2          = [John Kerry](https://second-renaissance.fandom.com/wiki/John_Kerry)
| party2            = Democratic Party (United States)
| home_state2       = [Massachusetts](https://second-renaissance.fandom.com/wiki/Massachusetts)
| running_mate2     = [John Edwards](https://second-renaissance.fandom.com/wiki/John_Edwards)
| electoral_vote2   = 251
| states_carried2   = 19 + [DC](679-washington-d-c.md)
| popular_vote2     = 59,028,444
| percentage2       = 48.3%
<!-- map -->
| map_image         = ElectoralCollege2004.svg
| map_size          = 270px
| map_caption       = Presidential election results map
<!-- bottom -->
| title             = President
| before_election   = [George W. Bush](https://second-renaissance.fandom.com/wiki/George_W._Bush)
| before_party      = Republican Party (United States)
| after_election    = [George W. Bush](https://second-renaissance.fandom.com/wiki/George_W._Bush)
| after_party       = Republican Party (United States)
}}</pre>
{{-}}

## Ongoing presidential
{{Infobox election
| election_name     = United States presidential election, 2008
| country           = United States
| type              = presidential
| ongoing           = yes
| previous_election = United States presidential election, 2004
| previous_year     = 2004
| election_date     = {{Start date|2008|11|04}}
| next_year         = 2012
<!-- Hillary Clinton -->
| image1            = [160x150px](https://second-renaissance.fandom.com/wiki/File:Hillary_Clinton_official_Secretary_of_State_portrait_crop.jpg)
| candidate1        = [Hillary Clinton](1296-hillary-clinton.md)
| party1            = Democratic Party (United States)
| home_state1       = [New York](1022-new-york.md)
| running_mate1     = 
| electoral_vote1   = 
| states_carried1   = 
| popular_vote1     = 
| percentage1       = 
<!-- Barack Obama -->
| image2            = [160x150px](https://second-renaissance.fandom.com/wiki/File:Official_portrait_of_Barack_Obama.jpg)
| candidate2        = [Barack Obama](https://second-renaissance.fandom.com/wiki/Barack_Obama)
| party2            = Democratic Party (United States)
| home_state2       = [Illinois](https://second-renaissance.fandom.com/wiki/Illinois)
| running_mate2     = 
| electoral_vote2   = 
| states_carried2   = 
| popular_vote2     = 
| percentage2       = 
<!-- John Edwards -->
| image3            = [160x150px](https://second-renaissance.fandom.com/wiki/File:John_Edwards,_official_Senate_photo_portrait.jpg)
| candidate3        = [John Edwards](https://second-renaissance.fandom.com/wiki/John_Edwards)
| party3            = Democratic Party (United States)
| home_state3       = [North Carolina](1003-north-carolina.md)
| running_mate3     = 
| electoral_vote3   = 
| states_carried3   = 
| popular_vote3     = 
| percentage3       = 
<!-- Rudy Giuliani -->
| image4            = [160x150px](https://second-renaissance.fandom.com/wiki/File:Rudy_Giuliani.jpg)
| candidate4        = [Rudy Giuliani](https://second-renaissance.fandom.com/wiki/Rudy_Giuliani)
| party4            = Republican Party (United States)
| home_state4       = [New York](1022-new-york.md)
| running_mate4     = 
| electoral_vote4   = 
| states_carried4   = 
| popular_vote4     = 
| percentage4       = 
<!-- Fred Thompson -->
| image5            = [160x150px](https://second-renaissance.fandom.com/wiki/File:Fred_Thompson.jpg)
| candidate5        = [Fred Thompson](https://second-renaissance.fandom.com/wiki/Fred_Thompson)
| party5            = Republican Party (United States)
| home_state5       = [Tennessee](1026-tennessee.md)
| running_mate5     = 
| electoral_vote5   = 
| states_carried5   = 
| popular_vote5     = 
| percentage5       = 
<!-- John McCain -->
| image6            = [160x150px](https://second-renaissance.fandom.com/wiki/File:John_McCain_official_portrait_2009.jpg)
| candidate6        = [John McCain](https://second-renaissance.fandom.com/wiki/John_McCain)
| party6            = Republican Party (United States)
| home_state6       = [Arizona](https://second-renaissance.fandom.com/wiki/Arizona)
| running_mate6     = 
| electoral_vote6   = 
| states_carried6   = 
| popular_vote6     = 
| percentage6       = 
<!-- polls -->
| poll1_date        = August 3, 2007
| poll1_source      = http://www.example.edu/poll/070803
| poll1_candidate1  = '''45%'''
| poll1_candidate2  = 22%
| poll1_candidate3  = 9%
| poll1_candidate4  = '''26%'''
| poll1_candidate5  = 21%
| poll1_candidate6  = 11%

| poll2_date        = August 1, 2007
| poll2_source      = http://www.example.edu/poll/070801
| poll2_candidate1  = '''46%'''
| poll2_candidate2  = 23%
| poll2_candidate3  = 12%
| poll2_candidate4  = '''32%'''
| poll2_candidate5  = 20%
| poll2_candidate6  = 13%

| poll3_date        = August 1, 2007
| poll3_source      = http://www.example.com/news/070801
| poll3_candidate1  = '''44%'''
| poll3_candidate2  = 23%
| poll3_candidate3  = 14%
| poll3_candidate4  = '''33%'''
| poll3_candidate5  = 20%
| poll3_candidate6  = 17%

| poll4_date        = July 30, 2007
| poll4_source      = http://www.example.com/news/070730
| poll4_candidate1  = '''43%'''
| poll4_candidate2  = 22%
| poll4_candidate3  = 13%
| poll4_candidate4  = '''30%'''
| poll4_candidate5  = 22%
| poll4_candidate6  = 13%
<!-- map -->
| map_image         = US Electoral College Map.PNG
| map_size          = 350px
| map_caption       = Presidential electoral votes by state.
<!-- bottom -->
| title             = President
| before_election   = [George W. Bush](https://second-renaissance.fandom.com/wiki/George_W._Bush)
| before_party      = Republican Party (United States)
| after_election    = 
| after_party       = 
}}
<pre style="overflow: auto">
{{Infobox election
| election_name     = United States presidential election, 2008
| country           = United States
| type              = presidential
| ongoing           = yes
| previous_election = United States presidential election, 2004
| previous_year     = 2004
| election_date     = {{Start date|2008|11|04}}
| next_election     = United States presidential election, 2012
| next_year         = 2012
<!-- Hillary Clinton -->
| image1            = [160x150px](https://second-renaissance.fandom.com/wiki/File:Hillary_Clinton_official_Secretary_of_State_portrait_crop.jpg)
| candidate1        = [Hillary Clinton](1296-hillary-clinton.md)
| party1            = Democratic Party (United States)
| home_state1       = [New York](1022-new-york.md)
| running_mate1     = 
| electoral_vote1   = 
| states_carried1   = 
| popular_vote1     = 
| percentage1       = 
<!-- Barack Obama -->
| image2            = [160x150px](https://second-renaissance.fandom.com/wiki/File:Official_portrait_of_Barack_Obama.jpg)
| candidate2        = [Barack Obama](https://second-renaissance.fandom.com/wiki/Barack_Obama)
| party2            = Democratic Party (United States)
| home_state2       = [Illinois](https://second-renaissance.fandom.com/wiki/Illinois)
| running_mate2     = 
| electoral_vote2   = 
| states_carried2   = 
| popular_vote2     = 
| percentage2       = 
<!-- John Edwards -->
| image3            = [160x150px](https://second-renaissance.fandom.com/wiki/File:John_Edwards,_official_Senate_photo_portrait.jpg)
| candidate3        = [John Edwards](https://second-renaissance.fandom.com/wiki/John_Edwards)
| party3            = Democratic Party (United States)
| home_state3       = [North Carolina](1003-north-carolina.md)
| running_mate3     = 
| electoral_vote3   = 
| states_carried3   = 
| popular_vote3     = 
| percentage3       = 
<!-- Rudy Giuliani -->
| image4            = [160x150px](https://second-renaissance.fandom.com/wiki/File:Rudy_Giuliani.jpg)
| candidate4        = [Rudy Giuliani](https://second-renaissance.fandom.com/wiki/Rudy_Giuliani)
| party4            = Republican Party (United States)
| home_state4       = [New York](1022-new-york.md)
| running_mate4     = 
| electoral_vote4   = 
| states_carried4   = 
| popular_vote4     = 
| percentage4       = 
<!-- Fred Thompson -->
| image5            = [160x150px](https://second-renaissance.fandom.com/wiki/File:Fred_Thompson.jpg)
| candidate5        = [Fred Thompson](https://second-renaissance.fandom.com/wiki/Fred_Thompson)
| party5            = Republican Party (United States)
| home_state5       = [Tennessee](1026-tennessee.md)
| running_mate5     = 
| electoral_vote5   = 
| states_carried5   = 
| popular_vote5     = 
| percentage5       = 
<!-- John McCain -->
| image6            = [160x150px](https://second-renaissance.fandom.com/wiki/File:John_McCain_official_portrait_2009.jpg)
| candidate6        = [John McCain](https://second-renaissance.fandom.com/wiki/John_McCain)
| party6            = Republican Party (United States)
| home_state6       = [Arizona](https://second-renaissance.fandom.com/wiki/Arizona)
| running_mate6     = 
| electoral_vote6   = 
| states_carried6   = 
| popular_vote6     = 
| percentage6       = 
<!-- polls -->
| poll1_date        = August 3, 2007
| poll1_source      = http://www.example.edu/poll/070803
| poll1_candidate1  = '''45%'''
| poll1_candidate2  = 22%
| poll1_candidate3  = 9%
| poll1_candidate4  = '''26%'''
| poll1_candidate5  = 21%
| poll1_candidate6  = 11%

| poll2_date        = August 1, 2007
| poll2_source      = http://www.example.edu/poll/070801
| poll2_candidate1  = '''46%'''
| poll2_candidate2  = 23%
| poll2_candidate3  = 12%
| poll2_candidate4  = '''32%'''
| poll2_candidate5  = 20%
| poll2_candidate6  = 13%

| poll3_date        = August 1, 2007
| poll3_source      = http://www.example.com/news/070801
| poll3_candidate1  = '''44%'''
| poll3_candidate2  = 23%
| poll3_candidate3  = 14%
| poll3_candidate4  = '''33%'''
| poll3_candidate5  = 20%
| poll3_candidate6  = 17%

| poll4_date        = July 30, 2007
| poll4_source      = http://www.example.com/news/070730
| poll4_candidate1  = '''43%'''
| poll4_candidate2  = 22%
| poll4_candidate3  = 13%
| poll4_candidate4  = '''30%'''
| poll4_candidate5  = 22%
| poll4_candidate6  = 13%
<!-- map -->
| map_image         = Electoral map.svg
| map_size          = 350px
| map_caption       = Presidential electoral votes by state.
<!-- bottom -->
| title             = President
| before_election   = [George W. Bush](https://second-renaissance.fandom.com/wiki/George_W._Bush)
| before_party      = Republican Party (United States)
| after_election    = 
| after_party       = 
}}</pre>
{{-}}

## Legislative or parliamentary
{{Infobox election
| election_name     = United Kingdom general election, 2005
| country           = United Kingdom
| type              = parliamentary
| previous_election = United Kingdom general election, 2001
| previous_year     = 2001
| previous_mps      = List of MPs elected in the United Kingdom general election, 2001
| election_date     = {{Start date|2005|05|05}}
| elected_mps       = [members](https://second-renaissance.fandom.com/wiki/List_of_MPs_elected_in_the_United_Kingdom_general_election,_2005)
| next_election     = United Kingdom general election, 2010
| next_year         = 2010
| next_mps          = List of MPs elected in the United Kingdom general election, 2010
| seats_for_election= All [646 seats](https://second-renaissance.fandom.com/wiki/List_of_United_Kingdom_Parliament_constituencies_2005–2010) to the [House of Commons](https://second-renaissance.fandom.com/wiki/House_of_Commons_of_the_United_Kingdom)
| majority_seats    = 324
| opinion_polls     = #Opinion polls
| turnout           = 61.4%
<!-- Labour -->
| image1            = [160x150px](https://second-renaissance.fandom.com/wiki/File:TonyBlairBasra.JPG)
| leader1           = [Tony Blair](https://second-renaissance.fandom.com/wiki/Tony_Blair)
| party1            = Labour Party (UK)
| leader_since1     = 21 July 1994
| leaders_seat1     = [Sedgefield](https://second-renaissance.fandom.com/wiki/Sedgefield_(UK_Parliament_constituency))
| last_election1    = 413 seats, 40.7%
| seats_before1     = 403
| seats1            = 355
| seat_change1      = -48
| popular_vote1     = 9,552,436
| percentage1       = 35.2%
| swing1            = -5.5%
<!-- Conservative -->
| image2            = [160x150px](https://second-renaissance.fandom.com/wiki/File:Michael_Howard_1099_cropped.jpg)
| leader2           = [Michael Howard](https://second-renaissance.fandom.com/wiki/Michael_Howard)
| party2            = Conservative Party (UK)
| leader_since2     = 6 November 2003
| leaders_seat2     = [Folkestone & Hythe](https://second-renaissance.fandom.com/wiki/Folkestone_and_Hythe_(UK_Parliament_constituency))
| last_election2    = 166 seats, 31.7%
| seats_before2     = 165
| seats2            = 198
| seat_change2      = +33
| popular_vote2     = 8,784,915
| percentage2       = 32.4%
| swing2            = +0.7%
<!-- Liberal Democrats -->
| image3            = [160x150px](https://second-renaissance.fandom.com/wiki/File:Charles_Kennedy.jpg)
| leader3           = [Charles Kennedy](https://second-renaissance.fandom.com/wiki/Charles_Kennedy)
| party3            = Liberal Democrats
| leader_since3     = 9 August 1999
| leaders_seat3     = [Ross, Skye, & Lochaber](https://second-renaissance.fandom.com/wiki/Ross,_Skye_and_Lochaber_(UK_Parliament_constituency))
| last_election3    = 52 seats, 18.3%
| seats_before3     = 51
| seats3            = 62
| seat_change3      = +11
| popular_vote3     = 5,985,454
| percentage3       = 22.0%
| swing3            = +3.7%
<!-- map -->
| map_image         = 2005UKElectionMap.svg
| map_size          = 250px
| map_caption       = Map of United Kingdom showing constituencies won
<!-- bottom -->
| title             = Prime Minister
| before_election   = [Tony Blair](https://second-renaissance.fandom.com/wiki/Tony_Blair)
| before_party      = Labour Party (UK)
| after_election    = [Tony Blair](https://second-renaissance.fandom.com/wiki/Tony_Blair)
| after_party       = Labour Party (UK)
}}
<pre style="overflow: auto">
{{Infobox election
| election_name     = United Kingdom general election, 2005
| country           = United Kingdom
| type              = parliamentary
| previous_election = United Kingdom general election, 2001
| previous_year     = 2001
| previous_mps      = List of MPs elected in the United Kingdom general election, 2001
| election_date     = {{Start date|2005|05|05}}
| elected_mps       = [members](https://second-renaissance.fandom.com/wiki/List_of_MPs_elected_in_the_United_Kingdom_general_election,_2005)
| next_election     = United Kingdom general election, 2010
| next_year         = 2010
| next_mps          = List of MPs elected in the United Kingdom general election, 2010
| seats_for_election= All [646 seats](https://second-renaissance.fandom.com/wiki/List_of_United_Kingdom_Parliament_constituencies_2005–2010) to the [House of Commons](https://second-renaissance.fandom.com/wiki/House_of_Commons_of_the_United_Kingdom)
| majority_seats    = 324
| opinion_polls     = #Opinion polls
| turnout           = 61.4%
<!-- Labour -->
| image1            = [160x150px](https://second-renaissance.fandom.com/wiki/File:TonyBlairBasra.JPG)
| leader1           = [Tony Blair](https://second-renaissance.fandom.com/wiki/Tony_Blair)
| party1            = Labour Party (UK)
| leader_since1     = 21 July 1994
| leaders_seat1     = [Sedgefield](https://second-renaissance.fandom.com/wiki/Sedgefield_(UK_Parliament_constituency))
| last_election1    = 413 seats, 40.7%
| seats_before1     = 403
| seats1            = 355
| seat_change1      = -48
| popular_vote1     = 9,552,436
| percentage1       = 35.2%
| swing1            = -5.5%
<!-- Conservative -->
| image2            = [160x150px](https://second-renaissance.fandom.com/wiki/File:Michael_Howard_1099_cropped.jpg)
| leader2           = [Michael Howard](https://second-renaissance.fandom.com/wiki/Michael_Howard)
| party2            = Conservative Party (UK)
| leader_since2     = 6 November 2003
| leaders_seat2     = [Folkestone & Hythe](https://second-renaissance.fandom.com/wiki/Folkestone_and_Hythe_(UK_Parliament_constituency))
| last_election2    = 166 seats, 31.7%
| seats_before2     = 165
| seats2            = 198
| seat_change2      = +33
| popular_vote2     = 8,784,915
| percentage2       = 32.4%
| swing2            = +0.7%
<!-- Liberal Democrats -->
| image3            = [160x150px](https://second-renaissance.fandom.com/wiki/File:Charles_Kennedy.jpg)
| leader3           = [Charles Kennedy](https://second-renaissance.fandom.com/wiki/Charles_Kennedy)
| party3            = Liberal Democrats
| leader_since3     = 9 August 1999
| leaders_seat3     = [Ross, Skye, & Lochaber](https://second-renaissance.fandom.com/wiki/Ross,_Skye_and_Lochaber_(UK_Parliament_constituency))
| last_election3    = 52 seats, 18.3%
| seats_before3     = 51
| seats3            = 62
| seat_change3      = +11
| popular_vote3     = 5,985,454
| percentage3       = 22.0%
| swing3            = +3.7%
<!-- map -->
| map_image         = 2005UKElectionMap.svg
| map_size          = 250px
| map_caption       = Map of United Kingdom showing constituencies won
<!-- bottom -->
| title             = Prime Minister
| before_election   = [Tony Blair](https://second-renaissance.fandom.com/wiki/Tony_Blair)
| before_party      = Labour Party (UK)
| after_election    = [Tony Blair](https://second-renaissance.fandom.com/wiki/Tony_Blair)
| after_party       = Labour Party (UK)
}}</pre>
{{-}}

## Ongoing legislative or parliamentary
{{Infobox election
| election_name     = 54th United Kingdom general election
| country           = United Kingdom
| type              = parliamentary
| ongoing           = yes
| previous_election = United Kingdom general election, 2005
| previous_year     = 2005
| previous_mps      = List of MPs elected in the United Kingdom general election, 2005
| election_date     = On or before {{Start date|2010|06|03}}
| elected_mps       = 
| next_election     = 
| next_year         = 
| next_mps          = 
| seats_for_election= All [650 seats](https://second-renaissance.fandom.com/wiki/List_of_United_Kingdom_Parliament_constituencies) to the [House of Commons](https://second-renaissance.fandom.com/wiki/House_of_Commons_of_the_United_Kingdom)
| majority_seats    = 326
| opinion_polls     = Opinion polling for the United Kingdom general election, 2010
| turnout           = 
<!-- Labour -->
| image1            = [160x150px](https://second-renaissance.fandom.com/wiki/File:GordonBrown1234_cropped.jpg)
| leader1           = [Gordon Brown](https://second-renaissance.fandom.com/wiki/Gordon_Brown)
| party1            = Labour Party (UK)
| leader_since1     = [24 June 2007](https://second-renaissance.fandom.com/wiki/Labour_Party_(UK)_leadership_election,_2007)
| leaders_seat1     = [Kirkcaldy & Cowdenbeath](https://second-renaissance.fandom.com/wiki/Kirkcaldy_and_Cowdenbeath_(UK_Parliament_constituency))
| last_election1    = 355 seats, 35.2%
| seats_before1     = 345
| seats_needed1     = -20
| seats1            = 
| seat_change1      = 
| popular_vote1     = 
| percentage1       = 
| swing1            = 
<!-- Conservative -->
| image2            = [160x150px](https://second-renaissance.fandom.com/wiki/File:David_Cameron_-_World_Economic_Forum_Annual_Meeting_Davos_2010.jpg)
| leader2           = [David Cameron](https://second-renaissance.fandom.com/wiki/David_Cameron)
| party2            = Conservative Party (UK)
| leader_since2     = [6 December 2005](https://second-renaissance.fandom.com/wiki/Conservative_Party_(UK)_leadership_election,_2005)
| leaders_seat2     = [Witney](https://second-renaissance.fandom.com/wiki/Witney_(UK_Parliament_constituency))
| last_election2    = 198 seats, 32.4%
| seats_before2     = 193
| seats_needed2     = 132
| seats2            = 
| seat_change2      = 
| popular_vote2     = 
| percentage2       = 
| swing2            = 
<!-- Liberal Democrat -->
| image3            = [160x150px](https://second-renaissance.fandom.com/wiki/File:Nick_Clegg_by_the_2009_budget_cropped.jpg)
| leader3           = [Nick Clegg](https://second-renaissance.fandom.com/wiki/Nick_Clegg)
| party3            = Liberal Democrats
| leader_since3     = [18 December 2007](https://second-renaissance.fandom.com/wiki/Liberal_Democrats_leadership_election,_2007)
| leaders_seat3     = [Sheffield Hallam](https://second-renaissance.fandom.com/wiki/Sheffield_Hallam_(UK_Parliament_constituency))
| last_election3    = 62 seats, 22.0%
| seats_before3     = 63
| seats_needed3     = 262
| seats3            = 
| seat_change3      = 
| popular_vote3     = 
| percentage3       = 
| swing3            = 
<!-- map -->
| map_image         = 
| map_size          = 
| map_caption       = 
<!-- bottom -->
| title             = Prime Minister
| before_election   = [Gordon Brown](https://second-renaissance.fandom.com/wiki/Gordon_Brown)
| before_party      = Labour Party (UK)
| after_election    = 
| after_party       = 
}}
<pre style="overflow: auto">
{{Infobox election
| election_name     = 54th United Kingdom general election
| country           = United Kingdom
| type              = parliamentary
| ongoing           = yes
| previous_election = United Kingdom general election, 2005
| previous_year     = 2005
| previous_mps      = List of MPs elected in the United Kingdom general election, 2005
| election_date     = On or before {{Start date|2010|06|03}}
| elected_mps       = 
| next_election     = 
| next_year         = 
| next_mps          = 
| seats_for_election= All [650 seats](https://second-renaissance.fandom.com/wiki/List_of_United_Kingdom_Parliament_constituencies) to the [House of Commons](https://second-renaissance.fandom.com/wiki/House_of_Commons_of_the_United_Kingdom)
| majority_seats    = 326
| opinion_polls     = Opinion polling for the United Kingdom general election, 2010
| turnout           = 
<!-- Labour -->
| image1            = [160x150px](https://second-renaissance.fandom.com/wiki/File:GordonBrown1234_cropped.jpg)
| leader1           = [Gordon Brown](https://second-renaissance.fandom.com/wiki/Gordon_Brown)
| party1            = Labour Party (UK)
| leader_since1     = [24 June, 2007](https://second-renaissance.fandom.com/wiki/Labour_Party_(UK)_leadership_election,_2007)
| leaders_seat1     = [Kirkcaldy & Cowdenbeath](https://second-renaissance.fandom.com/wiki/Kirkcaldy_and_Cowdenbeath_(UK_Parliament_constituency))
| last_election1    = 355 seats, 35.2%
| seats_before1     = 345
| seats_needed1     = -20
| seats1            = 
| seat_change1      = 
| popular_vote1     = 
| percentage1       = 
| swing1            = 
<!-- Conservative -->
| image2            = [160x150px](https://second-renaissance.fandom.com/wiki/File:David_Cameron_-_World_Economic_Forum_Annual_Meeting_Davos_2010.jpg)
| leader2           = [David Cameron](https://second-renaissance.fandom.com/wiki/David_Cameron)
| party2            = Conservative Party (UK)
| leader_since2     = [6 December, 2005](https://second-renaissance.fandom.com/wiki/Conservative_Party_(UK)_leadership_election,_2005)
| leaders_seat2     = [Witney](https://second-renaissance.fandom.com/wiki/Witney_(UK_Parliament_constituency))
| last_election2    = 198 seats, 32.4%
| seats_before2     = 193
| seats_needed2     = 132
| seats2            = 
| seat_change2      = 
| popular_vote2     = 
| percentage2       = 
| swing2            = 
<!-- Liberal Democrat -->
| image3            = [160x150px](https://second-renaissance.fandom.com/wiki/File:Nick_Clegg_by_the_2009_budget_cropped.jpg)
| leader3           = [Nick Clegg](https://second-renaissance.fandom.com/wiki/Nick_Clegg)
| party3            = Liberal Democrats
| leader_since3     = [18 December 2007](https://second-renaissance.fandom.com/wiki/Liberal_Democrats_leadership_election,_2007)
| leaders_seat3     = [Sheffield Hallam](https://second-renaissance.fandom.com/wiki/Sheffield_Hallam_(UK_Parliament_constituency))
| last_election3    = 62 seats, 22.0%
| seats_before3     = 63
| seats_needed3     = 262
| seats3            = 
| seat_change3      = 
| popular_vote3     = 
| percentage3       = 
| swing3            = 
<!-- map -->
| map_image         = 
| map_size          = 
| map_caption       = 
<!-- bottom -->
| title             = Prime Minister
| before_election   = [Gordon Brown](https://second-renaissance.fandom.com/wiki/Gordon_Brown)
| before_party      = Labour Party (UK)
| after_election    = 
| after_party       = 
}}</pre>
{{-}}

## By-election
{{Infobox election
| election_name = Bradford West by-election, 2012
| type = By-election
| country = United Kingdom
| seats_for_election = The [Bradford West](https://second-renaissance.fandom.com/wiki/Bradford_West_(UK_Parliament_constituency)) seat in the [House of Commons](https://second-renaissance.fandom.com/wiki/House_of_Commons_of_the_United_Kingdom).<br />Election by simple majority using [first past the post](https://second-renaissance.fandom.com/wiki/first_past_the_post).<br />Triggered by resignation of incumbent
| votes_for_election = 
| ongoing = no
| previous_election = United Kingdom general election, 2010
| previous_year = 2010
| next_election = 
| next_year = 
| election_date = {{Start date|2012|03|29|df=y}}
| candidate1 = [George Galloway](https://second-renaissance.fandom.com/wiki/George_Galloway)
| image1 =[100px](https://second-renaissance.fandom.com/wiki/File:George_Galloway_2007-02-24.jpg)
| party1 = Respect Party
| last_election1 = 1,245
| popular_vote1 = 18,341
| percentage1 = 55.9
| candidate2 = Imran Hussain
| image2 = &nbsp;
| party2 = Labour Party (UK)
| last_election2 = 18,401
| popular_vote2 = 8,201
| percentage2 = 25.0
| candidate3 = Jackie Whiteley
| image3 = &nbsp;
| party3 = Conservative Party (UK)
| last_election3 = 12,638
| popular_vote3 = 2,746
| percentage3 = 8.4
| candidate4 = Jeanette Sunderland
| image4 = 
| party4 = Liberal Democrats
| last_election4 = 4,732
| popular_vote4 = 1,505
| percentage4 = 4.6
| candidate5 = Sonja McNally
| image5 = &nbsp;
| party5 = UK Independence Party
| last_election5 = 812
| popular_vote5 = 1,085
| percentage5 = 3.3
| candidate6 = Dawud Islam
| image6 = &nbsp;
| party6 = Green Party of England and Wales
| last_election6 = 940
| popular_vote6 = 481
| percentage6 = 1.5
| title = MP
| posttitle = Subsequent MP
| before_election = [Marsha Singh](https://second-renaissance.fandom.com/wiki/Marsha_Singh)
| before_party = Labour Party (UK)
| after_election = [George Galloway](https://second-renaissance.fandom.com/wiki/George_Galloway)
| after_party = Respect Party
| map_image = BradfordWest2007Constituency.svg
| map_size = 200px
| map_alt = A map of West Yorkshire with black lines dividing the area into irregular shapes 
| map = 
| map_caption = Boundary of Bradford West in [West Yorkshire](https://second-renaissance.fandom.com/wiki/West_Yorkshire).
}}
<pre style="overflow: auto">
{{Infobox election
| election_name = Bradford West by-election, 2012
| type = By-election
| country = United Kingdom
| seats_for_election = The [Bradford West](https://second-renaissance.fandom.com/wiki/Bradford_West_(UK_Parliament_constituency)) seat in the [House of Commons](https://second-renaissance.fandom.com/wiki/House_of_Commons_of_the_United_Kingdom).<br />Elected by simple majority using [first past the post](https://second-renaissance.fandom.com/wiki/first_past_the_post).<br />Triggered by resignation of incumbent
| ongoing = no
| previous_election = United Kingdom general election, 2010
| previous_year = 2010
| next_election = 
| next_year = 
| election_date = {{Start date|2012|03|29|df=y}}
| candidate1 = [George Galloway](https://second-renaissance.fandom.com/wiki/George_Galloway)
| image1 =[100px](https://second-renaissance.fandom.com/wiki/File:George_Galloway_2007-02-24.jpg)
| party1 = Respect Party
| last_election1 = 1,245
| popular_vote1 = 18,341
| percentage1 = 55.9
| candidate2 = Imran Hussain
| image2 = &nbsp;
| party2 = Labour Party (UK)
| last_election2 = 18,401
| popular_vote2 = 8,201
| percentage2 = 25.0
| candidate3 = Jackie Whiteley
| image3 = &nbsp;
| party3 = Conservative Party (UK)
| last_election3 = 12,638
| popular_vote3 = 2,746
| percentage3 = 8.4
| candidate4 = Jeanette Sunderland
| image4 = 
| party4 = Liberal Democrats
| last_election4 = 4,732
| popular_vote4 = 1,505
| percentage4 = 4.6
| candidate5 = Sonja McNally
| image5 = &nbsp;
| party5 = UK Independence Party
| last_election5 = 812
| popular_vote5 = 1,085
| percentage5 = 3.3
| candidate6 = Dawud Islam
| image6 = &nbsp;
| party6 = Green Party of England and Wales
| last_election6 = 940
| popular_vote6 = 481
| percentage6 = 1.5
| title = MP
| posttitle = Subsequent MP
| before_election = [Marsha Singh](https://second-renaissance.fandom.com/wiki/Marsha_Singh)
| before_party = Labour Party (UK)
| after_election = [George Galloway](https://second-renaissance.fandom.com/wiki/George_Galloway)
| after_party = Respect Party
| map_image = BradfordWest2007Constituency.svg
| map_size = 200px
| map_alt = A map of West Yorkshire with black lines dividing the area into irregular shapes 
| map = 
| map_caption = Boundary of Bradford West in [West Yorkshire](https://second-renaissance.fandom.com/wiki/West_Yorkshire).
}}
</pre>
{{-}}

# Microformat
{{UF-hcal}}

Note: If no date is entered, then the microformat is not emitted.

# Template Data
{{TemplateDataHeader}}
<templatedata>{
  "description": "An infobox for election.",
  "params": {
  "election_name": {
      "label": "Name",
      "description": "Name given to the election.",
      "type": "string",
      "default": "PAGENAME",
      "required": false
    },
  "country": {
      "label": "Country",
      "description": "Country where the election took place.",
      "type": "string",
      "default": "",
      "required": false
    },
  "flag_year": {
      "label": "Flag year",
      "description": "For historical elections when an older flag design was in effect, enter the year the flag came into effect (not the election year).",
      "type": "string",
      "default": "current flag",
      "required": false
    },
  "flag_image": {
      "label": "Flag image",
      "description": "For non-country elections, specify the full name of the flag, coat-of-arms, or seal image to display.",
      "type": "string",
      "default": "",
      "required": false
    },
  "type": {
      "label": "Type",
      "description": "The type of election. Must be one of four: presidential, legislative, parliamentary or by-election. Legislative after the election will display majority and minority party, rather than first and second party.",
      "type": "string",
      "default": "",
      "required": false
    },
  "vote_type": {
      "label": "Vote type",
      "description": "The type of votes recorded at popular_voten",
      "type": "string",
      "default": "Popular",
      "required": false
    },
  "ongoing": {
      "label": "Ongoing",
      "description": "Must be either yes or no, whether the election is yet to take place, or completed. ",
      "type": "string",
      "default": "No",
      "required": false
    },
  "party_colour": {
      "label": "Party colour",
      "description": "Also spelled party_color. To turn off the party colours enter 'no'.",
      "type": "string",
      "default": "",
      "required": false
    },
  "party_name": {
      "label": "Party name",
      "description": "To turn off linking to the parties enter 'no'.",
      "type": "string",
      "default": "",
      "required": false
    },
  "alliance_name": {
      "label": "Alliance name",
      "description": "To turn off linking to the alliances enter 'no'.",
      "type": "string",
      "default": "",
      "required": false
    },
  "previous_election": {
      "label": "Previous election",
      "description": "The page name of the last election of this type.",
      "type": "string",
      "default": "",
      "required": false
    },
  "previous_year": {
      "label": "Previous year",
      "description": "The year the last election of this type took place.",
      "type": "string",
      "default": "",
      "required": false
    },
  "previous_mps": {
      "label": "Previous members",
      "description": "Also spelled previous_MPs or previous_members, page name for the members elected in the last election.",
      "type": "string",
      "default": "",
      "required": false
    },
  "election_date": {
      "label": "Election date",
      "description": "Date of election - use {{Start date}}.",
      "type": "string",
      "default": "",
      "required": false
    },
  "elected_mps": {
      "label": "Elected MPs",
      "description": "Wikilink to the MPs elected in this election.",
      "type": "string",
      "default": "",
      "required": false
    },
  "next_election": {
      "label": "Next election",
      "description": "The page name of the next election of this type. If red link (it doesn't exist), then it will appear unlinked.",
      "type": "string",
      "default": "",
      "required": false
    },
  "next_year": {
      "label": "Next year",
      "description": "The year the next election of this type took place.",
      "type": "string",
      "default": "",
      "required": false
    },
  "next_mps": {
      "label": "Next MPs",
      "description": "Also spelled next_MPs or next_members, page name for the members elected in the next election.",
      "type": "string",
      "default": "",
      "required": false
    },
  "votes_for_election": {
      "label": "Votes for election",
      "description": "The number of votes for election and the system of voting (eg. Electoral College).",
      "type": "number",
      "default": "",
      "required": false
    },
  "needed_votes": {
      "label": "Needed votes",
      "description": "The number of votes required to win. If there is an even number of votes, use the number that is said by the media.",
      "type": "string",
      "default": "",
      "required": false
    },
  "seats_for_election": {
      "label": "Seats for election",
      "description": "The number of seats for election and the house or chamber the seats are for.",
      "type": "number",
      "default": "",
      "required": false
    },
  "majority_seats": {
      "label": "Majority seats",
      "description": "The number of seats required for a majority government. If there is an even number of seats in the house or chamber, use the number that is said by the media.",
      "type": "number",
      "default": "",
      "required": false
    },
  "opinion_polls": {
      "label": "Opinion polls",
      "description": "Pagename or section anchor of opinion polls.",
      "type": "string",
      "default": "",
      "required": false
    },
  "turnout": {
      "label": "Turnout",
      "description": "Voter turnout for this election.",
      "type": "string",
      "default": "",
      "required": false
    },
  "image1": {
      "label": "Image 1",
      "description": "mage of Nominee, head of Party list or Party Leader. The number can be changed up to nine to display different Nominees, heads of Party list or Leaders at the same time. In order to work, colour1 or party1 must be entered.",
      "type": "wiki-page-name",
      "default": "",
      "required": false
    },
  "colour1": {
      "label": "Colour 1",
      "description": "Also spelt color1. Enter a hex colour code (without the #) to override the border colour of image1. The number can be changed up to nine to display different Nominees, heads of Party list or Leaders at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "nominee1": {
      "label": "Nominee 1",
      "description": "Name of Nominee. When appropriate, candidate1 can be used instead. The number can be changed up to nine to display different Nominees or Candidates at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "candidate1": {
      "label": "Candidate 1",
      "description": "Name of Candidate. The number can be changed up to nine to display different Candidates at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "leader1": {
      "label": "Leader 1",
      "description": "Name of head of Party list or Party Leader. The number can be changed up to nine to display different Parties at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "party1": {
      "label": "Party 1",
      "description": "Political Party using Political party shortname templates. The number can be changed up to nine to display different Parties at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "alliance1": {
      "label": "Alliance 1",
      "description": "Political alliance in elections where coalition politics is common.",
      "type": "string",
      "default": "",
      "required": false
    },
  "home_state1": {
      "label": "Home state 1",
      "description": "The state the Nominee or Candidate represents. The number can be changed up to nine to display different Nominees at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "running_mate1": {
      "label": "Running mate 1",
      "description": "The Nominee's Running mate. The number can be changed up to nine to display different Nominees at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "electoral_vote1": {
      "label": "Electoral vote 1",
      "description": "The electoral votes obtained by the Nominee. The number can be changed up to nine to display different Nominees at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "delegate_count1": {
      "label": "Delegate count 1",
      "description": "The aggregate number of delegates obtained by the candidate. The number can be changed up to nine to display different candidates at the same time. Intended for use in pre-election processes such as selection of delegates to United States presidential nominating conventions. Intended to be used instead of electoral_vote1 for these cases.",
      "type": "string",
      "default": "",
      "required": false
    },
  "states_carried1": {
      "label": "States carried 1",
      "description": "he states carried or won by the Nominee. The number can be changed up to nine to display different Nominees at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "districts_won1": {
      "label": "Districts won 1",
      "description": "The number of districts won by the Nominee. The number can be changed up to nine to display different Nominees at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "leader_since1": {
      "label": "Leader since 1",
      "description": "The date the Leader took office. The number can be changed up to nine to display different Parties at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "leaders_seat1": {
      "label": "Leaders seat 1",
      "description": "The seat the Leader represents. The number can be changed up to nine to display different Parties at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "last_election1": {
      "label": "Last election 1",
      "description": "The seat count and percentage of the vote received at the previous election. The number can be changed up to nine to display different Parties at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "seats_before1": {
      "label": "Seats before 1",
      "description": "The seat count before the election, labeled 'current seats' if the election is yet to take place. The number can be changed up to nine to display different Parties at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "seats_needed1": {
      "label": "Seats needed 1",
      "description": "The seats required to gain an overall majority. The number can be changed up to nine to display different Parties at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "seats1": {
      "label": "Seats 1",
      "description": "The seats won at the election. The number can be changed up to nine to display different Parties at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "seats_after1": {
      "label": "Seats after 1",
      "description": "The seat count after the election. The number can be changed up to nine to display different Parties at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "seat_change1": {
      "label": "Seat change 1",
      "description": "The change in the number of seats won at the election compared to the previous election. The number can be changed up to nine to display different Parties at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "popular_vote1": {
      "label": "Popular vote 1",
      "description": "The number of votes obtained by the Nominee or Party. The number can be changed up to nine to display different Nominees or Parties at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "percentage1": {
      "label": "Percentage 1",
      "description": "The percentage of the popular vote obtained by the Nominee or Party. The number can be changed up to nine to display different Nominees or Parties at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "swing1": {
      "label": "Swing 1",
      "description": "The swing or change in popular vote at the election compared to the previous election. The number can be changed up to nine to display different Parties at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "poll1_date": {
      "label": "Poll 1 date",
      "description": "The date of an opinion poll. The number can be changed up to five to display different polls at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "poll1_source": {
      "label": "Poll 1 source",
      "description": "The source or URL of the opinion poll. The number can be changed up to five to display different polls at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "poll1_nominee1": {
      "label": "Poll 1 nominee1",
      "description": "The percentage poll 1 gave to nominee 1. When appropriate, poll1_candidate1 can be used instead. The poll number can be changed up to five to display different polls at the same time. The nominee or candidate number can be changed up to nine to display different Nominees or Candidates at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "poll1_party1": {
      "label": "Poll 1 party 1",
      "description": "The percentage poll 1 gave to party 1. The poll number can be changed up to five to display different polls at the same time. The party number can be changed up to nine to display different Nominees at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "1blank": {
      "label": "1 blank",
      "description": "Title of an auxiliary row. The number can be changed up to six to display six extra rows.",
      "type": "string",
      "default": "",
      "required": false
    },
  "1data1": {
      "label": "1 data 1",
      "description": "Data 1 for nominee or party 1. The first number can be changed up to six to display six extra rows. The second number can be changed up to nine to display different Nominees or Parties at the same time.",
      "type": "string",
      "default": "",
      "required": false
    },
  "map_image": {
      "label": "Map image",
      "description": "Page name for the election map file.",
      "type": "wiki-page-name",
      "default": "",
      "required": false
    },
  "map_size": {
      "label": "Map size",
      "description": "Size of image of the election map to be displayed.",
      "type": "number",
      "default": "300px",
      "required": false
    },
  "map_alt": {
      "label": "Map alt",
      "description": "Alt text for the election map.",
      "type": "string",
      "default": "",
      "required": false
    },
  "map": {
      "label": "Map",
      "description": "A freeform replacement for the above, which can be used to insert extension:ImageMaps or templates instead of images.",
      "type": "line",
      "default": "",
      "required": false
    },
  "map_caption": {
      "label": "Map caption",
      "description": "Caption on image of the election map to be displayed.",
      "type": "string",
      "default": "",
      "required": false
    },
  "title": {
      "label": "Title",
      "description": "Title of the leader before the election. (President, Speaker, Government, Prime Minister).",
      "type": "string",
      "default": "",
      "required": false
    },
  "before_election": {
      "label": "Before election",
      "description": "The leader in power before the election, labeled incumbent if the election is yet to take place.",
      "type": "string",
      "default": "",
      "required": false
    },
  "before_party": {
      "label": "Before party",
      "description": "The party in power before the election. This can be set to 'Acting (law)' (which will display as 'Acting') if necessary.",
      "type": "string",
      "default": "",
      "required": false
    },
  "posttitle": {
      "label": "Post-title",
      "description": "Title of the victor of the election (President-elect, Prime Minister-designate), only if different than before.",
      "type": "string",
      "default": "",
      "required": false
    },
  "after_election": {
      "label": "After election",
      "description": "The leader in power as a result of the election.",
      "type": "string",
      "default": "",
      "required": false
    },
  "after_party": {
      "label": "After party",
      "description": "The party in power as a result of the election.",
      "type": "string",
      "default": "",
      "required": false
    }
  }
}</templatedata>

<includeonly>{{#ifeq:{{SUBPAGENAME}}|sandbox | |
<!-- Categories below this line, please; interwikis at Wikidata -->
[Election](https://second-renaissance.fandom.com/wiki/Category:Politics_and_government_infobox_templates)
}}</includeonly>
```

## Provenance

Raw source: `bronze/pages/672/1073.wikitext` · revision `1073` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AInfobox_election/doc)
