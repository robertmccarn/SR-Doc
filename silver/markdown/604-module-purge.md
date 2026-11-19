---
page_id: 604
revision_id: 842
source_url: https://second-renaissance.fandom.com/wiki/Module%3APurge
raw_sha256: 68fc0366049fc373d448cfb4f2651721a1ae9944bded34b21f9ea13581908f48
---

# Module:Purge

## Preserved source

```wikitext
-- This module implements [Template:Purge](583-template-purge.md).

local p = {}

local function makeUrlLink(url, display)
	return string.format('[%s %s]', url, display)
end

function p._main(args)
	-- Make the URL
	local url
	do
		local title
		if args.page then
			title = mw.title.new(args.page)
			if not title then
				error(string.format(
					"'%s' is not a valid page name",
					args.page
				), 2)
			end
		else
			title = mw.title.getCurrentTitle()
		end
		if args.anchor then
			title.fragment = args.anchor
		end
		url = title:fullUrl{action = 'purge'}
	end
	
	-- Make the display
	local display = mw.html.create('span')
	display
		:attr('title', 'Purge this page')
		:wikitext(args[1] or 'Purge')
	display = tostring(display)
	
	-- Output the HTML
	local root = mw.html.create('span')
	root
		:addClass('noprint')
		:addClass('plainlinks')
		:addClass('purgelink')
		:wikitext(makeUrlLink(url, display))
	
	return tostring(root)
end

function p.main(frame)
	local args = frame:getParent().args
	return p._main(args)
end

return p
```

## Provenance

Raw source: `bronze/pages/604/842.wikitext` · revision `842` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3APurge)
