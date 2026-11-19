---
page_id: 810
revision_id: 1091
source_url: https://second-renaissance.fandom.com/wiki/Module%3AData
raw_sha256: bfb2b7e4858611f57ef01875f416e183fdbab62565bc14141dc30bb6f5f0c719
---

# Module:Data

## Preserved source

```wikitext
local mt = {}

function mt.__index(t, k)
	return function(frame)
		local data = mw.loadData(k)
		for _,v in ipairs(frame.args) do
			data = data[v]
		end
		return data
	end
end

return setmetatable({}, mt)
```

## Provenance

Raw source: `bronze/pages/810/1091.wikitext` · revision `1091` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3AData)
