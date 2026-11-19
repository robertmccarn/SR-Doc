---
page_id: 807
revision_id: 1088
source_url: https://second-renaissance.fandom.com/wiki/Module%3ABreak
raw_sha256: 36d2f0581936d439ea40bacaf806b8626c524149b3a5ee9af904de8ff08894e2
---

# Module:Break

## Preserved source

```wikitext
-- This module implements {{break}}

local p = {}

function p.main( frame )
    local num = frame.args[1] or ''
    num = tonumber( num )
    if not num or num < 1 or math.floor( num ) ~= num or num == math.huge then
        num = 1
    end
    return mw.ustring.rep( '<br />', num )
end

return p
```

## Provenance

Raw source: `bronze/pages/807/1088.wikitext` · revision `1088` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3ABreak)
