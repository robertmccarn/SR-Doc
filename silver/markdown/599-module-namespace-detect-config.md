---
page_id: 599
revision_id: 837
source_url: https://second-renaissance.fandom.com/wiki/Module%3ANamespace_detect/config
raw_sha256: 3c30c90918ba9f1bba1e2ac54efc1434f1b702bd469725b3f34a97474af65662
---

# Module:Namespace detect/config

## Preserved source

```wikitext
--------------------------------------------------------------------------------
--                    Namespace detect configuration data                     --
--                                                                            --
-- This module stores configuration data for Module:Namespace detect. Here    --
-- you can localise the module to your wiki's language.                       --
--                                                                            --
-- To activate a configuration item, you need to uncomment it. This means     --
-- that you need to remove the text "-- " at the start of the line.           --
--------------------------------------------------------------------------------

local cfg = {} -- Don't edit this line.

--------------------------------------------------------------------------------
--                              Parameter names                               --
-- These configuration items specify custom parameter names. Values added     --
-- here will work in addition to the default English parameter names.         --
-- To add one extra name, you can use this format:                            --
--                                                                            --
-- cfg.foo = 'parameter name'                                                 --
--                                                                            --
-- To add multiple names, you can use this format:                            --
--                                                                            --
-- cfg.foo = {'parameter name 1', 'parameter name 2', 'parameter name 3'}     --
--------------------------------------------------------------------------------

---- This parameter displays content for the main namespace:
-- cfg.main = 'main'

---- This parameter displays in talk namespaces:
-- cfg.talk = 'talk'

---- This parameter displays content for "other" namespaces (namespaces for which
---- parameters have not been specified):
-- cfg.other = 'other'

---- This parameter makes talk pages behave as though they are the corresponding
---- subject namespace. Note that this parameter is used with [Module:Yesno](341-module-yesno.md).
---- Edit that module to change the default values of "yes", "no", etc.
-- cfg.subjectns = 'subjectns'

---- This parameter sets a demonstration namespace:
-- cfg.demospace = 'demospace'

---- This parameter sets a specific page to compare:
cfg.demopage = 'page'

--------------------------------------------------------------------------------
--                           Table configuration                              --
-- These configuration items allow customisation of the "table" function,     --
-- used to generate a table of possible parameters in the module              --
-- documentation.                                                             --
--------------------------------------------------------------------------------

---- The header for the namespace column in the wikitable containing the list of
---- possible subject-space parameters.
-- cfg.wikitableNamespaceHeader = 'Namespace'

---- The header for the wikitable containing the list of possible subject-space
---- parameters.
-- cfg.wikitableAliasesHeader = 'Aliases'

--------------------------------------------------------------------------------
--                        End of configuration data                           --
--------------------------------------------------------------------------------

return cfg -- Don't edit this line.
```

## Provenance

Raw source: `bronze/pages/599/837.wikitext` · revision `837` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3ANamespace_detect/config)
