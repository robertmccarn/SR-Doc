---
page_id: 670
revision_id: 937
source_url: https://second-renaissance.fandom.com/wiki/Module%3AIf_empty
raw_sha256: bfaa17aff4ad352aa81ccf7488013d16beddb9a0366a0e2dd1aee72eeb6e8f77
---

# Module:If empty

## Preserved source

```wikitext
local p = {}

function p.main(frame)
	local args = require('Module:Arguments').getArgs(frame, {wrappers = 'Template:If empty', removeBlanks = false})

	-- For backwards compatibility reasons, the first 8 parameters can be unset instead of being blank,
	-- even though there's really no legitimate use case for this. At some point, this will be removed.
	local lowestNil = math.huge
	for i = 8,1,-1 do
		if args[i] == nil then
			args[i] = ''
			lowestNil = i
		end
	end

	for k,v in ipairs(args) do
		if v ~= '' then
			if lowestNil < k then
				-- If any uses of this template depend on the behavior above, add them to a tracking category.
				-- This is a rather fragile, convoluted, hacky way to do it, but it ensures that this module's output won't be modified
				-- by it.
				frame:extensionTag('ref', '[Category:Instances of Template:If_empty missing arguments](https://second-renaissance.fandom.com/wiki/Category:Instances_of_Template:If_empty_missing_arguments)', {group = 'TrackingCategory'})
				frame:extensionTag('references', '', {group = 'TrackingCategory'})
			end
			return v
		end
	end
end

return p
```

## Provenance

Raw source: `bronze/pages/670/937.wikitext` · revision `937` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3AIf_empty)
