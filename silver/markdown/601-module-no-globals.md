---
page_id: 601
revision_id: 839
source_url: https://second-renaissance.fandom.com/wiki/Module%3ANo_globals
raw_sha256: 73e962b920efc313bb23232e779b15eddac8c7dc189ad3bd2333da19ac248c02
---

# Module:No globals

## Preserved source

```wikitext
local mt = getmetatable(_G) or {}
function mt.__index (t, k)
	if k ~= 'arg' then
		error('Tried to read nil global ' .. tostring(k), 2)
	end
	return nil
end
function mt.__newindex(t, k, v)
	if k ~= 'arg' then
		error('Tried to write global ' .. tostring(k), 2)
	end
	rawset(t, k, v)
end
setmetatable(_G, mt)
```

## Provenance

Raw source: `bronze/pages/601/839.wikitext` · revision `839` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3ANo_globals)
