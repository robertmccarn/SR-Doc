---
page_id: 3739
revision_id: 11716
source_url: https://second-renaissance.fandom.com/wiki/Template%3AStructuredQuote
raw_sha256: 55845b0252390a3214279f9fbb3f0676147c389fd0e3d56f585dbe67758451eb
---

# Template:StructuredQuote

## Preserved source

```wikitext
<blockquote class="pull-quote">
	<div class="pull-quote__text">{{{text|Text...}}}</div>
	<p style="text-align: right"><cite>—{{{speaker|speaker}}}{{#if:{{{receiver|}}}|, to {{{receiver|}}}}}{{#if:{{{attribution|}}}|, {{{attribution|}}}}}{{#if:{{{source|}}}|, {{{source|}}}}}</cite></p>
</blockquote>
<noinclude>
# Description
A template used for displaying Structured Quotes ( ''<nowiki>{{#SQuote:}}</nowiki>'' ). If you want to unlock the full potential of Structured Quotes, please avoid using this template directly, and consider ''<nowiki>{{#SQuote:}}</nowiki>'' markup instead.
See https://community.fandom.com/wiki/Help:Structured_Quotes for extra information about Structured Quotes.

# Syntax
<pre>
{{StructuredQuote
| text   =
| speaker =
| receiver =
| attribution =
| source  =
}}
</pre>

# Samples
{{StructuredQuote
|text=Size matters not. Look at me. Judge me by my size, do you? Hmm? Hmm. And well you should not. (...)
|speaker=[Yoda](https://second-renaissance.fandom.com/wiki/w:c:en.starwars:Yoda)
|receiver=[Luke Skywalker](https://second-renaissance.fandom.com/wiki/w:c:en.starwars:Luke_Skywalker)
|source=[Star Wars: Episode V The Empire Strikes Back](https://second-renaissance.fandom.com/wiki/w:c:en.starwars:Star_Wars:_Episode_V_The_Empire_Strikes_Back)
}}
<pre>
{{StructuredQuote
|text=Size matters not. Look at me. Judge me by my size, do you? Hmm? Hmm. And well you should not. (...)
|speaker=[Yoda](https://second-renaissance.fandom.com/wiki/Yoda)
|receiver=[Luke Skywalker](https://second-renaissance.fandom.com/wiki/Luke_Skywalker)
|source=[Star Wars: Episode V The Empire Strikes Back](https://second-renaissance.fandom.com/wiki/Star_Wars:_Episode_V_The_Empire_Strikes_Back)
}}
</pre>

# TemplateData
<templatedata>
	{
		"params": {
			"text": {
				"label": "Quote text",
				"description": "quote text",
				"type": "content",
				"required": true
			},
			"speaker": {
				"label": "Person(s) quoted",
				"description": "individual(s) who uttered or wrote the quoted words (wikitext links, comma-separated)",
				"type": "content",
				"required": true
			},
			"receiver": {
				"label": "Person(s) to whom the quote was spoken",
				"description": "person the quote was spoken to (wikitext links, comma-separated)",
				"type": "content",
				"suggested": true
			},
			"attribution": {
				"label": "Attribution(s)",
				"description": "attribution (wikitext links, comma-separated)",
				"type": "content",
				"suggested": true
			},
			"source": {
				"label": "Quote source",
				"description": "place where it was spoken (wikitext link)",
				"type": "content",
				"suggested": true
			}
		},
		"format": "block"
	}
</templatedata>
</noinclude>
```

## Provenance

Raw source: `bronze/pages/3739/11716.wikitext` · revision `11716` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AStructuredQuote)
