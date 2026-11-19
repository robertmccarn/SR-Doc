---
page_id: 589
revision_id: 827
source_url: https://second-renaissance.fandom.com/wiki/Module%3ACategory_handler/data
raw_sha256: 21ff34a0be36ab9e0ed5818e7f2c4f49c2401851f7c037ddb2b312eb353e9dcf
---

# Module:Category handler/data

## Preserved source

```wikitext
-- This module assembles data to be passed to [Module:Category handler](586-module-category-handler.md) using
-- mw.loadData. This includes the configuration data and whether the current
-- page matches the title blacklist.

local data = require('Module:Category handler/config')
local mShared = require('Module:Category handler/shared')
local blacklist = require('Module:Category handler/blacklist')
local title = mw.title.getCurrentTitle()

data.currentTitleMatchesBlacklist = mShared.matchesBlacklist(
	title.prefixedText,
	blacklist
)

data.currentTitleNamespaceParameters = mShared.getNamespaceParameters(
	title,
	mShared.getParamMappings()
)

return data
```

## Provenance

Raw source: `bronze/pages/589/827.wikitext` · revision `827` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3ACategory_handler/data)
