---
page_id: 605
revision_id: 843
source_url: https://second-renaissance.fandom.com/wiki/Module%3AString
raw_sha256: 6e972bffc7fbb57b76a9eaa197b9af6062e1dccc4dc8cfb467c9ee7680e5a6a7
---

# Module:String

## Preserved source

```wikitext
--[[  

This module is intended to provide access to basic string functions.

Most of the functions provided here can be invoked with named parameters, 
unnamed parameters, or a mixture.  If named parameters are used, Mediawiki will 
automatically remove any leading or trailing whitespace from the parameter.  
Depending on the intended use, it may be advantageous to either preserve or
remove such whitespace.

Global options
    ignore_errors: If set to 'true' or 1, any error condition will result in 
        an empty string being returned rather than an error message.  
        
    error_category: If an error occurs, specifies the name of a category to 
        include with the error message.  The default category is  
        [Category:Errors reported by Module String].
        
    no_category: If set to 'true' or 1, no category will be added if an error
        is generated.
        
Unit tests for this module are available at Module:String/tests.
]]

local str = {}

--[len|target_string|}}
OR
{{#invoke:String|len|s=target_string}}

Parameters
    s: The string whose length to report

If invoked using named parameters, Mediawiki will automatically remove any leading or
trailing whitespace from the target string.](https://second-renaissance.fandom.com/wiki/len

This_function_returns_the_length_of_the_target_string.

Usage:
{{)
function str.len( frame )
    local new_args = str._getParameters( frame.args, {'s'} );
    local s = new_args['s'] or '';
    return mw.ustring.len( s )
end

--[sub|target_string|start_index|end_index}}
OR
{{#invoke:String|sub|s=target_string|i=start_index|j=end_index}}

Parameters
    s: The string to return a subset of
    i: The fist index of the substring to return, defaults to 1.
    j: The last index of the string to return, defaults to the last character.
    
The first character of the string is assigned an index of 1.  If either i or j
is a negative value, it is interpreted the same as selecting a character by 
counting from the end of the string.  Hence, a value of -1 is the same as 
selecting the last character of the string.

If the requested indices are out of range for the given string, an error is 
reported.](https://second-renaissance.fandom.com/wiki/sub

This_function_returns_a_substring_of_the_target_string_at_specified_indices.

Usage:
{{)
function str.sub( frame )
    local new_args = str._getParameters( frame.args, { 's', 'i', 'j' } );
    local s = new_args['s'] or '';
    local i = tonumber( new_args['i'] ) or 1;
    local j = tonumber( new_args['j'] ) or -1;
    
    local len = mw.ustring.len( s );

    -- Convert negatives for range checking
    if i < 0 then
        i = len + i + 1;
    end
    if j < 0 then
        j = len + j + 1;
    end
    
    if i > len or j > len or i < 1 or j < 1 then
        return str._error( 'String subset index out of range' );
    end
    if j < i then
        return str._error( 'String subset indices out of order' );
    end
    
    return mw.ustring.sub( s, i, j )
end

--[This function implements that features of {{str sub old}} and is kept in order
to maintain these older templates.](https://second-renaissance.fandom.com/wiki/This_function_implements_that_features_of_{{str_sub_old}}_and_is_kept_in_order
to_maintain_these_older_templates.)
function str.sublength( frame )
    local i = tonumber( frame.args.i ) or 0
    local len = tonumber( frame.args.len )
    return mw.ustring.sub( frame.args.s, i + 1, len and ( i + len ) )
end

--[[
match

This function returns a substring from the source string that matches a 
specified pattern.

Usage:
{{#invoke:String|match|source_string|pattern_string|start_index|match_number|plain_flag|nomatch_output}}
OR
{{#invoke:String|pos|s=source_string|pattern=pattern_string|start=start_index
    |match=match_number|plain=plain_flag|nomatch=nomatch_output}}

Parameters
    s: The string to search
    pattern: The pattern or string to find within the string
    start: The index within the source string to start the search.  The first
        character of the string has index 1.  Defaults to 1.
    match: In some cases it may be possible to make multiple matches on a single 
        string.  This specifies which match to return, where the first match is 
        match= 1.  If a negative number is specified then a match is returned 
        counting from the last match.  Hence match = -1 is the same as requesting
        the last match.  Defaults to 1.
    plain: A flag indicating that the pattern should be understood as plain
        text.  Defaults to false.
    nomatch: If no match is found, output the "nomatch" value rather than an error.

If invoked using named parameters, Mediawiki will automatically remove any leading or
trailing whitespace from each string.  In some circumstances this is desirable, in 
other cases one may want to preserve the whitespace.

If the match_number or start_index are out of range for the string being queried, then
this function generates an error.  An error is also generated if no match is found.
If one adds the parameter ignore_errors=true, then the error will be suppressed and 
an empty string will be returned on any failure.

For information on constructing Lua patterns, a form of [regular expression], see:

* http://www.lua.org/manual/5.1/manual.html#5.4.1
* http://www.mediawiki.org/wiki/Extension:Scribunto/Lua_reference_manual#Patterns
* http://www.mediawiki.org/wiki/Extension:Scribunto/Lua_reference_manual#Ustring_patterns

]]
function str.match( frame )
    local new_args = str._getParameters( frame.args, {'s', 'pattern', 'start', 'match', 'plain', 'nomatch'} );
    local s = new_args['s'] or '';
    local start = tonumber( new_args['start'] ) or 1;
    local plain_flag = str._getBoolean( new_args['plain'] or false );
    local pattern = new_args['pattern'] or '';
    local match_index = math.floor( tonumber(new_args['match']) or 1 );
    local nomatch = new_args['nomatch'];
    
    if s == '' then
        return str._error( 'Target string is empty' );
    end
    if pattern == '' then
        return str._error( 'Pattern string is empty' );
    end
    if math.abs(start) < 1 or math.abs(start) > mw.ustring.len( s ) then
        return str._error( 'Requested start is out of range' );
    end
    if match_index == 0 then
        return str._error( 'Match index is out of range' );
    end
    if plain_flag then
        pattern = str._escapePattern( pattern );
    end
    
    local result
    if match_index == 1 then
        -- Find first match is simple case
        result = mw.ustring.match( s, pattern, start )
    else
        if start > 1 then
            s = mw.ustring.sub( s, start );
        end
        
        local iterator = mw.ustring.gmatch(s, pattern);
        if match_index > 0 then
            -- Forward search
            for w in iterator do
                match_index = match_index - 1;
                if match_index == 0 then
                    result = w;
                    break;
                end
            end    
        else
            -- Reverse search
            local result_table = {};
            local count = 1;
            for w in iterator do
                result_table[count] = w;
                count = count + 1;
            end
            
            result = result_table[ count + match_index ];            
        end
    end        
    
    if result == nil then
        if nomatch == nil then
            return str._error( 'Match not found' );
        else
            return nomatch;
        end
    else
        return result;
    end
end

--[pos|target_string|index_value}}
OR
{{#invoke:String|pos|target=target_string|pos=index_value}}

Parameters
    target: The string to search
    pos: The index for the character to return

If invoked using named parameters, Mediawiki will automatically remove any leading or
trailing whitespace from the target string.  In some circumstances this is desirable, in 
other cases one may want to preserve the whitespace.

The first character has an index value of 1.

If one requests a negative value, this function will select a character by counting backwards 
from the end of the string.  In other words pos = -1 is the same as asking for the last character.

A requested value of zero, or a value greater than the length of the string returns an error.](https://second-renaissance.fandom.com/wiki/pos

This_function_returns_a_single_character_from_the_target_string_at_position_pos.

Usage:
{{)
function str.pos( frame )
    local new_args = str._getParameters( frame.args, {'target', 'pos'} );
    local target_str = new_args['target'] or '';
    local pos = tonumber( new_args['pos'] ) or 0;

    if pos == 0 or math.abs(pos) > mw.ustring.len( target_str ) then
        return str._error( 'String index out of range' );
    end    
    
    return mw.ustring.sub( target_str, pos, pos );
end

--[str_find

This function duplicates the behavior of {{str_find}}, including all of its quirks.
This is provided in order to support existing templates, but is NOT RECOMMENDED for 
new code and templates.  New code is recommended to use the "find" function instead.

Returns the first index in "source" that is a match to "target".  Indexing is 1-based,
and the function returns -1 if the "target" string is not present in "source".

Important Note: If the "target" string is empty / missing, this function returns a
value of "1", which is generally unexpected behavior, and must be accounted for
separatetly.](https://second-renaissance.fandom.com/wiki/str_find

This_function_duplicates_the_behavior_of_{{str_find}},_including_all_of_its_quirks.
This_is_provided_in_order_to_support_existing_templates,_but_is_NOT_RECOMMENDED_for_
new_code_and_templates.__New_code_is_recommended_to_use_the_"find"_function_instead.

Returns_the_first_index_in_"source"_that_is_a_match_to_"target".__Indexing_is_1-based,
and_the_function_returns_-1_if_the_"target"_string_is_not_present_in_"source".

Important_Note:_If_the_"target"_string_is_empty_/_missing,_this_function_returns_a
value_of_"1",_which_is_generally_unexpected_behavior,_and_must_be_accounted_for
separatetly.)
function str.str_find( frame )
    local new_args = str._getParameters( frame.args, {'source', 'target'} );
    local source_str = new_args['source'] or '';
    local target_str = new_args['target'] or '';

    if target_str == '' then
        return 1;
    end    
    
    local start = mw.ustring.find( source_str, target_str, 1, true )
    if start == nil then
        start = -1
    end
    
    return start
end

--[find|source_str|target_string|start_index|plain_flag}}
OR
{{#invoke:String|find|source=source_str|target=target_str|start=start_index|plain=plain_flag}}

Parameters
    source: The string to search
    target: The string or pattern to find within source
    start: The index within the source string to start the search, defaults to 1
    plain: Boolean flag indicating that target should be understood as plain
        text and not as a Lua style regular expression, defaults to true

If invoked using named parameters, Mediawiki will automatically remove any leading or
trailing whitespace from the parameter.  In some circumstances this is desirable, in 
other cases one may want to preserve the whitespace.

This function returns the first index >= "start" where "target" can be found 
within "source".  Indices are 1-based.  If "target" is not found, then this 
function returns 0.  If either "source" or "target" are missing / empty, this
function also returns 0.

This function should be safe for UTF-8 strings.](https://second-renaissance.fandom.com/wiki/find

This_function_allows_one_to_search_for_a_target_string_or_pattern_within_another
string.

Usage:
{{)
function str.find( frame )
    local new_args = str._getParameters( frame.args, {'source', 'target', 'start', 'plain' } ); 
    local source_str = new_args['source'] or '';
    local pattern = new_args['target'] or '';
    local start_pos = tonumber(new_args['start']) or 1;
    local plain = new_args['plain'] or true;
        
    if source_str == '' or pattern == '' then
        return 0;
    end    
    
    plain = str._getBoolean( plain );

    local start = mw.ustring.find( source_str, pattern, start_pos, plain )
    if start == nil then
        start = 0
    end
    
    return start
end

--[replace|source_str|pattern_string|replace_string|replacement_count|plain_flag}}
OR
{{#invoke:String|replace|source=source_string|pattern=pattern_string|replace=replace_string|
   count=replacement_count|plain=plain_flag}}

Parameters
    source: The string to search
    pattern: The string or pattern to find within source
    replace: The replacement text
    count: The number of occurences to replace, defaults to all.
    plain: Boolean flag indicating that pattern should be understood as plain
        text and not as a Lua style regular expression, defaults to true](https://second-renaissance.fandom.com/wiki/replace

This_function_allows_one_to_replace_a_target_string_or_pattern_within_another
string.

Usage:
{{)
function str.replace( frame )
    local new_args = str._getParameters( frame.args, {'source', 'pattern', 'replace', 'count', 'plain' } ); 
    local source_str = new_args['source'] or '';
    local pattern = new_args['pattern'] or '';
    local replace = new_args['replace'] or '';
    local count = tonumber( new_args['count'] );
    local plain = new_args['plain'] or true;
        
    if source_str == '' or pattern == '' then
        return source_str;
    end    
    plain = str._getBoolean( plain );

    if plain then
        pattern = str._escapePattern( pattern );
        replace = mw.ustring.gsub( replace, "%%", "%%%%" ); --Only need to escape replacement sequences.
    end
    
    local result;

    if count ~= nil then
        result = mw.ustring.gsub( source_str, pattern, replace, count );
    else
        result = mw.ustring.gsub( source_str, pattern, replace );
    end        

    return result;
end

--[simple function to pipe string.rep to templates.](https://second-renaissance.fandom.com/wiki/simple_function_to_pipe_string.rep_to_templates.)

function str.rep( frame )
    local repetitions = tonumber( frame.args[2] )
    if not repetitions then 
        return str._error( 'function rep expects a number as second parameter, received "' .. ( frame.args[2] or '' ) .. '"' )
    end
    return string.rep( frame.args[1] or '', repetitions )
end

--[Helper function that populates the argument list given that user may need to use a mix of
named and unnamed parameters.  This is relevant because named parameters are not
identical to unnamed parameters due to string trimming, and when dealing with strings
we sometimes want to either preserve or remove that whitespace depending on the application.](https://second-renaissance.fandom.com/wiki/Helper_function_that_populates_the_argument_list_given_that_user_may_need_to_use_a_mix_of
named_and_unnamed_parameters.__This_is_relevant_because_named_parameters_are_not
identical_to_unnamed_parameters_due_to_string_trimming,_and_when_dealing_with_strings
we_sometimes_want_to_either_preserve_or_remove_that_whitespace_depending_on_the_application.)
function str._getParameters( frame_args, arg_list )
    local new_args = {};
    local index = 1;
    local value;
    
    for i,arg in ipairs( arg_list ) do
        value = frame_args[arg]
        if value == nil then
            value = frame_args[index];
            index = index + 1;
        end
        new_args[arg] = value;
    end
    
    return new_args;
end        

--[Helper function to handle error messages.](https://second-renaissance.fandom.com/wiki/Helper_function_to_handle_error_messages.)
function str._error( error_str )
    local frame = mw.getCurrentFrame();
    local error_category = frame.args.error_category or 'Errors reported by Module String';
    local ignore_errors = frame.args.ignore_errors or false;
    local no_category = frame.args.no_category or false;
    
    if str._getBoolean(ignore_errors) then
        return '';
    end
    
    local error_str = '<strong class="error">String Module Error: ' .. error_str .. '</strong>';
    if error_category ~= '' and not str._getBoolean( no_category ) then
        error_str = '[Category:' .. error_category .. '](https://second-renaissance.fandom.com/wiki/Category:'_.._error_category_.._')' .. error_str;
    end        
    
    return error_str;
end

--[Helper Function to interpret boolean strings](https://second-renaissance.fandom.com/wiki/Helper_Function_to_interpret_boolean_strings)
function str._getBoolean( boolean_str )
    local boolean_value;
    
    if type( boolean_str ) == 'string' then
        boolean_str = boolean_str:lower();
        if boolean_str == 'false' or boolean_str == 'no' or boolean_str == '0' 
                or boolean_str == '' then
            boolean_value = false;
        else
            boolean_value = true;
        end    
    elseif type( boolean_str ) == 'boolean' then
        boolean_value = boolean_str;
    else
        error( 'No boolean value found' );
    end    
    return boolean_value
end

--[Helper function that escapes all pattern characters so that they will be treated 
as plain text.](https://second-renaissance.fandom.com/wiki/Helper_function_that_escapes_all_pattern_characters_so_that_they_will_be_treated_
as_plain_text.)
function str._escapePattern( pattern_str )
    return mw.ustring.gsub( pattern_str, "([%(%)%.%%%+%-%*%?%[%^%$%]])", "%%%1" );
end

return str
```

## Provenance

Raw source: `bronze/pages/605/843.wikitext` · revision `843` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3AString)
