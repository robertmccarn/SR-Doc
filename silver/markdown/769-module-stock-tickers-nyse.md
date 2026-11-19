---
page_id: 769
revision_id: 1042
source_url: https://second-renaissance.fandom.com/wiki/Module%3AStock_tickers/NYSE
raw_sha256: 1a3248d6fdf398b36fb8474abd97c00d42a407d2a00f2f19147593a19d13e65c
---

# Module:Stock tickers/NYSE

## Preserved source

```wikitext
local getArgs = require('Module:Arguments').getArgs
local p = {}

function p.GetURL(frame)
	local args = getArgs(frame)
	return p._GetURL(args)
end
 
function p._GetURL(args)
	local ticker = args[1]
	local exchange = args.exchange
	
	-- By default the exchange will be NYSE
	if not exchange then exchange = 'NYSE' end
	
	-- Get corrected ticker
	ticker = p.FormatTickerURL(ticker)
	
	-- NYSE official URL
	url = 'https://www.nyse.com/quote/' .. exchangeCode[exchange] .. ':' .. ticker
	
	return url
end
 
function p.FormatTickerURL(ticker)
	
	-- Convert to upper case
	ticker = string.upper(ticker)
	
	-- NYSE.com formats for preferred shares / when issued
	-- Example: Input: PRE.PRD, Output: PREpD
	ticker = string.gsub(ticker, "%.PR", "p")
	ticker = string.gsub(ticker, "%.WI", "w")
	
	return ticker
end

-- Get NYSE exchange codes
exchangeCode = {
	['NYSE'] = 'XNYS',
	['AMEX'] = 'XASE',
	['ARCA'] = 'ARCX',
	['NASDAQ'] = 'XNAS'
}

return p
```

## Provenance

Raw source: `bronze/pages/769/1042.wikitext` · revision `1042` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3AStock_tickers/NYSE)
