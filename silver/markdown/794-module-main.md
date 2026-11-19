---
page_id: 794
revision_id: 1068
source_url: https://second-renaissance.fandom.com/wiki/Module%3AMain
raw_sha256: b26fe29d83a6b355600debec778d8f8759fb2fc3cf08a6a67709c8c737d8648c
---

# Module:Main

## Preserved source

```wikitext
--[-- This module produces a link to a main article or articles. It implements the
-- template {{main}}.
-- 
-- If the module is used in category or category talk space, it produces "The
-- main article for this category is xxx". Otherwise, it produces
-- "Main article: xxx".
--](https://second-renaissance.fandom.com/wiki/--_This_module_produces_a_link_to_a_main_article_or_articles._It_implements_the
--_template_{{main}}.
--_
--_If_the_module_is_used_in_category_or_category_talk_space,_it_produces_"The
--_main_article_for_this_category_is_xxx"._Otherwise,_it_produces
--_"Main_article:_xxx".
--)

local mHatnote = require('Module:Hatnote')
local mTableTools -- lazily initialise
local mArguments -- lazily initialise

local p = {}

function p.main(frame)
	mTableTools = require('Module:TableTools')
	mArguments = require('Module:Arguments')
	local args = mArguments.getArgs(frame, {parentOnly = true})
	local pages = {}
	for k, v in pairs(args) do
		if type(k) == 'number' then
			local display = args['l' .. tostring(k)]
			local page = {v, display}
			pages[k] = page
		end
	end
	pages = mTableTools.compressSparseArray(pages)
	local options = {
		selfref = args.selfref
	}
	return p._main(options, unpack(pages))
end

function p._main(options, ...)
	-- Get the list of pages. If no first page was specified we use the current
	-- page name.
	local pages = {...}
	local currentTitle = mw.title.getCurrentTitle()
	local firstPageTable = pages[1]
	local firstPage
	if firstPageTable then
		firstPage = firstPageTable[1]
	else
		firstPage = currentTitle.text
		firstPageTable = {firstPage}
		pages[1] = firstPageTable
	end

	-- Find the pagetype.
	local firstPageNs = mHatnote.findNamespaceId(firstPage)
	local pagetype = firstPageNs == 0 and 'article' or 'page'

	-- Make the formatted link text
	local links = mHatnote.formatPageTables(unpack(pages))
	links = mw.text.listToText(links)

	-- Build the text.
	local isPlural = #pages > 1
	local currentNs = currentTitle.namespace
	local isCategoryNamespace = currentNs - currentNs % 2 == 14
	local stringToFormat
	if isCategoryNamespace then
		if isPlural then
			stringToFormat = 'The main %ss for this'
				.. ' [category](https://second-renaissance.fandom.com/wiki/Wikipedia:Categorization) are %s'
		else
			stringToFormat = 'The main %s for this'
				.. ' [category](https://second-renaissance.fandom.com/wiki/Wikipedia:Categorization) is %s'
		end
	else
		if isPlural then
			stringToFormat = 'Main %ss: %s'
		else
			stringToFormat = 'Main %s: %s'
		end
	end
	local text = string.format(stringToFormat, pagetype, links)

	-- Process the options and pass the text to the _rellink function in
	-- [Module:Hatnote](596-module-hatnote.md).
	options = options or {}
	local hnOptions = {
		extraclasses = 'relarticle mainarticle',
		selfref = options.selfref
	}
	return mHatnote._hatnote(text, hnOptions)
end

return p
```

## Provenance

Raw source: `bronze/pages/794/1068.wikitext` · revision `1068` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3AMain)
