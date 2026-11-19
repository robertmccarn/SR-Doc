---
page_id: 783
revision_id: 1057
source_url: https://second-renaissance.fandom.com/wiki/Module%3AUses_Wikidata
raw_sha256: 334fda96e8aa16b86aa1cda852f17d38714590461ad11a98007ed7c158338898
---

# Module:Uses Wikidata

## Preserved source

```wikitext
local p = {}

function p.usesProperty(frame)
	local parent = frame.getParent(frame)
	local result = ''
	local ii = 1
	while true do
		local p_num = parent.args[ii] or ''
		if p_num ~= '' then
			local label = mw.wikibase.label(p_num) or "NO LABEL"
			result = result .. "<li><b><i>[" .. label .. " <small>(" .. string.upper(p_num) .. ")</small>](https://second-renaissance.fandom.com/wiki/d:Property:"_.._p_num_.._")</i></b> (see [uses](https://second-renaissance.fandom.com/wiki/d:Special:WhatLinksHere/Property:"_.._p_num_.._"))</li>"
			ii = ii + 1
		else break
		end
	end
	return result
end
 
return p
```

## Provenance

Raw source: `bronze/pages/783/1057.wikitext` · revision `1057` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3AUses_Wikidata)
