---
page_id: 624
revision_id: 865
source_url: https://second-renaissance.fandom.com/wiki/Module%3ACitation/CS1/Date_validation
raw_sha256: f4197af02d727bd9d612835047793a3172086eb0d13536fdb80d3803954ea6a2
---

# Module:Citation/CS1/Date validation

## Preserved source

```wikitext

local p = {}

--[accessdate= at time 00:00:00 UTC
today is the current date at time 00:00:00 UTC plus 48 hours
	if today is 2015-01-01T00:00:00 then
		adding 24 hours gives 2015-01-02T00:00:00 – one second more than today
		adding 24 hours gives 2015-01-03T00:00:00 – one second more than tomorrow](https://second-renaissance.fandom.com/wiki/--------------------------<_I_S___V_A_L_I_D___A_C_C_E_S_S_D_A_T_E_>----------------------------------------

returns_true_if:
	Wikipedia_start_date_<=_accessdate_<_today_+_2_days

Wikipedia_start_date_is_2001-01-15T00:00:00_UTC_which_is_979516800_seconds_after_1970-01-01T00:00:00_UTC_(the_start_of_Unix_time)
accessdate_is_the_date_provided_in)

local function is_valid_accessdate (accessdate)
	local lang = mw.getContentLanguage();
	local good1, good2;
	local access_ts, tomorrow_ts;												-- to hold unix time stamps representing the dates
		
	good1, access_ts = pcall( lang.formatDate, lang, 'U', accessdate );			-- convert accessdate value to unix timesatmp 
	good2, tomorrow_ts = pcall( lang.formatDate, lang, 'U', 'today + 2 days' );	-- today midnight + 2 days is one second more than all day tomorrow
	
	if good1 and good2 then
		access_ts = tonumber (access_ts);										-- convert to numbers for the comparison
		tomorrow_ts = tonumber (tomorrow_ts);
	else
		return false;															-- one or both failed to convert to unix time stamp
	end
	
	if 979516800 <= access_ts and access_ts < tomorrow_ts then					-- Wikipedia start date <= accessdate < tomorrow's date
		return true;
	else
		return false;															-- accessdate out of range
	end
end

--[--------------------------< G E T _ M O N T H _ N U M B E R >----------------------------------------------

returns a number according to the month in a date: 1 for January, etc.  Capitalization and spelling must be correct. If not a valid month, returns 0](https://second-renaissance.fandom.com/wiki/--------------------------<_G_E_T___M_O_N_T_H___N_U_M_B_E_R_>----------------------------------------------

returns_a_number_according_to_the_month_in_a_date:_1_for_January,_etc.__Capitalization_and_spelling_must_be_correct._If_not_a_valid_month,_returns_0)

local function get_month_number (month)
local long_months = {['January']=1, ['February']=2, ['March']=3, ['April']=4, ['May']=5, ['June']=6, ['July']=7, ['August']=8, ['September']=9, ['October']=10, ['November']=11, ['December']=12};
local short_months = {['Jan']=1, ['Feb']=2, ['Mar']=3, ['Apr']=4, ['May']=5, ['Jun']=6, ['Jul']=7, ['Aug']=8, ['Sep']=9, ['Oct']=10, ['Nov']=11, ['Dec']=12};
local temp;
	temp=long_months[month];
	if temp then return temp; end				-- if month is the long-form name
	temp=short_months[month];
	if temp then return temp; end				-- if month is the short-form name
	return 0;									-- misspelled, improper case, or not a month name
end

--[--------------------------< G E T _ S E A S O N _ N U M B E R >--------------------------------------------

returns a number according to the sequence of seasons in a year: 1 for Winter, etc.  Capitalization and spelling must be correct. If not a valid season, returns 0](https://second-renaissance.fandom.com/wiki/--------------------------<_G_E_T___S_E_A_S_O_N___N_U_M_B_E_R_>--------------------------------------------

returns_a_number_according_to_the_sequence_of_seasons_in_a_year:_1_for_Winter,_etc.__Capitalization_and_spelling_must_be_correct._If_not_a_valid_season,_returns_0)

local function get_season_number (season)
local season_list = {['Winter']=1, ['Spring']=2, ['Summer']=3, ['Fall']=4, ['Autumn']=4}
local temp;
	temp=season_list[season];
	if temp then return temp; end				-- if season is a valid name return its number
	return 0;									-- misspelled, improper case, or not a season name
end

--[--------------------------< I S _ P R O P E R _ N A M E >--------------------------------------------------

returns a non-zero number if date contains a recognized proper name.  Capitalization and spelling must be correct.](https://second-renaissance.fandom.com/wiki/--------------------------<_I_S___P_R_O_P_E_R___N_A_M_E_>--------------------------------------------------

returns_a_non-zero_number_if_date_contains_a_recognized_proper_name.__Capitalization_and_spelling_must_be_correct.)

local function is_proper_name (name)
local name_list = {['Christmas']=1}
local temp;
	temp=name_list[name];
	if temp then return temp; end				-- if name is a valid name return its number
	return 0;									-- misspelled, improper case, or not a proper name
end

--[--------------------------< I S _ V A L I D _ M O N T H _ O R _ S E A S O N >------------------------------

--returns true if month or season is valid (properly spelled, capitalized, abbreviated)](https://second-renaissance.fandom.com/wiki/--------------------------<_I_S___V_A_L_I_D___M_O_N_T_H___O_R___S_E_A_S_O_N_>------------------------------

--returns_true_if_month_or_season_is_valid_(properly_spelled,_capitalized,_abbreviated))

local function is_valid_month_or_season (month_season)
	if 0 == get_month_number (month_season) then		-- if month text isn't one of the twelve months, might be a season
		if 0 == get_season_number (month_season) then	-- not a month, is it a season?
			return false;								-- return false not a month or one of the five seasons
		end
	end
	return true;
end


--[--------------------------< I S _ V A L I D _ Y E A R >----------------------------------------------------

Function gets current year from the server and compares it to year from a citation parameter.  Years more than one year in the future are not acceptable.](https://second-renaissance.fandom.com/wiki/--------------------------<_I_S___V_A_L_I_D___Y_E_A_R_>----------------------------------------------------

Function_gets_current_year_from_the_server_and_compares_it_to_year_from_a_citation_parameter.__Years_more_than_one_year_in_the_future_are_not_acceptable.)

local function is_valid_year(year)
	if not is_set(year_limit) then
		year_limit = tonumber(os.date("%Y"))+1;			-- global variable so we only have to fetch it once
	end
	return tonumber(year) <= year_limit;				-- false if year is in the future more than one year
end

--[Returns true if day is less than or equal to the number of days in month and year is no farther into the future than next year; else returns false.

Assumes Julian calendar prior to year 1582 and Gregorian calendar thereafter. Accounts for Julian calendar leap years before 1582 and Gregorian leap years after 1582.
Where the two calendars overlap (1582 to approximately 1923) dates are assumed to be Gregorian.](https://second-renaissance.fandom.com/wiki/Returns_true_if_day_is_less_than_or_equal_to_the_number_of_days_in_month_and_year_is_no_farther_into_the_future_than_next_year;_else_returns_false.

Assumes_Julian_calendar_prior_to_year_1582_and_Gregorian_calendar_thereafter._Accounts_for_Julian_calendar_leap_years_before_1582_and_Gregorian_leap_years_after_1582.
Where_the_two_calendars_overlap_(1582_to_approximately_1923)_dates_are_assumed_to_be_Gregorian.)
local function is_valid_date (year, month, day)
local days_in_month = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
local month_length;
	if not is_valid_year(year) then	-- no farther into the future than next year
		return false;
	end
	
	if (2==month) then							-- if February
		month_length = 28;						-- then 28 days unless
		if 1582 > tonumber(year) then			-- Julian calendar
			if 0==(year%4) then
				month_length = 29;
			end
		else									-- Gregorian calendar
			if (0==(year%4) and (0~=(year%100) or 0==(year%400))) then	-- is a leap year?
				month_length = 29;				-- if leap year then 29 days in February
			end
		end
	else
		month_length=days_in_month[month];
	end

	if tonumber (day) > month_length then
		return false;
	end
	return true;
end

--[--------------------------< I S _ V A L I D _ M O N T H _ R A N G E _ S T Y L E >--------------------------

Months in a range are expected to have the same style: Jan–Mar or October–December but not February–Mar or Jul–August. 
There is a special test for May because it can be either short or long form.

Returns true when style for both months is the same](https://second-renaissance.fandom.com/wiki/--------------------------<_I_S___V_A_L_I_D___M_O_N_T_H___R_A_N_G_E___S_T_Y_L_E_>--------------------------

Months_in_a_range_are_expected_to_have_the_same_style:_Jan–Mar_or_October–December_but_not_February–Mar_or_Jul–August._
There_is_a_special_test_for_May_because_it_can_be_either_short_or_long_form.

Returns_true_when_style_for_both_months_is_the_same)

local function is_valid_month_range_style (month1, month2)
local len1 = month1:len();
local len2 = month2:len();
	if len1 == len2 then
		return true;															-- both months are short form so return true
	elseif 'May' == month1 or 'May'== month2 then
		return true;															-- both months are long form so return true
	elseif 3 == len1 or 3 == len2 then
		return false;															-- months are mixed form so return false
	else
		return true;															-- both months are long form so return true
	end
end


--[date=Fall-Winter yyyy (4-1) is the date.](https://second-renaissance.fandom.com/wiki/--------------------------<_I_S___V_A_L_I_D___M_O_N_T_H___S_E_A_S_O_N___R_A_N_G_E_>------------------------

Check_a_pair_of_months_or_seasons_to_see_if_both_are_valid_members_of_a_month_or_season_pair.

Month_pairs_are_expected_to_be_left_to_right,_earliest_to_latest_in_time.

Similarly,_seasons_are_also_left_to_right,_earliest_to_latest_in_time.__There_is_an_oddity_with_seasons:_winter_is_assigned_a_value_of_1,_spring_2,_...,
fall_and_autumn_4.__Because_winter_can_follow_fall/autumn_at_the_end_of_a_calender_year,_a_special_test_is_made_to_see_if)

local function is_valid_month_season_range(range_start, range_end)
	local range_start_number = get_month_number (range_start);
	
	if 0 == range_start_number then								-- is this a month range?
		local range_start_number = get_season_number (range_start);		-- not a month; is it a season? get start season number
		local range_end_number = get_season_number (range_end);			-- get end season number

		if 0 ~= range_start_number then							-- is start of range a season?
			if range_start_number < range_end_number then		-- range_start is a season
				return true;									-- return true when range_end is also a season and follows start season; else false
			end
			if 4 == range_start_number and 1 == range_end_number then	-- special case when range is Fall-Winter or Autumn-Winter
				return true;
			end
		end
		return false;		-- range_start is not a month or a season; or range_start is a season and range_end is not; or improper season sequence
	end

	local range_end_number = get_month_number (range_end);		-- get end month number
	if range_start_number < range_end_number then				-- range_start is a month; does range_start precede range_end?
		if is_valid_month_range_style (range_start, range_end) then				-- do months have the same style?
			return true;														-- proper order and same style
		end
	end
	return false;												-- range_start month number is greater than or equal to range end number; or range end isn't a month
end

--[--------------------------< C H E C K _ D A T E >----------------------------------------------------------

Check date format to see that it is one of the formats approved by WP:DATESNO or WP:DATERANGE. Exception: only allowed range separator is endash.
Additionally, check the date to see that it is a real date: no 31 in 30-day months; no 29 February when not a leap year.  Months, both long-form and three
character abbreviations, and seasons must be spelled correctly. Future years beyond next year are not allowed.

If the date fails the format tests, this function returns false and does not return values for anchor_year and COinS_date.  When this happens, the date parameter is
used in the COinS metadata and the CITEREF identifier gets its year from the year parameter if present otherwise CITEREF does not get a date value.

Inputs:
	date_string - date string from date-holding parameters (date, year, accessdate, embargo, archivedate, etc.)

Returns:
	false if date string is not a real date; else
	true, anchor_year, COinS_date
		anchor_year can be used in CITEREF anchors
		COinS_date is date_string without anchor_year disambiguator if any](https://second-renaissance.fandom.com/wiki/--------------------------<_C_H_E_C_K___D_A_T_E_>----------------------------------------------------------

Check_date_format_to_see_that_it_is_one_of_the_formats_approved_by_WP:DATESNO_or_WP:DATERANGE._Exception:_only_allowed_range_separator_is_endash.
Additionally,_check_the_date_to_see_that_it_is_a_real_date:_no_31_in_30-day_months;_no_29_February_when_not_a_leap_year.__Months,_both_long-form_and_three
character_abbreviations,_and_seasons_must_be_spelled_correctly._Future_years_beyond_next_year_are_not_allowed.

If_the_date_fails_the_format_tests,_this_function_returns_false_and_does_not_return_values_for_anchor_year_and_COinS_date.__When_this_happens,_the_date_parameter_is
used_in_the_COinS_metadata_and_the_CITEREF_identifier_gets_its_year_from_the_year_parameter_if_present_otherwise_CITEREF_does_not_get_a_date_value.

Inputs:
	date_string_-_date_string_from_date-holding_parameters_(date,_year,_accessdate,_embargo,_archivedate,_etc.)

Returns:
	false_if_date_string_is_not_a_real_date;_else
	true,_anchor_year,_COinS_date
		anchor_year_can_be_used_in_CITEREF_anchors
		COinS_date_is_date_string_without_anchor_year_disambiguator_if_any)
local function check_date (date_string)
	local year;			-- assume that year2, months, and days are not used;
	local year2=0;		-- second year in a year range
	local month=0;
	local month2=0;		-- second month in a month range
	local day=0;
	local day2=0;		-- second day in a day range
	local anchor_year;
	local coins_date;

	if date_string:match("^%d%d%d%d%-%d%d%-%d%d$") then										-- year-initial numerical year month day format
		year, month, day=string.match(date_string, "(%d%d%d%d)%-(%d%d)%-(%d%d)");
		month=tonumber(month);
		if 12 < month or 1 > month or 1583 > tonumber(year) then return false; end			-- month number not valid or not Gregorian calendar
		anchor_year = year;

	elseif date_string:match("^%a+ +[1-9]%d?, +[1-9]%d%d%d%a?$") then						-- month-initial: month day, year
		month, day, anchor_year, year=string.match(date_string, "(%a+)%s*(%d%d?),%s*((%d%d%d%d)%a?)");
		month = get_month_number (month);
		if 0 == month then return false; end												-- return false if month text isn't one of the twelve months
				
	elseif date_string:match("^%a+ +[1-9]%d?–[1-9]%d?, +[1-9]%d%d%d%a?$") then				-- month-initial day range: month day–day, year; days are separated by endash
		month, day, day2, anchor_year, year=string.match(date_string, "(%a+) +(%d%d?)–(%d%d?), +((%d%d%d%d)%a?)");
		if tonumber(day) >= tonumber(day2) then return false; end							-- date range order is left to right: earlier to later; dates may not be the same;
		month = get_month_number (month);
		if 0 == month then return false; end												-- return false if month text isn't one of the twelve months

	elseif date_string:match("^[1-9]%d? +%a+ +[1-9]%d%d%d%a?$") then						-- day-initial: day month year
		day, month, anchor_year, year=string.match(date_string, "(%d%d*)%s*(%a+)%s*((%d%d%d%d)%a?)");
		month = get_month_number (month);
		if 0 == month then return false; end												-- return false if month text isn't one of the twelve months

	elseif date_string:match("^[1-9]%d?–[1-9]%d? +%a+ +[1-9]%d%d%d%a?$") then				-- day-range-initial: day–day month year; days are separated by endash
		day, day2, month, anchor_year, year=string.match(date_string, "(%d%d?)–(%d%d?) +(%a+) +((%d%d%d%d)%a?)");
		if tonumber(day) >= tonumber(day2) then return false; end							-- date range order is left to right: earlier to later; dates may not be the same;
		month = get_month_number (month);
		if 0 == month then return false; end												-- return false if month text isn't one of the twelve months

	elseif date_string:match("^[1-9]%d? +%a+ – [1-9]%d? +%a+ +[1-9]%d%d%d%a?$") then		-- day initial month-day-range: day month - day month year; uses spaced endash
		day, month, day2, month2, anchor_year, year=date_string:match("(%d%d?) +(%a+) – (%d%d?) +(%a+) +((%d%d%d%d)%a?)");
		if (not is_valid_month_season_range(month, month2)) or not is_valid_year(year) then return false; end	-- date range order is left to right: earlier to later;
		month = get_month_number (month);
		month2 = get_month_number (month2);

	elseif date_string:match("^%a+ +[1-9]%d? – %a+ +[1-9]%d?, +[1-9]%d%d%d?%a?$") then		-- month initial month-day-range: month day – month day, year;  uses spaced endash
		month, day, month2, day2, anchor_year, year=date_string:match("(%a+) +(%d%d?) – (%a+) +(%d%d?), +((%d%d%d%d)%a?)");
		if (not is_valid_month_season_range(month, month2)) or not is_valid_year(year) then return false; end
		month = get_month_number (month);
		month2 = get_month_number (month2);

	elseif date_string:match("^[1-9]%d? +%a+ +[1-9]%d%d%d – [1-9]%d? +%a+ +[1-9]%d%d%d%a?$") then		-- day initial month-day-year-range: day month year - day month year; uses spaced endash
		day, month, year, day2, month2, anchor_year, year2=date_string:match("(%d%d?) +(%a+) +(%d%d%d%d?) – (%d%d?) +(%a+) +((%d%d%d%d?)%a?)");
		if tonumber(year2) <= tonumber(year) then return false; end							-- must be sequential years, left to right, earlier to later
		if not is_valid_year(year2) or not is_valid_month_range_style(month, month2) then return false; end		-- year2 no more than one year in the future; months same style
		month = get_month_number (month);
		month2 = get_month_number (month2);

	elseif date_string:match("^%a+ +[1-9]%d?, +[1-9]%d%d%d – %a+ +[1-9]%d?, +[1-9]%d%d%d%a?$") then		-- month initial month-day-year-range: month day, year – month day, year;  uses spaced endash
		month, day, year, month2, day2, anchor_year, year2=date_string:match("(%a+) +(%d%d?), +(%d%d%d%d) – (%a+) +(%d%d?), +((%d%d%d%d)%a?)");
		if tonumber(year2) <= tonumber(year) then return false; end							-- must be sequential years, left to right, earlier to later
		if not is_valid_year(year2) or not is_valid_month_range_style(month, month2) then return false; end		-- year2 no more than one year in the future; months same style
		month = get_month_number (month);
		month2 = get_month_number (month2);

	elseif date_string:match("^%a+ +[1-9]%d%d%d–%d%d%a?$") then								-- special case Winter/Summer year-year (YYYY-YY); year separated with unspaced endash
		if nil == date_string:match("^Winter") and nil == date_string:match("^Summer") then return false end;	-- 'month' can only be Winter or Summer
		local century;
		year, century, anchor_year, year2=date_string:match("%a+ +((%d%d)%d%d)–((%d%d)%a?)");
		anchor_year=year..'–'..anchor_year;													-- assemble anchor_year from both years
		year2 = century..year2;																-- add the century to year2 for comparisons
		if 1 ~= tonumber(year2) - tonumber(year) then return false; end						-- must be sequential years, left to right, earlier to later
		if not is_valid_year(year2) then return false; end									-- no year farther in the future than next year

	elseif date_string:match("^%a+ +[1-9]%d%d%d–[1-9]%d%d%d%a?$") then						-- special case Winter/Summer year-year; year separated with unspaced endash
		if nil == date_string:match("^Winter") and nil == date_string:match("^Summer") then return false end;	-- 'month' can only be Winter or Summer
		year, anchor_year, year2=date_string:match("%a+ +(%d%d%d%d)–((%d%d%d%d)%a?)");
		anchor_year=year..'–'..anchor_year;													-- assemble anchor_year from both years
		if 1 ~= tonumber(year2) - tonumber(year) then return false; end						-- must be sequential years, left to right, earlier to later
		if not is_valid_year(year2) then return false; end									-- no year farther in the future than next year

	elseif date_string:match("^%a+ +[1-9]%d%d%d% – %a+ +[1-9]%d%d%d%a?$") then				-- month/season year - month/season year; separated by spaced endash
		month, year, month2, anchor_year, year2=date_string:match("(%a+) +(%d%d%d%d) – (%a+) +((%d%d%d%d)%a?)");
		anchor_year=year..'–'..anchor_year;													-- assemble anchor_year from both years
		if tonumber(year) >= tonumber(year2) then return false; end							-- left to right, earlier to later, not the same
		if not is_valid_year(year2) then return false; end									-- no year farther in the future than next year
		if not((0 ~= get_month_number(month) and 0 ~= get_month_number(month2) and is_valid_month_range_style(month, month2)) or 	-- both must be month year, same month style
			(0 ~= get_season_number(month) and 0 ~= get_season_number(month2))) then return false; end								-- or season year, not mixed

	elseif date_string:match ("^%a+–%a+ +[1-9]%d%d%d%a?$") then								-- month/season range year; months separated by endash 
		month, month2, anchor_year, year=date_string:match ("(%a+)–(%a+)%s*((%d%d%d%d)%a?)");
		if (not is_valid_month_season_range(month, month2)) or (not is_valid_year(year)) then
			return false;
		end
		
	elseif date_string:match("^%a+ +%d%d%d%d%a?$") then							-- month/season year or proper-name year
		month, anchor_year, year=date_string:match("(%a+)%s*((%d%d%d%d)%a?)");
		if not is_valid_year(year) then return false; end
		if not is_valid_month_or_season (month) and 0 == is_proper_name (month) then return false; end

	elseif date_string:match("^[1-9]%d%d%d?–[1-9]%d%d%d?%a?$") then				-- Year range: YYY-YYY or YYY-YYYY or YYYY–YYYY; separated by unspaced endash; 100-9999
		year, anchor_year, year2=date_string:match("(%d%d%d%d?)–((%d%d%d%d?)%a?)");
		anchor_year=year..'–'..anchor_year;										-- assemble anchor year from both years
		if tonumber(year) >= tonumber(year2) then return false; end				-- left to right, earlier to later, not the same
		if not is_valid_year(year2) then return false; end						-- no year farther in the future than next year

	elseif date_string:match("^[1-9]%d%d%d–%d%d%a?$") then						-- Year range: YYYY–YY; separated by unspaced endash
		local century;
		year, century, anchor_year, year2=date_string:match("((%d%d)%d%d)–((%d%d)%a?)");
		anchor_year=year..'–'..anchor_year;										-- assemble anchor year from both years
		if 13 > tonumber(year2) then return false; end							-- don't allow 2003-05 which might be May 2003
		year2 = century..year2;													-- add the century to year2 for comparisons
		if tonumber(year) >= tonumber(year2) then return false; end				-- left to right, earlier to later, not the same
		if not is_valid_year(year2) then return false; end						-- no year farther in the future than next year

	elseif date_string:match("^[1-9]%d%d%d?%a?$") then							-- year; here accept either YYY or YYYY
		anchor_year, year=date_string:match("((%d%d%d%d?)%a?)");
		if false == is_valid_year(year) then
			return false;
		end

	else
		return false;											-- date format not one of the MOS:DATE approved formats
	end

	local result=true;											-- check whole dates for validity; assume true because not all dates will go through this test
	if 0 ~= year and 0 ~= month and 0 ~= day and 0 == year2 and 0 == month2 and 0 == day2 then		-- YMD (simple whole date)
		result=is_valid_date(year,month,day);

	elseif 0 ~= year and 0 ~= month and 0 ~= day and 0 == year2 and 0 == month2 and 0 ~= day2 then	-- YMD-d (day range)
		result=is_valid_date(year,month,day);
		result=result and is_valid_date(year,month,day2);

	elseif 0 ~= year and 0 ~= month and 0 ~= day and 0 == year2 and 0 ~= month2 and 0 ~= day2 then	-- YMD-md (day month range)
		result=is_valid_date(year,month,day);
		result=result and is_valid_date(year,month2,day2);

	elseif 0 ~= year and 0 ~= month and 0 ~= day and 0 ~= year2 and 0 ~= month2 and 0 ~= day2 then	-- YMD-ymd (day month year range)
		result=is_valid_date(year,month,day);
		result=result and is_valid_date(year2,month2,day2);
	end
	
	if false == result then return false; end
																-- if here, then date_string is valid; get coins_date from date_string (leave CITEREF disambiguator) ...
	coins_date=date_string:match("^(.+%d)%a?$");				-- last character of valid disambiguatable date is always a digit
	coins_date= mw.ustring.gsub(coins_date, "–", "-" );			-- ... and replace any ndash with a hyphen
	
	return true, anchor_year, coins_date;						-- format is good and date string represents a real date
end	

--[date= parameter test is unique, it is the only date holding parameter from which values for anchor_year (used in CITEREF identifiers) and COinS_date (used in
the COinS metadata) are derived.  The |date= parameter is the only date-holding parameter that is allowed to contain the no-date keywords "n.d." or "nd" (without quotes).

Unlike most error messages created in this module, only one error message is created by this function. Because all of the date holding parameters are processed serially,
a single error message is created as the dates are tested.](https://second-renaissance.fandom.com/wiki/--------------------------<_D_A_T_E_S_>--------------------------------------------------------------------

Cycle_the_date-holding_parameters_in_passed_table_date_parameters_list_through_check_date()_to_check_compliance_with_MOS:DATE._For_all_valid_dates,_check_date()_returns
true._The)

--function p.dates(date_parameters_list)
local function dates(date_parameters_list)
	local anchor_year;		-- will return as nil if the date being tested is not |date=
	local COinS_date;		-- will return as nil if the date being tested is not |date=
	local error_message = "";
	local mismatch = 0;
	local good_date = false;
	
	for k, v in pairs(date_parameters_list) do										-- for each date-holding parameter in the list
		if is_set(v) then															-- if the parameter has a value
			if v:match("^c%. [1-9]%d%d%d?%a?$") then								-- special case for c. year or with or without CITEREF disambiguator - only |date= and |year=
				local year = v:match("c%. ([1-9]%d%d%d?)%a?");						-- get the year portion so it can be tested
				if 'date'==k then
					anchor_year, COinS_date = v:match("((c%. [1-9]%d%d%d?)%a?)");	-- anchor year and COinS_date only from |date= parameter
					good_date = is_valid_year(year);
				elseif 'year'==k then
					good_date = is_valid_year(year);
				end
			elseif 'date'==k then													-- if the parameter is |date=
				if v:match("^n%.d%.%a?") then										-- if |date=n.d. with or without a CITEREF disambiguator
					good_date, anchor_year, COinS_date = true, v:match("((n%.d%.)%a?)");	--"n.d."; no error when date parameter is set to no date
				elseif v:match("^nd%a?$") then										-- if |date=nd with or without a CITEREF disambiguator
					good_date, anchor_year, COinS_date = true, v:match("((nd)%a?)");	--"nd";	no error when date parameter is set to no date
				else
					good_date, anchor_year, COinS_date = check_date (v);			-- go test the date
				end
			elseif 'accessdate'==k then												-- if the parameter is |date=
				good_date = check_date (v);											-- go test the date
				if true == good_date then											-- if the date is a valid date
					good_date = is_valid_accessdate (v);							-- is Wikipedia start date < accessdate < tomorrow's date?
				end
			else																	-- any other date-holding parameter
				good_date = check_date (v);											-- go test the date
			end
			if false==good_date then												-- assemble one error message so we don't add the tracking category multiple times
				if is_set(error_message) then										-- once we've added the first portion of the error message ...
					error_message=error_message .. ", ";							-- ... add a comma space separator
				end
				error_message=error_message .. "&#124;" .. k .. "=";				-- add the failed parameter
			end
		end
	end
	return anchor_year, COinS_date, error_message, mismatch;					-- and done
end

--[year= with the year value(s) provided in |date=.  This function returns a numeric value:
	0 - year value does not match the year value in date
	1 - (default) year value matches the year value in date or one of the year values when date contains two years
	2 - year value matches the year value in date when date is in the form YYYY-MM-DD and year is disambiguated (|year=YYYYx)](https://second-renaissance.fandom.com/wiki/--------------------------<_Y_E_A_R___D_A_T_E___C_H_E_C_K_>------------------------------------------------

Compare_the_value_provided_in)

local function year_date_check (year_string, date_string)
	local year;
	local date1;
	local date2;
	local result = 1;															-- result of the test; assume that the test passes
	
	year = year_string:match ('(%d%d%d%d?)');

	if date_string:match ('%d%d%d%d%-%d%d%-%d%d') and year_string:match ('%d%d%d%d%a') then	--special case where date and year required YYYY-MM-DD and YYYYx
		date1 = date_string:match ('(%d%d%d%d)');
		year = year_string:match ('(%d%d%d%d)');
		if year ~= date1 then
			result = 0;															-- years don't match
		else
			result = 2;															-- years match; but because disambiguated, don't add to maint cat
		end
		
	elseif date_string:match ("%d%d%d%d?.-%d%d%d%d?") then						-- any of the standard formats of date with two three- or four-digit years
		date1, date2 = date_string:match ("(%d%d%d%d?).-(%d%d%d%d?)");
		if year ~= date1 and year ~= date2 then
			result = 0;
		end

	elseif date_string:match ("%d%d%d%d[%s%-–]+%d%d") then						-- YYYY-YY date ranges
		local century;
		date1, century, date2 = date_string:match ("((%d%d)%d%d)[%s%-–]+(%d%d)");
		date2 = century..date2;													-- convert YY to YYYY
		if year ~= date1 and year ~= date2 then
			result = 0;
		end

	elseif date_string:match ("%d%d%d%d?") then									-- any of the standard formats of date with one year
		date1 = date_string:match ("(%d%d%d%d?)");
		if year ~= date1 then
			result = 0;
		end
	end
	return result;
end

return {dates = dates, year_date_check = year_date_check}						-- return exported functions
```

## Provenance

Raw source: `bronze/pages/624/865.wikitext` · revision `865` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3ACitation/CS1/Date_validation)
