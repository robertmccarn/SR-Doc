---
page_id: 775
revision_id: 1048
source_url: https://second-renaissance.fandom.com/wiki/Module%3AURL
raw_sha256: 276d133ba53c288d5254ee8c96939514fff19008fd3b24de6a1dd3e68991ca0d
---

# Module:URL

## Preserved source

```wikitext
--
-- This module implements {{URL}}
--
-- See unit tests at [Module:URL/tests](https://second-renaissance.fandom.com/wiki/Module:URL/tests)

local p = {}
 
function trim(s)
    return (mw.ustring.gsub(s, "^%s*(.-)%s*$", "%1"))
end

function safeUri(s)
    local success, uri = pcall(function()
        return mw.uri.new(s)
    end)
    if success then
        return uri
    end
end

function p._url(url, text)
    url = trim(url or '')
    text = trim(text or '')
    
    if url == '' then
        if text == '' then
            return mw.getCurrentFrame():expandTemplate{ title = 'tlx', args = { 'URL', "''example.com''", "''optional display text''" } }
        else
            return text
        end
    end
    
    -- If the URL contains any unencoded spaces, encode them, because MediaWiki will otherwise interpret a space as the end of the URL.
    url = mw.ustring.gsub(url, '%s', function(s) return mw.uri.encode(s, 'PATH') end)
    
    -- If there is an empty query string or fragment id, remove it as it will cause mw.uri.new to throw an error
    url = mw.ustring.gsub(url, '#$', '')
    url = mw.ustring.gsub(url, '%?$', '')
    
    -- If it's an HTTP[S] URL without the double slash, fix it.
    url = mw.ustring.gsub(url, '^[Hh][Tt][Tt][Pp]([Ss]?):(/?)([^/])', 'http%1://%3')

    -- Handle URLs from Wikidata of the format http&#58;//
    url = mw.ustring.gsub(url, '^[Hh][Tt][Tt][Pp]([Ss]?)&#58;//', 'http%1://')
    
    local uri = safeUri(url)
    
    -- Handle URL's without a protocol and URL's that are protocol-relative, 
    -- e.g. www.example.com/foo or www.example.com:8080/foo, and //www.example.com/foo
    if uri and (not uri.protocol or (uri.protocol and not uri.host)) and url:sub(1, 2) ~= '//' then
        url = 'http://' .. url
        uri = safeUri(url)
    end
    
    if text == '' then
        if uri then
            if uri.path == '/' then uri.path = '' end
            
            local port = ''
            if uri.port then port = ':' .. uri.port end
            
            text = mw.ustring.lower(uri.host or '') .. port .. (uri.relativePath or '')
        else -- URL is badly-formed, so just display whatever was passed in
            text = url
        end
    end

	-- Add <wbr> before _/.-# sequences
	text = mw.ustring.gsub(text,"(/+)","<wbr/>%1")      -- This entry MUST be the first. "<wbr/>" has a "/" in it, you know.
	text = mw.ustring.gsub(text,"(%.+)","<wbr/>%1")
	-- text = mw.ustring.gsub(text,"(%-+)","<wbr/>%1") 	-- DISABLED for now
	text = mw.ustring.gsub(text,"(%#+)","<wbr/>%1")
	text = mw.ustring.gsub(text,"(_+)","<wbr/>%1")
	
    return mw.ustring.format('<span class="url">[%s %s]</span>', url, text)
end

function p.url(frame)
    local templateArgs = frame.args
    local url = templateArgs[1] or ''
    local text = templateArgs[2] or ''
    return p._url(url, text)
end

return p
```

## Provenance

Raw source: `bronze/pages/775/1048.wikitext` · revision `1048` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3AURL)
