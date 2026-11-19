---
page_id: 341
revision_id: 532
source_url: https://second-renaissance.fandom.com/wiki/Module%3AYesno
raw_sha256: 74d4875983d497dfb575c9913a57e7e76248a91b1e4e49b10196ff9e594f9f66
---

# Module:Yesno

## Preserved source

```wikitext
-- Function allowing for consistent treatment of boolean-like wikitext input.
-- It works similarly to the template {{yesno}}.

return function (val, default)
	-- If your wiki uses non-ascii characters for any of "yes", "no", etc., you
	-- should replace "val:lower()" with "mw.ustring.lower(val)" in the
	-- following line.
	val = type(val) == 'string' and val:lower() or val
	if val == nil then
		return nil
	elseif val == true 
		or val == 'yes'
		or val == 'y'
		or val == 'true'
		or val == 't'
		or tonumber(val) == 1
	then
		return true
	elseif val == false
		or val == 'no'
		or val == 'n'
		or val == 'false'
		or val == 'f'
		or tonumber(val) == 0
	then
		return false
	else
		return default
	end
end
```

## Provenance

Raw source: `bronze/pages/341/532.wikitext` · revision `532` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3AYesno)
