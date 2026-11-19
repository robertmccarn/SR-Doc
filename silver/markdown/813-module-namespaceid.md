---
page_id: 813
revision_id: 1094
source_url: https://second-renaissance.fandom.com/wiki/Module%3ANAMESPACEID
raw_sha256: ead3164305707c40b48d285d85ce128745c08c75e97aad52bd7a71072a7f9243
---

# Module:NAMESPACEID

## Preserved source

```wikitext
-- This module implements {{NAMESPACEID}}.

local p = {}

function p.main(frame)
	local ns = frame:getParent().args[1] or mw.title.getCurrentTitle().namespace
	local nsTable = mw.site.namespaces[ns]
	if nsTable then
		return nsTable.id
	else
		return '<strong class="error">Invalid namespace in ' ..
		'&#123;&#123;[NAMESPACEID](https://second-renaissance.fandom.com/wiki/Template:NAMESPACEID)&#125;&#125;</strong>'
	end
end

return p
```

## Provenance

Raw source: `bronze/pages/813/1094.wikitext` · revision `1094` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3ANAMESPACEID)
