# Source audit notes — manifest tranche 1–300

**Scope:** First 300 entries in `bronze/manifests/pages.json`. Every corresponding original Bronze Wikitext file was opened from its manifest `raw_path` and reviewed. This tranche crosses all captured namespaces; it is not 300 main-namespace articles.

**Count:** 300 entries reviewed. Lionel Halvidar (page 212) and Interplanetary Trade Commission (page 216) were already directly reviewed in earlier tranches, so this tranche adds 298 unique reads. Four previously unverified prior claims are now directly verified: 21st Century (94), 22nd Century (96), Dylan J. Price (101), and Earth (272). Cumulative unique directly read pages: **361/3,579**.

## Namespace composition

| Namespace | Entries |
|---|---:|
| Template | 163 |
| File description | 75 |
| Main | 17 |
| User | 16 |
| Category | 13 |
| Board | 5 |
| MediaWiki | 3 |
| Message Wall | 3 |
| Thread | 3 |
| Template talk | 1 |
| Blog | 1 |
| **Total** | **300** |

## Main-namespace pages read

- Page 2 — **Second Renaissance Wikia**: project overview; the setting is described as realist-forecasting future history/high-concept science fiction, originally utopian, and explicitly subject to real-world events overtaking its forecasts and update lag.
- Page 84 — **Main Page**: redirect to Second Renaissance Wikia.
- Page 88 — **Timeline of major events**: chronology from the Great Reset through the 2160 Second Renaissance. It dates WWIII to 2051–55; first K'lerin contact to 2064; First Martian Revolution to 2079–81; India Crisis to 2119–26; Aztlan/Second American Civil War to 2133–34; Third Mexican War to 2134–39; Hispanic-American annexation to 2140; Eternal Spring Revolt to 2149.
- Page 94 — **21st Century**: describes life expectancy rising from 65 to 150 years, WWIII causing 110,000 deaths, Solar System settlement, augmentation rights, AI, quantum electronics, virtuals, geoengineering and cultural change.
- Page 96 — **22nd Century**: overview through 2160; Earth population just over 9bn in 2160, Mars about 3bn by 2130, Earth-sphere population about 14.7bn in 2160. Its politics list dates the India Crisis to 2126, unlike the timeline's 2119–26.
- Page 97 — **Little Cold War**: NATO–Russia confrontation c.2008–2029; Georgia, Ukraine, Syria, 2016 US election interference, space race and Korean standoff. The article contains substantial real-world 2022–26 narrative, including claims about 2025 summits and events through January 2026; these are recorded as source claims, not independently verified facts.
- Page 101 — **Dylan J. Price**: California governor (2027–29), US vice president (2029–37), president (2037–45). Infobox birth date is 13 April 1985, while prose says 9 November 1985. Sections cover the 2038 US–Japan trade war, 2043 Summer of Storms, federal management-AI reforms, cybersecurity certification and biotech investment.
- Page 107 — **World War III**: infobox dates 23 November 2051–14 January 2055; chronology records alternative end dates of 22 November 2054 (ceasefire), 2 January 2055 (Turkish surrender), and 8 October 2054 in some US histories. Infobox casualties are 54,000 and 56,000, matching the prose's 110,000 total dead. The conflict begins with Japan's attack on the US Orbital Defense Network and ends with Geneva settlement and US space-military supremacy.
- Page 119 — **Third Mexican-American War**: infobox dates 2 February 2133–4 April 2139, while the timeline and 22nd-century overview describe the Mexican invasion phase beginning in 2134. Narrative covers Aztlan secession, global theaters, colonial reinforcements, relativistic bombardment, nuclear winter, Treaty of San Juan and Mexico's annexation on 1 January 2140.
- Page 136 — **Progress Party (United States)**: infobox says founded 17 October 2023, while prose says founded in 2060 after a Democratic split; merged into UPP in December 2155.
- Page 212 — **Lionel Halvidar**: previously directly read; repeated manifest entry, not a new unique read.
- Page 214 — **President of the United States**: office overview and presidential list through 68th president Dom Terragno (since 2157); says 58 men and 10 women have served. It describes a post–Second Bill of Rights presidency with more military/diplomatic power and legislative duties shifted toward worlds/local leaders.
- Page 216 — **Interplanetary Trade Commission**: previously directly read; repeated manifest entry. Infobox says formed 8 December 2085 and dissolved 1 June 2134; body traces origins to the 2079–81 MarsCorp takeover and lists Lionel Halvidar as chair 2115–33. QEM and Planetary Guard funding are central functions.
- Page 217 — **United States of America**: history through future eras, demographics, government, political divisions, economy and military; infobox identifies Washington, D.C. as capital and Dom Terragno as president.
- Page 272 — **Earth**: Earth Commonwealth, 145 states, four protectorates and four freely associated states; 9bn population (2160), San Francisco capital, Victoria Li governor. Prose says formal establishment in 2136, while infobox says 4 July 2137.
- Page 273 — **Political parties in the United States**: marked WIP; discusses party systems, Democratic fragmentation, successor parties and 2155 UPP merger. Its table and prose do not consistently use the same party labels/founding dates.
- Page 277 — **President of the United States (The Second Renaissance)**: redirect to President of the United States.

## Cross-source continuity leads

1. **India Crisis:** timeline gives 2119–26; 22nd Century article's politics list says 2126. This is an internal chronology difference, not reconciled here.
2. **Third Mexican War:** dedicated war infobox begins 2 February 2133; timeline and 22nd Century overview describe the invasion/war phase as beginning in 2134. Preserve the distinction until further sources clarify whether they refer to different phases.
3. **Progress Party:** infobox founding date 17 October 2023 conflicts with prose founding in 2060; Political parties overview uses a 2155 foundation date for the New Progressive Party, apparently referring to the merger successor.
4. **World War III:** start is conventionally 23 November 2051, but source itself records other proposed start dates; end date likewise varies among ceasefire, surrender and treaty.
5. **Dylan J. Price:** infobox and prose disagree on date of birth by several months.
6. **Earth Commonwealth:** prose establishment date 2136 conflicts with infobox date 4 July 2137.
7. **Presidential totals:** presidential article says 58 men + 10 women have served and identifies the 68th president; retain the article's distinction between people and numbered presidential sequence for future cross-checking.

## Other namespace review

- **163 Template pages:** source code and documentation reviewed. Includes general formatting/navigation helpers; officeholder, country, political-party, military-conflict and election infoboxes; flag/country data; references; chart/bar-chart rendering; unit conversion; and Lua-backed helpers. `Template:NationInfo` and `Template:Infobox country` are separate large implementations with overlapping geography-infobox responsibilities. Large implementations include `Template:Bar chart` (69,485 chars), `Template:Infobox officeholder` (49,693 chars), `Template:NationInfo` (55,173 chars) and `Template:Infobox country` (55,235 chars).
- **75 File-description pages:** description Wikitext reviewed only. Many contain only categories; some are empty. Redirects: `File:180px-Gerald Ford.jpg` → `File:Gerald Ford.jpg`; `File:465px-William McKinley 1.png` → `File:William McKinley 1.png`. No underlying image has been visually inspected or credited.
- **16 User pages:** mostly platform/system-account descriptions or transclusions; not treated as narrative canon.
- **13 Category pages:** descriptions and taxonomy/navigation reviewed.
- **5 Board pages:** community discussion-board purposes reviewed.
- **3 MediaWiki pages:** interface/navigation messages reviewed.
- **3 Message Wall pages:** all three captured Wikitext pages are empty.
- **3 Thread pages:** captured welcome/onboarding messages reviewed.
- **1 Template talk page:** contains a political-party infobox implementation copy rather than narrative canon.
- **1 Blog page:** dynamic recent-post list configuration.

## Empty pages and redirects

Fourteen pages have empty Wikitext: 12 File-description pages and two Message Wall pages. Empty file descriptions do not imply the underlying asset is absent. Five redirects occur in this tranche: Main Page → Second Renaissance Wikia; Template:- → Template:Clear; President of the United States (The Second Renaissance) → President of the United States; and the two File redirects above.

## Media status

The page review does not constitute media inspection. The independent media ledger remains authoritative. Visually inspected media remains **0/900**.
