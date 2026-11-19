---
page_id: 791
revision_id: 1065
source_url: https://second-renaissance.fandom.com/wiki/Module%3ASeparated_entries
raw_sha256: 6bde94cd83445ad94f6f0df20be2abc279b621270675e50a5afac3a62f7b2dc3
---

# Module:Separated entries

## Preserved source

```wikitext
-- This module takes positional parameters as input and concatenates them with
-- an optional separator. The final separator (the "conjunction") can be
-- specified independently, enabling natural-language lists like
-- "foo, bar, baz and qux".

local compressSparseArray = require('Module:TableTools').compressSparseArray
local p = {}

function p._main(args)
	local separator = args.separator
		-- Decode (convert to Unicode) HTML escape sequences, such as "&#32;" for space.
		and mw.text.decode(args.separator) or ''
	local conjunction = args.conjunction and mw.text.decode(args.conjunction) or separator
	-- Discard named parameters.
	local values = compressSparseArray(args)
	return mw.text.listToText(values, separator, conjunction)
end

local function makeInvokeFunction(separator, conjunction)
	return function (frame)
		local args = require('Module:Arguments').getArgs(frame)
		args.separator = separator or args.separator
		args.conjunction = conjunction or args.conjunction
		return p._main(args)
	end
end

p.main = makeInvokeFunction()
p.br = makeInvokeFunction('<br />')
p.comma = makeInvokeFunction(mw.message.new('comma-separator'):plain())

return p
```

## Provenance

Raw source: `bronze/pages/791/1065.wikitext` · revision `1065` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3ASeparated_entries)
