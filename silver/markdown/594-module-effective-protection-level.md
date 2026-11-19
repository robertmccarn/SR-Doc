---
page_id: 594
revision_id: 832
source_url: https://second-renaissance.fandom.com/wiki/Module%3AEffective_protection_level
raw_sha256: 423275ef3d7d5eacc44e0b2beb310acbb7d773bb639843bdbeeea8b95acb09a0
---

# Module:Effective protection level

## Preserved source

```wikitext
local p = {}

-- Returns the permission required to perform a given action on a given title.
-- If no title is specified, the title of the page being displayed is used.
function p._main(action, pagename)
	local title
	if type(pagename) == 'table' and pagename.prefixedText then
		title = pagename
	elseif pagename then
		title = mw.title.new(pagename)
	else
		title = mw.title.getCurrentTitle()
	end
	pagename = title.prefixedText
	if action == 'autoreview' then
		local level = mw.getCurrentFrame():callParserFunction('PENDINGCHANGELEVEL', pagename)
		if level == 'review' then
			return 'reviewer'
		elseif level ~= '' then
			return level
		else
			return nil -- not '*'. a page not being PC-protected is distinct from it being PC-protected with anyone able to review. also not '', as that would mean PC-protected but nobody can review
		end
	elseif action ~= 'edit' and action ~= 'move' and action ~= 'create' and action ~= 'upload' then
		error( 'First parameter must be one of edit, move, create, upload, autoreview', 2 )
	end
	if title.namespace == 8 then -- MediaWiki namespace
		return 'sysop'
	elseif title.namespace == 2 and title.isSubpage and ( title.contentModel == 'javascript' or title.contentModel == 'css' ) then -- user JS or CSS page
		return 'sysop'
	end
	local level = title.protectionLevels[action] and title.protectionLevels[action][1]
	if level == 'sysop' or level == 'editprotected' then
		return 'sysop'
	elseif title.cascadingProtection.restrictions[action] and title.cascadingProtection.restrictions[action][1] then -- used by a cascading-protected page
		return 'sysop'
	elseif level == 'templateeditor' then
		return 'templateeditor'
	elseif action == 'move' then
		local blacklistentry = mw.ext.TitleBlacklist.test('edit', pagename) -- Testing action edit is correct, since this is for the source page. The target page name gets tested with action move.
		if blacklistentry and not blacklistentry.params.autoconfirmed then
			return 'templateeditor'
		elseif title.namespace == 6 then
			return 'filemover'
		else
			return 'autoconfirmed'
		end
	end
	local blacklistentry = mw.ext.TitleBlacklist.test(action, pagename)
	if blacklistentry then
		return blacklistentry.params.autoconfirmed and 'autoconfirmed' or 'templateeditor'
	elseif level == 'editsemiprotected' then -- create-semiprotected pages return this for some reason
		return 'autoconfirmed'
	elseif level then
		return level
	elseif action == 'upload' then
		return 'autoconfirmed'
	elseif action == 'create' and title.namespace % 2 == 0 and title.namespace ~= 118 then -- You need to be registered, but not autoconfirmed, to create non-talk pages other than drafts
		return 'user'
	else
		return '*'
	end
end

setmetatable(p, { __index = function(t, k)
	return function(frame)
		return t._main(k, frame.args[1])
	end
end })

return p
```

## Provenance

Raw source: `bronze/pages/594/832.wikitext` · revision `832` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3AEffective_protection_level)
