---
page_id: 591
revision_id: 829
source_url: https://second-renaissance.fandom.com/wiki/Module%3ADetails
raw_sha256: 26de2d85736472dab29c9ee9ed4a4d3e9de726b1a921b1047bdb54f751828d84
---

# Module:Details

## Preserved source

```wikitext
--[-- This module produces a "For more details on this topic" link. It implements
-- the {{details}} template.
--](https://second-renaissance.fandom.com/wiki/--_This_module_produces_a_"For_more_details_on_this_topic"_link._It_implements
--_the_{{details}}_template.
--)

local mHatnote = require('Module:Hatnote')
local mArguments -- lazily initialise

local p = {}

function p.details(frame)
	mArguments = require('Module:Arguments')
	local args = mArguments.getArgs(frame, {parentOnly = true})
	local page = args[1]
	local topic = args[2]
	if not page then
		return mHatnote.makeWikitextError(
			'no page name specified',
			'Template:Details#Errors',
			args.category
		)
	end
	local options = {
		selfref = args.selfref,
	}
	return p._details(page, topic, options)
end

function p._details(page, topic, options)
	page = mHatnote._formatLink(page)
	topic = topic or 'this topic'
	local text = string.format('For more details on %s, see %s.', topic, page)
	options = options or {}
	return mHatnote._hatnote(text, options)
end

return p
```

## Provenance

Raw source: `bronze/pages/591/829.wikitext` · revision `829` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3ADetails)
