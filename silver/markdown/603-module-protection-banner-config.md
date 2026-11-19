---
page_id: 603
revision_id: 841
source_url: https://second-renaissance.fandom.com/wiki/Module%3AProtection_banner/config
raw_sha256: f3506872535be1d7da4e5f14da2a877e9c7fcea3e5401225ac30147b4e52eacf
---

# Module:Protection banner/config

## Preserved source

```wikitext
-- This module provides configuration data for [Module:Protection banner](602-module-protection-banner.md).

return {

--------------------------------------------------------------------------------
--
--                                BANNER DATA
--
--------------------------------------------------------------------------------

--[-- Banner data consists of six fields:
-- * text - the main protection text that appears at the top of protection
--   banners.
-- * explanation - the text that appears below the main protection text, used
--   to explain the details of the protection.
-- * tooltip - the tooltip text you see when you move the mouse over a small
--   padlock icon.
-- * link - the page that the small padlock icon links to.
-- * alt - the alt text for the small padlock icon. This is also used as tooltip
--   text for the large protection banners.
-- * image - the padlock image used in both protection banners and small padlock
--   icons.
--
-- The module checks in three separate tables to find a value for each field.
-- First it checks the banners table, which has values specific to the reason
-- for the page being protected. Then the module checks the defaultBanners
-- table, which has values specific to each protection level. Finally, the
-- module checks the masterBanner table, which holds data for protection
-- templates to use if no data has been found in the previous two tables.
--
-- The values in the banner data can take parameters. These are specified
-- using ${TEXTLIKETHIS} (a dollar sign preceding a parameter name
-- enclosed in curly braces).
--
--                          Available parameters:
--
-- ${CURRENTVERSION} - a link to the page history or the move log, with the
-- display message "current-version-edit-display" or
-- "current-version-move-display".
--
-- ${EDITREQUEST} - a link to create an edit request for the current page.
--
-- ${EXPIRY} - the protection expiry date in the format DD Month YYYY. If
-- protection is indefinite or is not set, this is the blank string.
--
-- ${EXPLANATIONBLURB} - an explanation blurb, e.g. "Please discuss any changes
-- on the talk page; you may submit a request to ask an administrator to make
-- an edit if it is minor or supported by consensus."
--
-- ${IMAGELINK} - a link to set the image to, depending on the protection
-- action and protection level.
--
-- ${INTROBLURB} - the PROTECTIONBLURB parameter, plus the expiry if an expiry
-- is set. E.g. "Editing of this page by new or unregistered users is currently 
-- disabled until dd Month YYYY."
--
-- ${INTROFRAGMENT} - the same as ${INTROBLURB}, but without final punctuation
-- so that it can be used in run-on sentences.
--
-- ${PAGETYPE} - the type of the page, e.g. "article" or "template".
-- Defined in the cfg.pagetypes table.
--
-- ${PROTECTIONBLURB} - a blurb explaining the protection level of the page, e.g.
-- "Editing of this page by new or unregistered users is currently disabled"
--
-- ${PROTECTIONDATE} - the protection date, if it has been supplied to the
-- template.
--
-- ${PROTECTIONLEVEL} - the protection level, e.g. "fully protected" or
-- "semi-protected".
--
-- ${PROTECTIONLOG} - a link to the protection log or the pending changes log,
-- depending on the protection action.
--
-- ${TALKPAGE} - a link to the talk page. If a section is specified, links
-- straight to that talk page section.
--
-- ${TOOLTIPBLURB} - uses the PAGETYPE, PROTECTIONTYPE and EXPIRY parameters to
-- create a blurb like "This template is semi-protected", or "This article is
-- move-protected until DD Month YYYY".
--
-- ${VANDAL} - links for the specified username (or the root page name)
-- using Module:Vandal-m.
--
--                                 Functions
--
-- For advanced users, it is possible to use Lua functions instead of strings
-- in the banner config tables. Using functions gives flexibility that is not
-- possible just by using parameters. Functions take two arguments, the
-- protection object and the template arguments, and they must output a string.
--
-- For example:
--
-- text = function (protectionObj, args)
--     if protectionObj.level == 'autoconfirmed' then
--         return 'foo'
--     else
--         return 'bar'
--     end
-- end
--
-- Some protection object properties and methods that may be useful:
-- protectionObj.action - the protection action
-- protectionObj.level - the protection level
-- protectionObj.reason - the protection reason
-- protectionObj.expiry - the expiry. Nil if unset, the string "indef" if set
--     to indefinite, and the protection time in unix time if temporary.
-- protectionObj.protectionDate - the protection date in unix time, or nil if
--     unspecified.
-- protectionObj.bannerConfig - the banner config found by the module. Beware
--     of editing the config field used by the function, as it could create an
--     infinite loop.
-- protectionObj:isProtected - returns a boolean showing whether the page is
--     protected.
-- protectionObj:isTemporary - returns a boolean showing whether the expiry is
--     temporary.
-- protectionObj:isIncorrect - returns a boolean showing whether the protection
--     template is incorrect.
--](https://second-renaissance.fandom.com/wiki/--_Banner_data_consists_of_six_fields:
--_*_text_-_the_main_protection_text_that_appears_at_the_top_of_protection
--___banners.
--_*_explanation_-_the_text_that_appears_below_the_main_protection_text,_used
--___to_explain_the_details_of_the_protection.
--_*_tooltip_-_the_tooltip_text_you_see_when_you_move_the_mouse_over_a_small
--___padlock_icon.
--_*_link_-_the_page_that_the_small_padlock_icon_links_to.
--_*_alt_-_the_alt_text_for_the_small_padlock_icon._This_is_also_used_as_tooltip
--___text_for_the_large_protection_banners.
--_*_image_-_the_padlock_image_used_in_both_protection_banners_and_small_padlock
--___icons.
--
--_The_module_checks_in_three_separate_tables_to_find_a_value_for_each_field.
--_First_it_checks_the_banners_table,_which_has_values_specific_to_the_reason
--_for_the_page_being_protected._Then_the_module_checks_the_defaultBanners
--_table,_which_has_values_specific_to_each_protection_level._Finally,_the
--_module_checks_the_masterBanner_table,_which_holds_data_for_protection
--_templates_to_use_if_no_data_has_been_found_in_the_previous_two_tables.
--
--_The_values_in_the_banner_data_can_take_parameters._These_are_specified
--_using_${TEXTLIKETHIS}_(a_dollar_sign_preceding_a_parameter_name
--_enclosed_in_curly_braces).
--
--__________________________Available_parameters:
--
--_${CURRENTVERSION}_-_a_link_to_the_page_history_or_the_move_log,_with_the
--_display_message_"current-version-edit-display"_or
--_"current-version-move-display".
--
--_${EDITREQUEST}_-_a_link_to_create_an_edit_request_for_the_current_page.
--
--_${EXPIRY}_-_the_protection_expiry_date_in_the_format_DD_Month_YYYY._If
--_protection_is_indefinite_or_is_not_set,_this_is_the_blank_string.
--
--_${EXPLANATIONBLURB}_-_an_explanation_blurb,_e.g._"Please_discuss_any_changes
--_on_the_talk_page;_you_may_submit_a_request_to_ask_an_administrator_to_make
--_an_edit_if_it_is_minor_or_supported_by_consensus."
--
--_${IMAGELINK}_-_a_link_to_set_the_image_to,_depending_on_the_protection
--_action_and_protection_level.
--
--_${INTROBLURB}_-_the_PROTECTIONBLURB_parameter,_plus_the_expiry_if_an_expiry
--_is_set._E.g._"Editing_of_this_page_by_new_or_unregistered_users_is_currently_
--_disabled_until_dd_Month_YYYY."
--
--_${INTROFRAGMENT}_-_the_same_as_${INTROBLURB},_but_without_final_punctuation
--_so_that_it_can_be_used_in_run-on_sentences.
--
--_${PAGETYPE}_-_the_type_of_the_page,_e.g._"article"_or_"template".
--_Defined_in_the_cfg.pagetypes_table.
--
--_${PROTECTIONBLURB}_-_a_blurb_explaining_the_protection_level_of_the_page,_e.g.
--_"Editing_of_this_page_by_new_or_unregistered_users_is_currently_disabled"
--
--_${PROTECTIONDATE}_-_the_protection_date,_if_it_has_been_supplied_to_the
--_template.
--
--_${PROTECTIONLEVEL}_-_the_protection_level,_e.g._"fully_protected"_or
--_"semi-protected".
--
--_${PROTECTIONLOG}_-_a_link_to_the_protection_log_or_the_pending_changes_log,
--_depending_on_the_protection_action.
--
--_${TALKPAGE}_-_a_link_to_the_talk_page._If_a_section_is_specified,_links
--_straight_to_that_talk_page_section.
--
--_${TOOLTIPBLURB}_-_uses_the_PAGETYPE,_PROTECTIONTYPE_and_EXPIRY_parameters_to
--_create_a_blurb_like_"This_template_is_semi-protected",_or_"This_article_is
--_move-protected_until_DD_Month_YYYY".
--
--_${VANDAL}_-_links_for_the_specified_username_(or_the_root_page_name)
--_using_Module:Vandal-m.
--
--_________________________________Functions
--
--_For_advanced_users,_it_is_possible_to_use_Lua_functions_instead_of_strings
--_in_the_banner_config_tables._Using_functions_gives_flexibility_that_is_not
--_possible_just_by_using_parameters._Functions_take_two_arguments,_the
--_protection_object_and_the_template_arguments,_and_they_must_output_a_string.
--
--_For_example:
--
--_text_=_function_(protectionObj,_args)
--_____if_protectionObj.level_==_'autoconfirmed'_then
--_________return_'foo'
--_____else
--_________return_'bar'
--_____end
--_end
--
--_Some_protection_object_properties_and_methods_that_may_be_useful:
--_protectionObj.action_-_the_protection_action
--_protectionObj.level_-_the_protection_level
--_protectionObj.reason_-_the_protection_reason
--_protectionObj.expiry_-_the_expiry._Nil_if_unset,_the_string_"indef"_if_set
--_____to_indefinite,_and_the_protection_time_in_unix_time_if_temporary.
--_protectionObj.protectionDate_-_the_protection_date_in_unix_time,_or_nil_if
--_____unspecified.
--_protectionObj.bannerConfig_-_the_banner_config_found_by_the_module._Beware
--_____of_editing_the_config_field_used_by_the_function,_as_it_could_create_an
--_____infinite_loop.
--_protectionObj:isProtected_-_returns_a_boolean_showing_whether_the_page_is
--_____protected.
--_protectionObj:isTemporary_-_returns_a_boolean_showing_whether_the_expiry_is
--_____temporary.
--_protectionObj:isIncorrect_-_returns_a_boolean_showing_whether_the_protection
--_____template_is_incorrect.
--)

-- The master banner data, used if no values have been found in banners or
-- defaultBanners.
masterBanner = {
	text = '${INTROBLURB}',
	explanation = '${EXPLANATIONBLURB}',
	tooltip = '${TOOLTIPBLURB}',
	link = '${IMAGELINK}',
	alt = 'Page ${PROTECTIONLEVEL}'
},

-- The default banner data. This holds banner data for different protection
-- levels.
-- *required* - this table needs edit, move, and autoreview subtables.
defaultBanners = {
	edit = {},
	move = {},
	autoreview = {
		autoconfirmed = {
			alt = 'Page protected with pending changes level 1',
			tooltip = 'All edits by unregistered and new users are subject to review',
			image = 'Padlock-silver-light.svg'
		},
		default = {
			alt = 'Page protected with pending changes level 2',
			tooltip = 'All edits by users who are not reviewers or administrators are'
				.. ' subject to review',
		}
	}
},

-- The banner data. This holds banner data for different protection reasons.
-- In fact, the reasons specified in this table control which reasons are
-- valid inputs to the first positional parameter.
--
-- There is also a non-standard "description" field that can be used for items
-- in this table. This is a description of the protection reason for use in the
-- module documentation.
--
-- *required* - this table needs edit, move, and autoreview subtables.
banners = {
	edit = {
		blp = {
			description = 'For pages protected to promote compliance with the'
				.. ' [biographies of living persons](https://second-renaissance.fandom.com/wiki/Wikipedia:Biographies_of_living_persons'
				.._') policy.',
			text = '${INTROFRAGMENT} to promote compliance with'
				.. ' [Wikipedia's&nbsp;policy on&nbsp;the&nbsp;biographies"
				.. ' of&nbsp;living&nbsp;people](https://second-renaissance.fandom.com/wiki/Wikipedia:Biographies_of_living_persons'
				.._").',
			tooltip = '${TOOLTIPFRAGMENT} to promote compliance with the policy on'
				.. ' biographies of living people',
		},
		dmca = {
			description = 'For pages protected by the Wikimedia Foundation'
				.. ' due to Digital Millennium Copyright Act takedown requests.',
			explanation = function (protectionObj, args)
				local ret = 'Pursuant to a rights owner notice under the Digital'
					.. ' Millennium Copyright Act (DMCA) regarding some content'
					.. ' in this article, the Wikimedia Foundation acted under'
					.. ' applicable law and took down and restricted the content'
					.. ' in question.'
				if args.notice then
					ret = ret .. ' A copy of the received notice can be found here: '
						.. args.notice .. '.'
				end
				ret = ret .. ' For more information, including websites discussing'
					.. ' how to file a counter-notice, please see'
					.. " [Wikipedia:Office actions](https://second-renaissance.fandom.com/wiki/Wikipedia:Office_actions) and the article's ${TALKPAGE}."
					.. "'''Do not remove this template from the article until the"
					.. " restrictions are withdrawn'''."
				return ret
			end,
			image = 'Padlock-black.svg',
		},
		dispute = {
			description = 'For pages protected due to editing disputes.',
			text = function (protectionObj, args)
				-- Find the value of "disputes".
				local display = 'disputes'
				local disputes
				if args.section then
					disputes = string.format(
						'[%s](https://second-renaissance.fandom.com/wiki/%s:%s)',
						mw.site.namespaces[protectionObj.title.namespace].talk.name,
						protectionObj.title.text,
						args.section,
						display
					)
				else
					disputes = display
				end

				-- Make the blurb, depending on the expiry.
				local msg
				if type(protectionObj.expiry) == 'number' then
					msg = '${INTROFRAGMENT} or until editing %s have been resolved.'
				else
					msg = '${INTROFRAGMENT} until editing %s have been resolved.'
				end
				return string.format(msg, disputes)
			end,
			explanation = "This protection is '''not''' an endorsement of the"
				.. ' ${CURRENTVERSION}. ${EXPLANATIONBLURB}',
			tooltip = '${TOOLTIPFRAGMENT} due to editing disputes',
		},
		mainpage = {
			description = 'For pages protected for being displayed on the [Main Page](84-main-page.md).',
			text = 'This file is currently'
				.. ' [protected](https://second-renaissance.fandom.com/wiki/Wikipedia:This_page_is_protected) from'
				.. ' editing because it is currently or will soon be displayed'
				.. ' on the [Main Page](84-main-page.md).',
			explanation = 'Images on the Main Page are protected due to their high'
				.. ' visibility. Please discuss any necessary changes on the ${TALKPAGE}.'
				.. '<br /><span style="font-size:90%;">'
				.. "'''Administrators:''' Once this image is definitely off the Main Page,"
				.. ' please unprotect this file, or reduce to semi-protection,'
				.. ' as appropriate.</span>',
		},
		office = {
			description = 'For pages protected by the Wikimedia Foundation.',
			text = function (protectionObj, args)
				local ret = 'This ${PAGETYPE} is currently under the'
					.. ' scrutiny of the'
					.. ' [Wikimedia Foundation Office](https://second-renaissance.fandom.com/wiki/Wikipedia:Office_actions)'
					.. ' and is protected.'
				if protectionObj.protectionDate then
					ret = ret .. ' It has been protected since ${PROTECTIONDATE}.'
				end
				return ret
			end,
			explanation = "If you can edit this page, please discuss all changes and"
				.. " additions on the ${TALKPAGE} first. '''Do not remove protection from this"
				.. " page unless you are authorized by the Wikimedia Foundation to do"
				.. " so.'''",
			image = 'Padlock-black.svg',
		},
		reset = {
			description = 'For pages protected by the Wikimedia Foundation and'
				.. ' "reset" to a bare-bones version.',
 			text = 'This ${PAGETYPE} is currently under the'
					.. ' scrutiny of the'
					.. ' [Wikimedia Foundation Office](https://second-renaissance.fandom.com/wiki/Wikipedia:Office_actions)'
					.. ' and is protected.',
			explanation = function (protectionObj, args)
				local ret = ''
				if protectionObj.protectionDate then
					ret = ret .. 'On ${PROTECTIONDATE} this ${PAGETYPE} was'
				else
					ret = ret .. 'This ${PAGETYPE} has been'
				end
				ret = ret .. ' reduced to a'
				.. ' simplified, "bare bones" version so that it may be completely'
				.. ' rewritten to ensure it meets the policies of'
				.. ' [Neutral Point of View](https://second-renaissance.fandom.com/wiki/WP:NPOV) and [Verifiability](https://second-renaissance.fandom.com/wiki/WP:V).'
				.. ' Standard Wikipedia policies will apply to its rewriting—which'
				.. ' will eventually be open to all editors—and will be strictly'
				.. ' enforced. The ${PAGETYPE} has been ${PROTECTIONLEVEL} while'
				.. ' it is being rebuilt.\n\n'
				.. 'Any insertion of material directly from'
				.. ' pre-protection revisions of the ${PAGETYPE} will be removed, as'
				.. ' will any material added to the ${PAGETYPE} that is not properly'
				.. ' sourced. The associated talk page(s) were also cleared on the'
				.. " same date.\n\n"
				.. "If you can edit this page, please discuss all changes and"
				.. " additions on the ${TALKPAGE} first. '''Do not override"
				.. " this action, and do not remove protection from this page,"
				.. " unless you are authorized by the Wikimedia Foundation"
				.. " to do so. No editor may remove this notice.'''"

				return ret
			end,
			image = 'Padlock-black.svg',
		},
		sock = {
			description = 'For pages protected due to'
				.. ' [sock puppetry](https://second-renaissance.fandom.com/wiki/Wikipedia:Sock_puppetry).',
			text = '${INTROFRAGMENT} to prevent [sock puppets](https://second-renaissance.fandom.com/wiki/Wikipedia:Sock_puppetry) of'
				.. ' [blocked](https://second-renaissance.fandom.com/wiki/Wikipedia:Blocking_policy) or'
				.. ' [banned users](https://second-renaissance.fandom.com/wiki/Wikipedia:Banning_policy)'
				.. ' from editing it.',
			tooltip = '${TOOLTIPFRAGMENT} to prevent sock puppets of blocked or banned users from'
				.. ' editing it',
		},
		template = {
			description = 'For [high-risk](https://second-renaissance.fandom.com/wiki/Wikipedia:High-risk_templates)'
				.. ' templates and Lua modules.',
			text = 'This is a permanently [protected](https://second-renaissance.fandom.com/wiki/Help:Protection) ${PAGETYPE},'
				.. ' as it is [high-risk](https://second-renaissance.fandom.com/wiki/Wikipedia:High-risk_templates).',
			explanation = 'Please discuss any changes on the ${TALKPAGE}; you may'
				.. ' ${EDITREQUEST} to ask an'
				.. ' [administrator](https://second-renaissance.fandom.com/wiki/Wikipedia:Administrators) or'
				.. ' [template editor](https://second-renaissance.fandom.com/wiki/Wikipedia:Template_editor) to make an edit if'
				.. ' it is [uncontroversial](https://second-renaissance.fandom.com/wiki/Help:Minor_edit) or supported by'
				.. ' [consensus](https://second-renaissance.fandom.com/wiki/Wikipedia:Consensus). You can also'
				.. ' [request](https://second-renaissance.fandom.com/wiki/Wikipedia:Requests_for_page_protection) that the page be'
				.. ' unprotected.',
			tooltip = 'This high-risk ${PAGETYPE} is permanently ${PROTECTIONLEVEL}'
				.. ' to prevent vandalism',
			alt = 'Permanently protected ${PAGETYPE}',
		},
		usertalk = {
			description = 'For pages protected against disruptive edits by a'
				.. ' particular user.',
			text = '${INTROFRAGMENT} to prevent ${VANDAL} from using it to make disruptive edits,'
				.. ' such as abusing the'
				.. ' &#123;&#123;[unblock](https://second-renaissance.fandom.com/wiki/Template:unblock)&#125;&#125; template.',
			explanation = 'If you cannot edit this user talk page and you need to'
				.. ' make a change or leave a message, you can'
				.. ' [request an edit](https://second-renaissance.fandom.com/wiki/Wikipedia:Requests_for_page_protection'
				.._'),'
				.. ' [request unprotection](https://second-renaissance.fandom.com/wiki/Wikipedia:Requests_for_page_protection'
				.._'),'
				.. ' [log in](https://second-renaissance.fandom.com/wiki/Special:Userlogin),'
				.. ' or [create an account](https://second-renaissance.fandom.com/wiki/Special:UserLogin/signup).',
		},
		vandalism = {
			description = 'For pages protected against'
				.. ' [vandalism](https://second-renaissance.fandom.com/wiki/Wikipedia:Vandalism).',
			text = '${INTROFRAGMENT} due to [vandalism](https://second-renaissance.fandom.com/wiki/Wikipedia:Vandalism).',
			explanation = function (protectionObj, args)
				local ret = ''
				if protectionObj.level == 'sysop' then
					ret = ret .. "This protection is '''not''' an endorsement of the"
						.. ' ${CURRENTVERSION}. '
				end
				return ret .. '${EXPLANATIONBLURB}'
			end,
			tooltip = '${TOOLTIPFRAGMENT} due to vandalism',
		}
	},
	move = {
		dispute = {
			description = 'For pages protected against page moves due to'
				.. ' disputes over the page title.',
			explanation = "This protection is '''not''' an endorsement of the"
				.. ' ${CURRENTVERSION}. ${EXPLANATIONBLURB}',
			image = 'Padlock-olive.svg'
		},
		vandalism = {
			description = 'For pages protected against'
				.. ' [page-move vandalism](https://second-renaissance.fandom.com/wiki/Wikipedia:Vandalism).'
		}
	},
	autoreview = {}
},

--------------------------------------------------------------------------------
--
--                            GENERAL DATA TABLES
--
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
-- Protection blurbs
--------------------------------------------------------------------------------

-- This table produces the protection blurbs available with the
-- ${PROTECTIONBLURB} parameter. It is sorted by protection action and
-- protection level, and is checked by the module in the following order:
-- 1. page's protection action, page's protection level
-- 2. page's protection action, default protection level
-- 3. "edit" protection action, default protection level
--
-- It is possible to use banner parameters inside this table.
-- *required* - this table needs edit, move, and autoreview subtables.
protectionBlurbs = {
	edit = {
		default = 'This ${PAGETYPE} is currently ['
			.. 'protected](https://second-renaissance.fandom.com/wiki/Help:Protection) from editing',
		autoconfirmed = 'Editing of this ${PAGETYPE} by [new](https://second-renaissance.fandom.com/wiki/Wikipedia:User_access'
			.._'_levels) or [unregistered](https://second-renaissance.fandom.com/wiki/Wikipedia:User_access_levels) users is currently [disabled](https://second-renaissance.fandom.com/wiki/Help:Protection)'
	},
	move = {
		default = 'This ${PAGETYPE} is currently [protected](https://second-renaissance.fandom.com/wiki/Help:Protection)'
			.. ' from [page moves](https://second-renaissance.fandom.com/wiki/Help:Moving_a_page)'
	},
	autoreview = {
		autoconfirmed = 'All edits made to this ${PAGETYPE} by'
			.. ' [new](https://second-renaissance.fandom.com/wiki/Wikipedia:User_access_levels) or'
			.. ' [unregistered](https://second-renaissance.fandom.com/wiki/Wikipedia:User_access_levels)'
			.. ' users are currently'
			.. ' [subject to review](https://second-renaissance.fandom.com/wiki/Wikipedia:Pending_changes)',
		default = 'All edits made to this ${PAGETYPE} by users who are not'
			.. ' [reviewers](https://second-renaissance.fandom.com/wiki/Wikipedia:Reviewing) or'
			.. ' [administrators](https://second-renaissance.fandom.com/wiki/Wikipedia:Administrators) are currently'
			.. ' [subject to review](https://second-renaissance.fandom.com/wiki/Wikipedia:Pending_changes)'
	}
},


--------------------------------------------------------------------------------
-- Explanation blurbs
--------------------------------------------------------------------------------

-- This table produces the explanation blurbs available with the
-- ${EXPLANATIONBLURB} parameter. It is sorted by protection action,
-- protection level, and whether the page is a talk page or not. If the page is
-- a talk page it will have a talk key of "talk"; otherwise it will have a talk
-- key of "subject". The table is checked in the following order:
-- 1. page's protection action, page's protection level, page's talk key
-- 2. page's protection action, page's protection level, default talk key
-- 3. page's protection action, default protection level, page's talk key
-- 4. page's protection action, default protection level, default talk key
--
-- It is possible to use banner parameters inside this table.
-- *required* - this table needs edit, move, and autoreview subtables.
explanationBlurbs = {
	edit = {
		autoconfirmed = {
			subject = 'See the ['
				.. 'protection policy](https://second-renaissance.fandom.com/wiki/Wikipedia:Protection_policy) and ${PROTECTIONLOG} for more details. If you'
				.. ' cannot edit this ${PAGETYPE} and you wish to make a change, you can'
				.. ' ${EDITREQUEST}, discuss changes on the ${TALKPAGE},'
				.. ' [request unprotection](https://second-renaissance.fandom.com/wiki/Wikipedia:Requests_for_page_protection'
				.._'), [log in](https://second-renaissance.fandom.com/wiki/Special:Userlogin), or'
				.. ' [create an account](https://second-renaissance.fandom.com/wiki/Special:UserLogin/signup).',
			default = 'See the ['
				.. 'protection policy](https://second-renaissance.fandom.com/wiki/Wikipedia:Protection_policy) and ${PROTECTIONLOG} for more details. If you'
				.. ' cannot edit this ${PAGETYPE} and you wish to make a change, you can'
				.. ' [request unprotection](https://second-renaissance.fandom.com/wiki/Wikipedia:Requests_for_page_protection'
				.._'), [log in](https://second-renaissance.fandom.com/wiki/Special:Userlogin), or'
				.. ' [create an account](https://second-renaissance.fandom.com/wiki/Special:UserLogin/signup).',
		},
		default = {
			subject = 'See the ['
				.. 'protection policy](https://second-renaissance.fandom.com/wiki/Wikipedia:Protection_policy) and ${PROTECTIONLOG} for more details.'
				.. ' Please discuss any changes on the ${TALKPAGE}; you'
				.. ' may ${EDITREQUEST} to ask an'
				.. ' [administrator](https://second-renaissance.fandom.com/wiki/Wikipedia:Administrators) to make an edit if it'
				.. ' is [uncontroversial](https://second-renaissance.fandom.com/wiki/Help:Minor_edit) or supported by [consensus](https://second-renaissance.fandom.com/wiki/Wikipedia:Consensus'
				.._'). You may also [request](https://second-renaissance.fandom.com/wiki/Wikipedia:Requests_for'
				.._'_page_protection) that this page be unprotected.',
			default = 'See the ['
				.. 'protection policy](https://second-renaissance.fandom.com/wiki/Wikipedia:Protection_policy) and ${PROTECTIONLOG} for more details.'
				.. ' You may [request an'
				.. ' edit](https://second-renaissance.fandom.com/wiki/Wikipedia:Requests_for_page'
				.._'_protection) to this page, or [ask](https://second-renaissance.fandom.com/wiki/Wikipedia:Requests_for'
				.._'_page_protection) for it to be unprotected.'
		}
	},
	move = {
		default = {
			subject = 'See the ['
				.. 'protection policy](https://second-renaissance.fandom.com/wiki/Wikipedia:Protection_policy) and ${PROTECTIONLOG} for more details.'
				.. ' The page may still be edited but cannot be moved'
				.. ' until unprotected. Please discuss any suggested moves on the'
				.. ' ${TALKPAGE} or at [Wikipedia:Requested moves](https://second-renaissance.fandom.com/wiki/Wikipedia:Requested_moves). You can also'
				.. ' [request](https://second-renaissance.fandom.com/wiki/Wikipedia:Requests_for_page_protection) that the page be'
				.. ' unprotected.',
			default = 'See the ['
				.. 'protection policy](https://second-renaissance.fandom.com/wiki/Wikipedia:Protection_policy) and ${PROTECTIONLOG} for more details.'
				.. ' The page may still be edited but cannot be moved'
				.. ' until unprotected. Please discuss any suggested moves at'
				.. ' [Wikipedia:Requested moves](https://second-renaissance.fandom.com/wiki/Wikipedia:Requested_moves). You can also'
				.. ' [request](https://second-renaissance.fandom.com/wiki/Wikipedia:Requests_for_page_protection) that the page be'
				.. ' unprotected.'
		}
	},
	autoreview = {
		default = {
			reviewer = 'See the ['
				.. 'protection policy](https://second-renaissance.fandom.com/wiki/Wikipedia:Protection_policy) and ${PROTECTIONLOG} for more details.'
				.. ' Edits to this ${PAGETYPE} will not be visible to readers'
				.. ' until they are accepted by a reviewer or an administrator.'
				.. ' To avoid the need for your edits to be reviewed, you may'
				.. ' [request unprotection](https://second-renaissance.fandom.com/wiki/Wikipedia:Requests_for_page_protection'
				.._'). Experienced editors may also'
				.. ' request the [reviewer user right](https://second-renaissance.fandom.com/wiki/Wikipedia:Reviewing).',
			default = 'See the ['
				.. 'protection policy](https://second-renaissance.fandom.com/wiki/Wikipedia:Protection_policy) and ${PROTECTIONLOG} for more details.'
				.. ' Edits to this ${PAGETYPE} by new and unregistered users'
				.. ' will not be visible to readers until they are accepted by'
				.. ' a reviewer. To avoid the need for your edits to be'
				.. ' reviewed, you may'
				.. ' [request unprotection](https://second-renaissance.fandom.com/wiki/Wikipedia:Requests_for_page_protection'
				.._'), [log in](https://second-renaissance.fandom.com/wiki/Special:Userlogin), or'
				.. ' [create an account](https://second-renaissance.fandom.com/wiki/Special:UserLogin/signup).'
		},
	}
},

--------------------------------------------------------------------------------
-- Protection levels
--------------------------------------------------------------------------------

-- This table provides the data for the ${PROTECTIONLEVEL} parameter, which
-- produces a short label for different protection levels. It is sorted by
-- protection action and proteciton level, and is checked in the following
-- order:
-- 1. page's protection action, page's protection level
-- 2. page's protection action, default protection level
-- 3. "edit" protection action, default protection level
--
-- It is possible to use banner parameters inside this table.
-- *required* - this table needs edit, move, and autoreview subtables.
protectionLevels = {
	edit = {
		default = 'protected',
		templateeditor = 'template-protected',
		autoconfirmed = 'semi-protected',
	},
	move = {
		default = 'move-protected'
	},
	autoreview = {
	}
},

--------------------------------------------------------------------------------
-- Images
--------------------------------------------------------------------------------

-- This table lists different padlock images for each protection action and
-- protection level. It is used if an image is not specified in any of the
-- banner data tables, and if the page does not satisfy the conditions for using
-- the ['image-filename-indef'] image. It is checked in the following order:
-- 1. page's protection action, page's protection level
-- 2. page's protection action, default protection level
images = {
	edit = {
		default = 'Padlock.svg',
		templateeditor = 'Padlock-pink.svg',
		autoconfirmed = 'Padlock-silver.svg'
	},
	move = {
		default = 'Padlock-olive.svg',
	},
	autoreview = {
		autoconfirmed = 'Padlock-silver-light.svg',
		default = 'Padlock-orange.svg'
	}
},

-- Pages with a reason specified in this table will show the special "indef"
-- padlock, defined in the 'image-filename-indef' message, if no expiry is set.
indefImageReasons = {
	template = true
},

--------------------------------------------------------------------------------
-- Image links
--------------------------------------------------------------------------------

-- This table provides the data for the ${IMAGELINK} parameter, which gets
-- the image link for small padlock icons based on the page's protection action
-- and protection level. It is checked in the following order:
-- 1. page's protection action, page's protection level
-- 2. page's protection action, default protection level
-- 3. "edit" protection action, default protection level
--
-- It is possible to use banner parameters inside this table.
-- *required* - this table needs edit, move, and autoreview subtables.
imageLinks = {
	edit = {
		default = 'Wikipedia:Protection policy#full',
		templateeditor = 'Wikipedia:Protection policy#template',
		autoconfirmed = 'Wikipedia:Protection policy#semi'
	},
	move = {
		default = 'Wikipedia:Protection policy#move'
	},
	autoreview = {
		autoconfirmed = 'Wikipedia:Protection policy#pc1',
		reviewer = 'Wikipedia:Protection policy#pc2'
	}
},

--------------------------------------------------------------------------------
-- Padlock indicator names
--------------------------------------------------------------------------------

-- This table provides the "name" attribute for the <indicator> extension tag
-- with which small padlock icons are generated. All indicator tags on a page
-- are displayed in alphabetical order based on this attribute, and with
-- indicator tags with duplicate names, the last tag on the page wins.
-- The attribute is chosen based on the protection action; table keys must be a
-- protection action name or the string "default".
padlockIndicatorNames = {
	autoreview = 'pp-autoreview',
	default = 'pp-default'
},

--------------------------------------------------------------------------------
-- Protection categories
--------------------------------------------------------------------------------

--[-- The protection categories are stored in the protectionCategories table.
-- Keys to this table are made up of the following strings:
--
-- 1. the expiry date
-- 2. the namespace
-- 3. the protection reason (e.g. "dispute" or "vandalism")
-- 4. the protection level (e.g. "sysop" or "autoconfirmed")
-- 5. the action (e.g. "edit" or "move")
-- 
-- When the module looks up a category in the table, first it will will check to
-- see a key exists that corresponds to all five parameters. For example, a
-- user page semi-protected from vandalism for two weeks would have the key
-- "temp-user-vandalism-autoconfirmed-edit". If no match is found, the module
-- changes the first part of the key to "all" and checks the table again. It
-- keeps checking increasingly generic key combinations until it finds the
-- field, or until it reaches the key "all-all-all-all-all".
--
-- The module uses a binary matrix to determine the order in which to search.
-- This is best demonstrated by a table. In this table, the "0" values
-- represent "all", and the "1" values represent the original data (e.g.
-- "indef" or "file" or "vandalism").
--
--        expiry    namespace reason   level     action
-- order
-- 1      1         1         1        1         1
-- 2      0         1         1        1         1
-- 3      1         0         1        1         1
-- 4      0         0         1        1         1
-- 5      1         1         0        1         1
-- 6      0         1         0        1         1
-- 7      1         0         0        1         1
-- 8      0         0         0        1         1
-- 9      1         1         1        0         1
-- 10     0         1         1        0         1
-- 11     1         0         1        0         1
-- 12     0         0         1        0         1
-- 13     1         1         0        0         1
-- 14     0         1         0        0         1
-- 15     1         0         0        0         1
-- 16     0         0         0        0         1
-- 17     1         1         1        1         0
-- 18     0         1         1        1         0
-- 19     1         0         1        1         0
-- 20     0         0         1        1         0
-- 21     1         1         0        1         0
-- 22     0         1         0        1         0
-- 23     1         0         0        1         0
-- 24     0         0         0        1         0
-- 25     1         1         1        0         0
-- 26     0         1         1        0         0
-- 27     1         0         1        0         0
-- 28     0         0         1        0         0
-- 29     1         1         0        0         0
-- 30     0         1         0        0         0
-- 31     1         0         0        0         0
-- 32     0         0         0        0         0
--
-- In this scheme the action has the highest priority, as it is the last
-- to change, and the expiry has the least priority, as it changes the most.
-- The priorities of the expiry, the protection level and the action are
-- fixed, but the priorities of the reason and the namespace can be swapped
-- through the use of the cfg.bannerDataNamespaceHasPriority table.
--](https://second-renaissance.fandom.com/wiki/--_The_protection_categories_are_stored_in_the_protectionCategories_table.
--_Keys_to_this_table_are_made_up_of_the_following_strings:
--
--_1._the_expiry_date
--_2._the_namespace
--_3._the_protection_reason_(e.g._"dispute"_or_"vandalism")
--_4._the_protection_level_(e.g._"sysop"_or_"autoconfirmed")
--_5._the_action_(e.g._"edit"_or_"move")
--_
--_When_the_module_looks_up_a_category_in_the_table,_first_it_will_will_check_to
--_see_a_key_exists_that_corresponds_to_all_five_parameters._For_example,_a
--_user_page_semi-protected_from_vandalism_for_two_weeks_would_have_the_key
--_"temp-user-vandalism-autoconfirmed-edit"._If_no_match_is_found,_the_module
--_changes_the_first_part_of_the_key_to_"all"_and_checks_the_table_again._It
--_keeps_checking_increasingly_generic_key_combinations_until_it_finds_the
--_field,_or_until_it_reaches_the_key_"all-all-all-all-all".
--
--_The_module_uses_a_binary_matrix_to_determine_the_order_in_which_to_search.
--_This_is_best_demonstrated_by_a_table._In_this_table,_the_"0"_values
--_represent_"all",_and_the_"1"_values_represent_the_original_data_(e.g.
--_"indef"_or_"file"_or_"vandalism").
--
--________expiry____namespace_reason___level_____action
--_order
--_1______1_________1_________1________1_________1
--_2______0_________1_________1________1_________1
--_3______1_________0_________1________1_________1
--_4______0_________0_________1________1_________1
--_5______1_________1_________0________1_________1
--_6______0_________1_________0________1_________1
--_7______1_________0_________0________1_________1
--_8______0_________0_________0________1_________1
--_9______1_________1_________1________0_________1
--_10_____0_________1_________1________0_________1
--_11_____1_________0_________1________0_________1
--_12_____0_________0_________1________0_________1
--_13_____1_________1_________0________0_________1
--_14_____0_________1_________0________0_________1
--_15_____1_________0_________0________0_________1
--_16_____0_________0_________0________0_________1
--_17_____1_________1_________1________1_________0
--_18_____0_________1_________1________1_________0
--_19_____1_________0_________1________1_________0
--_20_____0_________0_________1________1_________0
--_21_____1_________1_________0________1_________0
--_22_____0_________1_________0________1_________0
--_23_____1_________0_________0________1_________0
--_24_____0_________0_________0________1_________0
--_25_____1_________1_________1________0_________0
--_26_____0_________1_________1________0_________0
--_27_____1_________0_________1________0_________0
--_28_____0_________0_________1________0_________0
--_29_____1_________1_________0________0_________0
--_30_____0_________1_________0________0_________0
--_31_____1_________0_________0________0_________0
--_32_____0_________0_________0________0_________0
--
--_In_this_scheme_the_action_has_the_highest_priority,_as_it_is_the_last
--_to_change,_and_the_expiry_has_the_least_priority,_as_it_changes_the_most.
--_The_priorities_of_the_expiry,_the_protection_level_and_the_action_are
--_fixed,_but_the_priorities_of_the_reason_and_the_namespace_can_be_swapped
--_through_the_use_of_the_cfg.bannerDataNamespaceHasPriority_table.
--)

-- If the reason specified to the template is listed in this table,
-- namespace data will take priority over reason data in the protectionCategories
-- table.
reasonsWithNamespacePriority = {
	vandalism = true,
},

-- The string to use as a namespace key for the protectionCategories table for each
-- namespace number.
categoryNamespaceKeys = {
	[  2] = 'user',
	[  3] = 'user',
	[  4] = 'project',
	[  6] = 'file',
	[  8] = 'mediawiki',
	[ 10] = 'template',
	[ 12] = 'project',
	[ 14] = 'category',
	[100] = 'portal',
	[828] = 'module',
},

protectionCategories = {
	['all|all|all|all|all']                  = 'Wikipedia protected pages',
	['all|all|office|all|all']               = 'Wikipedia Office-protected pages',
	['all|all|reset|all|all']                = 'Wikipedia Office-protected pages',
	['all|all|dmca|all|all']                 = 'Wikipedia Office-protected pages',
	['all|all|mainpage|all|all']             = 'Protected main page images',
	['all|template|all|all|edit']            = 'Wikipedia protected templates',
	['all|all|all|autoconfirmed|edit']       = 'Wikipedia semi-protected pages',
	['indef|all|all|autoconfirmed|edit']     = 'Wikipedia indefinitely semi-protected pages',
	['all|all|blp|autoconfirmed|edit']       = 'Wikipedia indefinitely semi-protected biographies of living people',
	['temp|all|blp|autoconfirmed|edit']      = 'Wikipedia temporarily semi-protected biographies of living people',
	['all|all|dispute|autoconfirmed|edit']   = 'Wikipedia pages semi-protected due to dispute',
	['all|all|sock|autoconfirmed|edit']      = 'Wikipedia pages semi-protected from banned users',
	['all|all|vandalism|autoconfirmed|edit'] = 'Wikipedia pages semi-protected against vandalism',
	['all|category|all|autoconfirmed|edit']  = 'Wikipedia semi-protected categories',
	['all|file|all|autoconfirmed|edit']      = 'Semi-protected images',
	['all|portal|all|autoconfirmed|edit']    = 'Semi-protected portals',
	['all|project|all|autoconfirmed|edit']   = 'Semi-protected project pages',
	['all|talk|all|autoconfirmed|edit']      = 'Semi-protected talk pages',
	['all|template|all|autoconfirmed|edit']  = 'Wikipedia semi-protected templates',
	['all|user|all|autoconfirmed|edit']      = 'Wikipedia semi-protected user and user talk pages',
	['all|all|blp|sysop|edit']               = 'Wikipedia indefinitely protected biographies of living people',
	['temp|all|blp|sysop|edit']              = 'Wikipedia temporarily protected biographies of living people',
	['all|all|dispute|sysop|edit']           = 'Wikipedia pages protected due to dispute',
	['all|all|sock|sysop|edit']              = 'Wikipedia pages protected from banned users',
	['all|all|vandalism|sysop|edit']         = 'Wikipedia pages protected against vandalism',
	['all|category|all|sysop|edit']          = 'Wikipedia protected categories',
	['all|file|all|sysop|edit']              = 'Protected images',
	['all|project|all|sysop|edit']           = 'Protected project pages',
	['all|talk|all|sysop|edit']              = 'Protected talk pages',
	['all|template|all|sysop|edit']          = 'Wikipedia protected templates',
	['all|user|all|sysop|edit']              = 'Wikipedia protected user and user talk pages',
	['all|module|all|all|edit']              = 'Wikipedia protected modules',
	['all|module|all|autoconfirmed|edit']    = 'Wikipedia semi-protected modules',
	['all|all|all|sysop|move']               = 'Wikipedia move-protected pages',
	['indef|all|all|sysop|move']             = 'Wikipedia indefinitely move-protected pages',
	['all|all|dispute|sysop|move']           = 'Wikipedia pages move-protected due to dispute',
	['all|all|vandalism|sysop|move']         = 'Wikipedia pages move-protected due to vandalism',
	['all|portal|all|sysop|move']            = 'Wikipedia move-protected portals',
	['all|portal|all|sysop|move']            = 'Wikipedia move-protected portals',
	['all|project|all|sysop|move']           = 'Wikipedia move-protected project pages',
	['all|talk|all|sysop|move']              = 'Wikipedia move-protected talk pages',
	['all|template|all|sysop|move']          = 'Wikipedia move-protected templates',
	['all|user|all|sysop|move']              = 'Wikipedia move-protected user and user talk pages',
	['all|all|all|autoconfirmed|autoreview'] = 'Wikipedia pending changes protected pages (level 1)',
	['all|all|all|reviewer|autoreview']      = 'Wikipedia pending changes protected pages (level 2)',
},

--------------------------------------------------------------------------------
-- Expiry category config
--------------------------------------------------------------------------------

-- This table configures the expiry category behaviour for each protection
-- action.
-- * If set to true, setting that action will always categorise the page if
--   an expiry parameter is not set.
-- * If set to false, setting that action will never categorise the page.
-- * If set to nil, the module will categorise the page if:
--   1) an expiry parameter is not set, and
--   2) a reason is provided, and
--   3) the specified reason is not blacklisted in the reasonsWithoutExpiryCheck
--      table.

expiryCheckActions = {
	edit = nil,
	move = false,
	autoreview = true
},

reasonsWithoutExpiryCheck = {
	blp = true,
	template = true,
},

--------------------------------------------------------------------------------
-- Pagetypes
--------------------------------------------------------------------------------

-- This table produces the page types available with the ${PAGETYPE} parameter.
-- Keys are namespace numbers, or the string "default" for the default value.
pagetypes = {
	[0] = 'article',
	[6] = 'file',
	[10] = 'template',
	[14] = 'category',
	[828] = 'module',
	default = 'page'
},

--------------------------------------------------------------------------------
-- Strings marking indefinite protection
--------------------------------------------------------------------------------

-- This table contains values passed to the expiry parameter that mean the page
-- is protected indefinitely.
indefStrings = {
	['indef'] = true,
	['indefinite'] = true,
	['indefinitely'] = true,
	['infinite'] = true,
},

--------------------------------------------------------------------------------
-- Group hierarchy
--------------------------------------------------------------------------------

-- This table maps each group to all groups that have a superset of the original
-- group's page editing permissions.
hierarchy = {
	sysop = {},
	reviewer = {'sysop'},
	filemover = {'sysop'},
	templateeditor = {'sysop'},
	autoconfirmed = {'reviewer', 'filemover', 'templateeditor'},
	user = {'autoconfirmed'},
	['*'] = {'user'}
},

--------------------------------------------------------------------------------
-- Wrapper templates and their default arguments
--------------------------------------------------------------------------------

-- This table contains wrapper templates used with the module, and their
-- default arguments. Templates specified in this table should contain the
-- following invocation, and no other template content:
--
-- {{#invoke:Protection banner|main}}
--
-- If other content is desired, it can be added between
-- <noinclude>...</noinclude> tags.
--
-- When a user calls one of these wrapper templates, they will use the
-- default arguments automatically. The arguments cannot be overwritten by the
-- user.
wrappers = {
	['Template:Pp']                         = {},
	['Template:Pp-blp']                     = {'blp'},
	-- we don't need Template:Pp-create
	['Template:Pp-dispute']                 = {'dispute'},
	['Template:Pp-main-page']                = {'mainpage'},
	['Template:Pp-move']                    = {action = 'move'},
	['Template:Pp-move-dispute']            = {'dispute', action = 'move'},
	-- we don't need Template:Pp-move-indef
	['Template:Pp-move-vandalism']          = {'vandalism', action = 'move'},
	['Template:Pp-office']                  = {'office'},
	['Template:Pp-office-dmca']             = {'dmca'},
	['Template:Pp-pc1']                     = {action = 'autoreview', small = true},
	['Template:Pp-pc2']                     = {action = 'autoreview', small = true},
	['Template:Pp-reset']                   = {'reset'},
	['Template:Pp-semi-indef']              = {expiry = 'indef', small = true},
	['Template:Pp-sock']                    = {'sock'},
	['Template:Pp-template']                = {'template', small = true},
	['Template:Pp-usertalk']                = {'usertalk'},
	['Template:Pp-vandalism']               = {'vandalism'},
},

--------------------------------------------------------------------------------
-- 
--                                 MESSAGES
-- 
--------------------------------------------------------------------------------

msg = {

--------------------------------------------------------------------------------
-- Intro blurb and intro fragment
--------------------------------------------------------------------------------

-- These messages specify what is produced by the ${INTROBLURB} and
-- ${INTROFRAGMENT} parameters. If the protection is temporary they use the
-- intro-blurb-expiry or intro-fragment-expiry, and if not they use
-- intro-blurb-noexpiry or intro-fragment-noexpiry.
-- It is possible to use banner parameters in these messages.
['intro-blurb-expiry'] = '${PROTECTIONBLURB} until ${EXPIRY}.',
['intro-blurb-noexpiry'] = '${PROTECTIONBLURB}.',
['intro-fragment-expiry'] = '${PROTECTIONBLURB} until ${EXPIRY},',
['intro-fragment-noexpiry'] = '${PROTECTIONBLURB}',

--------------------------------------------------------------------------------
-- Tooltip blurb
--------------------------------------------------------------------------------

-- These messages specify what is produced by the ${TOOLTIPBLURB} parameter.
-- If the protection is temporary the tooltip-blurb-expiry message is used, and
-- if not the tooltip-blurb-noexpiry message is used.
-- It is possible to use banner parameters in these messages.
['tooltip-blurb-expiry'] = 'This ${PAGETYPE} is ${PROTECTIONLEVEL} until ${EXPIRY}.',
['tooltip-blurb-noexpiry'] = 'This ${PAGETYPE} is ${PROTECTIONLEVEL}.',
['tooltip-fragment-expiry'] = 'This ${PAGETYPE} is ${PROTECTIONLEVEL} until ${EXPIRY},',
['tooltip-fragment-noexpiry'] = 'This ${PAGETYPE} is ${PROTECTIONLEVEL}',

--------------------------------------------------------------------------------
-- Special explanation blurb
--------------------------------------------------------------------------------

-- An explanation blurb for pages that cannot be unprotected, e.g. for pages
-- in the MediaWiki namespace.
-- It is possible to use banner parameters in this message.
['explanation-blurb-nounprotect'] = 'See the ['
	.. 'protection policy](https://second-renaissance.fandom.com/wiki/Wikipedia:Protection_policy) and ${PROTECTIONLOG} for more details.'
	.. ' Please discuss any changes on the ${TALKPAGE}; you'
	.. ' may ${EDITREQUEST} to ask an'
	.. ' [administrator](https://second-renaissance.fandom.com/wiki/Wikipedia:Administrators) to make an edit if it'
	.. ' is [uncontroversial](https://second-renaissance.fandom.com/wiki/Help:Minor_edit) or supported by [consensus](https://second-renaissance.fandom.com/wiki/Wikipedia:Consensus'
	.._').',

--------------------------------------------------------------------------------
-- Protection log display values
--------------------------------------------------------------------------------

-- These messages determine the display values for the protection log link
-- or the pending changes log link produced by the ${PROTECTIONLOG} parameter.
-- It is possible to use banner parameters in these messages.
['protection-log-display'] = 'protection log',
['pc-log-display'] = 'pending changes log',

--------------------------------------------------------------------------------
-- Current version display values
--------------------------------------------------------------------------------

-- These messages determine the display values for the page history link
-- or the move log link produced by the ${CURRENTVERSION} parameter.
-- It is possible to use banner parameters in these messages.
['current-version-move-display'] = 'current title',
['current-version-edit-display'] = 'current version',

--------------------------------------------------------------------------------
-- Talk page
--------------------------------------------------------------------------------

-- This message determines the display value of the talk page link produced
-- with the ${TALKPAGE} parameter.
-- It is possible to use banner parameters in this message.
['talk-page-link-display'] = 'talk page',

--------------------------------------------------------------------------------
-- Edit requests
--------------------------------------------------------------------------------

-- This message determines the display value of the edit request link produced
-- with the ${EDITREQUEST} parameter.
-- It is possible to use banner parameters in this message.
['edit-request-display'] = 'submit an edit request',

--------------------------------------------------------------------------------
-- Expiry date format
--------------------------------------------------------------------------------

-- This is the format for the blurb expiry date. It should be valid input for
-- the first parameter of the #time parser function.
['expiry-date-format'] = 'F j, Y',

--------------------------------------------------------------------------------
-- Tracking categories
--------------------------------------------------------------------------------

-- These messages determine which tracking categories the module outputs.
['tracking-category-incorrect'] = 'Wikipedia pages with incorrect protection templates',
['tracking-category-expiry'] = 'Wikipedia protected pages without expiry',
['tracking-category-template'] = 'Wikipedia template-protected pages other than templates and modules',

--------------------------------------------------------------------------------
-- Images
--------------------------------------------------------------------------------

-- These are images that are not defined by their protection action and protection level.
['image-filename-indef'] = 'Padlock-red.svg',
['image-filename-default'] = 'Transparent.gif',

--------------------------------------------------------------------------------
-- End messages
--------------------------------------------------------------------------------
}

--------------------------------------------------------------------------------
-- End configuration
--------------------------------------------------------------------------------
}
```

## Provenance

Raw source: `bronze/pages/603/841.wikitext` · revision `841` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3AProtection_banner/config)
