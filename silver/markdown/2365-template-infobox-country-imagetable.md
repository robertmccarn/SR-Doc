---
page_id: 2365
revision_id: 6850
source_url: https://second-renaissance.fandom.com/wiki/Template%3AInfobox_country/imagetable
raw_sha256: 343944a56cf2b1983f1c6b6f5f9d0702fb0a234ce7893385004b51130a6acc1d
---

# Template:Infobox country/imagetable

## Preserved source

```wikitext
{{#if:{{both|{{{image1a|}}}{{{image1b|}}}|{{{image2|}}}}}|
    <div style="display:table; width:100%;">
        <div style="display:table-cell; width:58%; vertical-align:middle; padding-left:5px;">
            {{#if:{{{image1a|}}}|<div style="padding-bottom:3px;">{{{image1a|}}}</div>}}{{#if:{{{image1b|}}}|<div style="padding: 2px 0px 3px;">{{{image1b|}}}</div>}}
            <div style="font-size:90%;">{{{caption1|}}}</div>
        </div>
        <div style="display:table-cell; vertical-align:middle; padding: 0px 5px;">
            <div style="padding-bottom:3px;">{{{image2|}}}</div>
            <div style="font-size:90%;">{{{caption2|}}}</div>
        </div>
    </div>
<!--else:-->|
    {{#if:{{{image1a|}}}{{{image1b|}}}|
        <div style="display:table; width:100%;">
            {{#if:{{{image1a|}}}|<div style="display:table-cell; vertical-align:middle; padding: 0px 5px 3px;">{{{image1a|}}}</div>}}{{#if:{{{image1b|}}}|<div style="display:table-cell; vertical-align:middle; padding: 0px 5px 3px 0px;">{{{image1b|}}}</div>}}
        </div>
        <div style="font-size:90%;">{{{caption1}}}</div>
    }}
    {{#if:{{{image2|}}}|
        <div style="padding: 0px 5px;">
            <div style="padding-bottom:3px;">{{{image2|}}}</div>
            <div style="font-size:90%;">{{{caption2}}}</div>
        </div>
    }}
}}<noinclude>
{{documentation|content=
This subtemplate is used to simplify the code of {{tl|infobox country}} and {{tl|infobox former country}}.  It should not be used directly.
}}</noinclude>
```

## Provenance

Raw source: `bronze/pages/2365/6850.wikitext` · revision `6850` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AInfobox_country/imagetable)
