---
page_id: 622
revision_id: 863
source_url: https://second-renaissance.fandom.com/wiki/Module%3ACitation/CS1
raw_sha256: e6f8e1062b2d0c12d499bd944da220f85517fe2c1071fb0a20b756833f81b9a6
---

# Module:Citation/CS1

## Preserved source

```wikitext

local z = {
	error_categories = {};		-- for categorizing citations that contain errors
	error_ids = {};
	message_tail = {};
	maintenance_cats = {};		-- for categorizing citations that aren't erroneous per se, but could use a little work
	properties_cats = {};		-- for categorizing citations based on certain properties, language of source for instance
}

--[--------------------------< F O R W A R D   D E C L A R A T I O N S >--------------------------------------](https://second-renaissance.fandom.com/wiki/--------------------------<_F_O_R_W_A_R_D___D_E_C_L_A_R_A_T_I_O_N_S_>--------------------------------------)
local dates, year_date_check	-- functions in Module:Citation/CS1/Date_validation

local cfg = {};					-- table of configuration tables that are defined in Module:Citation/CS1/Configuration
local whitelist = {};			-- table of tables listing valid template parameter names; defined in Module:Citation/CS1/Whitelist

--[--------------------------< I S _ S E T >------------------------------------------------------------------

Returns true if argument is set; false otherwise. Argument is 'set' when it exists (not nil) or when it is not an empty string.
This function is global because it is called from both this module and from Date validation](https://second-renaissance.fandom.com/wiki/--------------------------<_I_S___S_E_T_>------------------------------------------------------------------

Returns_true_if_argument_is_set;_false_otherwise._Argument_is_'set'_when_it_exists_(not_nil)_or_when_it_is_not_an_empty_string.
This_function_is_global_because_it_is_called_from_both_this_module_and_from_Date_validation)
function is_set( var )
	return not (var == nil or var == '');
end

--[--------------------------< F I R S T _ S E T >------------------------------------------------------------

First set variable or nil if none](https://second-renaissance.fandom.com/wiki/--------------------------<_F_I_R_S_T___S_E_T_>------------------------------------------------------------

First_set_variable_or_nil_if_none)

local function first_set(...)
	local list = {...};
	for _, var in pairs(list) do
		if is_set( var ) then
			return var;
		end
	end
end

--[--------------------------< I N _ A R R A Y >--------------------------------------------------------------

Whether needle is in haystack](https://second-renaissance.fandom.com/wiki/--------------------------<_I_N___A_R_R_A_Y_>--------------------------------------------------------------

Whether_needle_is_in_haystack)

local function in_array( needle, haystack )
	if needle == nil then
		return false;
	end
	for n,v in ipairs( haystack ) do
		if v == needle then
			return n;
		end
	end
	return false;
end

--[--------------------------< S U B S T I T U T E >----------------------------------------------------------

Populates numbered arguments in a message string using an argument table.](https://second-renaissance.fandom.com/wiki/--------------------------<_S_U_B_S_T_I_T_U_T_E_>----------------------------------------------------------

Populates_numbered_arguments_in_a_message_string_using_an_argument_table.)

local function substitute( msg, args )
	return args and mw.message.newRawMessage( msg, args ):plain() or msg;
end

--[--------------------------< E R R O R _ C O M M E N T >----------------------------------------------------

Wraps error messages with css markup according to the state of hidden.](https://second-renaissance.fandom.com/wiki/--------------------------<_E_R_R_O_R___C_O_M_M_E_N_T_>----------------------------------------------------

Wraps_error_messages_with_css_markup_according_to_the_state_of_hidden.)
local function error_comment( content, hidden )
	return substitute( hidden and cfg.presentation['hidden-error'] or cfg.presentation['visible-error'], content );
end

--[--------------------------< S E T _ E R R O R >--------------------------------------------------------------

Sets an error condition and returns the appropriate error message.  The actual placement of the error message in the output is
the responsibility of the calling function.](https://second-renaissance.fandom.com/wiki/--------------------------<_S_E_T___E_R_R_O_R_>--------------------------------------------------------------

Sets_an_error_condition_and_returns_the_appropriate_error_message.__The_actual_placement_of_the_error_message_in_the_output_is
the_responsibility_of_the_calling_function.)
local function set_error( error_id, arguments, raw, prefix, suffix )
	local error_state = cfg.error_conditions[ error_id ];
	
	prefix = prefix or "";
	suffix = suffix or "";
	
	if error_state == nil then
		error( cfg.messages['undefined_error'] );
	elseif is_set( error_state.category ) then
		table.insert( z.error_categories, error_state.category );
	end
	
	local message = substitute( error_state.message, arguments );
	
	message = message .. " ([[" .. cfg.messages['help page link'] .. 
		"#" .. error_state.anchor .. "|" ..
		cfg.messages['help page label'] .. "]])";
	
	z.error_ids[ error_id ] = true;
	if in_array( error_id, { 'bare_url_missing_title', 'trans_missing_title' } )
			and z.error_ids['citation_missing_title'] then
		return '', false;
	end
	
	message = table.concat({ prefix, message, suffix });
	
	if raw == true then
		return message, error_state.hidden;
	end		
		
	return error_comment( message, error_state.hidden );
end

--[--------------------------< A D D _ M A I N T _ C A T >------------------------------------------------------

Adds a category to z.maintenance_cats using names from the configuration file with additional text if any.
To prevent duplication, the added_maint_cats table lists the categories by key that have been added to z.maintenance_cats.](https://second-renaissance.fandom.com/wiki/--------------------------<_A_D_D___M_A_I_N_T___C_A_T_>------------------------------------------------------

Adds_a_category_to_z.maintenance_cats_using_names_from_the_configuration_file_with_additional_text_if_any.
To_prevent_duplication,_the_added_maint_cats_table_lists_the_categories_by_key_that_have_been_added_to_z.maintenance_cats.)

local added_maint_cats = {}														-- list of maintenance categories that have been added to z.maintenance_cats
local function add_maint_cat (key, arguments)
	if not added_maint_cats [key] then
		added_maint_cats [key] = true;											-- note that we've added this category
		table.insert( z.maintenance_cats, substitute (cfg.maint_cats [key], arguments));	-- make name then add to table
	end
end

--[--------------------------< A D D _ P R O P _ C A T >--------------------------------------------------------

Adds a category to z.properties_cats using names from the configuration file with additional text if any.](https://second-renaissance.fandom.com/wiki/--------------------------<_A_D_D___P_R_O_P___C_A_T_>--------------------------------------------------------

Adds_a_category_to_z.properties_cats_using_names_from_the_configuration_file_with_additional_text_if_any.)

local added_prop_cats = {}														-- list of property categories that have been added to z.properties_cats
local function add_prop_cat (key, arguments)
	if not added_prop_cats [key] then
		added_prop_cats [key] = true;											-- note that we've added this category
		table.insert( z.properties_cats, substitute (cfg.prop_cats [key], arguments));		-- make name then add to table
	end
end

--[--------------------------< A D D _ V A N C _ E R R O R >----------------------------------------------------

Adds a single Vancouver system error message to the template's output regardless of how many error actually exist.
To prevent duplication, added_vanc_errs is nil until an error message is emitted.](https://second-renaissance.fandom.com/wiki/--------------------------<_A_D_D___V_A_N_C___E_R_R_O_R_>----------------------------------------------------

Adds_a_single_Vancouver_system_error_message_to_the_template's_output_regardless_of_how_many_error_actually_exist.
To_prevent_duplication,_added_vanc_errs_is_nil_until_an_error_message_is_emitted.)

local added_vanc_errs;															-- flag so we only emit one Vancouver error / category
local function add_vanc_error ()
	if not added_vanc_errs then
		added_vanc_errs = true;													-- note that we've added this category
		table.insert( z.message_tail, { set_error( 'vancouver', {}, true ) } );
	end
end

--[--------------------------< C H E C K _ U R L >------------------------------------------------------------

Determines whether a URL string is valid.

At present the only check is whether the string appears to be prefixed with a URI scheme.  It is not determined whether 
the URI scheme is valid or whether the URL is otherwise well formed.](https://second-renaissance.fandom.com/wiki/--------------------------<_C_H_E_C_K___U_R_L_>------------------------------------------------------------

Determines_whether_a_URL_string_is_valid.

At_present_the_only_check_is_whether_the_string_appears_to_be_prefixed_with_a_URI_scheme.__It_is_not_determined_whether_
the_URI_scheme_is_valid_or_whether_the_URL_is_otherwise_well_formed.)

local function check_url( url_str )
	return url_str:sub(1,2) == "//" or url_str:match( "^[^/]*:" ) ~= nil;		-- Protocol-relative or URL scheme
end

--[--------------------------< S A F E _ F O R _ I T A L I C S >----------------------------------------------

Protects a string that will be wrapped in wiki italic markup '' ... ''

Note: We cannot use <i> for italics, as the expected behavior for italics specified by ''...'' in the title is that
they will be inverted (i.e. unitalicized) in the resulting references.  In addition, <i> and '' tend to interact
poorly under Mediawiki's HTML tidy.](https://second-renaissance.fandom.com/wiki/--------------------------<_S_A_F_E___F_O_R___I_T_A_L_I_C_S_>----------------------------------------------

Protects_a_string_that_will_be_wrapped_in_wiki_italic_markup_''_..._''

Note:_We_cannot_use_<i>_for_italics,_as_the_expected_behavior_for_italics_specified_by_''...''_in_the_title_is_that
they_will_be_inverted_(i.e._unitalicized)_in_the_resulting_references.__In_addition,_<i>_and_''_tend_to_interact
poorly_under_Mediawiki's_HTML_tidy.)

local function safe_for_italics( str )
	if not is_set(str) then
		return str;
	else
		if str:sub(1,1) == "'" then str = "<span />" .. str; end
		if str:sub(-1,-1) == "'" then str = str .. "<span />"; end
		
		-- Remove newlines as they break italics.
		return str:gsub( '\n', ' ' );
	end
end

--[--------------------------< S A F E _ F O R _ U R L >------------------------------------------------------

Escape sequences for content that will be used for URL descriptions](https://second-renaissance.fandom.com/wiki/--------------------------<_S_A_F_E___F_O_R___U_R_L_>------------------------------------------------------

Escape_sequences_for_content_that_will_be_used_for_URL_descriptions)

local function safe_for_url( str )
	if str:match( "%[%[.-%]%]" ) ~= nil then 
		table.insert( z.message_tail, { set_error( 'wikilink_in_url', {}, true ) } );
	end
	
	return str:gsub( '[%[%]\n]', {	
		['['] = '&#91;',
		[']'] = '&#93;',
		['\n'] = ' ' } );
end

--[--------------------------< W R A P _ S T Y L E >----------------------------------------------------------

Applies styling to various parameters.  Supplied string is wrapped using a message_list configuration taking one
argument; protects italic styled parameters.  Additional text taken from citation_config.presentation - the reason
this function is similar to but separate from wrap_msg().](https://second-renaissance.fandom.com/wiki/--------------------------<_W_R_A_P___S_T_Y_L_E_>----------------------------------------------------------

Applies_styling_to_various_parameters.__Supplied_string_is_wrapped_using_a_message_list_configuration_taking_one
argument;_protects_italic_styled_parameters.__Additional_text_taken_from_citation_config.presentation_-_the_reason
this_function_is_similar_to_but_separate_from_wrap_msg().)

local function wrap_style (key, str)
	if not is_set( str ) then
		return "";
	elseif in_array( key, { 'italic-title', 'trans-italic-title' } ) then
		str = safe_for_italics( str );
	end

	return substitute( cfg.presentation[key], {str} );
end

--[--------------------------< E X T E R N A L _ L I N K >----------------------------------------------------

Format an external link with error checking](https://second-renaissance.fandom.com/wiki/--------------------------<_E_X_T_E_R_N_A_L___L_I_N_K_>----------------------------------------------------

Format_an_external_link_with_error_checking)

local function external_link( URL, label, source )
	local error_str = "";
	if not is_set( label ) then
		label = URL;
		if is_set( source ) then
			error_str = set_error( 'bare_url_missing_title', { wrap_style ('parameter', source) }, false, " " );
		else
			error( cfg.messages["bare_url_no_origin"] );
		end			
	end
	if not check_url( URL ) then
		error_str = set_error( 'bad_url', {}, false, " " ) .. error_str;
	end
	return table.concat({ "[", URL, " ", safe_for_url( label ), "]", error_str });
end

--[--------------------------< E X T E R N A L _ L I N K _ I D >----------------------------------------------

Formats a wiki style external link](https://second-renaissance.fandom.com/wiki/--------------------------<_E_X_T_E_R_N_A_L___L_I_N_K___I_D_>----------------------------------------------

Formats_a_wiki_style_external_link)

local function external_link_id(options)
	local url_string = options.id;
	if options.encode == true or options.encode == nil then
		url_string = mw.uri.encode( url_string );
	end
	return mw.ustring.format( '[%s](1041-s.md)%s[%s%s%s %s]',
		options.link, options.label, options.separator or "&nbsp;",
		options.prefix, url_string, options.suffix or "",
		mw.text.nowiki(options.id)
	);
end

--[--------------------------< D E P R E C A T E D _ P A R A M E T E R >--------------------------------------

Categorize and emit an error message when the citation contains one or more deprecated parameters.  The function includes the
offending parameter name to the error message.  Only one error message is emitted regardless of the number of deprecated
parameters in the citation.](https://second-renaissance.fandom.com/wiki/--------------------------<_D_E_P_R_E_C_A_T_E_D___P_A_R_A_M_E_T_E_R_>--------------------------------------

Categorize_and_emit_an_error_message_when_the_citation_contains_one_or_more_deprecated_parameters.__The_function_includes_the
offending_parameter_name_to_the_error_message.__Only_one_error_message_is_emitted_regardless_of_the_number_of_deprecated
parameters_in_the_citation.)

local page_in_deprecated_cat;													-- sticky flag so that the category is added only once
local function deprecated_parameter(name)
	if not page_in_deprecated_cat then
		page_in_deprecated_cat = true;											-- note that we've added this category
		table.insert( z.message_tail, { set_error( 'deprecated_params', {name}, true ) } );		-- add error message
	end
end

--[title= or |chapter= parameter's value.
This function will positive kern either single or double quotes:
	"'Unkerned title with leading and trailing single quote marks'"
	" 'Kerned title with leading and trailing single quote marks' " (in real life the kerning isn't as wide as this example)
Double single quotes (italic or bold wikimarkup) are not kerned.

Call this function for chapter titles, for website titles, etc; not for book titles.](https://second-renaissance.fandom.com/wiki/--------------------------<_K_E_R_N___Q_U_O_T_E_S_>--------------------------------------------------------

Apply_kerning_to_open_the_space_between_the_quote_mark_provided_by_the_Module_and_a_leading_or_trailing_quote_mark_contained_in_a)

local function kern_quotes (str)
	local cap='';
	local cap2='';
	
	cap, cap2 = str:match ("^([\"\'])([^\'].+)");								-- match leading double or single quote but not double single quotes
	if is_set (cap) then
		str = substitute (cfg.presentation['kern-left'], {cap, cap2});
	end

	cap, cap2 = str:match ("^(.+[^\'])([\"\'])$")
	if is_set (cap) then
		str = substitute (cfg.presentation['kern-right'], {cap, cap2});
	end
	return str;
end

--[script-title= holds title parameters that are not written in Latin based scripts: Chinese, Japanese, Arabic, Hebrew, etc. These scripts should
not be italicized and may be written right-to-left.  The value supplied by |script-title= is concatenated onto Title after Title has been wrapped
in italic markup.

Regardless of language, all values provided by |script-title= are wrapped in <bdi>...</bdi> tags to isolate rtl languages from the English left to right.

|script-title= provides a unique feature.  The value in |script-title= may be prefixed with a two-character ISO639-1 language code and a colon:
	|script-title=ja:*** *** (where * represents a Japanese character)
Spaces between the two-character code and the colon and the colon and the first script character are allowed:
	|script-title=ja : *** ***
	|script-title=ja: *** ***
	|script-title=ja :*** ***
Spaces preceding the prefix are allowed: |script-title = ja:*** ***

The prefix is checked for validity.  If it is a valid ISO639-1 language code, the lang attribute (lang="ja") is added to the <bdi> tag so that browsers can
know the language the tag contains.  This may help the browser render the script more correctly.  If the prefix is invalid, the lang attribute
is not added.  At this time there is no error message for this condition.

At this writing, only |script-title= is supported.  It is anticipated that additional parameters will be created to use this function.

TODO: error messages when prefix is invalid ISO639-1 code; when script_value has prefix but no script;](https://second-renaissance.fandom.com/wiki/--------------------------<_F_O_R_M_A_T___S_C_R_I_P_T___V_A_L_U_E_>----------------------------------------)

local function format_script_value (script_value)
	local lang='';																-- initialize to empty string
	local name;
	if script_value:match('^%l%l%s*:') then										-- if first 3 non-space characters are script language prefix
		lang = script_value:match('^(%l%l)%s*:%s*%S.*');						-- get the language prefix or nil if there is no script
		if not is_set (lang) then
			return '';															-- script_value was just the prefix so return empty string
		end
																				-- if we get this far we have prefix and script
		name = mw.language.fetchLanguageName( lang, "en" );						-- get language name so that we can use it to categorize
		if is_set (name) then													-- is prefix a proper ISO 639-1 language code?
			script_value = script_value:gsub ('^%l%l%s*:%s*', '');				-- strip prefix from script
																				-- is prefix one of these language codes?
			if in_array (lang, {'ar', 'bg', 'bs', 'dv', 'el', 'fa', 'hy', 'ja', 'ka', 'ko', 'ku', 'he', 'ps', 'ru', 'sd', 'sr', 'th', 'uk', 'ug', 'yi', 'zh'}) then
				add_prop_cat ('script_with_name', {name, lang})
			else
				add_prop_cat ('script')
			end
			lang = ' lang="' .. lang .. '" ';									-- convert prefix into a lang attribute
		else
			lang = '';															-- invalid so set lang to empty string
		end
	end
	script_value = substitute (cfg.presentation['bdi'], {lang, script_value});	-- isolate in case script is rtl

	return script_value;
end

--[title= and |script-title=, this function concatenates those two parameter values after the script value has been 
wrapped in <bdi> tags.](https://second-renaissance.fandom.com/wiki/--------------------------<_S_C_R_I_P_T___C_O_N_C_A_T_E_N_A_T_E_>------------------------------------------

Initially_for)

local function script_concatenate (title, script)
	if is_set (script) then
		script = format_script_value (script);									-- <bdi> tags, lang atribute, categorization, etc; returns empty string on error
		if is_set (script) then
			title = title .. ' ' .. script;										-- concatenate title and script title
		end
	end
	return title;
end


--[--------------------------< W R A P _ M S G >--------------------------------------------------------------

Applies additional message text to various parameter values. Supplied string is wrapped using a message_list
configuration taking one argument.  Supports lower case text for {{citation}} templates.  Additional text taken
from citation_config.messages - the reason this function is similar to but separate from wrap_style().](https://second-renaissance.fandom.com/wiki/--------------------------<_W_R_A_P___M_S_G_>--------------------------------------------------------------

Applies_additional_message_text_to_various_parameter_values._Supplied_string_is_wrapped_using_a_message_list
configuration_taking_one_argument.__Supports_lower_case_text_for_{{citation}}_templates.__Additional_text_taken
from_citation_config.messages_-_the_reason_this_function_is_similar_to_but_separate_from_wrap_style().)

local function wrap_msg (key, str, lower)
	if not is_set( str ) then
		return "";
	end
	if true == lower then
		local msg;
		msg = cfg.messages[key]:lower();										-- set the message to lower case before 
		str = substitute( msg, {str} );											-- including template text
		return str;
	else
		return substitute( cfg.messages[key], {str} );
	end		
end

--[--------------------------< S E L E C T _ O N E >----------------------------------------------------------

Chooses one matching parameter from a list of parameters to consider
Generates an error if more than one match is present.](https://second-renaissance.fandom.com/wiki/--------------------------<_S_E_L_E_C_T___O_N_E_>----------------------------------------------------------

Chooses_one_matching_parameter_from_a_list_of_parameters_to_consider
Generates_an_error_if_more_than_one_match_is_present.)

local function select_one( args, possible, error_condition, index )
	local value = nil;
	local selected = '';
	local error_list = {};
	
	if index ~= nil then index = tostring(index); end
	
	-- Handle special case of "#" replaced by empty string
	if index == '1' then
		for _, v in ipairs( possible ) do
			v = v:gsub( "#", "" );
			if is_set(args[v]) then
				if value ~= nil and selected ~= v then
					table.insert( error_list, v );
				else
					value = args[v];
					selected = v;
				end
			end
		end		
	end
	
	for _, v in ipairs( possible ) do
		if index ~= nil then
			v = v:gsub( "#", index );
		end
		if is_set(args[v]) then
			if value ~= nil and selected ~=  v then
				table.insert( error_list, v );
			else
				value = args[v];
				selected = v;
			end
		end
	end
	
	if #error_list > 0 then
		local error_str = "";
		for _, k in ipairs( error_list ) do
			if error_str ~= "" then error_str = error_str .. cfg.messages['parameter-separator'] end
			error_str = error_str .. wrap_style ('parameter', k);
		end
		if #error_list > 1 then
			error_str = error_str .. cfg.messages['parameter-final-separator'];
		else
			error_str = error_str .. cfg.messages['parameter-pair-separator'];
		end
		error_str = error_str .. wrap_style ('parameter', selected);
		table.insert( z.message_tail, { set_error( error_condition, {error_str}, true ) } );
	end
	
	return value, selected;
end

--[chapter=, |trans-chapter=, and |chapter-url= into a single Chapter meta-
parameter (chapter_url_source used for error messages).](https://second-renaissance.fandom.com/wiki/--------------------------<_F_O_R_M_A_T___C_H_A_P_T_E_R___T_I_T_L_E_>--------------------------------------

Format_the_three_chapter_parameters:)

local function format_chapter_title (chapter, transchapter, chapterurl, chapter_url_source)
	local chapter_error = '';
	
	if not is_set (chapter) then
		chapter = '';															-- just to be safe for concatenation
		if is_set (transchapter) then
			chapter = wrap_style ('trans-quoted-title', transchapter);
			chapter_error = " " .. set_error ('trans_missing_chapter');
		end
		if is_set (chapterurl) then
			chapter = external_link (chapterurl, chapter, chapter_url_source);	-- adds bare_url_missing_title error if appropriate
		end
		return chapter .. chapter_error;
	else																		-- here when chapter is set
		chapter = kern_quotes (chapter);										-- if necessary, separate chapter title's leading and trailing quote marks from Module provided quote marks
		chapter = wrap_style ('quoted-title', chapter);
		if is_set (transchapter) then
			transchapter = wrap_style ('trans-quoted-title', transchapter);
			chapter = chapter .. ' ' .. transchapter;
		end
		if is_set (chapterurl) then
			chapter = external_link (chapterurl, chapter);						-- adds bare_url_missing_title error if appropriate
		end
	end
	return chapter;
end

--[Argument wrapper.  This function provides support for argument 
mapping defined in the configuration file so that multiple names
can be transparently aliased to single internal variable.](https://second-renaissance.fandom.com/wiki/Argument_wrapper.__This_function_provides_support_for_argument_
mapping_defined_in_the_configuration_file_so_that_multiple_names
can_be_transparently_aliased_to_single_internal_variable.)

local function argument_wrapper( args )
	local origin = {};
	
	return setmetatable({
		ORIGIN = function( self, k )
			local dummy = self[k]; --force the variable to be loaded.
			return origin[k];
		end
	},
	{
		__index = function ( tbl, k )
			if origin[k] ~= nil then
				return nil;
			end
			
			local args, list, v = args, cfg.aliases[k];
			
			if type( list ) == 'table' then
				v, origin[k] = select_one( args, list, 'redundant_parameters' );
				if origin[k] == nil then
					origin[k] = ''; -- Empty string, not nil
				end
			elseif list ~= nil then
				v, origin[k] = args[list], list;
			else
				-- maybe let through instead of raising an error?
				-- v, origin[k] = args[k], k;
				error( cfg.messages['unknown_argument_map'] );
			end
			
			-- Empty strings, not nil;
			if v == nil then
				v = cfg.defaults[k] or '';
				origin[k] = '';
			end
			
			tbl = rawset( tbl, k, v );
			return v;
		end,
	});
end

--[Looks for a parameter's name in the whitelist.

Parameters in the whitelist can have three values:
	true - active, supported parameters
	false - deprecated, supported parameters
	nil - unsupported parameters](https://second-renaissance.fandom.com/wiki/Looks_for_a_parameter's_name_in_the_whitelist.

Parameters_in_the_whitelist_can_have_three_values:
	true_-_active,_supported_parameters
	false_-_deprecated,_supported_parameters
	nil_-_unsupported_parameters)

local function validate( name )
	local name = tostring( name );
	local state = whitelist.basic_arguments[ name ];
	
	-- Normal arguments
	if true == state then return true; end		-- valid actively supported parameter
	if false == state then
		deprecated_parameter (name);				-- parameter is deprecated but still supported
		return true;
	end
	
	-- Arguments with numbers in them
	name = name:gsub( "%d+", "#" );				-- replace digit(s) with # (last25 becomes last#
	state = whitelist.numbered_arguments[ name ];
	if true == state then return true; end		-- valid actively supported parameter
	if false == state then
		deprecated_parameter (name);				-- parameter is deprecated but still supported
		return true;
	end
	
	return false;								-- Not supported because not found or name is set to nil
end


-- Formats a wiki style internal link
local function internal_link_id(options)
	return mw.ustring.format( '[%s](1041-s.md)%s[%s](https://second-renaissance.fandom.com/wiki/%s%s%s)',
		options.link, options.label, options.separator or "&nbsp;",
		options.prefix, options.id, options.suffix or "",
		mw.text.nowiki(options.id)
	);
end


--[--------------------------< N O W R A P _ D A T E >--------------------------------------------------------

When date is YYYY-MM-DD format wrap in nowrap span: <span ...>YYYY-MM-DD</span>.  When date is DD MMMM YYYY or is
MMMM DD, YYYY then wrap in nowrap span: <span ...>DD MMMM</span> YYYY or <span ...>MMMM DD,</span> YYYY

DOES NOT yet support MMMM YYYY or any of the date ranges.](https://second-renaissance.fandom.com/wiki/--------------------------<_N_O_W_R_A_P___D_A_T_E_>--------------------------------------------------------

When_date_is_YYYY-MM-DD_format_wrap_in_nowrap_span:_<span_...>YYYY-MM-DD</span>.__When_date_is_DD_MMMM_YYYY_or_is
MMMM_DD,_YYYY_then_wrap_in_nowrap_span:_<span_...>DD_MMMM</span>_YYYY_or_<span_...>MMMM_DD,</span>_YYYY

DOES_NOT_yet_support_MMMM_YYYY_or_any_of_the_date_ranges.)

local function nowrap_date (date)
	local cap='';
	local cap2='';

	if date:match("^%d%d%d%d%-%d%d%-%d%d$") then
		date = substitute (cfg.presentation['nowrap1'], date);
	
	elseif date:match("^%a+%s*%d%d?,%s*%d%d%d%d$") or date:match ("^%d%d?%s*%a+%s*%d%d%d%d$") then
		cap, cap2 = string.match (date, "^(.*)%s+(%d%d%d%d)$");
		date = substitute (cfg.presentation['nowrap2'], {cap, cap2});
	end
	
	return date;
end

--[--------------------------< IS _ V A L I D _ I S X N >-----------------------------------------------------

ISBN-10 and ISSN validator code calculates checksum across all isbn/issn digits including the check digit. ISBN-13 is checked in check_isbn().
If the number is valid the result will be 0. Before calling this function, issbn/issn must be checked for length and stripped of dashes,
spaces and other non-isxn characters.](https://second-renaissance.fandom.com/wiki/--------------------------<_IS___V_A_L_I_D___I_S_X_N_>-----------------------------------------------------

ISBN-10_and_ISSN_validator_code_calculates_checksum_across_all_isbn/issn_digits_including_the_check_digit._ISBN-13_is_checked_in_check_isbn().
If_the_number_is_valid_the_result_will_be_0._Before_calling_this_function,_issbn/issn_must_be_checked_for_length_and_stripped_of_dashes,
spaces_and_other_non-isxn_characters.)

local function is_valid_isxn (isxn_str, len)
	local temp = 0;
	isxn_str = { isxn_str:byte(1, len) };	-- make a table of byte values '0' → 0x30 .. '9'  → 0x39, 'X' → 0x58
	len = len+1;							-- adjust to be a loop counter
	for i, v in ipairs( isxn_str ) do		-- loop through all of the bytes and calculate the checksum
		if v == string.byte( "X" ) then		-- if checkdigit is X (compares the byte value of 'X' which is 0x58)
			temp = temp + 10*( len - i );	-- it represents 10 decimal
		else
			temp = temp + tonumber( string.char(v) )*(len-i);
		end
	end
	return temp % 11 == 0;					-- returns true if calculation result is zero
end


--[--------------------------< IS _ V A L I D _ I S X N  _ 1 3 >----------------------------------------------

ISBN-13 and ISMN validator code calculates checksum across all 13 isbn/ismn digits including the check digit.
If the number is valid, the result will be 0. Before calling this function, isbn-13/ismn must be checked for length
and stripped of dashes, spaces and other non-isxn-13 characters.](https://second-renaissance.fandom.com/wiki/--------------------------<_IS___V_A_L_I_D___I_S_X_N____1_3_>----------------------------------------------

ISBN-13_and_ISMN_validator_code_calculates_checksum_across_all_13_isbn/ismn_digits_including_the_check_digit.
If_the_number_is_valid,_the_result_will_be_0._Before_calling_this_function,_isbn-13/ismn_must_be_checked_for_length
and_stripped_of_dashes,_spaces_and_other_non-isxn-13_characters.)

local function is_valid_isxn_13 (isxn_str)
	local temp=0;
	
	isxn_str = { isxn_str:byte(1, 13) };										-- make a table of byte values '0' → 0x30 .. '9'  → 0x39
	for i, v in ipairs( isxn_str ) do
		temp = temp + (3 - 2*(i % 2)) * tonumber( string.char(v) );				-- multiply odd index digits by 1, even index digits by 3 and sum; includes check digit
	end
	return temp % 10 == 0;														-- sum modulo 10 is zero when isbn-13/ismn is correct
end

--[--------------------------< C H E C K _ I S B N >------------------------------------------------------------

Determines whether an ISBN string is valid](https://second-renaissance.fandom.com/wiki/--------------------------<_C_H_E_C_K___I_S_B_N_>------------------------------------------------------------

Determines_whether_an_ISBN_string_is_valid)

local function check_isbn( isbn_str )
	if nil ~= isbn_str:match("[^%s-0-9X]") then return false; end		-- fail if isbn_str contains anything but digits, hyphens, or the uppercase X
	isbn_str = isbn_str:gsub( "-", "" ):gsub( " ", "" );	-- remove hyphens and spaces
	local len = isbn_str:len();
 
	if len ~= 10 and len ~= 13 then
		return false;
	end

	if len == 10 then
		if isbn_str:match( "^%d*X?$" ) == nil then return false; end
		return is_valid_isxn(isbn_str, 10);
	else
		local temp = 0;
		if isbn_str:match( "^97[89]%d*$" ) == nil then return false; end		-- isbn13 begins with 978 or 979; ismn begins with 979
		return is_valid_isxn_13 (isbn_str);
	end
end

--[--------------------------< C H E C K _ I S M N >------------------------------------------------------------

Determines whether an ISMN string is valid.  Similar to isbn-13, ismn is 13 digits begining 979-0-... and uses the
same check digit calculations.  See http://www.ismn-international.org/download/Web_ISMN_Users_Manual_2008-6.pdf
section 2, pages 9–12.](https://second-renaissance.fandom.com/wiki/--------------------------<_C_H_E_C_K___I_S_M_N_>------------------------------------------------------------

Determines_whether_an_ISMN_string_is_valid.__Similar_to_isbn-13,_ismn_is_13_digits_begining_979-0-..._and_uses_the
same_check_digit_calculations.__See_http://www.ismn-international.org/download/Web_ISMN_Users_Manual_2008-6.pdf
section_2,_pages_9–12.)

local function ismn (id)
	local handler = cfg.id_handlers['ISMN'];
	local text;
	local valid_ismn = true;

	id=id:gsub( "[%s-–]", "" );													-- strip spaces, hyphens, and endashes from the ismn

	if 13 ~= id:len() or id:match( "^9790%d*$" ) == nil then					-- ismn must be 13 digits and begin 9790
		valid_ismn = false;
	else
		valid_ismn=is_valid_isxn_13 (id);										-- validate ismn
	end

--	text = internal_link_id({link = handler.link, label = handler.label,		-- use this (or external version) when there is some place to link to
--		prefix=handler.prefix,id=id,separator=handler.separator, encode=handler.encode})
 
	text="[" .. handler.label .. "](https://second-renaissance.fandom.com/wiki/"_.._handler.link_.._"):" .. handler.separator .. id;		-- because no place to link to yet

	if false == valid_ismn then
		text = text .. ' ' .. set_error( 'bad_ismn' )							-- add an error message if the issn is invalid
	end 
	
	return text;
end

--[[--------------------------< I S S N >----------------------------------------------------------------------

Validate and format an issn.  This code fixes the case where an editor has included an ISSN in the citation but has separated the two groups of four
digits with a space.  When that condition occurred, the resulting link looked like this:

	|issn=0819 4327 gives: [http://www.worldcat.org/issn/0819 4327 0819 4327]  -- can't have spaces in an external link
	
This code now prevents that by inserting a hyphen at the issn midpoint.  It also validates the issn for length and makes sure that the checkdigit agrees
with the calculated value.  Incorrect length (8 digits), characters other than 0-9 and X, or checkdigit / calculated value mismatch will all cause a check issn
error message.  The issn is always displayed with a hyphen, even if the issn was given as a single group of 8 digits.

]]

local function issn(id)
	local issn_copy = id;		-- save a copy of unadulterated issn; use this version for display if issn does not validate
	local handler = cfg.id_handlers['ISSN'];
	local text;
	local valid_issn = true;

	id=id:gsub( "[%s-–]", "" );									-- strip spaces, hyphens, and endashes from the issn

	if 8 ~= id:len() or nil == id:match( "^%d*X?$" ) then		-- validate the issn: 8 digits long, containing only 0-9 or X in the last position
		valid_issn=false;										-- wrong length or improper character
	else
		valid_issn=is_valid_isxn(id, 8);						-- validate issn
	end

	if true == valid_issn then
		id = string.sub( id, 1, 4 ) .. "-" .. string.sub( id, 5 );	-- if valid, display correctly formatted version
	else
		id = issn_copy;											-- if not valid, use the show the invalid issn with error message
	end
	
	text = external_link_id({link = handler.link, label = handler.label,
		prefix=handler.prefix,id=id,separator=handler.separator, encode=handler.encode})
 
	if false == valid_issn then
		text = text .. ' ' .. set_error( 'bad_issn' )			-- add an error message if the issn is invalid
	end 
	
	return text
end

--[asin= with |isbn=.
Error message if not 10 characters, if not isbn10, if mixed and first character is a digit.](https://second-renaissance.fandom.com/wiki/--------------------------<_A_M_A_Z_O_N_>------------------------------------------------------------------

Formats_a_link_to_Amazon.__Do_simple_error_checking:_asin_must_be_mix_of_10_numeric_or_uppercase_alpha
characters.__If_a_mix,_first_character_must_be_uppercase_alpha;_if_all_numeric,_asins_must_be_10-digit
isbn._If_10-digit_isbn,_add_a_maintenance_category_so_a_bot_or_awb_script_can_replace)

local function amazon(id, domain)
	local err_cat = ""

	if not id:match("^[%d%u][%d%u][%d%u][%d%u][%d%u][%d%u][%d%u][%d%u][%d%u][%d%u]$") then
		err_cat =  ' ' .. set_error ('bad_asin');								-- asin is not a mix of 10 uppercase alpha and numeric characters
	else
		if id:match("^%d%d%d%d%d%d%d%d%d[%dX]$") then								-- if 10-digit numeric (or 9 digits with terminal X)
			if check_isbn( id ) then												-- see if asin value is isbn10
				add_maint_cat ('ASIN');
			elseif not is_set (err_cat) then
				err_cat =  ' ' .. set_error ('bad_asin');						-- asin is not isbn10
			end
		elseif not id:match("^%u[%d%u]+$") then
			err_cat =  ' ' .. set_error ('bad_asin');							-- asin doesn't begin with uppercase alpha
		end
	end
	if not is_set(domain) then 
		domain = "com";
	elseif in_array (domain, {'jp', 'uk'}) then			-- Japan, United Kingdom
		domain = "co." .. domain;
	elseif in_array (domain, {'au', 'br', 'mx'}) then	-- Australia, Brazil, Mexico
		domain = "com." .. domain;
	end
	local handler = cfg.id_handlers['ASIN'];
	return external_link_id({link = handler.link,
		label=handler.label , prefix="//www.amazon."..domain.."/dp/",id=id,
		encode=handler.encode, separator = handler.separator}) .. err_cat;
end

--[--------------------------< A R X I V >--------------------------------------------------------------------

See: http://arxiv.org/help/arxiv_identifier

format and error check arXiv identifier.  There are three valid forms of the identifier:
the first form, valid only between date codes 9108 and 0703 is:
	arXiv:<archive>.<class>/<date code><number><version>
where:
	<archive> is a string of alpha characters - may be hyphenated; no other punctuation
	<class> is a string of alpha characters - may be hyphenated; no other punctuation
	<date code> is four digits in the form YYMM where YY is the last two digits of the four-digit year and MM is the month number January = 01
		first digit of YY for this form can only 9 and 0
	<number> is a three-digit number
	<version> is a 1 or more digit number preceded with a lowercase v; no spaces (undocumented)
	
the second form, valid from April 2007 through December 2014 is:
	arXiv:<date code>.<number><version>
where:
	<date code> is four digits in the form YYMM where YY is the last two digits of the four-digit year and MM is the month number January = 01
	<number> is a four-digit number
	<version> is a 1 or more digit number preceded with a lowercase v; no spaces

the third form, valid from January 2015 is:
	arXiv:<date code>.<number><version>
where:
	<date code> and <version> are as defined for 0704-1412
	<number> is a five-digit number](https://second-renaissance.fandom.com/wiki/--------------------------<_A_R_X_I_V_>--------------------------------------------------------------------

See:_http://arxiv.org/help/arxiv_identifier

format_and_error_check_arXiv_identifier.__There_are_three_valid_forms_of_the_identifier:
the_first_form,_valid_only_between_date_codes_9108_and_0703_is:
	arXiv:<archive>.<class>/<date_code><number><version>
where:
	<archive>_is_a_string_of_alpha_characters_-_may_be_hyphenated;_no_other_punctuation
	<class>_is_a_string_of_alpha_characters_-_may_be_hyphenated;_no_other_punctuation
	<date_code>_is_four_digits_in_the_form_YYMM_where_YY_is_the_last_two_digits_of_the_four-digit_year_and_MM_is_the_month_number_January_=_01
		first_digit_of_YY_for_this_form_can_only_9_and_0
	<number>_is_a_three-digit_number
	<version>_is_a_1_or_more_digit_number_preceded_with_a_lowercase_v;_no_spaces_(undocumented)
	
the_second_form,_valid_from_April_2007_through_December_2014_is:
	arXiv:<date_code>.<number><version>
where:
	<date_code>_is_four_digits_in_the_form_YYMM_where_YY_is_the_last_two_digits_of_the_four-digit_year_and_MM_is_the_month_number_January_=_01
	<number>_is_a_four-digit_number
	<version>_is_a_1_or_more_digit_number_preceded_with_a_lowercase_v;_no_spaces

the_third_form,_valid_from_January_2015_is:
	arXiv:<date_code>.<number><version>
where:
	<date_code>_and_<version>_are_as_defined_for_0704-1412
	<number>_is_a_five-digit_number)

local function arxiv (id, class)
	local handler = cfg.id_handlers['ARXIV'];
	local year, month, version;
	local err_cat = '';
	local text;
	
	if id:match("^%a[%a%.%-]+/[90]%d[01]%d%d%d%d$") or id:match("^%a[%a%.%-]+/[90]%d[01]%d%d%d%dv%d+$") then	-- test for the 9108-0703 format w/ & w/o version
		year, month = id:match("^%a[%a%.%-]+/([90]%d)([01]%d)%d%d%d[v%d]*$");
		year = tonumber(year);
		month = tonumber(month);
		if ((not (90 < year or 8 > year)) or (1 > month or 12 < month)) or		-- if invalid year or invalid month
			((91 == year and 7 > month) or (7 == year and 3 < month)) then		-- if years ok, are starting and ending months ok?
				err_cat = ' ' .. set_error( 'bad_arxiv' );						-- set error message
		end
	elseif id:match("^%d%d[01]%d%.%d%d%d%d$") or id:match("^%d%d[01]%d%.%d%d%d%dv%d+$") then	-- test for the 0704-1412 w/ & w/o version
		year, month = id:match("^(%d%d)([01]%d)%.%d%d%d%d[v%d]*$");
		year = tonumber(year);
		month = tonumber(month);
		if ((7 > year) or (14 < year) or (1 > month or 12 < month)) or			-- is year invalid or is month invalid? (doesn't test for future years)
			((7 == year) and (4 > month)) then --or									-- when year is 07, is month invalid (before April)?
				err_cat = ' ' .. set_error( 'bad_arxiv' );						-- set error message
		end
	elseif id:match("^%d%d[01]%d%.%d%d%d%d%d$") or id:match("^%d%d[01]%d%.%d%d%d%d%dv%d+$") then	-- test for the 1501- format w/ & w/o version
		year, month = id:match("^(%d%d)([01]%d)%.%d%d%d%d%d[v%d]*$");
		year = tonumber(year);
		month = tonumber(month);
		if ((15 > year) or (1 > month or 12 < month)) then						-- is year invalid or is month invalid? (doesn't test for future years)
			err_cat = ' ' .. set_error( 'bad_arxiv' );							-- set error message
		end
	else
		err_cat = ' ' .. set_error( 'bad_arxiv' );								-- arXiv id doesn't match any format
	end

	text = external_link_id({link = handler.link, label = handler.label,
			prefix=handler.prefix,id=id,separator=handler.separator, encode=handler.encode}) .. err_cat;

	if is_set (class) then
		class = ' [' .. '//arxiv.org/archive/' .. class .. ' ' .. class .. '](https://second-renaissance.fandom.com/wiki/'_.._'//arxiv.org/archive/'_.._class_.._'_'_.._class_.._')';	-- external link within square brackets, not wikilink
	else
		class = '';																-- empty string for concatenation
	end
	
	return text .. class;
end

--[lccn normalization (http://www.loc.gov/marc/lccn-namespace.html](https://second-renaissance.fandom.com/wiki/lccn_normalization_(http://www.loc.gov/marc/lccn-namespace.html)

local function normalize_lccn (lccn)
	lccn = lccn:gsub ("%s", "");									-- 1. strip whitespace

	if nil ~= string.find (lccn,'/') then
		lccn = lccn:match ("(.-)/");								-- 2. remove forward slash and all character to the right of it
	end

	local prefix
	local suffix
	prefix, suffix = lccn:match ("(.+)%-(.+)");						-- 3.a remove hyphen by splitting the string into prefix and suffix

	if nil ~= suffix then											-- if there was a hyphen
		suffix=string.rep("0", 6-string.len (suffix)) .. suffix;	-- 3.b.2 left fill the suffix with 0s if suffix length less than 6
		lccn=prefix..suffix;										-- reassemble the lccn
	end
	
	return lccn;
	end

--[[
Format LCCN link and do simple error checking.  LCCN is a character string 8-12 characters long. The length of the LCCN dictates the character type of the first 1-3 characters; the
rightmost eight are always digits. http://info-uri.info/registry/OAIHandler?verb=GetRecord&metadataPrefix=reg&identifier=info:lccn/

length = 8 then all digits
length = 9 then lccn[1] is lower case alpha
length = 10 then lccn[1] and lccn[2] are both lower case alpha or both digits
length = 11 then lccn[1] is lower case alpha, lccn[2] and lccn[3] are both lower case alpha or both digits
length = 12 then lccn[1] and lccn[2] are both lower case alpha

]]

local function lccn(lccn)
	local handler = cfg.id_handlers['LCCN'];
	local err_cat =  '';								-- presume that LCCN is valid
	local id = lccn;									-- local copy of the lccn

	id = normalize_lccn (id);							-- get canonical form (no whitespace, hyphens, forward slashes)
	local len = id:len();								-- get the length of the lccn

	if 8 == len then
		if id:match("[^%d]") then						-- if LCCN has anything but digits (nil if only digits)
			err_cat = ' ' .. set_error( 'bad_lccn' );	-- set an error message
		end
	elseif 9 == len then								-- LCCN should be adddddddd
		if nil == id:match("%l%d%d%d%d%d%d%d%d") then			-- does it match our pattern?
			err_cat = ' ' .. set_error( 'bad_lccn' );	-- set an error message
		end
	elseif 10 == len then								-- LCCN should be aadddddddd or dddddddddd
		if id:match("[^%d]") then							-- if LCCN has anything but digits (nil if only digits) ...
			if nil == id:match("^%l%l%d%d%d%d%d%d%d%d") then	-- ... see if it matches our pattern
				err_cat = ' ' .. set_error( 'bad_lccn' );	-- no match, set an error message
			end
		end
	elseif 11 == len then								-- LCCN should be aaadddddddd or adddddddddd
		if not (id:match("^%l%l%l%d%d%d%d%d%d%d%d") or id:match("^%l%d%d%d%d%d%d%d%d%d%d")) then	-- see if it matches one of our patterns
			err_cat = ' ' .. set_error( 'bad_lccn' );	-- no match, set an error message
		end
	elseif 12 == len then								-- LCCN should be aadddddddddd
		if not id:match("^%l%l%d%d%d%d%d%d%d%d%d%d") then	-- see if it matches our pattern
			err_cat = ' ' .. set_error( 'bad_lccn' );	-- no match, set an error message
		end
	else
		err_cat = ' ' .. set_error( 'bad_lccn' );		-- wrong length, set an error message
	end

	if not is_set (err_cat) and nil ~= lccn:find ('%s') then
		err_cat = ' ' .. set_error( 'bad_lccn' );		-- lccn contains a space, set an error message
	end

	return external_link_id({link = handler.link, label = handler.label,
			prefix=handler.prefix,id=lccn,separator=handler.separator, encode=handler.encode}) .. err_cat;
end

--[Format PMID and do simple error checking.  PMIDs are sequential numbers beginning at 1 and counting up.  This code checks the PMID to see that it
contains only digits and is less than test_limit; the value in local variable test_limit will need to be updated periodically as more PMIDs are issued.](https://second-renaissance.fandom.com/wiki/Format_PMID_and_do_simple_error_checking.__PMIDs_are_sequential_numbers_beginning_at_1_and_counting_up.__This_code_checks_the_PMID_to_see_that_it
contains_only_digits_and_is_less_than_test_limit;_the_value_in_local_variable_test_limit_will_need_to_be_updated_periodically_as_more_PMIDs_are_issued.)

local function pmid(id)
	local test_limit = 30000000;						-- update this value as PMIDs approach
	local handler = cfg.id_handlers['PMID'];
	local err_cat =  '';								-- presume that PMID is valid
	
	if id:match("[^%d]") then							-- if PMID has anything but digits
		err_cat = ' ' .. set_error( 'bad_pmid' );		-- set an error message
	else												-- PMID is only digits
		local id_num = tonumber(id);					-- convert id to a number for range testing
		if 1 > id_num or test_limit < id_num then		-- if PMID is outside test limit boundaries
			err_cat = ' ' .. set_error( 'bad_pmid' );	-- set an error message
		end
	end
	
	return external_link_id({link = handler.link, label = handler.label,
			prefix=handler.prefix,id=id,separator=handler.separator, encode=handler.encode}) .. err_cat;
end

--[embargo= against today's date.  If embargo date is
in the future, returns the content of |embargo=; otherwise, returns and empty string because the embargo has expired or because
|embargo= was not set in this cite.](https://second-renaissance.fandom.com/wiki/--------------------------<_I_S___E_M_B_A_R_G_O_E_D_>------------------------------------------------------

Determines_if_a_PMC_identifier's_online_version_is_embargoed._Compares_the_date_in)

local function is_embargoed (embargo)
	if is_set (embargo) then
		local lang = mw.getContentLanguage();
		local good1, embargo_date, good2, todays_date;
		good1, embargo_date = pcall( lang.formatDate, lang, 'U', embargo );
		good2, todays_date = pcall( lang.formatDate, lang, 'U' );
	
		if good1 and good2 then													-- if embargo date and today's date are good dates
			if tonumber( embargo_date ) >= tonumber( todays_date ) then			-- is embargo date is in the future?
				return embargo;													-- still embargoed
			else
				add_maint_cat ('embargo')
				return '';														-- unset because embargo has expired
			end
		end
	end
	return '';																	-- |embargo= not set return empty string
end

--[[--------------------------< P M C >------------------------------------------------------------------------

Format a PMC, do simple error checking, and check for embargoed articles.

The embargo parameter takes a date for a value. If the embargo date is in the future the PMC identifier will not
be linked to the article.  If the embargo date is today or in the past, or if it is empty or omitted, then the
PMC identifier is linked to the article through the link at cfg.id_handlers['PMC'].prefix.

PMC embargo date testing is done in function is_embargoed () which is called earlier because when the citation
has |pmc=<value> but does not have a |url= then |title= is linked with the PMC link.  Function is_embargoed ()
returns the embargo date if the PMC article is still embargoed, otherwise it returns an empty string.

PMCs are sequential numbers beginning at 1 and counting up.  This code checks the PMC to see that it contains only digits and is less
than test_limit; the value in local variable test_limit will need to be updated periodically as more PMCs are issued.

]]

local function pmc(id, embargo)
	local test_limit = 5000000;							-- update this value as PMCs approach
	local handler = cfg.id_handlers['PMC'];
	local err_cat =  '';								-- presume that PMC is valid
	
	local text;

	if id:match("[^%d]") then							-- if PMC has anything but digits
		err_cat = ' ' .. set_error( 'bad_pmc' );			-- set an error message
	else												-- PMC is only digits
		local id_num = tonumber(id);					-- convert id to a number for range testing
		if 1 > id_num or test_limit < id_num then		-- if PMC is outside test limit boundaries
			err_cat = ' ' .. set_error( 'bad_pmc' );		-- set an error message
		end
	end
	
	if is_set (embargo) then													-- is PMC is still embargoed?
		text="[" .. handler.label .. "](https://second-renaissance.fandom.com/wiki/"_.._handler.link_.._"):" .. handler.separator .. id .. err_cat;	-- still embargoed so no external link
	else
		text = external_link_id({link = handler.link, label = handler.label,			-- no embargo date or embargo has expired, ok to link to article
			prefix=handler.prefix,id=id,separator=handler.separator, encode=handler.encode}) .. err_cat;
	end
	return text;
end

-- Formats a DOI and checks for DOI errors.

-- DOI names contain two parts: prefix and suffix separated by a forward slash.
--  Prefix: directory indicator '10.' followed by a registrant code
--  Suffix: character string of any length chosen by the registrant

-- This function checks a DOI name for: prefix/suffix.  If the doi name contains spaces or endashes,
-- or, if it ends with a period or a comma, this function will emit a bad_doi error message.

-- DOI names are case-insensitive and can incorporate any printable Unicode characters so the test for spaces, endash,
-- and terminal punctuation may not be technically correct but it appears, that in practice these characters are rarely if ever used in doi names.

local function doi(id, inactive)
	local cat = ""
	local handler = cfg.id_handlers['DOI'];
	
	local text;
	if is_set(inactive) then
		local inactive_year = inactive:match("%d%d%d%d") or '';		-- try to get the year portion from the inactive date
		text = "[" .. handler.label .. "](https://second-renaissance.fandom.com/wiki/"_.._handler.link_.._"):" .. id;
		if is_set(inactive_year) then
			table.insert( z.error_categories, "Pages with DOIs inactive since " .. inactive_year );
		else
			table.insert( z.error_categories, "Pages with inactive DOIs" );	-- when inactive doesn't contain a recognizable year
		end
		inactive = " (" .. cfg.messages['inactive'] .. " " .. inactive .. ")" 
	else 
		text = external_link_id({link = handler.link, label = handler.label,
			prefix=handler.prefix,id=id,separator=handler.separator, encode=handler.encode})
		inactive = "" 
	end

	if nil == id:match("^10%.[^%s–]-/[^%s–]-[^%.,]$") then	-- doi must begin with '10.', must contain a fwd slash, must not contain spaces or endashes, and must not end with period or comma
		cat = ' ' .. set_error( 'bad_doi' );
	end
	return text .. inactive .. cat 
end

-- Formats an OpenLibrary link, and checks for associated errors.
local function openlibrary(id)
	local code = id:match("^%d+([AMW])$");					-- only digits followed by 'A', 'M', or 'W'
	local handler = cfg.id_handlers['OL'];

	if ( code == "A" ) then
		return external_link_id({link=handler.link, label=handler.label,
			prefix="http://openlibrary.org/authors/OL",id=id, separator=handler.separator,
			encode = handler.encode})
	elseif ( code == "M" ) then
		return external_link_id({link=handler.link, label=handler.label,
			prefix="http://openlibrary.org/books/OL",id=id, separator=handler.separator,
			encode = handler.encode})
	elseif ( code == "W" ) then
		return external_link_id({link=handler.link, label=handler.label,
			prefix= "http://openlibrary.org/works/OL",id=id, separator=handler.separator,
			encode = handler.encode})
	else
		return external_link_id({link=handler.link, label=handler.label,
			prefix= "http://openlibrary.org/OL",id=id, separator=handler.separator,
			encode = handler.encode}) .. 
			' ' .. set_error( 'bad_ol' );
	end
end


--[--------------------------< M E S S A G E _ I D >----------------------------------------------------------

Validate and format a usenet message id.  Simple error checking, looks for 'id-left@id-right' not enclosed in
'<' and/or '>' angle brackets.](https://second-renaissance.fandom.com/wiki/--------------------------<_M_E_S_S_A_G_E___I_D_>----------------------------------------------------------

Validate_and_format_a_usenet_message_id.__Simple_error_checking,_looks_for_'id-left@id-right'_not_enclosed_in
'<'_and/or_'>'_angle_brackets.)

local function message_id (id)
	local handler = cfg.id_handlers['USENETID'];

	text = external_link_id({link = handler.link, label = handler.label,
		prefix=handler.prefix,id=id,separator=handler.separator, encode=handler.encode})
 
	if not id:match('^.+@.+$') or not id:match('^[^<].*[^>]$')then				-- doesn't have '@' or has one or first or last character is '< or '>'
		text = text .. ' ' .. set_error( 'bad_message_id' )						-- add an error message if the message id is invalid
	end 
	
	return text
end

--[type=<default value>) for those templates that have defaults.
Also handles the special case where it is desirable to omit the title type from the rendered citation (|type=none).](https://second-renaissance.fandom.com/wiki/--------------------------<_S_E_T___T_I_T_L_E_T_Y_P_E_>----------------------------------------------------

This_function_sets_default_title_types_(equivalent_to_the_citation_including)

local function set_titletype (cite_class, title_type)
	if is_set(title_type) then
		if "none" == title_type then
			title_type = "";													-- if |type=none then type parameter not displayed
		end
		return title_type;														-- if |type= has been set to any other value use that value
	end

	return cfg.title_types [cite_class] or '';									-- set template's default title type; else empty string for concatenation
end

--[--------------------------< C L E A N _ I S B N >----------------------------------------------------------

Removes irrelevant text and dashes from ISBN number
Similar to that used for Special:BookSources](https://second-renaissance.fandom.com/wiki/--------------------------<_C_L_E_A_N___I_S_B_N_>----------------------------------------------------------

Removes_irrelevant_text_and_dashes_from_ISBN_number
Similar_to_that_used_for_Special:BookSources)

local function clean_isbn( isbn_str )
	return isbn_str:gsub( "[^-0-9X]", "" );
end

--[--------------------------< E S C A P E _ L U A _ M A G I C _ C H A R S >----------------------------------

Returns a string where all of lua's magic characters have been escaped.  This is important because functions like
string.gsub() treat their pattern and replace strings as patterns, not literal strings.](https://second-renaissance.fandom.com/wiki/--------------------------<_E_S_C_A_P_E___L_U_A___M_A_G_I_C___C_H_A_R_S_>----------------------------------

Returns_a_string_where_all_of_lua's_magic_characters_have_been_escaped.__This_is_important_because_functions_like
string.gsub()_treat_their_pattern_and_replace_strings_as_patterns,_not_literal_strings.)
local function escape_lua_magic_chars (argument)
	argument = argument:gsub("%%", "%%%%");										-- replace % with %%
	argument = argument:gsub("([%^%$%(%)%.%[%]%*%+%-%?])", "%%%1");				-- replace all other lua magic pattern characters
	return argument;
end

--[--------------------------< S T R I P _ A P O S T R O P H E _ M A R K U P >--------------------------------

Strip wiki italic and bold markup from argument so that it doesn't contaminate COinS metadata.
This function strips common patterns of apostrophe markup.  We presume that editors who have taken the time to
markup a title have, as a result, provided valid markup. When they don't, some single apostrophes are left behind.](https://second-renaissance.fandom.com/wiki/--------------------------<_S_T_R_I_P___A_P_O_S_T_R_O_P_H_E___M_A_R_K_U_P_>--------------------------------

Strip_wiki_italic_and_bold_markup_from_argument_so_that_it_doesn't_contaminate_COinS_metadata.
This_function_strips_common_patterns_of_apostrophe_markup.__We_presume_that_editors_who_have_taken_the_time_to
markup_a_title_have,_as_a_result,_provided_valid_markup._When_they_don't,_some_single_apostrophes_are_left_behind.)

local function strip_apostrophe_markup (argument)
	if not is_set (argument) then return argument; end

	while true do
		if argument:match ("%'%'%'%'%'") then									-- bold italic (5)
			argument=argument:gsub("%'%'%'%'%'", "");							-- remove all instances of it
		elseif argument:match ("%'%'%'%'") then									-- italic start and end without content (4)
			argument=argument:gsub("%'%'%'%'", "");
		elseif argument:match ("%'%'%'") then									-- bold (3)
			argument=argument:gsub("%'%'%'", "");
		elseif argument:match ("%'%'") then										-- italic (2)
			argument=argument:gsub("%'%'", "");
		else
			break;
		end
	end
	return argument;															-- done
end

--[--------------------------< M A K E _ C O I N S _ T I T L E >----------------------------------------------

Makes a title for COinS from Title and / or ScriptTitle (or any other name-script pairs)

Apostrophe markup (bold, italics) is stripped from each value so that the COinS metadata isn't correupted with strings
of %27%27...](https://second-renaissance.fandom.com/wiki/--------------------------<_M_A_K_E___C_O_I_N_S___T_I_T_L_E_>----------------------------------------------

Makes_a_title_for_COinS_from_Title_and_/_or_ScriptTitle_(or_any_other_name-script_pairs)

Apostrophe_markup_(bold,_italics)_is_stripped_from_each_value_so_that_the_COinS_metadata_isn't_correupted_with_strings
of_%27%27...)

local function make_coins_title (title, script)
	if is_set (title) then
		title = strip_apostrophe_markup (title);								-- strip any apostrophe markup
	else
		title='';																-- if not set, make sure title is an empty string
	end
	if is_set (script) then
		script = script:gsub ('^%l%l%s*:%s*', '');								-- remove language prefix if present (script value may now be empty string)
		script = strip_apostrophe_markup (script);								-- strip any apostrophe markup
	else
		script='';																-- if not set, make sure script is an empty string
	end
	if is_set (title) and is_set (script) then
		script = ' ' .. script;													-- add a space before we concatenate
	end
	return title .. script;														-- return the concatenation
end

--[page=, |pages=, or |at= parameters for use in COinS.](https://second-renaissance.fandom.com/wiki/--------------------------<_G_E_T___C_O_I_N_S___P_A_G_E_S_>------------------------------------------------

Extract_page_numbers_from_external_wikilinks_in_any_of_the)

local function get_coins_pages (pages)
	local pattern;
	if not is_set (pages) then return pages; end								-- if no page numbers then we're done
	
	while true do
		pattern = pages:match("%[(%w*:?//[^ ]+%s+)[%w%d].*%]");					-- pattern is the opening bracket, the url and following space(s): "[url "
		if nil == pattern then break; end										-- no more urls
		pattern = escape_lua_magic_chars (pattern);								-- pattern is not a literal string; escape lua's magic pattern characters
		pages = pages:gsub(pattern, "");										-- remove as many instances of pattern as possible
	end
	pages = pages:gsub("[%[%]]", "");											-- remove the brackets
	pages = pages:gsub("–", "-" );							-- replace endashes with hyphens
	pages = pages:gsub("&%w+;", "-" );						-- and replace html entities (&ndash; etc.) with hyphens; do we need to replace numerical entities like &#32; and the like?
	return pages;
end

-- Gets the display text for a wikilink like [B](https://second-renaissance.fandom.com/wiki/A) or [B](https://second-renaissance.fandom.com/wiki/B) gives B
local function remove_wiki_link( str )
	return (str:gsub( "%[%[([^%[%]]*)%]%]", function(l)
		return l:gsub( "^[^|]*|(.*)$", "%1" ):gsub("^%s*(.-)%s*$", "%1");
	end));
end

-- Converts a hyphen to a dash
local function hyphen_to_dash( str )
	if not is_set(str) or str:match( "[%[%]{}<>]" ) ~= nil then
		return str;
	end	
	return str:gsub( '-', '–' );
end

--[--------------------------< S A F E _ J O I N >------------------------------------------------------------

Joins a sequence of strings together while checking for duplicate separation characters.](https://second-renaissance.fandom.com/wiki/--------------------------<_S_A_F_E___J_O_I_N_>------------------------------------------------------------

Joins_a_sequence_of_strings_together_while_checking_for_duplicate_separation_characters.)

local function safe_join( tbl, duplicate_char )
	--[Note: we use string functions here, rather than ustring functions.
	
	This has considerably faster performance and should work correctly as 
	long as the duplicate_char is strict ASCII.  The strings
	in tbl may be ASCII or UTF8.](https://second-renaissance.fandom.com/wiki/Note:_we_use_string_functions_here,_rather_than_ustring_functions.
	
	This_has_considerably_faster_performance_and_should_work_correctly_as_
	long_as_the_duplicate_char_is_strict_ASCII.__The_strings
	in_tbl_may_be_ASCII_or_UTF8.)
	
	local str = '';																-- the output string
	local comp = '';															-- what does 'comp' mean?
	local end_chr = '';
	local trim;
	for _, value in ipairs( tbl ) do
		if value == nil then value = ''; end
		
		if str == '' then														-- if output string is empty
			str = value;														-- assign value to it (first time through the loop)
		elseif value ~= '' then
			if value:sub(1,1) == '<' then										-- Special case of values enclosed in spans and other markup.
				comp = value:gsub( "%b<>", "" );								-- remove html markup (<span>string</span> -> string)
			else
				comp = value;
			end
																				-- typically duplicate_char is sepc
			if comp:sub(1,1) == duplicate_char then								-- is first charactier same as duplicate_char? why test first character?
																				--   Because individual string segments often (always?) begin with terminal punct for th
																				--   preceding segment: 'First element' .. 'sepc next element' .. etc?
				trim = false;
				end_chr = str:sub(-1,-1);										-- get the last character of the output string
				-- str = str .. "<HERE(enchr=" .. end_chr.. ")"					-- debug stuff?
				if end_chr == duplicate_char then								-- if same as separator
					str = str:sub(1,-2);										-- remove it
				elseif end_chr == "'" then										-- if it might be wikimarkup
					if str:sub(-3,-1) == duplicate_char .. "''" then			-- if last three chars of str are sepc'' 
						str = str:sub(1, -4) .. "''";							-- remove them and add back ''
					elseif str:sub(-5,-1) == duplicate_char .. "]]''" then		-- if last five chars of str are sepc]]'' 
						trim = true;											-- why? why do this and next differently from previous?
					elseif str:sub(-4,-1) == duplicate_char .. "]''" then		-- if last four chars of str are sepc]'' 
						trim = true;											-- same question
					end
				elseif end_chr == "]" then										-- if it might be wikimarkup
					if str:sub(-3,-1) == duplicate_char .. "]]" then			-- if last three chars of str are sepc]] wikilink 
						trim = true;
					elseif str:sub(-2,-1) == duplicate_char .. "]" then			-- if last two chars of str are sepc] external link
						trim = true;
					elseif str:sub(-4,-1) == duplicate_char .. "'']" then		-- normal case when |url=something & |title=Title.
						trim = true;
					end
				elseif end_chr == " " then										-- if last char of output string is a space
					if str:sub(-2,-1) == duplicate_char .. " " then				-- if last two chars of str are <sepc><space>
						str = str:sub(1,-3);									-- remove them both
					end
				end

				if trim then
					if value ~= comp then 										-- value does not equal comp when value contains html markup
						local dup2 = duplicate_char;
						if dup2:match( "%A" ) then dup2 = "%" .. dup2; end		-- if duplicate_char not a letter then escape it
						
						value = value:gsub( "(%b<>)" .. dup2, "%1", 1 )			-- remove duplicate_char if it follows html markup
					else
						value = value:sub( 2, -1 );								-- remove duplicate_char when it is first character
					end
				end
			end
			str = str .. value;													--add it to the output string
		end
	end
	return str;
end  

--[[--------------------------< I S _ G O O D _ V A N C _ N A M E >--------------------------------------------

For Vancouver Style, author/editor names are supposed to be rendered in Latin (read ASCII) characters.  When a name
uses characters that contain diacritical marks, those characters are to converted to the corresponding Latin character.
When a name is written using a non-Latin alphabet or logogram, that name is to be transliterated into Latin characters.
These things are not currently possible in this module so are left to the editor to do.

This test allows |first= and |last= names to contain any of the letters defined in the four Unicode Latin character sets
	[http://www.unicode.org/charts/PDF/U0000.pdf C0 Controls and Basic Latin] 0041–005A, 0061–007A
	[http://www.unicode.org/charts/PDF/U0080.pdf C1 Controls and Latin-1 Supplement] 00C0–00D6, 00D8–00F6, 00F8–00FF
	[http://www.unicode.org/charts/PDF/U0100.pdf Latin Extended-A] 0100–017F
	[http://www.unicode.org/charts/PDF/U0180.pdf Latin Extended-B] 0180–01BF, 01C4–024F

|lastn= also allowed to contain hyphens, spaces, and apostrophes. (http://www.ncbi.nlm.nih.gov/books/NBK7271/box/A35029/)
|firstn= also allowed to contain hyphens, spaces, apostrophes, and periods

At the time of this writing, I had to write the 'if nil == mw.ustring.find ...' test ouside of the code editor and paste it here
because the code editor gets confused between character insertion point and cursor position.

]]

local function is_good_vanc_name (last, first)
	if nil == mw.ustring.find (last, "^[A-Za-zÀ-ÖØ-öø-ƿǄ-ɏ%-%s%']*$") or nil == mw.ustring.find (first, "^[A-Za-zÀ-ÖØ-öø-ƿǄ-ɏ%-%s%'%.]*$") then
		add_vanc_error ();
		return false;															-- not a string of latin characters; Vancouver required Romanization
	end;
	return true;
end

--[name-list-format=vanc.  

Names in |firstn= may be separated by spaces or hyphens, or for initials, a period. See http://www.ncbi.nlm.nih.gov/books/NBK7271/box/A35062/.

Vancouver style requires family rank designations (Jr, II, III, etc) to be rendered as Jr, 2nd, 3rd, etc.  This form is not
currently supported by this code so correctly formed names like Smith JL 2nd are converted to Smith J2. See http://www.ncbi.nlm.nih.gov/books/NBK7271/box/A35085/.

This function uses ustring functions because firstname initials may be any of the unicode Latin characters accepted by is_good_vanc_name ().](https://second-renaissance.fandom.com/wiki/--------------------------<_R_E_D_U_C_E___T_O___I_N_I_T_I_A_L_S_>------------------------------------------

Attempts_to_convert_names_to_initials_in_support_of)

local function reduce_to_initials(first)
	if mw.ustring.match(first, "^%u%u$") then return first end;					-- when first contains just two upper-case letters, nothing to do
	local initials = {}
	local i = 0;																-- counter for number of initials
	for word in mw.ustring.gmatch(first, "[^%s%.%-]+") do						-- names separated by spaces, hyphens, or periods
		table.insert(initials, mw.ustring.sub(word,1,1))						-- Vancouver format does not include full stops.
		i = i + 1;																-- bump the counter 
		if 2 <= i then break; end												-- only two initials allowed in Vancouver system; if 2, quit
	end
	return table.concat(initials)												-- Vancouver format does not include spaces.
end

--[--------------------------< L I S T  _ P E O P L E >-------------------------------------------------------

Formats a list of people (e.g. authors / editors)](https://second-renaissance.fandom.com/wiki/--------------------------<_L_I_S_T____P_E_O_P_L_E_>-------------------------------------------------------

Formats_a_list_of_people_(e.g._authors_/_editors))

local function list_people(control, people, etal)
	local sep;
	local namesep;
	local format = control.format
	local maximum = control.maximum
	local lastauthoramp = control.lastauthoramp;
	local text = {}

	if 'vanc' == format then													-- Vancouver-like author/editor name styling?
		sep = ',';																-- name-list separator between authors is a comma
		namesep = ' ';															-- last/first separator is a space
	else
		sep = ';'																-- name-list separator between authors is a semicolon
		namesep = ', '															-- last/first separator is <comma><space>
	end
	
	if sep:sub(-1,-1) ~= " " then sep = sep .. " " end
	if is_set (maximum) and maximum < 1 then return "", 0; end					-- returned 0 is for EditorCount; not used for authors
	
	for i,person in ipairs(people) do
		if is_set(person.last) then
			local mask = person.mask
			local one
			local sep_one = sep;
			if is_set (maximum) and i > maximum then
				etal = true;
				break;
			elseif (mask ~= nil) then
				local n = tonumber(mask)
				if (n ~= nil) then
					one = string.rep("&mdash;",n)
				else
					one = mask;
					sep_one = " ";
				end
			else
				one = person.last
				local first = person.first
				if is_set(first) then 
					if ( "vanc" == format ) then								-- if vancouver format
						one = one:gsub ('%.', '');								-- remove periods from surnames (http://www.ncbi.nlm.nih.gov/books/NBK7271/box/A35029/)
						if not person.corporate and is_good_vanc_name (one, first) then					-- and name is all Latin characters; corporate authors not tested
							first = reduce_to_initials(first)					-- attempt to convert first name(s) to initials
						end
					end
					one = one .. namesep .. first 
				end
				if is_set(person.link) and person.link ~= control.page_name then
					one = "[" .. one .. "](https://second-renaissance.fandom.com/wiki/"_.._person.link_.._")"				-- link author/editor if this page is not the author's/editor's page
				end

				if is_set(person.link) and ((nil ~= person.link:find("//")) or (nil ~= person.link:find("[%[%]]"))) then
					one = one .. " " .. set_error( 'bad_authorlink' ) end		-- url or wikilink in author link;
			end
			table.insert( text, one )
			table.insert( text, sep_one )
		end
	end

	local count = #text / 2;													-- (number of names + number of separators) divided by 2
	if count > 0 then 
		if count > 1 and is_set(lastauthoramp) and not etal then
			text[#text-2] = " & ";												-- replace last separator with ampersand text
		end
		text[#text] = nil;														-- erase the last separator
	end
	
	local result = table.concat(text)											-- construct list
	if etal and is_set (result) then											-- etal may be set by |display-authors=etal but we might not have a last-first list
		result = result .. ' ' .. cfg.messages['et al'];						-- we've go a last-first list and etal so add et al.
	end
	
	return result, count
end

--[--------------------------< A N C H O R _ I D >------------------------------------------------------------

Generates a CITEREF anchor ID if we have at least one name or a date.  Otherwise returns an empty string.](https://second-renaissance.fandom.com/wiki/--------------------------<_A_N_C_H_O_R___I_D_>------------------------------------------------------------

Generates_a_CITEREF_anchor_ID_if_we_have_at_least_one_name_or_a_date.__Otherwise_returns_an_empty_string.)

local function anchor_id( options )
	local id = table.concat( options );											-- concatenate names and year for CITEREF id
	if is_set (id) then															-- if concatenation is not an empty string
		return "CITEREF" .. id;													-- add the CITEREF portion
	else
		return '';																-- return an empty string; no reason to include CITEREF id in this citation
	end
end

--[display-authors=etal or |displayeditors=etal](https://second-renaissance.fandom.com/wiki/--------------------------<_N_A_M_E___H_A_S___E_T_A_L_>----------------------------------------------------

Evaluates_the_content_of_author_and_editor_name_parameters_for_variations_on_the_theme_eof_et_al.__If_found,
the_et_al._is_removed,_a_flag_is_set_to_true_and_the_function_returns_the_modified_name_and_the_flag.

This_function_never_sets_the_flag_to_false_but_returns_it's_previous_state_because_it_may_have_been_set_by
previous_passes_through_this_function_or_by_the_parameters)

local function name_has_etal (name, etal, nocat)

	if is_set (name) then														-- name can be nil in which case just return
		local pattern = "[;,]? *[\"']*%f[Ee][Ee][Tt] *[Aa][Ll][%.\"']*$"		-- variations on the 'et al' theme
		
		if name:match (pattern) then											-- variants on et al.
			name = name:gsub (pattern, '');										-- if found, remove
			etal = true;														-- set flag (may have been set previously here or by |display-authors=etal)
			if not nocat then													-- no categorization for |vauthors=
				add_maint_cat ('etal');											-- and add a category if not already added
			end
		end
	end
	return name, etal;															-- 
end

--[lastn= and |firstn= parameters (or their aliases), and their matching link and mask parameters.
Stops searching when both |lastn= and |firstn= are not found in args after two sequential attempts: found |last1=, |last2=, and |last3= but doesn't
find |last4= and |last5= then the search is done.

This function emits an error message when there is a |firstn= without a matching |lastn=.  When there are 'holes' in the list of last names, |last1= and |last3=
are present but |last2= is missing, an error message is emitted. |lastn= is not required to have a matching |firstn=.

When an author or editor parameter contains some form of 'et al.', the 'et al.' is stripped from the parameter and a flag (etal) returned
that will cause list_people() to add the static 'et al.' text from Module:Citation/CS1/Configuration.  This keeps 'et al.' out of the 
template's metadata.  When this occurs, the page is added to a maintenance category.](https://second-renaissance.fandom.com/wiki/--------------------------<_E_X_T_R_A_C_T___N_A_M_E_S_>----------------------------------------------------
Gets_name_list_from_the_input_arguments

Searches_through_args_in_sequential_order_to_find)

local function extract_names(args, list_name)
	local names = {};			-- table of names
	local last;					-- individual name components
	local first;
	local link;
	local mask;
	local i = 1;				-- loop counter/indexer
	local n = 1;				-- output table indexer
	local count = 0;			-- used to count the number of times we haven't found a |last= (or alias for authors, |editor-last or alias for editors)
	local etal=false;			-- return value set to true when we find some form of et al. in an author parameter

	local err_msg_list_name = list_name:match ("(%w+)List") .. 's list';		-- modify AuthorList or EditorList for use in error messages if necessary

	while true do
		last = select_one( args, cfg.aliases[list_name .. '-Last'], 'redundant_parameters', i );		-- search through args for name components beginning at 1
		first = select_one( args, cfg.aliases[list_name .. '-First'], 'redundant_parameters', i );
		link = select_one( args, cfg.aliases[list_name .. '-Link'], 'redundant_parameters', i );
		mask = select_one( args, cfg.aliases[list_name .. '-Mask'], 'redundant_parameters', i );

		last, etal = name_has_etal (last, etal, false);								-- find and remove variations on et al.
		first, etal = name_has_etal (first, etal, false);								-- find and remove variations on et al.

		if first and not last then												-- if there is a firstn without a matching lastn
			table.insert( z.message_tail, { set_error( 'first_missing_last', {err_msg_list_name, i}, true ) } );	-- add this error message
		elseif not first and not last then										-- if both firstn and lastn aren't found, are we done?
			count = count + 1;													-- number of times we haven't found last and first
			if 2 <= count then													-- two missing names and we give up
				break;															-- normal exit or there is a two-name hole in the list; can't tell which
			end
		else																	-- we have last with or without a first
			names[n] = {last = last, first = first, link = link, mask = mask, corporate=false};	-- add this name to our names list (corporate for |vauthors= only)
			n = n + 1;															-- point to next location in the names table
			if 1 == count then													-- if the previous name was missing
				table.insert( z.message_tail, { set_error( 'missing_name', {err_msg_list_name, i-1}, true ) } );		-- add this error message
			end
			count = 0;															-- reset the counter, we're looking for two consecutive missing names
		end
		i = i + 1;																-- point to next args location
	end
	
	return names, etal;															-- all done, return our list of names
end

-- Populates ID table from arguments using configuration settings
local function extract_ids( args )
	local id_list = {};
	for k, v in pairs( cfg.id_handlers ) do	
		v = select_one( args, v.parameters, 'redundant_parameters' );
		if is_set(v) then id_list[k] = v; end
	end
	return id_list;
end

--[--------------------------< B U I L D _ I D _ L I S T >--------------------------------------------------------

Takes a table of IDs and turns it into a table of formatted ID outputs.](https://second-renaissance.fandom.com/wiki/--------------------------<_B_U_I_L_D___I_D___L_I_S_T_>--------------------------------------------------------

Takes_a_table_of_IDs_and_turns_it_into_a_table_of_formatted_ID_outputs.)

local function build_id_list( id_list, options )
	local new_list, handler = {};

	function fallback(k) return { __index = function(t,i) return cfg.id_handlers[k][i] end } end;
	
	for k, v in pairs( id_list ) do
		-- fallback to read-only cfg
		handler = setmetatable( { ['id'] = v }, fallback(k) );
		
		if handler.mode == 'external' then
			table.insert( new_list, {handler.label, external_link_id( handler ) } );
		elseif handler.mode == 'internal' then
			table.insert( new_list, {handler.label, internal_link_id( handler ) } );
		elseif handler.mode ~= 'manual' then
			error( cfg.messages['unknown_ID_mode'] );
		elseif k == 'DOI' then
			table.insert( new_list, {handler.label, doi( v, options.DoiBroken ) } );
		elseif k == 'ARXIV' then
			table.insert( new_list, {handler.label, arxiv( v, options.Class ) } ); 
		elseif k == 'ASIN' then
			table.insert( new_list, {handler.label, amazon( v, options.ASINTLD ) } ); 
		elseif k == 'LCCN' then
			table.insert( new_list, {handler.label, lccn( v ) } );
		elseif k == 'OL' then
			table.insert( new_list, {handler.label, openlibrary( v ) } );
		elseif k == 'PMC' then
			table.insert( new_list, {handler.label, pmc( v, options.Embargo ) } );
		elseif k == 'PMID' then
			table.insert( new_list, {handler.label, pmid( v ) } );
		elseif k == 'ISMN' then
			table.insert( new_list, {handler.label, ismn( v ) } );
		elseif k == 'ISSN' then
			table.insert( new_list, {handler.label, issn( v ) } );
		elseif k == 'ISBN' then
			local ISBN = internal_link_id( handler );
			if not check_isbn( v ) and not is_set(options.IgnoreISBN) then
				ISBN = ISBN .. set_error( 'bad_isbn', {}, false, " ", "" );
			end
			table.insert( new_list, {handler.label, ISBN } );				
		elseif k == 'USENETID' then
			table.insert( new_list, {handler.label, message_id( v ) } );
		else
			error( cfg.messages['unknown_manual_ID'] );
		end
	end
	
	function comp( a, b )	-- used in following table.sort()
		return a[1] < b[1];
	end
	
	table.sort( new_list, comp );
	for k, v in ipairs( new_list ) do
		new_list[k] = v[2];
	end
	
	return new_list;
end
  

-- COinS metadata (see <http://ocoins.info/>) allows automated tools to parse
-- the citation information.
local function COinS(data, class)
	if 'table' ~= type(data) or nil == next(data) then
		return '';
	end
	
	local ctx_ver = "Z39.88-2004";
	
	-- treat table strictly as an array with only set values.
	local OCinSoutput = setmetatable( {}, {
		__newindex = function(self, key, value)
			if is_set(value) then
				rawset( self, #self+1, table.concat{ key, '=', mw.uri.encode( remove_wiki_link( value ) ) } );
			end
		end
	});
	
	if is_set(data.Chapter) then
		OCinSoutput.rft_val_fmt = "info:ofi/fmt:kev:mtx:book";
		OCinSoutput["rft.genre"] = "bookitem";
		OCinSoutput["rft.atitle"] = data.Chapter;
		OCinSoutput["rft.btitle"] = data.Title;
	elseif is_set(data.Periodical) then
		OCinSoutput.rft_val_fmt = "info:ofi/fmt:kev:mtx:journal";
		if 'arxiv' == class then
			OCinSoutput["rft.genre"] = "preprint";								-- cite arxiv
		else
			OCinSoutput["rft.genre"] = "article";
		end
		OCinSoutput["rft.jtitle"] = data.Periodical;
		OCinSoutput["rft.atitle"] = data.Title;
	else
		OCinSoutput.rft_val_fmt = "info:ofi/fmt:kev:mtx:book";
		OCinSoutput["rft.genre"] = "book"
		OCinSoutput["rft.btitle"] = data.Title;
	end
	
	OCinSoutput["rft.place"] = data.PublicationPlace;
	OCinSoutput["rft.date"] = data.Date;
	OCinSoutput["rft.series"] = data.Series;
	OCinSoutput["rft.volume"] = data.Volume;
	OCinSoutput["rft.issue"] = data.Issue;
	OCinSoutput["rft.pages"] = data.Pages;
	OCinSoutput["rft.edition"] = data.Edition;
	OCinSoutput["rft.pub"] = data.PublisherName;
	
	for k, v in pairs( data.ID_list ) do
		local id, value = cfg.id_handlers[k].COinS;
		if k == 'ISBN' then value = clean_isbn( v ); else value = v; end
		if string.sub( id or "", 1, 4 ) == 'info' then
			OCinSoutput["rft_id"] = table.concat{ id, "/", v };
		else
			OCinSoutput[ id ] = value;
		end
	end
	
	local last, first;
	for k, v in ipairs( data.Authors ) do
		last, first = v.last, v.first;
		if k == 1 then
			if is_set(last) then
				OCinSoutput["rft.aulast"] = last;
			end
			if is_set(first) then 
				OCinSoutput["rft.aufirst"] = first;
			end
		end
		if is_set(last) and is_set(first) then
			OCinSoutput["rft.au"] = table.concat{ last, ", ", first };
		elseif is_set(last) then
			OCinSoutput["rft.au"] = last;
		end
	end
	
	OCinSoutput.rft_id = data.URL;
	OCinSoutput.rfr_id = table.concat{ "info:sid/", mw.site.server:match( "[^/]*$" ), ":", data.RawPage };
	OCinSoutput = setmetatable( OCinSoutput, nil );
	
	-- sort with version string always first, and combine.
	table.sort( OCinSoutput );
	table.insert( OCinSoutput, 1, "ctx_ver=" .. ctx_ver );  -- such as "Z39.88-2004"
	return table.concat(OCinSoutput, "&");
end


--[language= parameter if not an ISO639-1 code.  Handles the special case that is Norwegian where
ISO639-1 code 'no' is mapped to language name 'Norwegian Bokmål' by Extention:CLDR.

Returns the language name and associated ISO639-1 code.  Because case of the source may be incorrect or different from the case that Wikimedia
uses, the name comparisons are done in lower case and when a match is found, the Wikimedia version (assumed to be correct) is returned along
with the code.  When there is no match, we return the original language name string.

mw.language.fetchLanguageNames() will return a list of languages that aren't part of ISO639-1. Names that aren't ISO639-1 but that are included
in the list will be found if that name is provided in the |language= parameter.  For example, if |language=Samaritan Aramaic, that name will be
found with the associated code 'sam', not an ISO639-1 code.  When names are found and the associated code is not two characters, this function
returns only the Wikimedia language name.

Adapted from code taken from Module:Check ISO 639-1.](https://second-renaissance.fandom.com/wiki/--------------------------<_G_E_T___I_S_O_6_3_9___C_O_D_E_>------------------------------------------------

Validates_language_names_provided_in)

local function get_iso639_code (lang)
	if 'norwegian' == lang:lower() then											-- special case related to Wikimedia remap of code 'no' at Extension:CLDR
		return 'Norwegian', 'no';												-- Make sure rendered version is properly capitalized
	end
	
	local languages = mw.language.fetchLanguageNames('en', 'all')				-- get a list of language names known to Wikimedia
																				-- ('all' is required for North Ndebele, South Ndebele, and Ojibwa)
	local langlc = mw.ustring.lower(lang);										-- lower case version for comparisons
	
	for code, name in pairs(languages) do										-- scan the list to see if we can find our language
		if langlc == mw.ustring.lower(name) then
			if 2 ~= code:len() then												-- ISO639-1 codes only
				return name;													-- so return the name but not the code
			end
			return name, code;													-- found it, return name to ensure proper capitalization and the ISO639-1 code
		end
	end
	return lang;																-- not valid language; return language in original case and nil for ISO639-1 code
end

--[language=no.  We presume that editors don't know about the variants or can't descriminate between them.

See Help talk:Citation Style_1#An ISO 639-1 language name test

When |language= contains a valid ISO639-1 code, the page is assigned to the category for that code: Category:Norwegian-language sources (no) if
the page is a mainspace page and the ISO639-1 code is not 'en'.  Similarly, if the  parameter is |language=Norwegian, it will be categorized in the same way.

This function supports multiple languages in the form |language=nb, French, th where the language names or codes are separated from each other by commas.](https://second-renaissance.fandom.com/wiki/--------------------------<_L_A_N_G_U_A_G_E___P_A_R_A_M_E_T_E_R_>------------------------------------------

Get_language_name_from_ISO639-1_code_value_provided.__If_a_code_is_valid_use_the_returned_name;_if_not,_then_use_the_value_that_was_provided_with_the_language_parameter.

There_is_an_exception.__There_are_three_ISO639-1_codes_for_Norewegian_language_variants.__There_are_two_official_variants:_Norwegian_Bokmål_(code_'nb')_and
Norwegian_Nynorsk_(code_'nn').__The_third,_code_'no',__is_defined_by_ISO639-1_as_'Norwegian'_though_in_Norway_this_is_pretty_much_meaningless.__However,_it_appears
that_on_enwiki,_editors_are_for_the_most_part_unaware_of_the_nb_and_nn_variants_(compare_page_counts_for_these_variants_at_Category:Articles_with_non-English-language_external_links.

Because_Norwegian_Bokmål_is_the_most_common_language_variant,_Media_wiki_has_been_modified_to_return_Norwegian_Bokmål_for_ISO639-1_code_'no'._Here_we_undo_that_and
return_'Norwegian'_when_editors_use)

local function language_parameter (lang)
	local code;																	-- the ISO639-1 two character code
	local name;																	-- the language name
	local language_list = {};													-- table of language names to be rendered
	local names_table = {};														-- table made from the value assigned to |language=

	names_table = mw.text.split (lang, '%s*,%s*');								-- names should be a comma separated list

	for _, lang in ipairs (names_table) do										-- reuse lang

		if 2 == lang:len() then													-- ISO639-1 language code are 2 characters (fetchLanguageName also supports 3 character codes)
			name = mw.language.fetchLanguageName( lang:lower(), "en" );			-- get ISO 639-1 language name if Language is a proper code
		end
	
		if is_set (name) then													-- if Language specified a valid ISO639-1 code
			code = lang:lower();												-- save it
		else
			name, code = get_iso639_code (lang);								-- attempt to get code from name (assign name here so that we are sure of proper capitalization)
		end
	
		if is_set (code) then
			if 'no' == code then name = 'Norwegian' end;						-- override wikimedia when code is 'no'
			if 'en' ~= code then												-- English not the language
				add_prop_cat ('foreign_lang_source', {name, code})
			end
		else
			add_maint_cat ('unknown_lang');										-- add maint category if not already added
		end
		
		table.insert (language_list, name);
		name = '';																-- so we can reuse it
	end
	
	code = #language_list														-- reuse code as number of languages in the list
	if 2 >= code then
		name = table.concat (language_list, ' and ')							-- insert '<space>and<space>' between two language names
	elseif 2 < code then
		language_list[code] = 'and ' .. language_list[code];					-- prepend last name with 'and<space>'
		name = table.concat (language_list, ', ')								-- and concatenate with '<comma><space>' separators
	end
	if 'English' == name then
		return '';																-- if one language and that language is English return an enpty string (no annotation)
	end
	return (" " .. wrap_msg ('language', name));								-- otherwise wrap with '(in ...)'
end

--[--------------------------< S E T _ C S 1 _ S T Y L E >----------------------------------------------------

Set style settings for CS1 citation templates. Returns separator and postscript settings](https://second-renaissance.fandom.com/wiki/--------------------------<_S_E_T___C_S_1___S_T_Y_L_E_>----------------------------------------------------

Set_style_settings_for_CS1_citation_templates._Returns_separator_and_postscript_settings)

local function set_cs1_style (ps)
	if not is_set (ps) then														-- unless explicitely set to something
		ps = '.';																-- terminate the rendered citation with a period
	end
	return '.', ps;																-- separator is a full stop
end

--[--------------------------< S E T _ C S 2 _ S T Y L E >----------------------------------------------------

Set style settings for CS2 citation templates. Returns separator, postscript, ref settings](https://second-renaissance.fandom.com/wiki/--------------------------<_S_E_T___C_S_2___S_T_Y_L_E_>----------------------------------------------------

Set_style_settings_for_CS2_citation_templates._Returns_separator,_postscript,_ref_settings)

local function set_cs2_style (ps, ref)
	if not is_set (ps) then														-- if |postscript= has not been set, set cs2 default
		ps = '';																-- make sure it isn't nil
	end
	if not is_set (ref) then													-- if |ref= is not set
		ref = "harv";															-- set default |ref=harv
	end
	return ',', ps, ref;														-- separator is a comma
end

--[mode= is not set or when its value is invalid, use config.CitationClass and parameter values to establish
rendered style.](https://second-renaissance.fandom.com/wiki/--------------------------<_G_E_T___S_E_T_T_I_N_G_S___F_R_O_M___C_I_T_E___C_L_A_S_S_>----------------------

When)

local function get_settings_from_cite_class (ps, ref, cite_class)
	local sep;
	if (cite_class == "citation") then											-- for citation templates (CS2)
		sep, ps, ref = set_cs2_style (ps, ref);
	else																		-- not a citation template so CS1
		sep, ps = set_cs1_style (ps);
	end

	return sep, ps, ref															-- return them all
end

--[mode= if set and valid or uses
config.CitationClass from the template's #invoke: to establish style.](https://second-renaissance.fandom.com/wiki/--------------------------<_S_E_T___S_T_Y_L_E_>------------------------------------------------------------

Establish_basic_style_settings_to_be_used_when_rendering_the_citation.__Uses)

local function set_style (mode, ps, ref, cite_class)
	local sep;
	if 'cs2' == mode then														-- if this template is to be rendered in CS2 (citation) style
		sep, ps, ref = set_cs2_style (ps, ref);
	elseif 'cs1' == mode then													-- if this template is to be rendered in CS1 (cite xxx) style
		sep, ps = set_cs1_style (ps);
	else																		-- anything but cs1 or cs2
		if is_set (mode) then
			table.insert( z.message_tail, { set_error( 'invalid_param_val', {'mode', mode}, true ) } );		-- add error message
		end
		sep, ps, ref = get_settings_from_cite_class (ps, ref, cite_class);		-- get settings based on the template's CitationClass
	end
	if 'none' == ps:lower() then												-- if assigned value is 'none' then
		ps = '';																-- set to empty string
	end
	
	return sep, ps, ref
end

--[=[-------------------------< I S _ P D F >------------------------------------------------------------------

Determines if a url has the file extension is one of the pdf file extensions used by [MediaWiki:Common.css](https://second-renaissance.fandom.com/wiki/MediaWiki:Common.css) when
applying the pdf icon to external links.

returns true if file extension is one of the recognized extension, else false

]=]

local function is_pdf (url)
	return url:match ('%.pdf[%?#]?') or url:match ('%.PDF[%?#]?');
end

--[format=, |chapter-format=, etc.  Also emits an error message if the format parameter does
not have a matching url parameter.  If the format parameter is not set and the url contains a file extension that
is recognized as a pdf document by MediaWiki's commons.css, this code will set the format parameter to (PDF) with
the appropriate styling.](https://second-renaissance.fandom.com/wiki/--------------------------<_S_T_Y_L_E___F_O_R_M_A_T_>------------------------------------------------------

Applies_css_style_to)

local function style_format (format, url, fmt_param, url_param)
	if is_set (format) then
		format = wrap_style ('format', format);									-- add leading space, parenthases, resize
		if not is_set (url) then
			format = format .. set_error( 'format_missing_url', {fmt_param, url_param} );	-- add an error message
		end
	elseif is_pdf (url) then													-- format is not set so if url is a pdf file then
		format = wrap_style ('format', 'PDF');									-- set format to pdf
	else
		format = '';															-- empty string for concatenation
	end
	return format;
end

--[display-authors= is a number greater than or equal to zero, return the number and
the previous state of the 'etal' flag (false by default but may have been set to true if the name list contains
some variant of the text 'et al.').

When the value assigned to |display-authors= is the keyword 'etal', return a number that is one greater than the
number of authors in the list and set the 'etal' flag true.  This will cause the list_people() to display all of
the names in the name list followed by 'et al.'

In all other cases, returns nil and the previous state of the 'etal' flag.](https://second-renaissance.fandom.com/wiki/--------------------------<_G_E_T___D_I_S_P_L_A_Y___A_U_T_H_O_R_S___E_D_I_T_O_R_S_>------------------------

Returns_a_number_that_may_or_may_not_limit_the_length_of_the_author_or_editor_name_lists.

When_the_value_assigned_to)

local function get_display_authors_editors (max, count, list_name, etal)
	if is_set (max) then
		if 'etal' == max:lower():gsub("[ '%.]", '') then						-- the :gsub() portion makes 'etal' from a variety of 'et al.' spellings and stylings
			max = count + 1;													-- number of authors + 1 so display all author name plus et al.
			etal = true;														-- overrides value set by extract_names()
		elseif max:match ('^%d+$') then											-- if is a string of numbers
			max = tonumber (max);												-- make it a number
			if max >= count and 'authors' == list_name then	-- AUTHORS ONLY		-- if |display-xxxxors= value greater than or equal to number of authors/editors
				add_maint_cat ('disp_auth_ed', list_name);
			end
		else																	-- not a valid keyword or number
			table.insert( z.message_tail, { set_error( 'invalid_param_val', {'display-' .. list_name, max}, true ) } );		-- add error message
			max = nil;															-- unset
		end
	elseif 'authors' == list_name then		-- AUTHORS ONLY	need to clear implicit et al category
		max = count + 1;														-- number of authors + 1
	end
	
	return max, etal;
end

--[[--------------------------< E X T R A _ T E X T _ I N _ P A G E _ C H E C K >------------------------------

Adds page to Category:CS1 maint: extra text if |page= or |pages= has what appears to be some form of p. or pp. 
abbreviation in the first characters of the parameter content.

check Page and Pages for extraneous p, p., pp, and pp. at start of parameter value:
	good pattern: '^P[^%.P%l]' matches when |page(s)= begins PX or P# but not Px where x and X are letters and # is a dgiit
	bad pattern: '^[Pp][Pp]' matches matches when |page(s)= begins pp or pP or Pp or PP

]]

local function extra_text_in_page_check (page, nopp)
--	local good_pattern = '^P[^%.P%l]';
	local good_pattern = '^P[^%.Pp]';										-- ok to begin with uppercase P: P7 (pg 7 of section P) but not p123 (page 123) TODO: add Gg for PG or Pg?
--	local bad_pattern = '^[Pp][Pp]';
	local bad_pattern = '^[Pp]?[Pp]%.?[ %d]';

	if is_set (nopp) then													-- don't bother checking if |nopp= is set
		return;
	end

	if not page:match (good_pattern) and (page:match (bad_pattern) or  page:match ('^[Pp]ages?')) then
		add_maint_cat ('extra_text');
	end
--		if Page:match ('^[Pp]?[Pp]%.?[ %d]') or  Page:match ('^[Pp]ages?[ %d]') or
--			Pages:match ('^[Pp]?[Pp]%.?[ %d]') or  Pages:match ('^[Pp]ages?[ %d]') then
--				add_maint_cat ('extra_text');
--		end
end


--[vauthors= or |veditors= and finds matching |xxxxor-maskn= and
|xxxxor-linkn= in args.  It then returns a table of assembled names just as extract_names() does.

Author / editor names in |vauthors= or |veditors= must be in Vancouver system style. Corporate or institutional names
may sometimes be required and because such names will often fail the is_good_vanc_name() and other format compliance
tests, are wrapped in doubled paranethese ((corporate name)) to suppress the format tests.](https://second-renaissance.fandom.com/wiki/--------------------------<_P_A_R_S_E___V_A_U_T_H_O_R_S___V_E_D_I_T_O_R_S_>--------------------------------

This_function_extracts_author_/_editor_names_from)

local function parse_vauthors_veditors (args, vparam, list_name)
	local names = {};															-- table of names assembled from |vauthors=, |author-maskn=, |author-linkn=
	local v_name_table = {};
	local etal = false;															-- return value set to true when we find some form of et al. vauthors parameter
	local last, first, link, mask;
	local corporate = false;

	vparam, etal = name_has_etal (vparam, etal, true);							-- find and remove variations on et al. do not categorize (do it here because et al. might have a period)
	if vparam:find ('%[%[') or vparam:find ('%]%]')	then						-- no wikilinking vauthors names
		add_vanc_error ();
	end
	v_name_table = mw.text.split(vparam, "%s*,%s*")								-- names are separated by commas

	for i, v_name in ipairs(v_name_table) do
		if v_name:match ('^%(%(.+%)%)$') then									-- corporate authors are wrapped in doubled parenthese to supress vanc formatting and error detection
			first = '';															-- set to empty string for concatenation and because it may have been set for previous author/editor
			last = v_name:match ('^%(%((.+)%)%)$')
			corporate = true;
		elseif string.find(v_name, "%s") then
		    lastfirstTable = {}
		    lastfirstTable = mw.text.split(v_name, "%s")
		    first = table.remove(lastfirstTable);								-- removes and returns value of last element in table which should be author intials
		    last  = table.concat(lastfirstTable, " ")							-- returns a string that is the concatenation of all other names that are not initials
		else
			first = '';															-- set to empty string for concatenation and because it may have been set for previous author/editor
			last = v_name;														-- last name or single corporate name?  Doesn't support multiword corporate names? do we need this?
		end
																
		if is_set (first) and not mw.ustring.match (first, "^%u?%u$") then		-- first shall contain one or two upper-case letters, nothing else
			add_vanc_error ();
		end
																				-- this from extract_names ()
		link = select_one( args, cfg.aliases[list_name .. '-Link'], 'redundant_parameters', i );
		mask = select_one( args, cfg.aliases[list_name .. '-Mask'], 'redundant_parameters', i );
		names[i] = {last = last, first = first, link = link, mask = mask, corporate=corporate};		-- add this assembled name to our names list
	end
	return names, etal;															-- all done, return our list of names
end

--[authors=, |authorn= / |lastn / firstn=, or |vauthors= as the source of the author name list or
select one of |editors=, |editorn= / editor-lastn= / |editor-firstn= or |veditors= as the source of the editor name list.

Only one of these appropriate three will be used.  The hierarchy is: |authorn= (and aliases) highest and |authors= lowest and
similarly, |editorn= (and aliases) highest and |editors= lowest

When looking for |authorn= / |editorn= parameters, test |xxxxor1= and |xxxxor2= (and all of their aliases); stops after the second
test which mimicks the test used in extract_names() when looking for a hole in the author name list.  There may be a better
way to do this, I just haven't discovered what that way is.

Emits an error message when more than one xxxxor name source is provided.

In this function, vxxxxors = vauthors or veditors; xxxxors = authors or editors as appropriate.](https://second-renaissance.fandom.com/wiki/--------------------------<_S_E_L_E_C_T___A_U_T_H_O_R___E_D_I_T_O_R___S_O_U_R_C_E_>------------------------

Select_one_of)

local function select_author_editor_source (vxxxxors, xxxxors, args, list_name)
local lastfirst = false;
	if select_one( args, cfg.aliases[list_name .. '-Last'], 'redundant_parameters', 1 ) or		-- do this twice incase we have a first 1 without a last1
		select_one( args, cfg.aliases[list_name .. '-Last'], 'redundant_parameters', 2 ) then
			lastfirst=true;
	end

	if (is_set (vxxxxors) and true == lastfirst) or								-- these are the three error conditions
		(is_set (vxxxxors) and is_set (xxxxors)) or
		(true == lastfirst and is_set (xxxxors)) then
			local err_name;
			if 'AuthorList' == list_name then									-- figure out which name should be used in error message
				err_name = 'author';
			else
				err_name = 'editor';
			end
			table.insert( z.message_tail, { set_error( 'redundant_parameters',
				{err_name .. '-name-list parameters'}, true ) } );				-- add error message
	end

	if true == lastfirst then return 1 end;										-- return a number indicating which author name source to use
	if is_set (vxxxxors) then return 2 end;
	if is_set (xxxxors) then return 3 end;
	return 0;																	-- no authors so return 0 
end

--[--------------------------< C I T A T I O N 0 >------------------------------------------------------------

This is the main function doing the majority of the citation formatting.](https://second-renaissance.fandom.com/wiki/--------------------------<_C_I_T_A_T_I_O_N_0_>------------------------------------------------------------

This_is_the_main_function_doing_the_majority_of_the_citation_formatting.)

local function citation0( config, args)
	--[Load Input Parameters
	The argument_wrapper facilitates the mapping of multiple aliases to single internal variable.](https://second-renaissance.fandom.com/wiki/Load_Input_Parameters
	The_argument_wrapper_facilitates_the_mapping_of_multiple_aliases_to_single_internal_variable.)
	local A = argument_wrapper( args );

	local i 
	local PPrefix = A['PPrefix']
	local PPPrefix = A['PPPrefix']
	local NoPP = A['NoPP'] 
	if in_array(NoPP:lower(), {'yes', 'true', 'y'}) then
		PPPrefix = '';															-- unset these, prefix if used is in |page= or |pages=
		PPrefix = '';
	else
		NoPP = nil;																-- unset, used as a flag later
	end

	-- Pick out the relevant fields from the arguments.  Different citation templates
	-- define different field names for the same underlying things.	
	local author_etal;
	local a	= {};																-- authors list from |lastn= / |firstn= pairs or |vauthors=
	local Authors;
	local NameListFormat = A['NameListFormat'];									-- replaces |author-format= and |editor-format=

	do																			-- to limit scope of selected
		local selected = select_author_editor_source (A['Vauthors'], A['Authors'], args, 'AuthorList');
		if 1 == selected then
			a, author_etal = extract_names (args, 'AuthorList');				-- fetch author list from |authorn= / |lastn= / |firstn=, |author-linkn=, and |author-maskn=
		elseif 2 == selected then
			NameListFormat = 'vanc';											-- override whatever |name-list-format= might be
			a, author_etal = parse_vauthors_veditors (args, args.vauthors, 'AuthorList');	-- fetch author list from |vauthors=, |author-linkn=, and |author-maskn=
		elseif 3 == selected then
			Authors = A['Authors'];												-- use content of |authors=
		end
	end

	local Coauthors = A['Coauthors'];
	local Others = A['Others'];

	local editor_etal;
	local e	= {};																-- editors list from |editor-lastn= / |editor-firstn= pairs or |veditors=
	local Editors;

	do																			-- to limit scope of selected
		local selected = select_author_editor_source (A['Veditors'], A['Editors'], args, 'EditorList');
		if 1 == selected then
			e, editor_etal = extract_names (args, 'EditorList');				-- fetch editor list from |editorn= / |editor-lastn= / |editor-firstn=, |editor-linkn=, and |editor-maskn=
		elseif 2 == selected then
			NameListFormat = 'vanc';											-- override whatever |name-list-format= might be
			e, editor_etal = parse_vauthors_veditors (args, args.veditors, 'EditorList');	-- fetch editor list from |veditors=, |editor-linkn=, and |editor-maskn=
		elseif 3 == selected then
			Editors = A['Editors'];												-- use content of |editors=
		end
	end

	if is_set (NameListFormat) and ('vanc' ~= NameListFormat) then											-- only accepted value for this parameter is 'vanc'
		table.insert( z.message_tail, { set_error( 'invalid_param_val', {'name-list-format', NameListFormat}, true ) } );	-- not vanc so add error message
		NameListFormat = '';													-- set to empty string
	end

	local Year = A['Year'];
	local PublicationDate = A['PublicationDate'];
	local OrigYear = A['OrigYear'];
	local Date = A['Date'];
	local LayDate = A['LayDate'];
	------------------------------------------------- Get title data
	local Title = A['Title'];
	local ScriptTitle = A['ScriptTitle'];
	local BookTitle = A['BookTitle'];
	local Conference = A['Conference'];
	local TransTitle = A['TransTitle'];
	local TitleNote = A['TitleNote'];
	local TitleLink = A['TitleLink'];
	local Chapter = A['Chapter'];
	local ChapterLink = A['ChapterLink'];										-- deprecated but used internally by cite episode
	local TransChapter = A['TransChapter'];
	local TitleType = A['TitleType'];
	local Degree = A['Degree'];
	local Docket = A['Docket'];
	local ArchiveFormat = A['ArchiveFormat'];
	local ArchiveURL = A['ArchiveURL'];
	local URL = A['URL']
	local URLorigin = A:ORIGIN('URL');											-- get name of parameter that holds URL
	local ChapterURL = A['ChapterURL'];
	local ChapterURLorigin = A:ORIGIN('ChapterURL');							-- get name of parameter that holds ChapterURL
	local ConferenceFormat = A['ConferenceFormat'];
	local ConferenceURL = A['ConferenceURL'];
	local ConferenceURLorigin = A:ORIGIN('ConferenceURL');						-- get name of parameter that holds ConferenceURL
	local Periodical = A['Periodical'];

	local Series = A['Series'];
	local Volume = A['Volume'];
	local Issue = A['Issue'];
	local Position = '';
	local Page = A['Page'];
	local Pages = hyphen_to_dash( A['Pages'] );	
	local At = A['At'];

	local Edition = A['Edition'];
	local PublicationPlace = A['PublicationPlace']
	local Place = A['Place'];
	
	local PublisherName = A['PublisherName'];
	local RegistrationRequired = A['RegistrationRequired'];
	local SubscriptionRequired = A['SubscriptionRequired'];
	local Via = A['Via'];
	local AccessDate = A['AccessDate'];
	local ArchiveDate = A['ArchiveDate'];
	local Agency = A['Agency'];
	local DeadURL = A['DeadURL']
	local Language = A['Language'];
	local Format = A['Format'];
	local ChapterFormat = A['ChapterFormat'];
	local DoiBroken = A['DoiBroken'];
	local ID = A['ID'];
	local ASINTLD = A['ASINTLD'];
	local IgnoreISBN = A['IgnoreISBN'];
	local Embargo = A['Embargo'];
	local Class = A['Class'];													-- arxiv class identifier

	local ID_list = extract_ids( args );

	local Quote = A['Quote'];

	local LayFormat = A['LayFormat'];
	local LayURL = A['LayURL'];
	local LaySource = A['LaySource'];
	local Transcript = A['Transcript'];
	local TranscriptFormat = A['TranscriptFormat'];
	local TranscriptURL = A['TranscriptURL'] 
	local TranscriptURLorigin = A:ORIGIN('TranscriptURL');						-- get name of parameter that holds TranscriptURL

	local LastAuthorAmp = A['LastAuthorAmp'];
	local no_tracking_cats = A['NoTracking'];

--these are used by cite interview
	local Callsign = A['Callsign'];
	local City = A['City'];
	local Program = A['Program'];

--local variables that are not cs1 parameters
	local use_lowercase;								-- controls capitalization of certain static text
	local this_page = mw.title.getCurrentTitle();		-- also used for COinS and for language
	local anchor_year;									-- used in the CITEREF identifier
	local COinS_date;									-- used in the COinS metadata

-- set default parameter values defined by |mode= parameter.  If |mode= is empty or omitted, use CitationClass to set these values
	local sepc;											-- separator between citation elements for CS1 a period, for CS2, a comma
	local PostScript;
	local Ref;
	sepc, PostScript, Ref = set_style (A['Mode']:lower(), A['PostScript'], A['Ref'], config.CitationClass);
	use_lowercase = ( sepc == ',' );					-- used to control capitalization for certain static text

--check this page to see if it is in one of the namespaces that cs1 is not supposed to add to the error categories
	if not is_set (no_tracking_cats) then										-- ignore if we are already not going to categorize this page
		if in_array (this_page.nsText, cfg.uncategorized_namespaces) then
			no_tracking_cats = "true";											-- set no_tracking_cats
		end
		for _,v in ipairs (cfg.uncategorized_subpages) do						-- cycle through page name patterns
			if this_page.text:match (v) then									-- test page name against each pattern
				no_tracking_cats = "true";										-- set no_tracking_cats
				break;															-- bail out if one is found
			end
		end
	end

-- check for extra |page=, |pages= or |at= parameters. 
	if is_set(Page) then
		if is_set(Pages) or is_set(At) then
			Page = Page .. " " .. set_error('extra_pages');						-- add error message
			Pages = '';															-- unset the others
			At = '';
		end
		extra_text_in_page_check (Page, NoPP);									-- add this page to maint cat if |page= value begins with what looks like p. or pp.
	elseif is_set(Pages) then
		if is_set(At) then
			Pages = Pages .. " " .. set_error('extra_pages');					-- add error messages
			At = '';															-- unset
		end
		extra_text_in_page_check (Pages, NoPP);									-- add this page to maint cat if |page= value begins with what looks like p. or pp.
	end	

-- both |publication-place= and |place= (|location=) allowed if different
	if not is_set(PublicationPlace) and is_set(Place) then
		PublicationPlace = Place;							-- promote |place= (|location=) to |publication-place
	end
	
	if PublicationPlace == Place then Place = ''; end		-- don't need both if they are the same
	
--[encyclopedia and |title then map |title to |article and |encyclopedia to |title
	|encyclopedia and |article then map |encyclopedia to |title
	|encyclopedia then map |encyclopedia to |title

	|trans_title maps to |trans_chapter when |title is re-mapped
	|url maps to |chapterurl when |title is remapped

All other combinations of |encyclopedia, |title, and |article are not modified
TODO: script-title to script-chapter if and when we support script-chapter](https://second-renaissance.fandom.com/wiki/Parameter_remapping_for_cite_encyclopedia:
When_the_citation_has_these_parameters:)

local Encyclopedia = A['Encyclopedia'];

	if ( config.CitationClass == "encyclopaedia" ) or ( config.CitationClass == "citation" and is_set (Encyclopedia)) then	-- test code for citation
		if is_set(Periodical) then					-- Periodical is set when |encyclopedia is set
			if is_set(Title) then
				if not is_set(Chapter) then
					Chapter = Title;				-- |encyclopedia and |title are set so map |title to |article and |encyclopedia to |title
					TransChapter = TransTitle;
					ChapterURL = URL;
					if not is_set (ChapterURL) and is_set (TitleLink) then
						Chapter= '[' .. Chapter .. '](https://second-renaissance.fandom.com/wiki/'_.._TitleLink_.._')';
					end
					Title = Periodical;
					ChapterFormat = Format;
					Periodical = '';				-- redundant so unset
					TransTitle = '';				-- redundant so unset
					URL = '';						-- redundant so unset
					Format = '';					-- redundant so unset
					TitleLink = '';					-- redundant so unset
				end
			else									-- |title not set
				Title = Periodical;					-- |encyclopedia set and |article set or not set so map |encyclopedia to |title
				Periodical = '';					-- redundant so unset
			end
		end
	end

-- Special case for cite techreport.
	if (config.CitationClass == "techreport") then	-- special case for cite techreport
		if is_set(Issue) then						-- cite techreport uses 'number', which other citations aliase to 'issue'
			if not is_set(ID) then					-- can we use ID for the "number"?
				ID = Issue;							-- yes, use it
				Issue = "";							-- unset Issue so that "number" isn't duplicated in the rendered citation or COinS metadata
			else									-- can't use ID so emit error message
				ID = ID .. " " .. set_error('redundant_parameters', '<code>&#124;id=</code> and <code>&#124;number=</code>');
			end
		end	
	end

-- special case for cite interview
	if (config.CitationClass == "interview") then
		if is_set(Program) then
			ID = ' ' .. Program;
		end
		if is_set(Callsign) then
			if is_set(ID) then
				ID = ID .. sepc .. ' ' .. Callsign;
			else
				ID = ' ' .. Callsign;
			end
		end
		if is_set(City) then
			if is_set(ID) then
				ID = ID .. sepc .. ' ' .. City;
			else
				ID = ' ' .. City;
			end
		end

		if is_set(Others) then
			if is_set(TitleType) then
				Others = ' ' .. TitleType .. ' with ' .. Others;
				TitleType = '';
			else
				Others = ' ' .. 'Interview with ' .. Others;
			end
		else
			Others = '(Interview)';
		end
	end

-- special case for cite mailing list
	if (config.CitationClass == "mailinglist") then
		Periodical = A ['MailingList'];
	end

-- Account for the oddity that is {{cite conference}}, before generation of COinS data.
	if 'conference' == config.CitationClass then
		if is_set(BookTitle) then
			Chapter = Title;
--			ChapterLink = TitleLink;											-- |chapterlink= is deprecated
			ChapterURL = URL;
			ChapterURLorigin = URLorigin;
			URLorigin = '';
			ChapterFormat = Format;
			TransChapter = TransTitle;
			Title = BookTitle;
			Format = '';
--			TitleLink = '';
			TransTitle = '';
			URL = '';
		end
	elseif 'speech' ~= config.CitationClass then
		Conference = '';														-- not cite conference or cite speech so make sure this is empty string
	end

-- cite map oddities
	local Cartography = "";
	local Scale = "";
	local Sheet = A['Sheet'] or '';
	local Sheets = A['Sheets'] or '';
	if config.CitationClass == "map" then
		Chapter = A['Map'];
		ChapterURL = A['MapURL'];
		TransChapter = A['TransMap'];
		ChapterURLorigin = A:ORIGIN('MapURL');
		ChapterFormat = A['MapFormat'];
		
		Cartography = A['Cartography'];
		if is_set( Cartography ) then
			Cartography = sepc .. " " .. wrap_msg ('cartography', Cartography, use_lowercase);
		end		
		Scale = A['Scale'];
		if is_set( Scale ) then
			Scale = sepc .. " " .. Scale;
		end
	end

-- Account for the oddities that are {{cite episode}} and {{cite serial}}, before generation of COinS data.
	if 'episode' == config.CitationClass or 'serial' == config.CitationClass then
		local AirDate = A['AirDate'];
		local Began = A['Began'];												-- these two are deprecated because the module understands date ranges
		local Ended = A['Ended'];
		local SeriesLink = A['SeriesLink'];
		local Network = A['Network'];
		local Station = A['Station'];
		local s, n = {}, {};

																				-- do common parameters first
		if is_set(Network) then table.insert(n, Network); end
		if is_set(Station) then table.insert(n, Station); end
		ID = table.concat(n, sepc .. ' ');
		
		if not is_set (Date) then												-- promote airdate or Began/Ended to date
			if is_set (AirDate) then
				Date = AirDate;
			elseif is_set (Began) then											-- deprecated
				if Began:match('%s') or Ended:match('%s') then					-- so we don't create errors: if either has spaces then
					Date = Began .. ' – ' .. Ended;								-- use spaced ndash as separator
				else
					Date = Began .. '–' .. Ended;								-- elsewise no spaces
				end
			end
		end

		if 'episode' == config.CitationClass then								-- handle the oddities that are strictly {{cite episode}}
			local Season = A['Season'];
			local SeriesNumber = A['SeriesNumber'];

			if is_set (Season) and is_set (SeriesNumber) then					-- these are mutually exclusive so if both are set
				table.insert( z.message_tail, { set_error( 'redundant_parameters', {wrap_style ('parameter', 'season') .. ' and ' .. wrap_style ('parameter', 'seriesno')}, true ) } );		-- add error message
				SeriesNumber = '';												-- unset; prefer |season= over |seriesno=
			end
																				-- assemble a table of parts concatenated later into Series
			if is_set(Season) then table.insert(s, wrap_msg ('season', Season, use_lowercase)); end
			if is_set(SeriesNumber) then table.insert(s, wrap_msg ('series', SeriesNumber, use_lowercase)); end
			if is_set(Issue) then table.insert(s, wrap_msg ('episode', Issue, use_lowercase)); end
			Issue = '';															-- unset because this is not a unique parameter
	
			Chapter = Title;													-- promote title parameters to chapter
			ChapterLink = TitleLink;											-- alias episodelink
			TransChapter = TransTitle;
			ChapterURL = URL;
			ChapterURLorigin = A:ORIGIN('URL');
			
			Title = Series;														-- promote series to title
			TitleLink = SeriesLink;
			Series = table.concat(s, sepc .. ' ');								-- this is concatenation of season, seriesno, episode number

			if is_set (ChapterLink) and not is_set (ChapterURL) then			-- link but not URL
				Chapter = '[' .. Chapter .. '](https://second-renaissance.fandom.com/wiki/'_.._ChapterLink_.._')';		-- ok to wikilink
			elseif is_set (ChapterLink) and is_set (ChapterURL) then			-- if both are set, URL links episode;
				Series = '[' .. Series .. '](https://second-renaissance.fandom.com/wiki/'_.._ChapterLink_.._')';			-- series links with ChapterLink (episodelink -> TitleLink -> ChapterLink) ugly
			end
			URL = '';															-- unset
			TransTitle = '';													-- unset
			
		else																	-- now oddities that are cite serial
			Issue = '';														-- unset because this parameter no longer supported by the citation/core version of cite serial
			Chapter = A['Episode'];												-- TODO: make |episode= available to cite episode someday?
			if is_set (Series) and is_set (SeriesLink) then
				Series = '[' .. Series .. '](https://second-renaissance.fandom.com/wiki/'_.._SeriesLink_.._')';
			end
			Series = wrap_style ('italic-title', Series);						-- series is italicized
		end	
	end
-- end of {{cite episode}} stuff

-- Account for the oddities that are {{cite arxiv}}, before generation of COinS data.
	if 'arxiv' == config.CitationClass then
		if not is_set (ID_list['ARXIV']) then									-- |arxiv= or |eprint= required for cite arxiv
			table.insert( z.message_tail, { set_error( 'arxiv_missing', {}, true ) } );		-- add error message
		elseif is_set (Series) then												-- series is an alias of version
			ID_list['ARXIV'] = ID_list['ARXIV'] .. Series;						-- concatenate version onto the end of the arxiv identifier
			Series = '';														-- unset
			deprecated_parameter ('version');									-- deprecated parameter but only for cite arxiv
		end
		
		if first_set (AccessDate, At, Chapter, Format, Page, Pages, Periodical, PublisherName, URL,	-- a crude list of parameters that are not supported by cite arxiv
			ID_list['ASIN'], ID_list['BIBCODE'], ID_list['DOI'], ID_list['ISBN'], ID_list['ISSN'],
			ID_list['JFM'], ID_list['JSTOR'], ID_list['LCCN'], ID_list['MR'], ID_list['OCLC'], ID_list['OL'],
			ID_list['OSTI'], ID_list['PMC'], ID_list['PMID'], ID_list['RFC'], ID_list['SSRN'], ID_list['USENETID'], ID_list['ZBL']) then
				table.insert( z.message_tail, { set_error( 'arxiv_params_not_supported', {}, true ) } );		-- add error message

				AccessDate= '';													-- set these to empty string; not supported in cite arXiv
				PublisherName = '';												-- (if the article has been published, use cite journal, or other)
				Chapter = '';
				URL = '';
				Format = '';
				Page = ''; Pages = ''; At = '';
		end
		Periodical = 'arXiv';													-- set to arXiv for COinS; after that, must be set to empty string
	end

-- handle type parameter for those CS1 citations that have default values

	if in_array(config.CitationClass, {"AV-media-notes", "DVD-notes", "mailinglist", "map", "podcast", "pressrelease", "report", "techreport", "thesis"}) then
		TitleType = set_titletype (config.CitationClass, TitleType);
		if is_set(Degree) and "Thesis" == TitleType then						-- special case for cite thesis
			TitleType = Degree .. " thesis";
		end
	end

	if is_set(TitleType) then													-- if type parameter is specified
		TitleType = " (" .. TitleType .. ")";									-- display it in parentheses
	end

-- legacy: promote concatenation of |month=, and |year= to Date if Date not set; or, promote PublicationDate to Date if neither Date nor Year are set.
	if not is_set (Date) then
		Date = Year;						-- promote Year to Date
		Year = nil;							-- make nil so Year as empty string isn't used for CITEREF
		if is_set(Date) then
			local Month = A['Month'];
			if is_set(Month) then
				Date = Month .. " " .. Date;
			end
		elseif is_set(PublicationDate) then	-- use PublicationDate when |date= and |year= are not set
			Date = PublicationDate;			-- promote PublicationDate to Date
			PublicationDate = '';			-- unset, no longer needed
		end
	end

	if PublicationDate == Date then PublicationDate = ''; end	-- if PublicationDate is same as Date, don't display in rendered citation

--[Go test all of the date-holding parameters for valid MOS:DATE format and make sure that dates are real dates. This must be done before we do COinS because here is where
we get the date used in the metadata.

Date validation supporting code is in Module:Citation/CS1/Date_validation](https://second-renaissance.fandom.com/wiki/Go_test_all_of_the_date-holding_parameters_for_valid_MOS:DATE_format_and_make_sure_that_dates_are_real_dates._This_must_be_done_before_we_do_COinS_because_here_is_where
we_get_the_date_used_in_the_metadata.

Date_validation_supporting_code_is_in_Module:Citation/CS1/Date_validation)
	do	-- create defined block to contain local variables error_message and mismatch
		local error_message = '';
																				-- AirDate has been promoted to Date so not necessary to check it
		anchor_year, COinS_date, error_message = dates({['accessdate']=AccessDate, ['archivedate']=ArchiveDate, ['date']=Date, ['doi_brokendate']=DoiBroken,
			['embargo']=Embargo, ['laydate']=LayDate, ['publicationdate']=PublicationDate, ['year']=Year});

		if is_set (Year) and is_set (Date) then									-- both |date= and |year= not normally needed; 
			local mismatch = year_date_check (Year, Date)
			if 0 == mismatch then												-- |year= does not match a year-value in |date=
				if is_set (error_message) then									-- if there is already an error message
					error_message = error_message .. ', ';						-- tack on this additional message
				end
				error_message = error_message .. '&#124;year= / &#124;date= mismatch';
			elseif 1 == mismatch then											-- |year= matches year-value in |date=
				add_maint_cat ('date_year');
			end
		end

		if is_set(error_message) then
			table.insert( z.message_tail, { set_error( 'bad_date', {error_message}, true ) } );	-- add this error message
		end
	end	-- end of do

-- Account for the oddity that is {{cite journal}} with |pmc= set and |url= not set.  Do this after date check but before COInS.
-- Here we unset Embargo if PMC not embargoed (|embargo= not set in the citation) or if the embargo time has expired. Otherwise, holds embargo date
	Embargo = is_embargoed (Embargo);											-- 

	if config.CitationClass == "journal" and not is_set(URL) and is_set(ID_list['PMC']) then
		if not is_set (Embargo) then											-- if not embargoed or embargo has expired
			URL=cfg.id_handlers['PMC'].prefix .. ID_list['PMC'];				-- set url to be the same as the PMC external link if not embargoed
			URLorigin = cfg.id_handlers['PMC'].parameters[1];					-- set URLorigin to parameter name for use in error message if citation is missing a |title=
		end
	end

-- At this point fields may be nil if they weren't specified in the template use.  We can use that fact.
	-- Test if citation has no title
	if	not is_set(Title) and
		not is_set(TransTitle) and
		not is_set(ScriptTitle) then
		table.insert( z.message_tail, { set_error( 'citation_missing_title', {}, true ) } );
	end
	
	if 'none' == Title and is_set(Periodical) and not (( config.CitationClass == "encyclopaedia" ) or ( config.CitationClass == "citation" and is_set (Encyclopedia))) then								-- special case
		Title = '';																-- set title to empty string
		add_maint_cat ('untitled');
	end

	-- COinS metadata (see <http://ocoins.info/>) for automated parsing of citation information.
	-- handle the oddity that is cite encyclopedia and {{citation |encyclopedia=something}}. Here we presume that
	-- when Periodical, Title, and Chapter are all set, then Periodical is the book (encyclopedia) title, Title
	-- is the article title, and Chapter is a section within the article.  So, we remap 
	
	local coins_chapter = Chapter;												-- default assuming that remapping not required
	local coins_title = Title;													-- et tu
	if 'encyclopaedia' == config.CitationClass or ('citation' == config.CitationClass and is_set (Encyclopedia)) then
		if is_set (Chapter) and is_set (Title) and is_set (Periodical) then		-- if all are used then
			coins_chapter = Title;												-- remap
			coins_title = Periodical;
		end
	end
	
	-- this is the function call to COinS()
	local OCinSoutput = COinS({
		['Periodical'] = Periodical,
		['Chapter'] = strip_apostrophe_markup (coins_chapter),					-- Chapter stripped of bold / italic wikimarkup
		['Title'] = make_coins_title (coins_title, ScriptTitle),				-- Title and ScriptTitle stripped of bold / italic wikimarkup
		['PublicationPlace'] = PublicationPlace,
		['Date'] = first_set(COinS_date, Date),		-- COinS_date has correctly formatted date if Date is valid; any reason to keep Date here?  Should we be including invalid dates in metadata?
		['Series'] = Series,
		['Volume'] = Volume,
		['Issue'] = Issue,
		['Pages'] = get_coins_pages (first_set(Sheet, Sheets, Page, Pages, At)),				-- pages stripped of external links
		['Edition'] = Edition,
		['PublisherName'] = PublisherName,
		['URL'] = first_set( URL, ChapterURL ),
		['Authors'] = a,
		['ID_list'] = ID_list,
		['RawPage'] = this_page.prefixedText,
	}, config.CitationClass);

-- Account for the oddities that are {{cite arxiv}}, AFTER generation of COinS data.
	if 'arxiv' == config.CitationClass then										-- we have set rft.jtitle in COinS to arXiv, now unset so it isn't displayed
		Periodical = '';														-- periodical not allowed in cite arxiv; if article has been published, use cite journal
	end

-- special case for cite newsgroup.  Do this after COinS because we are modifying Publishername to include some static text
	if 'newsgroup' == config.CitationClass then
		if is_set (PublisherName) then
			PublisherName = '[Newsgroup](https://second-renaissance.fandom.com/wiki/Usenet_newsgroup):&nbsp;' ..  external_link( 'news:' .. PublisherName, PublisherName );
		end
	end



	-- Now perform various field substitutions.
	-- We also add leading spaces and surrounding markup and punctuation to the
	-- various parts of the citation, but only when they are non-nil.
	do																			-- do-block to limit scope of last_first_list
		local last_first_list;
		local maximum = A['DisplayAuthors'];

		maximum , author_etal = get_display_authors_editors (maximum, #a, 'authors', author_etal);

		local control = { 
			format = NameListFormat,											-- empty string or 'vanc'
			maximum = maximum,
			lastauthoramp = LastAuthorAmp,
			page_name = this_page.text											-- get current page name so that we don't wikilink to it via authorlinkn
			};
		
		if is_set(Coauthors) then												-- if the coauthor field is also used, prevent ampersand and et al. formatting.
			control.lastauthoramp = nil;
			control.maximum = #a + 1;
		end
		
		last_first_list = list_people(control, a, author_etal);

		if is_set (Authors) then
			Authors, author_etal = name_has_etal (Authors, author_etal, false);	-- find and remove variations on et al.
			if author_etal then
				Authors = Authors .. ' ' .. cfg.messages['et al'];				-- add et al. to authors parameter
			end
		else
			Authors = last_first_list;											-- either an author name list or an empty string
		end

	end																			-- end of do

	if not is_set(Authors) and is_set(Coauthors) then	-- coauthors aren't displayed if one of authors=, authorn=, or lastn= isn't specified
		table.insert( z.message_tail, { set_error('coauthors_missing_author', {}, true) } );	-- emit error message
	end

	local EditorCount;															-- used only for choosing {ed.) or (eds.) annotation at end of editor name-list
	do
		local last_first_list;
		local maximum = A['DisplayEditors'];

		maximum , editor_etal = get_display_authors_editors (maximum, #e, 'editors', editor_etal);
		-- Preserve old-style implicit et al.
		if not is_set(maximum) and #e == 4 then 
			maximum = 3;
			table.insert( z.message_tail, { set_error('implict_etal_editor', {}, true) } );
		end

		local control = { 
			format = NameListFormat,											-- empty string or 'vanc'
			maximum = maximum,
			lastauthoramp = LastAuthorAmp,
			page_name = this_page.text											-- get current page name so that we don't wikilink to it via editorlinkn
		};

		last_first_list, EditorCount = list_people(control, e, editor_etal);

		if is_set (Editors) then
			if editor_etal then
				Editors = Editors .. ' ' .. cfg.messages['et al'];				-- add et al. to editors parameter beause |display-editors=etal
				EditorCount = 2;												-- with et al., |editors= is multiple names; spoof to display (eds.) annotation
			else
				EditorCount = 2;												-- we don't know but assume |editors= is multiple names; spoof to display (eds.) annotation
			end
		else
			Editors = last_first_list;											-- either an author name list or an empty string
		end

		if 1 == EditorCount and (true == editor_etal or 1 < #e) then			-- only one editor displayed but includes etal then 
			EditorCount = 2;													-- spoof to display (eds.) annotation
		end
	end


-- apply |[xx-]format= styling; at the end, these parameters hold correctly styled format annotation,
-- an error message if the associated url is not set, or an empty string for concatenation
	ArchiveFormat = style_format (ArchiveFormat, ArchiveURL, 'archive-format', 'archive-url');
	ChapterFormat = style_format (ChapterFormat, ChapterURL, 'chapter-format', 'chapter-url');
	ConferenceFormat = style_format (ConferenceFormat, ConferenceURL, 'conference-format', 'conference-url');
	Format = style_format (Format, URL, 'format', 'url');
	LayFormat = style_format (LayFormat, LayURL, 'lay-format', 'lay-url');
	TranscriptFormat = style_format (TranscriptFormat, TranscriptURL, 'transcript-format', 'transcripturl');

	if  not is_set(URL) then --and
--		not is_set(ArchiveURL) then --and										-- prevents format_missing_url error from registering
--		not is_set(ConferenceURL) and											-- TODO: keep this here? conference as part of cite web or cite podcast?
--		not is_set(TranscriptURL) then											-- TODO: remove? |transcript-url= and |transcript= has separate test
		
		-- Test if cite web or cite podcast |url= is missing or empty 
		if in_array(config.CitationClass, {"web","podcast", "mailinglist"}) then	
			table.insert( z.message_tail, { set_error( 'cite_web_url', {}, true ) } );
		end
		
		-- Test if accessdate is given without giving a URL
		if is_set(AccessDate) and not is_set(ChapterURL)then					-- ChapterURL may be set when the others are not set; TODO: move this to a separate test?
			table.insert( z.message_tail, { set_error( 'accessdate_missing_url', {}, true ) } );
			AccessDate = '';
		end
	end

	local OriginalURL, OriginalFormat;											-- TODO: swap chapter and title here so that archive applies to most specific if both are set?
	DeadURL = DeadURL:lower();													-- used later when assembling archived text
	if is_set( ArchiveURL ) then
		if is_set (URL) then
			OriginalURL = URL;													-- save copy of original source URL
			OriginalFormat = Format;											-- and original |format=
			if 'no' ~= DeadURL then												-- if URL set then archive-url applies to it
				URL = ArchiveURL												-- swap-in the archive's url
				URLorigin = A:ORIGIN('ArchiveURL')								-- name of archive url parameter for error messages
				Format = ArchiveFormat or '';									-- swap in archive's format
			end
		elseif is_set (ChapterURL) then 										-- URL not set so if chapter-url is set apply archive url to it
			OriginalURL = ChapterURL;											-- save copy of source chapter's url for archive text
			OriginalFormat = ChapterFormat;										-- and original |format=
			if 'no' ~= DeadURL then
				ChapterURL = ArchiveURL											-- swap-in the archive's url
				URLorigin = A:ORIGIN('ArchiveURL')								-- name of archive url parameter for error messages
				ChapterFormat = ArchiveFormat or '';							-- swap in archive's format
			end
		end
	end

	if in_array(config.CitationClass, {"web","news","journal","pressrelease","podcast", "newsgroup", 'arxiv'}) or
		('citation' == config.CitationClass and is_set (Periodical) and not is_set (Encyclopedia)) then
			if is_set (Chapter) or is_set (TransChapter) or is_set (ChapterURL)then	-- chapter parameters not supported for these citation types
				table.insert( z.message_tail, { set_error( 'chapter_ignored', {}, true ) } );		-- add error message
				Chapter = '';														-- set to empty string to be safe with concatenation
				TransChapter = '';
				ChapterURL = '';
			end
	else																		-- otherwise, format chapter / article title
		Chapter = format_chapter_title (Chapter, TransChapter, ChapterURL, ChapterURLorigin);
		if is_set (Chapter) then
			if 'map' == config.CitationClass and is_set (TitleType) then
				Chapter = Chapter .. ' ' .. TitleType;
			end
			Chapter = Chapter .. ChapterFormat .. sepc .. ' ';
		end
	end

	-- Format main title.
	if is_set(TitleLink) and is_set(Title) then
		Title = "[" .. Title .. "](https://second-renaissance.fandom.com/wiki/"_.._TitleLink_.._")"
	end

	if in_array(config.CitationClass, {"web","news","journal","pressrelease","podcast", "newsgroup", "mailinglist", 'arxiv'}) or
		('citation' == config.CitationClass and is_set (Periodical) and not is_set (Encyclopedia)) or
		('map' == config.CitationClass and is_set (Periodical)) then			-- special case for cite map when the map is in a periodical treat as an article
			Title = kern_quotes (Title);										-- if necessary, separate title's leading and trailing quote marks from Module provided quote marks
			Title = wrap_style ('quoted-title', Title);
	
			Title = script_concatenate (Title, ScriptTitle);					-- <bdi> tags, lang atribute, categorization, etc; must be done after title is wrapped
			TransTitle= wrap_style ('trans-quoted-title', TransTitle );
	elseif 'report' == config.CitationClass then								-- no styling for cite report
		Title = script_concatenate (Title, ScriptTitle);						-- <bdi> tags, lang atribute, categorization, etc; must be done after title is wrapped
		TransTitle= wrap_style ('trans-quoted-title', TransTitle );				-- for cite report, use this form for trans-title
	else
		Title = wrap_style ('italic-title', Title);
		Title = script_concatenate (Title, ScriptTitle);						-- <bdi> tags, lang atribute, categorization, etc; must be done after title is wrapped
		TransTitle = wrap_style ('trans-italic-title', TransTitle);
	end

	TransError = "";
	if is_set(TransTitle) then
		if is_set(Title) then
			TransTitle = " " .. TransTitle;
		else
			TransError = " " .. set_error( 'trans_missing_title' );
		end
	end
	
	Title = Title .. TransTitle;
	
	if is_set(Title) then
		if not is_set(TitleLink) and is_set(URL) then 
			Title = external_link( URL, Title ) .. TransError .. Format;
			URL = "";
			Format = "";
		else
			Title = Title .. TransError;
		end
	end

	if is_set(Place) then
		Place = " " .. wrap_msg ('written', Place, use_lowercase) .. sepc .. " ";
	end

	if is_set (Conference) then
		if is_set (ConferenceURL) then
			Conference = external_link( ConferenceURL, Conference );
		end
		Conference = sepc .. " " .. Conference .. ConferenceFormat;
	elseif is_set(ConferenceURL) then
		Conference = sepc .. " " .. external_link( ConferenceURL, nil, ConferenceURLorigin );
	end

	if not is_set(Position) then
		local Minutes = A['Minutes'];
		if is_set(Minutes) then
			Position = " " .. Minutes .. " " .. cfg.messages['minutes'];
		else
			local Time = A['Time'];
			if is_set(Time) then
				local TimeCaption = A['TimeCaption']
				if not is_set(TimeCaption) then
					TimeCaption = cfg.messages['event'];
					if sepc ~= '.' then
						TimeCaption = TimeCaption:lower();
					end
				end
				Position = " " .. TimeCaption .. " " .. Time;
			end
		end
	else
		Position = " " .. Position;
		At = '';
	end
	
	if not is_set(Page) then
		if is_set(Pages) then
			if is_set(Periodical) and
				not in_array(config.CitationClass, {"encyclopaedia","web","book","news","podcast"}) then
				Pages = ": " .. Pages;
			elseif tonumber(Pages) ~= nil then
				Pages = sepc .." " .. PPrefix .. Pages;
			else
				Pages = sepc .." " .. PPPrefix .. Pages;
			end
		end
	else
		if is_set(Periodical) and
			not in_array(config.CitationClass, {"encyclopaedia","web","book","news","podcast"}) then
			Page = ": " .. Page;
		else
			Page = sepc .." " .. PPrefix .. Page;
		end
	end

	if 'map' == config.CitationClass then										-- cite map oddity done after COinS call (and with other in-source locators)
		if is_set (Sheet) or is_set (Sheets) then
			local err_msg1 = 'sheet=, &#124;sheets';							-- default error message in case any of page pages or at are set
			local err_msg2;
			if is_set (Page) or is_set (Pages) or is_set (At) then				-- are any set?
				err_msg2 = 'page=, &#124;pages=, &#124;at';						-- a generic error message
				Page = ''; Pages = ''; At = '';
			elseif is_set (Sheet) and is_set (Sheets) then						-- if both are set make error message
				err_msg1 = 'sheet';
				err_msg2 = 'sheets';
			end
			if is_set (err_msg2) then
				table.insert( z.message_tail, { set_error( 'redundant_parameters', {wrap_style ('parameter', err_msg1) .. ' and ' .. wrap_style ('parameter', err_msg2)}, true ) } );		-- add error message
			end
			if not is_set (Sheet) then											-- do sheet static text and formatting; Sheet has priority over Sheets if both provided
				if is_set (Sheets) then
					if is_set (Periodical) then
						Sheet = ": Sheets " .. Sheets;							-- because Sheet has priority, no need to support both later on
					else
						Sheet = sepc .. " Sheets " .. Sheets;
					end
				end
			else
				if is_set (Periodical) then
					Sheet = ": Sheet " .. Sheet;
				else
					Sheet = sepc .. " Sheet " .. Sheet;
				end
			end
		end
	end

	At = is_set(At) and (sepc .. " " .. At) or "";
	Position = is_set(Position) and (sepc .. " " .. Position) or "";
	if config.CitationClass == 'map' then
		local Section = A['Section'];
		local Sections = A['Sections'];
		local Inset = A['Inset'];
		
		if is_set( Inset ) then
			Inset = sepc .. " " .. wrap_msg ('inset', Inset, use_lowercase);
		end			

		if is_set( Sections ) then
			Section = sepc .. " " .. wrap_msg ('sections', Sections, use_lowercase);
		elseif is_set( Section ) then
			Section = sepc .. " " .. wrap_msg ('section', Section, use_lowercase);
		end
		At = At .. Inset .. Section;		
	end	

	if is_set (Language) then
		Language = language_parameter (Language);								-- format, categories, name from ISO639-1, etc
	else
		Language="";															-- language not specified so make sure this is an empty string;
	end

	Others = is_set(Others) and (sepc .. " " .. Others) or "";

	TitleNote = is_set(TitleNote) and (sepc .. " " .. TitleNote) or "";
	if is_set (Edition) then
		if Edition:match ('[Ee]d%.?$') or Edition:match ('[Ee]dition$') then
			add_maint_cat ('extra_text', 'edition');
		end
		Edition = " " .. wrap_msg ('edition', Edition);
	else
		Edition = '';
	end
	Issue = is_set(Issue) and (" (" .. Issue .. ")") or "";
	Series = is_set(Series) and (sepc .. " " .. Series) or "";
	OrigYear = is_set(OrigYear) and (" [" .. OrigYear .. "]") or "";
	Agency = is_set(Agency) and (sepc .. " " .. Agency) or "";

	if is_set(Volume) then
		if ( mw.ustring.len(Volume) > 4 )
		  then Volume = sepc .." " .. Volume;
		  else Volume = " <b>" .. hyphen_to_dash(Volume) .. "</b>";
		end
	end

	------------------------------------ totally unrelated data
	if is_set(Via) then
		Via = " " .. wrap_msg ('via', Via);
	end

--[Subscription implies paywall; Registration does not.  If both are used in a citation, the subscription required link
note is displayed. There are no error messages for this condition.](https://second-renaissance.fandom.com/wiki/Subscription_implies_paywall;_Registration_does_not.__If_both_are_used_in_a_citation,_the_subscription_required_link
note_is_displayed._There_are_no_error_messages_for_this_condition.)
	if in_array(SubscriptionRequired:lower(), {'yes', 'true', 'y'}) then
		SubscriptionRequired = sepc .. " " .. cfg.messages['subscription'];		-- subscription required message
	elseif in_array(RegistrationRequired:lower(), {'yes', 'true', 'y'}) then
		SubscriptionRequired = sepc .. " " .. cfg.messages['registration'];		-- registration required message
	else
		SubscriptionRequired = '';												-- either or both might be set to something other than yes true y
	end

	if is_set(AccessDate) then
		local retrv_text = " " .. cfg.messages['retrieved']

		AccessDate = nowrap_date (AccessDate);									-- wrap in nowrap span if date in appropriate format
		if (sepc ~= ".") then retrv_text = retrv_text:lower() end				-- if 'citation', lower case
		AccessDate = substitute (retrv_text, AccessDate);						-- add retrieved text
																				-- neither of these work; don't know why; it seems that substitute() isn't being called	
		AccessDate = substitute (cfg.presentation['accessdate'], {sepc, AccessDate});	-- allow editors to hide accessdates
	end
	
	if is_set(ID) then ID = sepc .." ".. ID; end
   	if "thesis" == config.CitationClass and is_set(Docket) then
		ID = sepc .." Docket ".. Docket .. ID;
	end
   	if "report" == config.CitationClass and is_set(Docket) then					-- for cite report when |docket= is set
		ID = sepc .. ' ' .. Docket;												-- overwrite ID even if |id= is set
	end

	ID_list = build_id_list( ID_list, {DoiBroken = DoiBroken, ASINTLD = ASINTLD, IgnoreISBN = IgnoreISBN, Embargo=Embargo, Class = Class} );

	if is_set(URL) then
		URL = " " .. external_link( URL, nil, URLorigin );
	end

	if is_set(Quote) then
		if Quote:sub(1,1) == '"' and Quote:sub(-1,-1) == '"' then
			Quote = Quote:sub(2,-2);
		end
		Quote = sepc .." " .. wrap_style ('quoted-text', Quote ); 				-- wrap in <q>...</q> tags
		PostScript = "";														-- CS1 does not supply terminal punctuation when |quote= is set
	end
	
	local Archived
	if is_set(ArchiveURL) then
		if not is_set(ArchiveDate) then
			ArchiveDate = set_error('archive_missing_date');
		end
		if "no" == DeadURL then
			local arch_text = cfg.messages['archived'];
			if sepc ~= "." then arch_text = arch_text:lower() end
			Archived = sepc .. " " .. substitute( cfg.messages['archived-not-dead'],
				{ external_link( ArchiveURL, arch_text ) .. ArchiveFormat, ArchiveDate } );
			if not is_set(OriginalURL) then
				Archived = Archived .. " " .. set_error('archive_missing_url');							   
			end
		elseif is_set(OriginalURL) then
			local arch_text = cfg.messages['archived-dead'];
			if sepc ~= "." then arch_text = arch_text:lower() end
			Archived = sepc .. " " .. substitute( arch_text,
				{ external_link( OriginalURL, cfg.messages['original'] ) .. OriginalFormat, ArchiveDate } );	-- format already styled
		else
			local arch_text = cfg.messages['archived-missing'];
			if sepc ~= "." then arch_text = arch_text:lower() end
			Archived = sepc .. " " .. substitute( arch_text, 
				{ set_error('archive_missing_url'), ArchiveDate } );
		end
	elseif is_set (ArchiveFormat) then
		Archived = ArchiveFormat;												-- if set and ArchiveURL not set ArchiveFormat has error message
	else
		Archived = ""
	end
	
	local Lay = '';
	if is_set(LayURL) then
		if is_set(LayDate) then LayDate = " (" .. LayDate .. ")" end
		if is_set(LaySource) then 
			LaySource = " &ndash; ''" .. safe_for_italics(LaySource) .. "''";
		else
			LaySource = "";
		end
		if sepc == '.' then
			Lay = sepc .. " " .. external_link( LayURL, cfg.messages['lay summary'] ) .. LayFormat .. LaySource .. LayDate
		else
			Lay = sepc .. " " .. external_link( LayURL, cfg.messages['lay summary']:lower() ) .. LayFormat .. LaySource .. LayDate
		end			
	elseif is_set (LayFormat) then												-- Test if |lay-format= is given without giving a |lay-url=
		Lay = sepc .. LayFormat;												-- if set and LayURL not set, then LayFormat has error message
	end

	if is_set(Transcript) then
		if is_set(TranscriptURL) then
			Transcript = external_link( TranscriptURL, Transcript );
		end
		Transcript = sepc .. ' ' .. Transcript .. TranscriptFormat;
	elseif is_set(TranscriptURL) then
		Transcript = external_link( TranscriptURL, nil, TranscriptURLorigin );
	end

	local Publisher;
	if is_set(Periodical) and
		not in_array(config.CitationClass, {"encyclopaedia","web","pressrelease","podcast"}) then
		if is_set(PublisherName) then
			if is_set(PublicationPlace) then
				Publisher = PublicationPlace .. ": " .. PublisherName;
			else
				Publisher = PublisherName;  
			end
		elseif is_set(PublicationPlace) then
			Publisher= PublicationPlace;
		else 
			Publisher = "";
		end
		if is_set(PublicationDate) then
			if is_set(Publisher) then
				Publisher = Publisher .. ", " .. wrap_msg ('published', PublicationDate);
			else
				Publisher = PublicationDate;
			end
		end
		if is_set(Publisher) then
			Publisher = " (" .. Publisher .. ")";
		end
	else
		if is_set(PublicationDate) then
			PublicationDate = " (" .. wrap_msg ('published', PublicationDate) .. ")";
		end
		if is_set(PublisherName) then
			if is_set(PublicationPlace) then
				Publisher = sepc .. " " .. PublicationPlace .. ": " .. PublisherName .. PublicationDate;
			else
				Publisher = sepc .. " " .. PublisherName .. PublicationDate;  
			end			
		elseif is_set(PublicationPlace) then 
			Publisher= sepc .. " " .. PublicationPlace .. PublicationDate;
		else 
			Publisher = PublicationDate;
		end
	end
	
	-- Several of the above rely upon detecting this as nil, so do it last.
	if is_set(Periodical) then
		if is_set(Title) or is_set(TitleNote) then 
			Periodical = sepc .. " " .. wrap_style ('italic-title', Periodical) 
		else 
			Periodical = wrap_style ('italic-title', Periodical)
		end
	end

--[department=) and forces it to be " (Speech)" so that
the annotation directly follows the |title= parameter value in the citation rather than the |event= parameter value (if provided).](https://second-renaissance.fandom.com/wiki/Handle_the_oddity_that_is_cite_speech.__This_code_overrides_whatever_may_be_the_value_assigned_to_TitleNote_(through)
	if "speech" == config.CitationClass then				-- cite speech only
		TitleNote = " (Speech)";							-- annotate the citation
		if is_set (Periodical) then							-- if Periodical, perhaps because of an included |website= or |journal= parameter 
			if is_set (Conference) then						-- and if |event= is set
				Conference = Conference .. sepc .. " ";		-- then add appropriate punctuation to the end of the Conference variable before rendering
			end
		end
	end

	-- Piece all bits together at last.  Here, all should be non-nil.
	-- We build things this way because it is more efficient in LUA
	-- not to keep reassigning to the same string variable over and over.

	local tcommon
	if in_array(config.CitationClass, {"journal","citation"}) and is_set(Periodical) then
		if is_set(Others) then Others = Others .. sepc .. " " end
		tcommon = safe_join( {Others, Title, TitleNote, Conference, Periodical, Format, TitleType, Series, 
			Language, Edition, Publisher, Agency, Volume, Issue}, sepc );
		
	elseif 'map' == config.CitationClass then									-- special cases for cite map
		if is_set (Chapter) then												-- map in a book; TitleType is part of Chapter
			tcommon = safe_join( {Title, Format, Edition, Scale, Series, Language, Cartography, Others, Publisher, Volume}, sepc );
		elseif is_set (Periodical) then											-- map in a periodical
			tcommon = safe_join( {Title, TitleType, Format, Periodical, Scale, Series, Language, Cartography, Others, Publisher, Volume, Issue}, sepc );
		else																	-- a sheet or stand-alone map
			tcommon = safe_join( {Title, TitleType, Format, Edition, Scale, Series, Language, Cartography, Others, Publisher}, sepc );
		end
		
	elseif 'episode' == config.CitationClass then								-- special case for cite episode
		tcommon = safe_join( {Title, TitleNote, TitleType, Series, Transcript, Language, Edition, Publisher}, sepc );
	else																		-- all other CS1 templates
		tcommon = safe_join( {Title, TitleNote, Conference, Periodical, Format, TitleType, Series, Language, 
			Volume, Issue, Others, Edition, Publisher, Agency}, sepc );
	end
	
	if #ID_list > 0 then
		ID_list = safe_join( { sepc .. " ",  table.concat( ID_list, sepc .. " " ), ID }, sepc );
	else
		ID_list = ID;
	end
	
	local idcommon = safe_join( { ID_list, URL, Archived, AccessDate, Via, SubscriptionRequired, Lay, Quote }, sepc );
	local text;
	local pgtext = Position .. Sheet .. Page .. Pages .. At;
	
	if is_set(Authors) then
		if is_set(Coauthors) then
			local sep = '; ';
			if 'vanc' == NameListFormat then
				sep = ', ';
			end
			Authors = Authors .. sep .. Coauthors;
		end
		if is_set(Date) then
			Date = " ("..Date..")" .. OrigYear .. sepc .. " "
		elseif string.sub(Authors,-1,-1) == sepc then
			Authors = Authors .. " "
		else
			Authors = Authors .. sepc .. " "
		end
		if is_set(Editors) then
			local in_text = " ";
			local post_text = "";
			if is_set(Chapter) then
				in_text = in_text .. cfg.messages['in'] .. " "
			else
				if EditorCount <= 1 then
					post_text = ", " .. cfg.messages['editor'];
				else
					post_text = ", " .. cfg.messages['editors'];
				end
			end 
			if (sepc ~= '.') then in_text = in_text:lower() end
			Editors = in_text .. Editors .. post_text;
			if (string.sub(Editors,-1,-1) == sepc) or (string.sub(Editors,-3,-1) == sepc .. ']]') then	-- if last editor name ends with sepc char
				Editors = Editors .. " ";										-- don't add another
			else
				Editors = Editors .. sepc .. " "								-- otherwise terninate the editor list
			end
		end
		text = safe_join( {Authors, Date, Chapter, Place, Editors, tcommon }, sepc );
		text = safe_join( {text, pgtext, idcommon}, sepc );
	elseif is_set(Editors) then
		if is_set(Date) then
			if EditorCount <= 1 then
				Editors = Editors .. ", " .. cfg.messages['editor'];
			else
				Editors = Editors .. ", " .. cfg.messages['editors'];
			end
			Date = " (" .. Date ..")" .. OrigYear .. sepc .. " "
		else
			if EditorCount <= 1 then
				Editors = Editors .. " (" .. cfg.messages['editor'] .. ")" .. sepc .. " "
			else
				Editors = Editors .. " (" .. cfg.messages['editors'] .. ")" .. sepc .. " "
			end
		end
		text = safe_join( {Editors, Date, Chapter, Place, tcommon}, sepc );
		text = safe_join( {text, pgtext, idcommon}, sepc );
	else
		if is_set(Date) then
			if ( string.sub(tcommon,-1,-1) ~= sepc )
			  then Date = sepc .." " .. Date .. OrigYear
			  else Date = " " .. Date .. OrigYear
			end
		end
		if config.CitationClass=="journal" and is_set(Periodical) then
			text = safe_join( {Chapter, Place, tcommon}, sepc );
			text = safe_join( {text, pgtext, Date, idcommon}, sepc );
		else
			text = safe_join( {Chapter, Place, tcommon, Date}, sepc );
			text = safe_join( {text, pgtext, idcommon}, sepc );
		end
	end
	
	if is_set(PostScript) and PostScript ~= sepc then
		text = safe_join( {text, sepc}, sepc );  --Deals with italics, spaces, etc.
		text = text:sub(1,-sepc:len()-1);
	end	
	
	text = safe_join( {text, PostScript}, sepc );

	-- Now enclose the whole thing in a <span/> element
	local options = {};
	
	if is_set(config.CitationClass) and config.CitationClass ~= "citation" then
		options.class = "citation " .. config.CitationClass;
	else
		options.class = "citation";
	end
	
	if is_set(Ref) and Ref:lower() ~= "none" then
		local id = Ref
		if ( "harv" == Ref ) then
			local names = {} --table of last names & year
			if #a > 0 then
				for i,v in ipairs(a) do 
					names[i] = v.last 
					if i == 4 then break end
				end
			elseif #e > 0 then
				for i,v in ipairs(e) do 
					names[i] = v.last 
					if i == 4 then break end				
				end
			end
			names[ #names + 1 ] = first_set(Year, anchor_year);	-- Year first for legacy citations and for YMD dates that require disambiguation
			id = anchor_id(names)
		end
		options.id = id;
	end
	
	if string.len(text:gsub("<span[^>/]*>.-</span>", ""):gsub("%b<>","")) <= 2 then
		z.error_categories = {};
		text = set_error('empty_citation');
		z.message_tail = {};
	end
	
	if is_set(options.id) then 
		text = '<span id="' .. mw.uri.anchorEncode(options.id) ..'" class="' .. mw.text.nowiki(options.class) .. '">' .. text .. "</span>";
	else
		text = '<span class="' .. mw.text.nowiki(options.class) .. '">' .. text .. "</span>";
	end		

	local empty_span = '<span style="display:none;">&nbsp;</span>';
	
	-- Note: Using display: none on then COinS span breaks some clients.
	local OCinS = '<span title="' .. OCinSoutput .. '" class="Z3988">' .. empty_span .. '</span>';
	text = text .. OCinS;
	
	if #z.message_tail ~= 0 then
		text = text .. " ";
		for i,v in ipairs( z.message_tail ) do
			if is_set(v[1]) then
				if i == #z.message_tail then
					text = text .. error_comment( v[1], v[2] );
				else
					text = text .. error_comment( v[1] .. "; ", v[2] );
				end
			end
		end
	end

	if #z.maintenance_cats ~= 0 then
		text = text .. '<span class="citation-comment" style="display:none; color:#33aa33">';
		for _, v in ipairs( z.maintenance_cats ) do								-- append maintenance categories
			text = text .. ' ' .. v .. ' ([link](https://second-renaissance.fandom.com/wiki/:Category:'_.._v_..'))';
		end
		text = text .. '</span>';	-- maintenance mesages (realy just the names of the categories for now)
	end
	
	no_tracking_cats = no_tracking_cats:lower();
	if in_array(no_tracking_cats, {"", "no", "false", "n"}) then
		for _, v in ipairs( z.error_categories ) do
			text = text .. '[Category:' .. v ..'](https://second-renaissance.fandom.com/wiki/Category:'_.._v_..')';
		end
		for _, v in ipairs( z.maintenance_cats ) do								-- append maintenance categories
			text = text .. '[Category:' .. v ..'](https://second-renaissance.fandom.com/wiki/Category:'_.._v_..')';
		end
		for _, v in ipairs( z.properties_cats ) do								-- append maintenance categories
			text = text .. '[Category:' .. v ..'](https://second-renaissance.fandom.com/wiki/Category:'_.._v_..')';
		end
	end
	
	return text
end

-- This is used by templates such as {{cite book}} to create the actual citation text.
function z.citation(frame)
	local pframe = frame:getParent()
	local validation;
	
	if nil ~= string.find (frame:getTitle(), 'sandbox', 1, true) then			-- did the {{#invoke:}} use sandbox version?
		cfg = mw.loadData ('Module:Citation/CS1/Configuration/sandbox');		-- load sandbox versions of Configuration and Whitelist and ...
		whitelist = mw.loadData ('Module:Citation/CS1/Whitelist/sandbox');
		validation = require ('Module:Citation/CS1/Date_validation/sandbox');	-- ... sandbox version of date validation code

	else																		-- otherwise
		cfg = mw.loadData ('Module:Citation/CS1/Configuration');				-- load live versions of Configuration and Whitelist and ...
		whitelist = mw.loadData ('Module:Citation/CS1/Whitelist');
		validation = require ('Module:Citation/CS1/Date_validation');			-- ... live version of date validation code
	end

	dates = validation.dates;													-- imported functions
	year_date_check = validation.year_date_check;

	local args = {};
	local suggestions = {};
	local error_text, error_state;

	local config = {};
	for k, v in pairs( frame.args ) do
		config[k] = v;
		args[k] = v;	   
	end	

	for k, v in pairs( pframe.args ) do
		if v ~= '' then
			if not validate( k ) then			
				error_text = "";
				if type( k ) ~= 'string' then
					-- Exclude empty numbered parameters
					if v:match("%S+") ~= nil then
						error_text, error_state = set_error( 'text_ignored', {v}, true );
					end
				elseif validate( k:lower() ) then 
					error_text, error_state = set_error( 'parameter_ignored_suggest', {k, k:lower()}, true );
				else
					if #suggestions == 0 then
						suggestions = mw.loadData( 'Module:Citation/CS1/Suggestions' );
					end
					if suggestions[ k:lower() ] ~= nil then
						error_text, error_state = set_error( 'parameter_ignored_suggest', {k, suggestions[ k:lower() ]}, true );
					else
						error_text, error_state = set_error( 'parameter_ignored', {k}, true );
					end
				end				  
				if error_text ~= '' then
					table.insert( z.message_tail, {error_text, error_state} );
				end				
			end
			args[k] = v;
		elseif args[k] ~= nil or (k == 'postscript') then
			args[k] = v;
		end		
	end	
	
	return citation0( config, args)
end

return z
```

## Provenance

Raw source: `bronze/pages/622/863.wikitext` · revision `863` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3ACitation/CS1)
