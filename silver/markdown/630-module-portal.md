---
page_id: 630
revision_id: 872
source_url: https://second-renaissance.fandom.com/wiki/Module%3APortal
raw_sha256: da949fb388567b22ead09d10eb38d8e81ce6baa8d366df3206defd263258df2d
---

# Module:Portal

## Preserved source

```wikitext
--[==[ This module is a Lua implementation of the old {{Portal}} template. As of August 2013 it is used on nearly 5,000,000 articles.
-- Please take care when updating it! It outputs two functions: p.portal, which generates a table of portals, and p.image, which
-- produces the image name for an individual portal.

-- The portal image data is kept in submodules of [Module:Portal/images](https://second-renaissance.fandom.com/wiki/Module:Portal/images), listed below:
-- [Module:Portal/images/a](1055-module-portal-images-a.md)		- for portal names beginning with "A".
-- [Module:Portal/images/b](1051-module-portal-images-b.md)		- for portal names beginning with "B".
-- [Module:Portal/images/c](1047-module-portal-images-c.md)		- for portal names beginning with "C".
-- [Module:Portal/images/d](1065-module-portal-images-d.md)		- for portal names beginning with "D".
-- [Module:Portal/images/e](2279-module-portal-images-e.md)		- for portal names beginning with "E".
-- [Module:Portal/images/f](1064-module-portal-images-f.md)		- for portal names beginning with "F".
-- [Module:Portal/images/g](631-module-portal-images-g.md)		- for portal names beginning with "G".
-- [Module:Portal/images/h](1062-module-portal-images-h.md)		- for portal names beginning with "H".
-- [Module:Portal/images/i](1060-module-portal-images-i.md)		- for portal names beginning with "I".
-- [Module:Portal/images/j](1058-module-portal-images-j.md)		- for portal names beginning with "J".
-- [Module:Portal/images/k](1056-module-portal-images-k.md)		- for portal names beginning with "K".
-- [Module:Portal/images/l](1054-module-portal-images-l.md)		- for portal names beginning with "L".
-- [Module:Portal/images/m](1049-module-portal-images-m.md)		- for portal names beginning with "M".
-- [Module:Portal/images/n](632-module-portal-images-n.md)		- for portal names beginning with "N".
-- [Module:Portal/images/o](1045-module-portal-images-o.md)		- for portal names beginning with "O".
-- [Module:Portal/images/p](2280-module-portal-images-p.md)		- for portal names beginning with "P".
-- [Module:Portal/images/q](2281-module-portal-images-q.md)		- for portal names beginning with "Q".
-- [Module:Portal/images/r](1063-module-portal-images-r.md)		- for portal names beginning with "R".
-- [Module:Portal/images/s](1061-module-portal-images-s.md)		- for portal names beginning with "S".
-- [Module:Portal/images/t](1059-module-portal-images-t.md)		- for portal names beginning with "T".
-- [Module:Portal/images/u](606-module-portal-images-u.md)		- for portal names beginning with "U".
-- [Module:Portal/images/v](1057-module-portal-images-v.md)		- for portal names beginning with "V".
-- [Module:Portal/images/w](2282-module-portal-images-w.md)		- for portal names beginning with "W".
-- [Module:Portal/images/x](1053-module-portal-images-x.md)		- for portal names beginning with "X".
-- [Module:Portal/images/y](1050-module-portal-images-y.md)		- for portal names beginning with "Y".
-- [Module:Portal/images/z](1046-module-portal-images-z.md)		- for portal names beginning with "Z".
-- [Module:Portal/images/other](1048-module-portal-images-other.md)	- for portal names beginning with any other letters. This includes numbers,
-- 									  letters with diacritics, and letters in non-Latin alphabets.
-- [Module:Portal/images/aliases](1052-module-portal-images-aliases.md)	- for adding aliases for existing portal names. Use this page for variations
-- 									  in spelling and diacritics, etc., no matter what letter the portal begins with.
--
-- The images data pages are separated by the first letter to reduce server load when images are added, changed, or removed.
-- Previously all the images were on one data page at [Module:Portal/images](https://second-renaissance.fandom.com/wiki/Module:Portal/images), but this had the disadvantage that all
-- 5,000,000 pages using this module needed to be refreshed every time an image was added or removed.
]==]

local p = {}

local function matchImagePage(s)
	-- Finds the appropriate image subpage given a lower-case
	-- portal name plus the first letter of that portal name.
	if type(s) ~= 'string' or #s < 1 then return end
	local firstLetter = mw.ustring.sub(s, 1, 1)
	local imagePage
	if mw.ustring.find(firstLetter, '^[a-z]') then
		imagePage = 'Module:Portal/images/' .. firstLetter
	else
		imagePage = 'Module:Portal/images/other'
	end
	return mw.loadData(imagePage)[s]
end

local function getAlias(s)
	-- Gets an alias from the image alias data page.
	local aliasData = mw.loadData('Module:Portal/images/aliases')
	for portal, aliases in pairs(aliasData) do
		for _, alias in ipairs(aliases) do
			if alias == s then
				return portal
			end
		end
	end
end

local function getImageName(s)
	-- Gets the image name for a given string.
	if type(s) ~= 'string' or #s < 1 then
		return 'Portal-puzzle.svg'
	end
	s = mw.ustring.lower(s)
	return matchImagePage(s) or matchImagePage(getAlias(s)) or 'Portal-puzzle.svg'
end

function p._portal(portals, args)
	-- This function builds the portal box used by the {{portal}} template.
	local root = mw.html.create('div')
		:addClass('noprint portal')
		:addClass(args.left and 'tleft' or 'tright')
		:css('border', 'solid #aaa 1px')
		:css('margin', args.margin or (args.left == 'yes' and '0.5em 1em 0.5em 0') or '0.5em 0 0.5em 1em')
		:newline()

	-- Start the table. This corresponds to the start of the wikitext table in the old [Template:Portal](615-template-portal.md).
	local tableroot = root:tag('table')
		:css('background', '#f9f9f9')
		:css('font-size', '85%')
		:css('line-height', '110%')
		:css('max-width', '175px')
		:css('width', type(args.boxsize) == 'string' and (args.boxsize .. 'px') or nil)

	-- If no portals have been specified, display an error and add the page to a tracking category.
	if not portals[1] then
		tableroot:wikitext('<strong class="error">No portals specified: please specify at least one portal</strong>[Category:Portal templates without a parameter](https://second-renaissance.fandom.com/wiki/Category:Portal_templates_without_a_parameter)')
	end

	-- Display the portals specified in the positional arguments.
	for _, portal in ipairs(portals) do
		local image = getImageName(portal)

		-- Generate the html for the image and the portal name.
		tableroot
			:newline()
			:tag('tr')
				:css('vertical-align', 'middle')
				:tag('td')
					:css('text-align', 'center')
					:wikitext(string.format('[32x28px|alt=Portal icon|class=noviewer](https://second-renaissance.fandom.com/wiki/File:%s)', image))
					:done()
				:tag('td')
					:css('padding', '0 0.2em')
					:css('vertical-align', 'middle')
					:css('font-style', 'italic')
					:css('font-weight', 'bold')
					:wikitext(string.format('[%s%sportal](https://second-renaissance.fandom.com/wiki/Portal:%s)', portal, portal, args['break'] and '<br />' or ' '))
	end
	return tostring(root)
end

function p._image(portals)

	-- Wrapper function to allow getImageName() to be accessed through #invoke.
	return getImageName(portals[1])
end

local function getAllImageTables()
	-- Returns an array containing all image subpages (minus aliases) as loaded by mw.loadData.
	local images = {}
	for i, subpage in ipairs{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'other'} do
		images[i] = mw.loadData('Module:Portal/images/' .. subpage)
	end
	return images
end

function p._displayAll(portals, args)
	-- This function displays all portals that have portal images. This function is for maintenance purposes and should not be used in
	-- articles, for two reasons: 1) there are over 1500 portals with portal images, and 2) the module doesn't record how the portal
	-- names are capitalized, so the portal links may be broken.
	local lang = mw.language.getContentLanguage()
	local count = 1
	for _, imageTable in ipairs(getAllImageTables()) do
		for portal in pairs(imageTable) do
			portals[count] = lang:ucfirst(portal)
			count = count + 1
		end
	end
	return p._portal(portals, args)
end

function p._imageDupes()
	-- This function searches the image subpages to find duplicate images. If duplicate images exist, it is not necessarily a bad thing,
	-- as different portals might just happen to choose the same image. However, this function is helpful in identifying images that
	-- should be moved to a portal alias for ease of maintenance.
	local exists, dupes = {}, {}
	for _, imageTable in ipairs(getAllImageTables()) do
		for portal, image in pairs(imageTable) do
			if not exists[image] then
				exists[image] = portal
			else
				table.insert(dupes, string.format('The image "[%s](https://second-renaissance.fandom.com/wiki/:File:%s)" is used for both portals "%s" and "%s".', image, image, exists[image], portal))
			end
		end
	end
	if #dupes < 1 then
		return 'No duplicate images found.'
	else
		return 'The following duplicate images were found:\n* ' .. table.concat(dupes, '\n* ')
	end
end

local function processPortalArgs(args)
	-- This function processes a table of arguments and returns two tables: an array of portal names for processing by ipairs, and a table of
	-- the named arguments that specify style options, etc. We need to use ipairs because we want to list all the portals in the order
	-- they were passed to the template, but we also want to be able to deal with positional arguments passed explicitly, for example
	-- {{portal|2=Politics}}. The behaviour of ipairs is undefined if nil values are present, so we need to make sure they are all removed.
	args = type(args) == 'table' and args or {}
	local portals = {}
	local namedArgs = {}
	for k, v in pairs(args) do
		if type(k) == 'number' and type(v) == 'string' then -- Make sure we have no non-string portal names.
			table.insert(portals, k)
		elseif type(k) ~= 'number' then
			namedArgs[k] = v
		end
	end
	table.sort(portals)
	for i, v in ipairs(portals) do
		portals[i] = args[v]
	end
	return portals, namedArgs
end

local function makeWrapper(funcName)
	-- Processes external arguments and sends them to the other functions.
	return function (frame)
		-- If called via #invoke, use the args passed into the invoking
		-- template, or the args passed to #invoke if any exist. Otherwise
		-- assume args are being passed directly in from the debug console
		-- or from another Lua module.
		local origArgs
		if type(frame.getParent) == 'function' then
			origArgs = frame:getParent().args
			for k, v in pairs(frame.args) do
				origArgs = frame.args
				break
			end
		else
			origArgs = frame
		end
		-- Trim whitespace and remove blank arguments.
		local args = {}
		for k, v in pairs(origArgs) do
			if type(v) == 'string' then
				v = mw.text.trim(v)
			end
			if v ~= '' then
				args[k] = v
			end
		end
		return p[funcName](processPortalArgs(args)) -- passes two tables to func: an array of portal names, and a table of named arguments.
	end
end

for _, funcName in ipairs{'portal', 'image', 'imageDupes', 'displayAll'} do
	p[funcName] = makeWrapper('_' .. funcName)
end

return p
```

## Provenance

Raw source: `bronze/pages/630/872.wikitext` · revision `872` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3APortal)
