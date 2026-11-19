---
page_id: 746
revision_id: 1018
source_url: https://second-renaissance.fandom.com/wiki/Module%3ASee_also
raw_sha256: 0b9ec06466f874d67698e39f9cef757afc1ef43649e001776130e4e09d36e5f9
---

# Module:See also

## Preserved source

```wikitext
--[-- This module produces a "See also: a, b and c" link. It implements the
-- template {{see also}}.
--](https://second-renaissance.fandom.com/wiki/--_This_module_produces_a_"See_also:_a,_b_and_c"_link._It_implements_the
--_template_{{see_also}}.
--)

local mHatnote = require('Module:Hatnote')
local mTableTools -- lazily initialise
local mArguments -- lazily initialise

local p = {}

function p.seealso(frame)
	mTableTools = require('Module:TableTools')
	mArguments = require('Module:Arguments')
	local args = mArguments.getArgs(frame, {parentOnly = true})
	local pages = {}
	for k, v in pairs(args) do
		if type(k) == 'number' then
			local numstring = tostring(k)
			local display = args['label ' .. numstring]
				or args['l' .. numstring]
			local page = {v, display}
			pages[k] = page
		end
	end
	pages = mTableTools.compressSparseArray(pages)
	if not pages[1] then
		return mHatnote.makeWikitextError(
			'no page names specified',
			'Template:See also#Errors',
			args.category
		)
	end
	local options = {
		altphrase = args.altphrase,
		selfref = args.selfref
	}
	return p._seealso(options, unpack(pages))
end

function p._seealso(options, ...)
	local altphrase = options and options.altphrase or 'See also'
	local links = mHatnote.formatPageTables(...)
	links = mw.text.listToText(links)
	local text = altphrase .. ': ' .. links

	-- Pass options through.
	local hnOptions = {}
	hnOptions.selfref = options.selfref

	return mHatnote._hatnote(text, hnOptions)
end

return p
```

## Provenance

Raw source: `bronze/pages/746/1018.wikitext` · revision `1018` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3ASee_also)
