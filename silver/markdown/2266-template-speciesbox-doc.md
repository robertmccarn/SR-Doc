---
page_id: 2266
revision_id: 6425
source_url: https://second-renaissance.fandom.com/wiki/Template%3ASpeciesbox/doc
raw_sha256: e58c8ef2be1df214728ad40af2dca1faf502780821b96ea304cd3ecbbc1291b5
---

# Template:Speciesbox/doc

## Preserved source

```wikitext
{{Documentation subpage}}
{{Lua|Module:Autotaxobox}}{{clear}}
{{Automatic_taxobox/doc/nav/boxed}}
<!-- Please place categories where indicated at the bottom of this page and interwikis at Wikidata (see [Wikipedia:Wikidata](https://second-renaissance.fandom.com/wiki/Wikipedia:Wikidata)) -->

This template is used to display a taxobox for a species whose parent's taxonomy is stored in the [taxonomy templates](https://second-renaissance.fandom.com/wiki/Wikipedia:Automated_taxobox_system/taxonomy_templates) of the [automated taxobox system](https://second-renaissance.fandom.com/wiki/WP:Automated_taxobox_system). A requirement is that the name of the species is displayed as a simple binomial (i.e. in the form ''Genus species''). In a few special cases, the name of the species is displayed differently (as for example at ''[Halictus? savenyei](https://second-renaissance.fandom.com/wiki/Halictus?_savenyei)''), when [Template:Automatic taxobox](https://second-renaissance.fandom.com/wiki/Template:Automatic_taxobox) is used.

Using this template effectively requires some familiarity with the automated taxobox system; see the [introduction to the system](https://second-renaissance.fandom.com/wiki/WP:Automated_taxobox_system/intro).

The Speciesbox template does not require or make use of a taxonomy template for the species; it only uses the taxonomy template for the parent taxon, normally the genus.

# Usage
Usage is basically the same as [Template:Automatic taxobox](https://second-renaissance.fandom.com/wiki/Template:Automatic_taxobox) (with one slight variation noted below).

There are five main cases to consider in using this template:
* [[#Simple cases|Simple cases]], where the species is not a hybrid so that the × symbol is not present, the genus name is unique and not duplicated between kingdoms, and the species is not the only one in the genus.
* [[#Hybrid species|Hybrid species names]], where the symbol × is required.
* [[#Genus names duplicated across kingdoms|Species where the genus name is duplicated between kingdoms]], so the taxonomy for the genus must distinguish between kingdoms (e.g. [''Acanthocarpus'' (plant)](https://second-renaissance.fandom.com/wiki/Acanthocarpus_(plant)) and [''Acanthocarpus'' (crab)](https://second-renaissance.fandom.com/wiki/Acanthocarpus_(crab))).
* [[#Monospecific genera|Monospecific genera]], where the species and genus articles are combined, with the article title being the genus name.
* [[#Parent taxon is not the genus|Parent taxon not the genus]], where the parent taxon must be specified as it cannot be deduced from the binomial.

## Simple cases
If the article is about a species whose binomial and genus name are both straightforward (e.g. no rank between the species and its genus, no hybrid symbol, no parenthesized disambiguation in the genus name), then the minimum requirement is to specify the <code>taxon</code> parameter:<ref group=note>If the <code>taxon</code> or <code>genus</code>/<code>species</code> parameters are omitted, the template will try to use the page title as the taxon name. This is deprecated, since it is not self-documenting, so is confusing to editors not familiar with the template, and causes problems if the page is moved.</ref>
* {{para|taxon|name of the species without any formatting (e.g. Quercus major, Lobatus gigas)}}

:(Alternatively you can use the <code>genus</code> and <code>species</code> parameters separately – this is different from {{tl|Automatic taxobox}}:
:* {{para|genus|name of the genus without any formatting (e.g. Quercus, Lobatus)}}
:* {{para|species|specific epithet or name without any formatting (e.g. major, gigas)}}
:This slightly reduces the processing needed.)

If necessary, you can also use:
* {{para|subgenus|link to subgenus}} – deprecated, use {{para|parent}} – [[#Parent taxon is not the genus|see below]]
* {{para|extinct|yes}} if the species (but not the genus) is extinct (if the genus is extinct, this should be marked in its taxonomy template, so will be picked up automatically); <code>true</code> is also accepted.

It's not necessary to include {{tl|italic title}} in the article; this will be added automatically by the Speciesbox template if needed.

For more complicated cases, see the other sections below.

### Simple examples
* Page at the binomial name; displayed taxobox to have the binomial name as its title, e.g. ''[Lobatus gigas](https://second-renaissance.fandom.com/wiki/Lobatus_gigas)''.

:<code><nowiki>{{Speciesbox</nowiki>
:| taxon = Lobatus gigas</code>
:<code>| authority = (Linnaeus, 1758)</code> ''--optional; this is the binomial authority''
:<code>...</code> ''--other optional parameters, e.g. for an image''
:<code><nowiki>}}</nowiki></code>

* Page at the binomial name; displayed taxobox to have the common name as its title, e.g. ''[Allium moly](https://second-renaissance.fandom.com/wiki/Allium_moly)''.

:<code><nowiki>{{Speciesbox</nowiki>
:| name = Golden garlic</code> ''--required if title of taxobox ≠ taxon name''
:<code>| taxon = Allium moly</code>
:<code>| authority = L.</code> ''--optional; this is the binomial authority''
:<code>...</code> ''--other optional parameters, e.g. for an image''
:<code><nowiki>}}</nowiki></code>

* Page at the common name; displayed taxobox to have the same common name as its title, e.g. [Garlic chives](https://second-renaissance.fandom.com/wiki/Garlic_chives).

:<code><nowiki>{{Speciesbox</nowiki>
:| name = Garlic chives</code> ''--optional''
:<code>| taxon = Allium tuberosum</code> ''--essential''
:<code>...</code> ''--other optional parameters, e.g. for an image''
:<code><nowiki>}}</nowiki></code>

## Hybrid species
Care is needed to obtain the correct italicization of hybrid species names in the displayed taxobox since the hybrid sign, ×, should not be italicized, whereas the rest of the binomial should be. The example below shows one way of achieving the desired effect. Assume that the name of the article is "Polygonatum × hybridum", which should display as the title "[''Polygonatum'' × ''hybridum''](https://second-renaissance.fandom.com/wiki/Polygonatum_×_hybridum)".

:<code><nowiki>{{DISPLAYTITLE:''Polygonatum'' × ''hybridum''}}</nowiki>
:<nowiki>{{Speciesbox</nowiki>
:| taxon   = Polygonatum <nowiki>{{hybrid}}</nowiki> hybridum
:| ...
:}}</code>

Notes:
* Use <code><nowiki>{{hybrid}}</nowiki></code> rather than the × character in the value of the <code><nowiki>taxon</nowiki></code> parameter; this ensures that it will not be italicized in the displayed taxobox.
* In the article body, you can either use <code><nowiki>''Polygonatum'' × ''hybridum''</nowiki></code> or <code><nowiki>''Polygonatum {{hybrid}} hybridum''</nowiki></tt> to obtain the correct italicization.

## Genus names duplicated across kingdoms
A special case is where the name of the genus is duplicated in different kingdoms, e.g. ''Acanthocarpus'', which is used for a plant and a crab. The taxonomy template for the plant has to be at [Template:Taxonomy/Acanthocarpus (plant)](https://second-renaissance.fandom.com/wiki/Template:Taxonomy/Acanthocarpus_(plant)) to allow there to be a separate page at "Template:Taxonomy/Acanthocarpus (crab)". Consider the page ''[Acanthocarpus preissii](https://second-renaissance.fandom.com/wiki/Acanthocarpus_preissii)''. The taxobox has to be set up in this way:

:<tt><nowiki>{{Speciesbox</nowiki>
:| genus   = Acanthocarpus (plant)
:| species = preissii
:| ...
:}}</tt>

The corresponding taxonomy template for the genus, [:Template:Taxonomy/Acanthocarpus (plant)](https://second-renaissance.fandom.com/wiki/:Template:Taxonomy/Acanthocarpus_(plant)), contains the line:

:<tt>| link  = Acanthocarpus (plant)|Acanthocarpus</tt>

to ensure that wikilinks are to "Acanthocarpus (plant)" whereas the displayed genus name is "''Acanthocarpus''".

Note that this approach is ''only'' necessary when the disambiguation is needed because genus names are duplicated across kingdoms.<!--Need an example here? Previously used Liriope muscari, but now that there's a jellyfish genus with this name it doesn't work-->

## Monospecific genera
Another special case is where the article is about a genus with only one species. The article will be at the genus name, but the final taxon to be displayed in the taxobox should be the species. An example is ''[Aphyllanthes](https://second-renaissance.fandom.com/wiki/Aphyllanthes)'', with the sole species ''Aphyllanthes monspeliensis''.

:<tt><nowiki>{{Speciesbox</nowiki>
:|taxon = Aphyllanthes monspeliensis
:|parent_authority = L. </tt>''--authority for genus''<tt>
:|authority = L. </tt>''--authority for binomial (i.e. the species)''<tt>
:|... </tt>''--other optional parameters''<tt>
:}}</tt>

The use of the Speciesbox template with the <tt>taxon</tt> parameter set to the species name ensures that the taxobox ends with the binomial name even though the page title is the genus name. The mediawiki software automatically replaces the generated wikilink <nowiki>[Aphyllanthes](https://second-renaissance.fandom.com/wiki/Aphyllanthes)</nowiki> by bold text since it goes to the same page. In this case we want to display the authority for both the species and the genus, since there is no other article. The parameters <tt>parent_authority</tt>, <tt>grandparent_authority</tt>, etc. are the way to display authorities up the classification hierarchy.

## Parent taxon is not the genus
By default, the Speciesbox template uses the genus name as the name of the parent taxon. If this is not the case, because the parent taxon is at a rank between the species and its genus, such as subgenus or botanical section, then use:
*{{para|parent|''parent_taxon''}}

"Template:Taxonomy/''parent_taxon''" must then exist. Conventions for the name of a taxonomy template at a rank between species and genus include:
*"Template:Taxonomy/''Genus'' (''Subgenus'')" for a zoological subgenus, e.g. [Template:Taxonomy/Mus (Coelomys)](https://second-renaissance.fandom.com/wiki/Template:Taxonomy/Mus_(Coelomys))
*"Template:Taxonomy/''Genus'' subg. ''Subgenus''" for a botanical subgenus, e.g. [Template:Taxonomy/Pinus subg. Pinus](https://second-renaissance.fandom.com/wiki/Template:Taxonomy/Pinus_subg._Pinus)
*"Template:Taxonomy/''Genus'' sect. ''Section''" for a botanical section, e.g. [Template:Taxonomy/Pinus sect. Trifoliae](https://second-renaissance.fandom.com/wiki/Template:Taxonomy/Pinus_sect._Trifoliae)

Thus if a zoological subgenus is to be shown, then the taxobox is set up in this way:

:<code><nowiki>{{Speciesbox</nowiki>
:| name = House mouse
:| parent = Mus (Mus)
:| taxon = Mus musculus
:| ...
:}}</code>

# Italicizing the article title
The template can normally determine whether the page title matches the species or the genus in the taxobox, and if so outputs {{tl|italic title}}, so usually it is not necessary to add this template. In a very few cases the automatic italicization will be wrong (e.g. if the article is at the English name and this is the same as the genus name). Automatic italicization can be over-ridden by setting {{para|italic_title|no}}.

# Requirement for correct display
The template will generate a taxobox which will display correctly only if the taxonomy for the genus (or {{para|parent}}) has already been created (i.e. "Template:Taxonomy/''genusname''" or "Template:Taxonomy/''parent''" already exists). If it does not, you will be asked to create it. One way is to look for the "fix" link and open it.

# See also
* An example: [Template:Speciesbox/example](https://second-renaissance.fandom.com/wiki/Template:Speciesbox/example)
* [Template:Taxonbar](https://second-renaissance.fandom.com/wiki/Template:Taxonbar)

# Notes
{{reflist|group=note}}

# Template Data
{{TemplateDataHeader}}
<templatedata>
{
	"params": {
		"taxon": {
			"type": "string",
			"suggested": true
		},
		"authority": {
			"type": "string",
			"suggested": true
		},
		"genus": {
			"type": "string"
		},
		"species": {
			"type": "string"
		},
		"subgenus": {
			"type": "string"
		},
		"parent": {
			"type": "string"
		},
		"extinct": {
			"type": "string"
		},
		"name": {
			"type": "string"
		},
		"parent_authority": {
			"type": "string"
		},
		"image": {
			"type": "wiki-file-name",
			"suggested": true
		},
		"image_caption": {
			"type": "string"
		},
		"status": {
			"type": "string"
		},
		"status_system": {
			"type": "string"
		},
		"status_ref": {
			"type": "string"
		},
		"fossil_range": {
			"type": "string"
		},
		"image_width": {
			"deprecated": "Use image_upright",
			"type": "string"
		},
		"synonyms_ref": {
			"type": "string"
		},
		"synonyms": {
			"type": "string"
		},
		"display_parents": {
			"type": "string"
		},
		"range_map": {
			"type": "wiki-file-name"
		},
		"image2": {
			"type": "wiki-file-name"
		},
		"range_map_caption": {
			"type": "string"
		},
		"image2_caption": {},
		"subdivision_ranks": {
			"type": "string"
		},
		"subdivision": {
			"type": "string"
		},
		"status2": {
			"type": "string"
		},
		"status2_ref": {
			"type": "string"
		},
		"status2_system": {},
		"image_upright": {
			"type": "number"
		},
		"grandparent_authority": {
			"type": "string"
		},
		"image_alt": {
			"type": "string"
		},
		"range_map_upright": {
			"type": "number"
		},
		"range_map_alt": {
			"type": "string"
		},
		"greatgrandparent_authority": {
			"type": "string"
		},
		"range_map_width": {
			"type": "string",
			"deprecated": "Use range_map_upright"
		},
		"range_map2": {
			"type": "wiki-file-name"
		},
		"range_map2_caption": {
			"type": "string"
		},
		"range_map2_alt": {
			"type": "string"
		},
		"range_map2_width": {
			"type": "string",
			"deprecated": "Use range_map2_upright"
		},
		"range_map2_upright": {
			"type": "number"
		},
		"image2_alt": {
			"type": "string"
		},
		"image2_upright": {
			"type": "number"
		},
		"image2_width": {
			"type": "string",
			"deprecated": "Use image2_upright"
		},
		"classification_status": {
			"type": "string"
		},
		"color_as": {
			"type": "string"
		},
	},
	"description": "An infobox for species of organisms where {{tl|Automatic taxobox}} is used at the genus and higher ranks",
	"paramOrder": [
		"color_as",
		"name",
		"taxon",
		"authority",
		"parent",
		"fossil_range",
		"image",
		"image_width",
		"image_upright",
		"image_alt",
		"image_caption",
		"image2",
		"image2_width",
		"image2_upright",
		"image2_alt",
		"image2_caption",
		"status",
		"status_system",
		"status_ref",
		"status2",
		"status2_system",
		"status2_ref",
		"extinct",
		"classification_status",
		"greatgrandparent_authority",
		"grandparent_authority",
		"parent_authority",
		"display_parents",
		"genus",
		"subgenus",
		"species",
		"subdivision_ranks",
		"subdivision",
		"range_map",
		"range_map_width",
		"range_map_upright",
		"range_map_alt",
		"range_map_caption",
		"range_map2",
		"range_map2_width",
		"range_map2_upright",
		"range_map2_alt",
		"range_map2_caption",
		"synonyms",
		"synonyms_ref"
	]
}
</templatedata>

<includeonly>{{#ifeq:{{SUBPAGENAME}}|sandbox | |
<!-- Categories below this line, please; interwikis at Wikidata -->
[Category:Taxobox templates](https://second-renaissance.fandom.com/wiki/Category:Taxobox_templates)
}}</includeonly>
```

## Provenance

Raw source: `bronze/pages/2266/6425.wikitext` · revision `6425` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ASpeciesbox/doc)
