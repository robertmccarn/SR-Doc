---
page_id: 587
revision_id: 825
source_url: https://second-renaissance.fandom.com/wiki/Module%3ACategory_handler/blacklist
raw_sha256: d881f58d9ccb69e610bda93a25a56f993fb5cc698149baee1fb51ac499ce1869
---

# Module:Category handler/blacklist

## Preserved source

```wikitext
-- This module contains the blacklist used by [Module:Category handler](586-module-category-handler.md).
-- Pages that match Lua patterns in this list will not be categorised unless
-- categorisation is explicitly requested.

return {
    '^Main Page$', -- don't categorise the main page.
 
    -- Don't categorise the following pages or their subpages.
    -- "%f[/\0]" matches if the next character is "/" or the end of the string.
    '^Wikipedia:Cascade%-protected items%f[/\0]',
    '^User:UBX%f[/\0]', -- The userbox "template" space.
    '^User talk:UBX%f[/\0]',
 
    -- Don't categorise subpages of these pages, but allow
    -- categorisation of the base page.
    '^Wikipedia:Template messages/.*$',
 
    '/[aA]rchive' -- Don't categorise archives.
}
```

## Provenance

Raw source: `bronze/pages/587/825.wikitext` · revision `825` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3ACategory_handler/blacklist)
