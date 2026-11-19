---
page_id: 751
revision_id: 1023
source_url: https://second-renaissance.fandom.com/wiki/Module%3AToolbar
raw_sha256: ac971cb229b29d526ec7d1ac8425a12d110b0bebfdddab83ba20908b650213c2
---

# Module:Toolbar

## Preserved source

```wikitext
-- This module implements {{toolbar}}.

local mArguments -- Lazily initialise [Module:Arguments](585-module-arguments.md)
local mTableTools = require('Module:TableTools')
local yesno = require('Module:Yesno')

local p = {}

function p.main(frame)
	mArguments = require('Module:Arguments')
	local args = mArguments.getArgs(frame)
	return p._main(args)
end

function p._main(args)
	local toolbarItems = p.makeToolbarItems(args)
	if not toolbarItems then
		-- Return the blank string if no arguments were specified, rather than
		-- returning empty brackets.
		return ''
	elseif yesno(args.span) == false then
		return string.format(
			'(%s)',
			toolbarItems
		)
	else
		return string.format(
			'<span class="plainlinks%s"%s>(%s)</span>',
			type(args.class) == 'string' and ' ' .. args.class or '',
			type(args.style) == 'string' and string.format(' style="%s"', args.style) or '',
			toolbarItems
		)
	end
end

function p.makeToolbarItems(args)
	local nums = mTableTools.numKeys(args)
	local sep = (args.separator or 'pipe') .. '-separator'
	sep = mw.message.new(sep):plain()
	local ret = {}
	for i, v in ipairs(nums) do
		ret[#ret + 1] = args[v]
	end
	if #ret > 0 then
		return table.concat(ret, sep)
	else
		return nil
	end
end

return p
```

## Provenance

Raw source: `bronze/pages/751/1023.wikitext` · revision `1023` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3AToolbar)
