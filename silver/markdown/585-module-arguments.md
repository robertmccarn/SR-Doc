---
page_id: 585
revision_id: 823
source_url: https://second-renaissance.fandom.com/wiki/Module%3AArguments
raw_sha256: 96d41d2789381fdea1efeb8750b56be4509fa1788aaa2f74616e10de42ba9fec
---

# Module:Arguments

## Preserved source

```wikitext
-- This module provides easy processing of arguments passed to Scribunto from
-- #invoke. It is intended for use by other Lua modules, and should not be
-- called from #invoke directly.

local libraryUtil = require('libraryUtil')
local checkType = libraryUtil.checkType

local arguments = {}

-- Generate four different tidyVal functions, so that we don't have to check the
-- options every time we call it.

local function tidyValDefault(key, val)
	if type(val) == 'string' then
		val = val:match('^%s*(.-)%s*$')
		if val == '' then
			return nil
		else
			return val
		end
	else
		return val
	end
end

local function tidyValTrimOnly(key, val)
	if type(val) == 'string' then
		return val:match('^%s*(.-)%s*$')
	else
		return val
	end
end

local function tidyValRemoveBlanksOnly(key, val)
	if type(val) == 'string' then
		if val:find('%S') then
			return val
		else
			return nil
		end
	else
		return val
	end
end

local function tidyValNoChange(key, val)
	return val
end

local function matchesTitle(given, title)
	local tp = type( given )
	return (tp == 'string' or tp == 'number') and mw.title.new( given ).prefixedText == title
end

local translate_mt = { __index = function(t, k) return k end }

function arguments.getArgs(frame, options)
	checkType('getArgs', 1, frame, 'table', true)
	checkType('getArgs', 2, options, 'table', true)
	frame = frame or {}
	options = options or {}

	--[-- Set up argument translation.
	--](https://second-renaissance.fandom.com/wiki/--_Set_up_argument_translation.
	--)
	options.translate = options.translate or {}
	if getmetatable(options.translate) == nil then
		setmetatable(options.translate, translate_mt)
	end
	if options.backtranslate == nil then
		options.backtranslate = {}
		for k,v in pairs(options.translate) do
			options.backtranslate[v] = k
		end
	end
	if options.backtranslate and getmetatable(options.backtranslate) == nil then
		setmetatable(options.backtranslate, {
			__index = function(t, k)
				if options.translate[k] ~= k then
					return nil
				else
					return k
				end
			end
		})
	end

	--[-- Get the argument tables. If we were passed a valid frame object, get the
	-- frame arguments (fargs) and the parent frame arguments (pargs), depending
	-- on the options set and on the parent frame's availability. If we weren't
	-- passed a valid frame object, we are being called from another Lua module
	-- or from the debug console, so assume that we were passed a table of args
	-- directly, and assign it to a new variable (luaArgs).
	--](https://second-renaissance.fandom.com/wiki/--_Get_the_argument_tables._If_we_were_passed_a_valid_frame_object,_get_the
	--_frame_arguments_(fargs)_and_the_parent_frame_arguments_(pargs),_depending
	--_on_the_options_set_and_on_the_parent_frame's_availability._If_we_weren't
	--_passed_a_valid_frame_object,_we_are_being_called_from_another_Lua_module
	--_or_from_the_debug_console,_so_assume_that_we_were_passed_a_table_of_args
	--_directly,_and_assign_it_to_a_new_variable_(luaArgs).
	--)
	local fargs, pargs, luaArgs
	if type(frame.args) == 'table' and type(frame.getParent) == 'function' then
		if options.wrappers then
			--[-- The wrappers option makes Module:Arguments look up arguments in
			-- either the frame argument table or the parent argument table, but
			-- not both. This means that users can use either the](https://second-renaissance.fandom.com/wiki/--_The_wrappers_option_makes_Module:Arguments_look_up_arguments_in
			--_either_the_frame_argument_table_or_the_parent_argument_table,_but
			--_not_both._This_means_that_users_can_use_either_the)
			local parent = frame:getParent()
			if not parent then
				fargs = frame.args
			else
				local title = parent:getTitle():gsub('/sandbox$', '')
				local found = false
				if matchesTitle(options.wrappers, title) then
					found = true
				elseif type(options.wrappers) == 'table' then
					for _,v in pairs(options.wrappers) do
						if matchesTitle(v, title) then
							found = true
							break
						end
					end
				end

				-- We test for false specifically here so that nil (the default) acts like true.
				if found or options.frameOnly == false then
					pargs = parent.args
				end
				if not found or options.parentOnly == false then
					fargs = frame.args
				end
			end
		else
			-- options.wrapper isn't set, so check the other options.
			if not options.parentOnly then
				fargs = frame.args
			end
			if not options.frameOnly then
				local parent = frame:getParent()
				pargs = parent and parent.args or nil
			end
		end
		if options.parentFirst then
			fargs, pargs = pargs, fargs
		end
	else
		luaArgs = frame
	end

	-- Set the order of precedence of the argument tables. If the variables are
	-- nil, nothing will be added to the table, which is how we avoid clashes
	-- between the frame/parent args and the Lua args.
	local argTables = {fargs}
	argTables[#argTables + 1] = pargs
	argTables[#argTables + 1] = luaArgs

	--[-- Generate the tidyVal function. If it has been specified by the user, we
	-- use that; if not, we choose one of four functions depending on the
	-- options chosen. This is so that we don't have to call the options table
	-- every time the function is called.
	--](https://second-renaissance.fandom.com/wiki/--_Generate_the_tidyVal_function._If_it_has_been_specified_by_the_user,_we
	--_use_that;_if_not,_we_choose_one_of_four_functions_depending_on_the
	--_options_chosen._This_is_so_that_we_don't_have_to_call_the_options_table
	--_every_time_the_function_is_called.
	--)
	local tidyVal = options.valueFunc
	if tidyVal then
		if type(tidyVal) ~= 'function' then
			error(
				"bad value assigned to option 'valueFunc'"
					.. '(function expected, got '
					.. type(tidyVal)
					.. ')',
				2
			)
		end
	elseif options.trim ~= false then
		if options.removeBlanks ~= false then
			tidyVal = tidyValDefault
		else
			tidyVal = tidyValTrimOnly
		end
	else
		if options.removeBlanks ~= false then
			tidyVal = tidyValRemoveBlanksOnly
		else
			tidyVal = tidyValNoChange
		end
	end

	--[-- Set up the args, metaArgs and nilArgs tables. args will be the one
	-- accessed from functions, and metaArgs will hold the actual arguments. Nil
	-- arguments are memoized in nilArgs, and the metatable connects all of them
	-- together.
	--](https://second-renaissance.fandom.com/wiki/--_Set_up_the_args,_metaArgs_and_nilArgs_tables._args_will_be_the_one
	--_accessed_from_functions,_and_metaArgs_will_hold_the_actual_arguments._Nil
	--_arguments_are_memoized_in_nilArgs,_and_the_metatable_connects_all_of_them
	--_together.
	--)
	local args, metaArgs, nilArgs, metatable = {}, {}, {}, {}
	setmetatable(args, metatable)

	local function mergeArgs(tables)
		--[-- Accepts multiple tables as input and merges their keys and values
		-- into one table. If a value is already present it is not overwritten;
		-- tables listed earlier have precedence. We are also memoizing nil
		-- values, which can be overwritten if they are 's' (soft).
		--](https://second-renaissance.fandom.com/wiki/--_Accepts_multiple_tables_as_input_and_merges_their_keys_and_values
		--_into_one_table._If_a_value_is_already_present_it_is_not_overwritten;
		--_tables_listed_earlier_have_precedence._We_are_also_memoizing_nil
		--_values,_which_can_be_overwritten_if_they_are_'s'_(soft).
		--)
		for _, t in ipairs(tables) do
			for key, val in pairs(t) do
				if metaArgs[key] == nil and nilArgs[key] ~= 'h' then
					local tidiedVal = tidyVal(key, val)
					if tidiedVal == nil then
						nilArgs[key] = 's'
					else
						metaArgs[key] = tidiedVal
					end
				end
			end
		end
	end

	--[-- Define metatable behaviour. Arguments are memoized in the metaArgs table,
	-- and are only fetched from the argument tables once. Fetching arguments
	-- from the argument tables is the most resource-intensive step in this
	-- module, so we try and avoid it where possible. For this reason, nil
	-- arguments are also memoized, in the nilArgs table. Also, we keep a record
	-- in the metatable of when pairs and ipairs have been called, so we do not
	-- run pairs and ipairs on the argument tables more than once. We also do
	-- not run ipairs on fargs and pargs if pairs has already been run, as all
	-- the arguments will already have been copied over.
	--](https://second-renaissance.fandom.com/wiki/--_Define_metatable_behaviour._Arguments_are_memoized_in_the_metaArgs_table,
	--_and_are_only_fetched_from_the_argument_tables_once._Fetching_arguments
	--_from_the_argument_tables_is_the_most_resource-intensive_step_in_this
	--_module,_so_we_try_and_avoid_it_where_possible._For_this_reason,_nil
	--_arguments_are_also_memoized,_in_the_nilArgs_table._Also,_we_keep_a_record
	--_in_the_metatable_of_when_pairs_and_ipairs_have_been_called,_so_we_do_not
	--_run_pairs_and_ipairs_on_the_argument_tables_more_than_once._We_also_do
	--_not_run_ipairs_on_fargs_and_pargs_if_pairs_has_already_been_run,_as_all
	--_the_arguments_will_already_have_been_copied_over.
	--)

	metatable.__index = function (t, key)
		--[-- Fetches an argument when the args table is indexed. First we check
		-- to see if the value is memoized, and if not we try and fetch it from
		-- the argument tables. When we check memoization, we need to check
		-- metaArgs before nilArgs, as both can be non-nil at the same time.
		-- If the argument is not present in metaArgs, we also check whether
		-- pairs has been run yet. If pairs has already been run, we return nil.
		-- This is because all the arguments will have already been copied into
		-- metaArgs by the mergeArgs function, meaning that any other arguments
		-- must be nil.
		--](https://second-renaissance.fandom.com/wiki/--_Fetches_an_argument_when_the_args_table_is_indexed._First_we_check
		--_to_see_if_the_value_is_memoized,_and_if_not_we_try_and_fetch_it_from
		--_the_argument_tables._When_we_check_memoization,_we_need_to_check
		--_metaArgs_before_nilArgs,_as_both_can_be_non-nil_at_the_same_time.
		--_If_the_argument_is_not_present_in_metaArgs,_we_also_check_whether
		--_pairs_has_been_run_yet._If_pairs_has_already_been_run,_we_return_nil.
		--_This_is_because_all_the_arguments_will_have_already_been_copied_into
		--_metaArgs_by_the_mergeArgs_function,_meaning_that_any_other_arguments
		--_must_be_nil.
		--)
		if type(key) == 'string' then
			key = options.translate[key]
		end
		local val = metaArgs[key]
		if val ~= nil then
			return val
		elseif metatable.donePairs or nilArgs[key] then
			return nil
		end
		for _, argTable in ipairs(argTables) do
			local argTableVal = tidyVal(key, argTable[key])
			if argTableVal ~= nil then
				metaArgs[key] = argTableVal
				return argTableVal
			end
		end
		nilArgs[key] = 'h'
		return nil
	end

	metatable.__newindex = function (t, key, val)
		-- This function is called when a module tries to add a new value to the
		-- args table, or tries to change an existing value.
		if type(key) == 'string' then
			key = options.translate[key]
		end
		if options.readOnly then
			error(
				'could not write to argument table key "'
					.. tostring(key)
					.. '"; the table is read-only',
				2
			)
		elseif options.noOverwrite and args[key] ~= nil then
			error(
				'could not write to argument table key "'
					.. tostring(key)
					.. '"; overwriting existing arguments is not permitted',
				2
			)
		elseif val == nil then
			--[-- If the argument is to be overwritten with nil, we need to erase
			-- the value in metaArgs, so that __index, __pairs and __ipairs do
			-- not use a previous existing value, if present; and we also need
			-- to memoize the nil in nilArgs, so that the value isn't looked
			-- up in the argument tables if it is accessed again.
			--](https://second-renaissance.fandom.com/wiki/--_If_the_argument_is_to_be_overwritten_with_nil,_we_need_to_erase
			--_the_value_in_metaArgs,_so_that___index,___pairs_and___ipairs_do
			--_not_use_a_previous_existing_value,_if_present;_and_we_also_need
			--_to_memoize_the_nil_in_nilArgs,_so_that_the_value_isn't_looked
			--_up_in_the_argument_tables_if_it_is_accessed_again.
			--)
			metaArgs[key] = nil
			nilArgs[key] = 'h'
		else
			metaArgs[key] = val
		end
	end

	local function translatenext(invariant)
		local k, v = next(invariant.t, invariant.k)
		invariant.k = k
		if k == nil then
			return nil
		elseif type(k) ~= 'string' or not options.backtranslate then
			return k, v
		else
			local backtranslate = options.backtranslate[k]
			if backtranslate == nil then
				-- Skip this one. This is a tail call, so this won't cause stack overflow
				return translatenext(invariant)
			else
				return backtranslate, v
			end
		end
	end

	metatable.__pairs = function ()
		-- Called when pairs is run on the args table.
		if not metatable.donePairs then
			mergeArgs(argTables)
			metatable.donePairs = true
		end
		return translatenext, { t = metaArgs }
	end

	local function inext(t, i)
		-- This uses our __index metamethod
		local v = t[i + 1]
		if v ~= nil then
			return i + 1, v
		end
	end

	metatable.__ipairs = function (t)
		-- Called when ipairs is run on the args table.
		return inext, t, 0
	end

	return args
end

return arguments
```

## Provenance

Raw source: `bronze/pages/585/823.wikitext` · revision `823` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3AArguments)
