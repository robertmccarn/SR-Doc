---
page_id: 793
revision_id: 1067
source_url: https://second-renaissance.fandom.com/wiki/Module%3AAnchor
raw_sha256: 11ef4009120daef99a5d16dcf30c45cf76eda3dac5bcb69f24aa4a2d198ae784
---

# Module:Anchor

## Preserved source

```wikitext
-- This module implements {{anchor}}.

local getArgs = require('Module:Arguments').getArgs
local tableTools = require('Module:TableTools')

local p = {}

function p.main(frame)
	-- Get the positional arguments from #invoke, remove any nil values,
	-- and pass them to p._main.
	local args = getArgs(frame)
	local argArray = tableTools.compressSparseArray(args)
	return p._main(unpack(argArray))
end

function p._main(...)
	-- Generate the list of anchors.
	local anchors = {...}
	local ret = {}
	for _, anchor in ipairs(anchors) do
		ret[#ret + 1] = '<span id="' .. anchor .. '"></span>'
	end
	return table.concat(ret)
end

return p
```

## Provenance

Raw source: `bronze/pages/793/1067.wikitext` · revision `1067` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3AAnchor)
