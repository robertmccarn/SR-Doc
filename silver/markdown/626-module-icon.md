---
page_id: 626
revision_id: 867
source_url: https://second-renaissance.fandom.com/wiki/Module%3AIcon
raw_sha256: 43d837fd5d00cee2aa7fc16c58f6db90a0e90c7b1a52091e2bc0df8c5585c022
---

# Module:Icon

## Preserved source

```wikitext
-- This module implements [Template:Icon](608-template-icon.md).

local data = mw.loadData('Module:Icon/data')

local p = {}

function p._main(args)
	local code = args.class or args[1]
	local iconData
	if code then
		code = code:match('^%s*(.-)%s*$'):lower() -- trim whitespace and put in lower case
		iconData = data[code]
	end
	if not iconData then
		iconData = data._DEFAULT
	end
	return string.format(
		'[%s|link=](https://second-renaissance.fandom.com/wiki/File:%s%s)',
		iconData.image,
		iconData.tooltip and '|' .. iconData.tooltip or '',
		args.size or '16x16px'
	)
end

function p.main(frame)
	local args = {}
	for k, v in pairs(frame:getParent().args) do
		args[k] = v
	end
	return p._main(args)
end

return p
```

## Provenance

Raw source: `bronze/pages/626/867.wikitext` · revision `867` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3AIcon)
