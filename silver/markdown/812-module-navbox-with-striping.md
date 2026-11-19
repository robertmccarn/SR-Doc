---
page_id: 812
revision_id: 1093
source_url: https://second-renaissance.fandom.com/wiki/Module%3ANavbox_with_striping
raw_sha256: 4b039feb477fcc1833a538c75553bc584c7bc70b0a11f644b1a798ca44dfb1c5
---

# Module:Navbox with striping

## Preserved source

```wikitext
-- Proof-of-concept for automatic striping
local p = {}

local Navbox = require('Module:Navbox')

function p.navbox(frame)
	local args = frame:getParent().args

	local listnums = {}
	local listcount = 0
	local t = {}

	for k,v in pairs(args) do
		if type(k) == 'string' and k:match('^list[0-9][0-9]*$') then
			if( v and v ~= '') then
				listcount = listcount + 1
				listnums[listcount] = mw.ustring.gsub(k,'^list([0-9][0-9]*)$', '%1')
			end
		elseif type(k) == 'string' and k:match('^group[0-9][0-9]*$') then
			-- skip for now, processed below
		elseif( v and v ~= '') then
			t[k] = v
		end
    end
	local function lcomp(n1, n2)
		return (tonumber(n1) or 0) < (tonumber(n2) or 0)
	end
	table.sort(listnums, lcomp)
	for i = 1,listcount do
		t['list' .. i] = args['list' .. listnums[i]]
		if( args['group' .. listnums[i]] ~= nil and args['group' .. listnums[i]] ~= '') then
			t['group' .. i] = args['group' .. listnums[i]]
		end
	end
	
	return Navbox._navbox(t)

end

return p
```

## Provenance

Raw source: `bronze/pages/812/1093.wikitext` · revision `1093` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3ANavbox_with_striping)
