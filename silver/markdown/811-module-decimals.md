---
page_id: 811
revision_id: 1092
source_url: https://second-renaissance.fandom.com/wiki/Module%3ADecimals
raw_sha256: aa839eb1f39f183f7c6872d1892af0ba349991f6c09442aaa515630cbe89fd78
---

# Module:Decimals

## Preserved source

```wikitext
require('Module:No globals')

local p = {}

function p._main(n, d)
	local num = tonumber(n)
	if not num then
		error('Unable to convert "' .. tostring(n) .. '" to a number')
	end
	local decimals = tonumber(d)
	if not decimals then
		error('Unable to convert "' .. tostring(d) .. '" to a number')
	end
	local maxDecimals = 14 - math.floor(math.log10(num)) -- to allow a maximum of 15 significant figures, which is the highest guaranteed correct with doubles
	if decimals > maxDecimals then decimals = maxDecimals end
	local mult = 10^decimals
	num = math.floor(num * mult + 0.5) / mult
	if decimals < 0 then
		return tostring(num)
	else
		return string.format('%.' .. decimals .. 'f', num)
	end
end

function p.main(frame)
	local args, pargs = frame.args, frame:getParent().args
	return p._main(mw.ext.ParserFunctions.expr(args[1] or pargs[1]), mw.ext.ParserFunctions.expr(args[2] or pargs[2]))
end

return p
```

## Provenance

Raw source: `bronze/pages/811/1092.wikitext` · revision `1092` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3ADecimals)
