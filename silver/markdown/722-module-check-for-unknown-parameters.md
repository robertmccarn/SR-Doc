---
page_id: 722
revision_id: 993
source_url: https://second-renaissance.fandom.com/wiki/Module%3ACheck_for_unknown_parameters
raw_sha256: df75f4f9becfb3828c7c5075b7b2c299cb2ef2f32a392cd270c015f99e75615a
---

# Module:Check for unknown parameters

## Preserved source

```wikitext
-- This module may be used to compare the arguments passed to the parent
-- with a list of arguments, returning a specified result if an argument is
-- not on the list
local p = {}

local function isnotempty(s)
	return s and s:match( '^%s*(.-)%s*$' ) ~= ''
end

function p.check (frame)
	local args = frame.args
	local pargs = frame:getParent().args
	local ignoreblank = isnotempty(frame.args['ignoreblank'])
	local checkpos = isnotempty(frame.args['checkpositional'])
	local knownargs = {}
	local unknown = 'Found _VALUE_, '

	local res = {}
	local regexps = {}
	local comments = {}
	local commentstr = ''
	
	-- create the list of known args, regular expressions, and the return string
	for k, v in pairs(args) do
		if type(k) == 'number' then
			v = mw.ustring.gsub(v, '^%s*(.-)%s*$', '%1')
			knownargs[v] = 1
		else
			if (k == 'unknown' and type(v) == 'string') then
				unknown = v
			elseif (mw.ustring.match(k, '^regexp[%d]*$') and type(v) == 'string') then
				table.insert(regexps, '^' .. v .. '$')
			end
		end
	end

	-- loop over the parent args, and make sure they are on the list
	for k,v in pairs(pargs) do
		if (type(k) == 'string' and knownargs[k] == nil) then
			local knownflag = nil
			for r = 1,#regexps do
				if( mw.ustring.match(k,regexps[r]) ) then
					knownflag = 1
				end
			end
			if( (not knownflag) and ( (not ignoreblank) or (ignoreblank and isnotempty(v)) ) ) then
				k = mw.ustring.gsub(k, '[^%w\-_ ]', '?')
				local r = mw.ustring.gsub(unknown, '_VALUE_', k)
				table.insert(res, r)
				table.insert(comments, '"' .. k .. '"')
			end
		elseif(checkpos and type(k) == 'number' and knownargs[tostring(k)] == nil) then
			if( (not ignoreblank) or (ignoreblank and isnotempty(v)) ) then
				local r = mw.ustring.gsub(unknown, '_VALUE_', k)
				table.insert(res, r)
				table.insert(comments, '"' .. k .. '"')
			end
		end
	end

	if(#comments > 0) then
		commentstr = '<!-- Module:Check for unknown parameters results: ' ..
			table.concat(comments, ', ') .. '-->'
	end
	
	return table.concat(res) .. commentstr
end

return p
```

## Provenance

Raw source: `bronze/pages/722/993.wikitext` · revision `993` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3ACheck_for_unknown_parameters)
