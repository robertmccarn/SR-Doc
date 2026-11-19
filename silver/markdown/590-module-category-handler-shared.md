---
page_id: 590
revision_id: 828
source_url: https://second-renaissance.fandom.com/wiki/Module%3ACategory_handler/shared
raw_sha256: 833854cbe53983ce41d461dfc25980311f102bec123f3ed3b4dabd6863ec3a56
---

# Module:Category handler/shared

## Preserved source

```wikitext
-- This module contains shared functions used by [Module:Category handler](586-module-category-handler.md)
-- and its submodules.

local p = {}

function p.matchesBlacklist(page, blacklist)
	for i, pattern in ipairs(blacklist) do
		local match = mw.ustring.match(page, pattern)
		if match then
			return true
		end
	end
	return false
end

function p.getParamMappings(useLoadData)
	local dataPage = 'Module:Namespace detect/data'
	if useLoadData then
		return mw.loadData(dataPage).mappings
	else
		return require(dataPage).mappings
	end
end

function p.getNamespaceParameters(titleObj, mappings)
	-- We don't use title.nsText for the namespace name because it adds
	-- underscores.
	local mappingsKey
	if titleObj.isTalkPage then
		mappingsKey = 'talk'
	else
		mappingsKey = mw.site.namespaces[titleObj.namespace].name
	end
	mappingsKey = mw.ustring.lower(mappingsKey)
	return mappings[mappingsKey] or {}
end

return p
```

## Provenance

Raw source: `bronze/pages/590/828.wikitext` · revision `828` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3ACategory_handler/shared)
