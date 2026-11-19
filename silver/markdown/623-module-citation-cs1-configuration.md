---
page_id: 623
revision_id: 864
source_url: https://second-renaissance.fandom.com/wiki/Module%3ACitation/CS1/Configuration
raw_sha256: a4e28c9067fd6dd070792762b39f67c5bd624a2b49e401b51853062234151fd8
---

# Module:Citation/CS1/Configuration

## Preserved source

```wikitext

local citation_config = {};

-- override <code>...</code> styling to remove color, border, and padding.  <code> css is specified here:
-- https://git.wikimedia.org/blob/mediawiki%2Fcore.git/69cd73811f7aadd093050dbf20ed70ef0b42a713/skins%2Fcommon%2FcommonElements.css#L199
local code_style="color:inherit; border:inherit; padding:inherit;";

--[--------------------------< U N C A T E G O R I Z E D _ N A M E S P A C E S >------------------------------

List of namespaces that should not be included in citation error categories.  Same as setting notracking = true by default

Note: Namespace names should use underscores instead of spaces.](https://second-renaissance.fandom.com/wiki/--------------------------<_U_N_C_A_T_E_G_O_R_I_Z_E_D___N_A_M_E_S_P_A_C_E_S_>------------------------------

List_of_namespaces_that_should_not_be_included_in_citation_error_categories.__Same_as_setting_notracking_=_true_by_default

Note:_Namespace_names_should_use_underscores_instead_of_spaces.)
local uncategorized_namespaces = { 'User', 'Talk', 'User_talk', 'Wikipedia_talk', 'File_talk', 'Template_talk',
	'Help_talk', 'Category_talk', 'Portal_talk', 'Book_talk', 'Draft', 'Draft_talk', 'Education_Program_talk', 
	'Module_talk', 'MediaWiki_talk' };

local uncategorized_subpages = {'/[Ss]andbox', '/[Tt]estcases'};		-- list of Lua patterns found in page names of pages we should not categorize

--[--------------------------< M E S S A G E S >--------------------------------------------------------------

Translation table

The following contains fixed text that may be output as part of a citation.
This is separated from the main body to aid in future translations of this
module.](https://second-renaissance.fandom.com/wiki/--------------------------<_M_E_S_S_A_G_E_S_>--------------------------------------------------------------

Translation_table

The_following_contains_fixed_text_that_may_be_output_as_part_of_a_citation.
This_is_separated_from_the_main_body_to_aid_in_future_translations_of_this
module.)

local messages = {
  ['published'] = 'published $1',
  ['lay summary'] = 'Lay summary',
  ['retrieved'] = 'Retrieved $1',
  ['inactive'] = 'inactive',
  ['archived-dead'] = 'Archived from $1 on $2',
  ['archived-not-dead'] = '$1 from the original on $2',
  ['archived-missing'] = 'Archived from the original$1 on $2',
  ['archived'] = 'Archived',
  ['original'] = 'the original',
  ['editor'] = 'ed.',
  ['editors'] = 'eds.', 
  ['edition'] = '($1 ed.)', 
  ['episode'] = 'Episode $1',
  ['season'] = 'Season $1', 
  ['series'] = 'Series $1',
  ['cartography'] = 'Cartography by $1',
  ['section'] = '§ $1',
  ['sections'] = '§§ $1',
  ['inset'] = '$1 inset',
  ['written'] = 'Written at $1',
  ['in'] = 'In',
  ['et al'] = 'et al.', 
  
  ['subscription'] = '<span style="font-size:0.95em; font-size:90%; color:#555">(subscription required (<span title="Sources are not required to be available online. Online sources do not have to be freely available. The site may require a paid subscription." style="border-bottom:1px dotted;cursor:help">help</span>))</span>' ..
  	'[Category:Pages containing links to subscription-only content](https://second-renaissance.fandom.com/wiki/Category:Pages_containing_links_to_subscription-only_content)', 

  ['registration']='<span style="font-size:0.95em; font-size:90%; color:#555">(registration required (<span title="Sources are not required to be available online. Online sources do not have to be freely available. The site may require registration." style="border-bottom:1px dotted;cursor:help">help</span>))</span>' ..
  	'[Category:Pages with login required references or sources](https://second-renaissance.fandom.com/wiki/Category:Pages_with_login_required_references_or_sources)',
  
  ['language'] = '(in $1)', 
  ['via'] = " &ndash; via $1",
  ['event'] = 'Event occurs at',
  ['minutes'] = 'minutes in', 

  ['parameter-separator'] = ', ',
  ['parameter-final-separator'] = ', and ',
  ['parameter-pair-separator'] = ' and ',

  -- Determines the location of the help page
  ['help page link'] = 'Help:CS1 errors',
  ['help page label'] = 'help',
  
  -- Internal errors (should only occur if configuration is bad)
  ['undefined_error'] = 'Called with an undefined error condition',
  ['unknown_manual_ID'] = 'Unrecognized manual ID mode',
  ['unknown_ID_mode'] = 'Unrecognized ID mode',
  ['unknown_argument_map'] = 'Argument map not defined for this variable',
  ['bare_url_no_origin'] = 'Bare url found but origin indicator is nil or empty',
}

--[--------------------------< P R E S E N T A T I O N >------------------------------------------------------

Fixed presentation markup.  Originally part of citation_config.messages it has been moved into its own, more semantically
correct place.](https://second-renaissance.fandom.com/wiki/--------------------------<_P_R_E_S_E_N_T_A_T_I_O_N_>------------------------------------------------------

Fixed_presentation_markup.__Originally_part_of_citation_config.messages_it_has_been_moved_into_its_own,_more_semantically
correct_place.)
local presentation = 
	{
	-- Error output
	-- .error class is specified at https://git.wikimedia.org/blob/mediawiki%2Fcore.git/9553bd02a5595da05c184f7521721fb1b79b3935/skins%2Fcommon%2Fshared.css#L538
	-- .citation-comment class is specified at Help:CS1_errors#Controlling_error_message_display
	['hidden-error'] = '<span style="display:none;font-size:100%" class="error citation-comment">$1</span>',
	['visible-error'] = '<span style="font-size:100%" class="error citation-comment">$1</span>',

	['accessdate'] = '<span class="reference-accessdate">$1$2</span>',			-- to allow editors to hide accessdate using personal css

	['bdi'] = '<bdi$1>$2</bdi>',												-- bidirectional isolation used with |script-title= and the like

	['format'] = ' <span style="font-size:85%;">($1)</span>',					-- for |format=, |chapter-format=, etc

	['italic-title'] = "''$1''",

	['kern-left'] = '<span style="padding-left:0.2em;">$1</span>$2',			-- spacing to use when title contains leading single or double quote mark
	['kern-right'] = '$1<span style="padding-right:0.2em;">$2</span>',			-- spacing to use when title contains trailing single or double quote mark

	['nowrap1'] = '<span class="nowrap">$1</span>',								-- for nowrapping an item: <span ...>yyyy-mm-dd</span>
	['nowrap2'] = '<span class="nowrap">$1</span> $2',							-- for nowrapping portions of an item: <span ...>dd mmmm</span> yyyy (note white space)
	
	['parameter'] = '<code style="'..code_style..'">&#124;$1=</code>',

	['quoted-text'] = '<q>$1</q>',												-- for wrapping |quote= content
	['quoted-title'] = '"$1"',

	['trans-italic-title'] = "&#91;''$1''&#93;",
	['trans-quoted-title'] = "&#91;$1&#93;",
	}

--[--------------------------< A L I A S E S >----------------------------------------------------------------

Aliases table for commonly passed parameters](https://second-renaissance.fandom.com/wiki/--------------------------<_A_L_I_A_S_E_S_>----------------------------------------------------------------

Aliases_table_for_commonly_passed_parameters)

local aliases = {
	['AccessDate'] = {'access-date', 'accessdate'},
	['Agency'] = 'agency',
	['AirDate'] = {'air-date', 'airdate'},
	['ArchiveDate'] = {'archive-date', 'archivedate'},
	['ArchiveFormat'] = 'archive-format',
	['ArchiveURL'] = {'archive-url', 'archiveurl'},
	['ASINTLD'] = {'ASIN-TLD', 'asin-tld'},
	['At'] = 'at',
	['Authors'] = {'authors', 'people', 'host', 'credits'},
	['AuthorFormat'] = {'author-format', 'authorformat'},						-- deprecated in favor of NameListFormat;
	['AuthorSeparator'] = 'author-separator',									-- deprecated
	['AuthorNameSeparator'] = 'author-name-separator',							-- deprecated
	['Began'] = 'began',														-- cite episode and cite series
	['BookTitle'] = {'book-title', 'booktitle'},
	['Callsign'] = {'call-sign', 'callsign'},									-- cite interview
	['Cartography'] = 'cartography',
	['Chapter'] = {'chapter', 'contribution', 'entry', 'article', 'section'},
	['ChapterFormat'] = {'chapter-format', 'contribution-format', 'section-format'};
	['ChapterLink'] = {'chapter-link', 'chapterlink'},							-- deprecated; remove after 1 January 2015?
	['ChapterURL'] = {'chapter-url', 'chapterurl', 'contribution-url', 'contributionurl', 'section-url', 'sectionurl'},
	['City'] = 'city',															-- cite interview
	['Class'] = 'class',														-- cite arxiv and arxiv identifiers
	['Coauthors'] = {'coauthors', 'coauthor'},									-- coauthor and coauthors are deprecated; remove after 1 January 2015?
	['Conference'] = {'conference', 'event'},
	['ConferenceFormat'] = {'conference-format', 'event-format'},
	['ConferenceURL'] = {'conference-url', 'conferenceurl', 'event-url', 'eventurl'},
	['Date'] = {'date', 'air-date', 'airdate'},
	['DeadURL'] = {'dead-url', 'deadurl'},
	['Degree'] = 'degree',
	['DisplayAuthors'] = {'display-authors', 'displayauthors'},
	['DisplayEditors'] = {'display-editors', 'displayeditors'},
	['Docket'] = 'docket',
	['DoiBroken'] = {'doi-broken', 'doi-broken-date', 'doi-inactive-date', 'doi_brokendate', 'doi_inactivedate'},
	['Edition'] = 'edition',
	['Editors'] = 'editors',
	['EditorFormat'] = {'editor-format', 'editorformat'},						-- deprecated in favor of NameListFormat;
	['EditorSeparator'] = 'editor-separator',									-- deprecated
	['EditorNameSeparator'] = 'editor-name-separator',							-- deprecated
	['Embargo'] = 'embargo',
	['Encyclopedia'] = {'encyclopedia', 'encyclopaedia'},						-- this one only used by citation
	['Ended'] = 'ended',														-- cite episode and cite series
	['Episode'] = 'episode',													-- cite serial only TODO: make available to cite episode?
	['Format'] = 'format',
	['ID'] = {'id', 'ID'},
	['IgnoreISBN'] = {'ignore-isbn-error', 'ignoreisbnerror'},
	['Inset'] = 'inset',
	['Issue'] = {'issue', 'number'},
	['Language'] = {'language', 'in'},
	['LastAuthorAmp'] = {'last-author-amp', 'lastauthoramp'},
	['LayDate'] = {'lay-date', 'laydate'},
	['LayFormat'] = 'lay-format',
	['LaySource'] = {'lay-source', 'laysource'},
	['LayURL'] = {'lay-url', 'lay-summary', 'layurl', 'laysummary'},
	['MailingList'] = {'mailinglist', 'mailing-list'},							-- cite mailing list only
	['Map'] = 'map',															-- cite map only
	['MapFormat'] = 'map-format',												-- cite map only
	['MapURL'] = {'mapurl', 'map-url'},											-- cite map only
	['MessageID'] = 'message-id',
	['Minutes'] = 'minutes',
	['Mode'] = 'mode',
	['Month'] = 'month',														-- deprecated; remove after 1 January 2015?
	['NameListFormat'] = {'name-list-format', 'author-format', 'authorformat', 'editor-format', 'editorformat'},
	['NameSeparator'] = 'name-separator',										-- deprecated
	['Network'] = 'network',
	['NoPP'] = {'no-pp', 'nopp'},
	['NoTracking'] = {'template-doc-demo', 'template doc demo', 'no-cat', 'nocat', 
		'no-tracking', 'notracking'},
	['OrigYear'] = {'orig-year', 'origyear'},
	['Others'] = {'others', 'interviewer', 'interviewers'},
	['Page'] = {'p', 'page'},
	['Pages'] = {'pp', 'pages'},
	['Periodical'] = {'journal', 'newspaper', 'magazine', 'work',
		'website',  'periodical', 'encyclopedia', 'encyclopaedia', 'dictionary'},
	['Place'] = {'place', 'location'},
	['PPrefix'] = {'p-prefix', 'PPrefix'},
	['PPPrefix'] = 'pp-prefix',
	['Program'] = 'program',													-- cite interview
	['PostScript'] = 'postscript',
	['PublicationDate'] = {'publicationdate', 'publication-date'},
	['PublicationPlace'] = {'publication-place', 'publicationplace'},
	['PublisherName'] = {'publisher', 'distributor', 'institution', 'newsgroup'},
	['Quote'] = {'quote', 'quotation'},
	['Ref'] = {'ref', 'Ref'},
	['RegistrationRequired'] = 'registration',
	['Scale'] = 'scale',
	['ScriptTitle'] = 'script-title',
	['Section'] = 'section',
	['Season'] = 'season',
	['Sections'] = 'sections',													-- cite map only
	['Separator'] = 'separator',												-- deprecated in favor of Mode
	['Series'] = {'series', 'version'},
	['SeriesSeparator'] = 'series-separator',
	['SeriesLink'] = {'series-link', 'serieslink'},
	['SeriesNumber'] = {'series-number', 'series-no', 'seriesnumber', 'seriesno'},
	['Sheet'] = 'sheet',														-- cite map only
	['Sheets'] = 'sheets',														-- cite map only
	['Station'] = 'station',
	['SubscriptionRequired'] = 'subscription',
	['Time'] = 'time',
	['TimeCaption'] = {'time-caption', 'timecaption'},
	['Title'] = 'title',
	['TitleLink'] = {'title-link', 'episode-link', 'titlelink', 'episodelink'},
	['TitleNote'] = 'department',
	['TitleType'] = {'type', 'medium'},
	['TransChapter'] = {'trans-chapter', 'trans_chapter'},
	['TransMap'] = 'trans-map',													-- cite map only
	['Transcript'] = 'transcript',
	['TranscriptFormat'] = 'transcript-format',
	['TranscriptURL'] = {'transcript-url', 'transcripturl'},
	['TransTitle'] = {'trans-title', 'trans_title'},
	['URL'] = {'url', 'URL'},
	['Vauthors'] = 'vauthors',
	['Veditors'] = 'veditors',
	['Via'] = 'via',
	['Volume'] = 'volume',
	['Year'] = 'year',

	['AuthorList-First'] = {"first#", "given#", "author-first#", "author#-first"},
	['AuthorList-Last'] = {"last#", "author#", "surname#", "author-last#", "author#-last", "subject#", "Author#"},
	['AuthorList-Link'] = {"authorlink#", "author-link#", "author#-link", "subjectlink#", "author#link", "subject-link#", "subject#-link", "subject#link"},
	['AuthorList-Mask'] = {"author-mask#", "authormask#", "author#mask", "author#-mask"},
	
	['EditorList-First'] = {"editor-first#", "editor#-first", "editor-given#", "editor#-given", "EditorGiven#"},
	['EditorList-Last'] = {"editor#", "editor-last#", "editor#-last", "editor-surname#", "editor#-surname", "EditorSurname#", "Editor#"},
	['EditorList-Link'] = {"editor-link#", "editor#-link", "editorlink#", "editor#link"},
	['EditorList-Mask'] = {"editor-mask#", "editor#-mask", "editormask#", "editor#mask"},
}

--[--------------------------< D E F A U L T S >--------------------------------------------------------------

-- Default parameter values](https://second-renaissance.fandom.com/wiki/--------------------------<_D_E_F_A_U_L_T_S_>--------------------------------------------------------------

--_Default_parameter_values)

local defaults = {
	['DeadURL'] = 'yes',
	['PPrefix'] = "p.&nbsp;",
	['PPPrefix'] = "pp.&nbsp;",	
}

--[--------------------------< M A I N T E N A N C E _ C A T E G O R I E S >----------------------------------

Here we name maintenance categories to be used in maintenance messages.](https://second-renaissance.fandom.com/wiki/--------------------------<_M_A_I_N_T_E_N_A_N_C_E___C_A_T_E_G_O_R_I_E_S_>----------------------------------

Here_we_name_maintenance_categories_to_be_used_in_maintenance_messages.)

local maint_cats = {
	['ASIN'] = 'CS1 maint: ASIN uses ISBN',
	['date_year'] = 'CS1 maint: Date and year',
	['disp_auth_ed'] = 'CS1 maint: display-$1',									-- $1 is authors or editors
	['embargo'] = 'CS1 maint: PMC embargo expired',
	['english'] = 'CS1 maint: English language specified',
	['etal'] = 'CS1 maint: Explicit use of et al.',
	['extra_text'] = 'CS1 maint: Extra text',
	['unknown_lang'] = 'CS1 maint: Unrecognized language',
	['untitled'] = 'CS1 maint: Untitled periodical',
	}

--[--------------------------< P R O P E R T I E S _ C A T E G O R I E S >------------------------------------

Here we name properties categories](https://second-renaissance.fandom.com/wiki/--------------------------<_P_R_O_P_E_R_T_I_E_S___C_A_T_E_G_O_R_I_E_S_>------------------------------------

Here_we_name_properties_categories)

local prop_cats = {
	['foreign_lang_source'] = 'CS1 $1-language sources ($2)',					-- |language= categories; $1 is language name, $2 is ISO639-1 code
	['script'] = 'CS1 uses foreign language script',							-- when language specified by |script-title=xx: doesn't have its own category
	['script_with_name'] = 'CS1 uses $1-language script ($2)',					-- |script-title=xx: has matching category; $1 is language name, $2 is ISO639-1 code
	}



--[--------------------------< T I T L E _ T Y P E S >--------------------------------------------------------

Here we map a template's CitationClass to TitleType](https://second-renaissance.fandom.com/wiki/--------------------------<_T_I_T_L_E___T_Y_P_E_S_>--------------------------------------------------------

Here_we_map_a_template's_CitationClass_to_TitleType)

local title_types = {
	['AV-media-notes'] = 'Media notes',
	['DVD-notes'] = 'Media notes',
	['mailinglist'] = 'Mailing list',
	['map'] = 'Map',
	['podcast'] = 'Podcast',
	['pressrelease'] = 'Press release',
	['report'] = 'Report',
	['techreport'] = 'Technical report',
	['thesis'] = 'Thesis',
	}

--[--------------------------< E R R O R _ C O N D I T I O N S >----------------------------------------------

Error condition table

The following contains a list of IDs for various error conditions defined in the 
code.  For each ID, we specify a text message to display, an error category to
include, and whether the error message should be wrapped as a hidden comment.

Anchor changes require identical changes to matching anchor in Help:CS1 errors](https://second-renaissance.fandom.com/wiki/--------------------------<_E_R_R_O_R___C_O_N_D_I_T_I_O_N_S_>----------------------------------------------

Error_condition_table

The_following_contains_a_list_of_IDs_for_various_error_conditions_defined_in_the_
code.__For_each_ID,_we_specify_a_text_message_to_display,_an_error_category_to
include,_and_whether_the_error_message_should_be_wrapped_as_a_hidden_comment.

Anchor_changes_require_identical_changes_to_matching_anchor_in_Help:CS1_errors)

local error_conditions = {
	accessdate_missing_url = {
		message = '<code style="'..code_style..'">&#124;accessdate=</code> requires <code style="'..code_style..'">&#124;url=</code>',
		anchor = 'accessdate_missing_url',
		category = 'Pages using citations with accessdate and no URL',
		hidden = true },
	archive_missing_date = {
		message = '<code style="'..code_style..'">&#124;archiveurl=</code> requires <code style="'..code_style..'">&#124;archivedate=</code>',
		anchor = 'archive_missing_date',
		category = 'Pages with archiveurl citation errors',
		hidden = false },
	archive_missing_url = {
		message = '<code style="'..code_style..'">&#124;archiveurl=</code> requires <code style="'..code_style..'">&#124;url=</code>',
		anchor = 'archive_missing_url',
		category = 'Pages with archiveurl citation errors',
		hidden = false },
	arxiv_missing = {
		message = '<code style="'..code_style..'">&#124;arxiv=</code> required',
		anchor = 'arxiv_missing',
		category = 'CS1 errors: arXiv',											-- same as bad arxiv
		hidden = false },
	arxiv_params_not_supported = {
		message = 'Unsupported parameter(s) in cite arXiv',
		anchor = 'arxiv_params_not_supported',
		category = 'CS1 errors: arXiv',											-- same as bad arxiv
		hidden = false },
	bad_arxiv = {
		message = 'Check <code style="'..code_style..'">&#124;arxiv=</code> value',
		anchor = 'bad_arxiv',
		category = 'CS1 errors: arXiv',
		hidden = false },
	bad_asin = {
		message = 'Check <code style="'..code_style..'">&#124;asin=</code> value',
		anchor = 'bad_asin',
		category ='CS1 errors: ASIN',
		hidden = false },
	bad_authorlink = {
		message = 'Check <code style="'..code_style..'">&#124;authorlink=</code> value',
		anchor = 'bad_authorlink',
		category = 'CS1 errors: authorlink',
		hidden = false },
	bad_date = {
		message = 'Check date values in: <code style="'..code_style..'">$1</code>',
		anchor = 'bad_date',
		category = 'CS1 errors: dates',
		hidden = false },
	bad_doi = {
		message = 'Check <code style="'..code_style..'">&#124;doi=</code> value',
		anchor = 'bad_doi',
		category = 'CS1 errors: DOI',
		hidden = false },
	bad_isbn = {
		message = 'Check <code style="'..code_style..'">&#124;isbn=</code> value',
		anchor = 'bad_isbn',
		category = 'Pages with ISBN errors',
		hidden = false },
	bad_ismn = {
		message = 'Check <code style="'..code_style..'">&#124;ismn=</code> value',
		anchor = 'bad_ismn',
		category = 'CS1 errors: ISMN',
		hidden = false },
	bad_issn = {
		message = 'Check <code style="'..code_style..'">&#124;issn=</code> value',
		anchor = 'bad_issn',
		category = 'CS1 errors: ISSN',
		hidden = false },
	bad_lccn = {
		message = 'Check <code style="'..code_style..'">&#124;lccn=</code> value',
		anchor = 'bad_lccn',
		category = 'CS1 errors: LCCN',
		hidden = false },
	bad_message_id = {
		message = 'Check <code style="'..code_style..'">&#124;message-id=</code> value',
		anchor = 'bad_message_id',
		category = 'CS1 errors: message-id',
		hidden = false },
	bad_ol = {
		message = 'Check <code style="'..code_style..'">&#124;ol=</code> value',
		anchor = 'bad_ol',
		category = 'CS1 errors: OL',
		hidden = false },
	bad_pmc = {
		message = 'Check <code style="'..code_style..'">&#124;pmc=</code> value',
		anchor = 'bad_pmc',
		category = 'CS1 errors: PMC',
		hidden = false },
	bad_pmid = {
		message = 'Check <code style="'..code_style..'">&#124;pmid=</code> value',
		anchor = 'bad_pmid',
		category = 'CS1 errors: PMID',
		hidden = false },
	bad_url = {
		message = 'Check <code style="'..code_style..'">&#124;url=</code> scheme',
		anchor = 'bad_url',
		category = 'Pages with URL errors',
		hidden = false },
	bare_url_missing_title = {
		message = '$1 missing title',
		anchor = 'bare_url_missing_title',
		category = 'Pages with citations having bare URLs',
		hidden = false },
	chapter_ignored = {
		message = '<code style="'..code_style..'">&#124;chapter=</code> ignored',
		anchor = 'chapter_ignored',
		category = 'CS1 errors: chapter ignored',
		hidden = false },
	citation_missing_title = {
		message = 'Missing or empty <code style="'..code_style..'">&#124;title=</code>',
		anchor = 'citation_missing_title',
		category = 'Pages with citations lacking titles',
		hidden = false },
	cite_web_url = {															-- this error applies to cite web and to cite podcast
		message = 'Missing or empty <code style="'..code_style..'">&#124;url=</code>',
		anchor = 'cite_web_url',
		category = 'Pages using web citations with no URL',
		hidden = true },
	coauthors_missing_author = {
		message = '<code style="'..code_style..'">&#124;coauthors=</code> requires <code style="'..code_style..'">&#124;author=</code>',
		anchor = 'coauthors_missing_author',
		category = 'CS1 errors: coauthors without author',
		hidden = false },
	deprecated_params = {
		message = 'Cite uses deprecated parameter <code style="'..code_style..'">&#124;$1=</code>',
		anchor = 'deprecated_params',
		category = 'Pages containing cite templates with deprecated parameters',
		hidden = true },
	empty_citation = {
		message = 'Empty citation',
		anchor = 'empty_citation',
		category = 'Pages with empty citations',
		hidden = false },
	extra_pages = {
		message = 'Extra <code style="'..code_style..'">&#124;pages=</code> or <code style="'..code_style..'">&#124;at=</code>',
		anchor = 'extra_pages',
		category = 'Pages with citations using conflicting page specifications',
		hidden = false },
	first_missing_last = {
		message = '<code style="'..code_style..'">&#124;first$2=</code> missing <code style="'..code_style..'">&#124;last$2=</code> in $1',
		anchor = 'first_missing_last',
		category = 'CS1 errors: missing author or editor',
		hidden = false },
	format_missing_url = {
		message = '<code style="'..code_style..'">&#124;$1=</code> requires <code style="'..code_style..'">&#124;$2=</code>',
		anchor = 'format_missing_url',
		category = 'Pages using citations with format and no URL',
		hidden = true },
	implict_etal_editor = {
		message = '<code style="'..code_style..'">&#124;displayeditors=</code> suggested',
		anchor = 'displayeditors',
		category = 'Pages using citations with old-style implicit et al. in editors',
		hidden = true },
	invalid_param_val = {
		message = 'Invalid <code style="'..code_style..'">&#124;$1=$2</code>',
		anchor = 'invalid_param_val',
		category = 'CS1 errors: invalid parameter value',
		hidden = false },
	missing_name = {
		message = 'Missing <code style="'..code_style..'">&#124;last$2=</code> in $1',
		anchor = 'missing_name',
		category = 'CS1 errors: missing author or editor',
		hidden = false },
	parameter_ignored = {
		message = 'Unknown parameter <code style="'..code_style..'">&#124;$1=</code> ignored',
		anchor = 'parameter_ignored',
		category = 'Pages with citations using unsupported parameters',
		hidden = false },
	parameter_ignored_suggest = {
		message = 'Unknown parameter <code style="'..code_style..'">&#124;$1=</code> ignored (<code style="'..code_style..'">&#124;$2=</code> suggested)',
		anchor = 'parameter_ignored_suggest',
		category = 'Pages with citations using unsupported parameters',
		hidden = false },
	redundant_parameters = {
		message = 'More than one of $1 specified',
		anchor = 'redundant_parameters',
		category = 'Pages with citations having redundant parameters',
		hidden = false },
	text_ignored = {
		message = 'Text "$1" ignored',
		anchor = 'text_ignored',
		category = 'Pages with citations using unnamed parameters',
		hidden = false },
	trans_missing_chapter = {
		message = '<code style="'..code_style..'">&#124;trans-chapter=</code> requires <code style="'..code_style..'">&#124;chapter=</code>',
		anchor = 'trans_missing_chapter',
		category = 'Pages with citations using translated terms without the original',
		hidden = false },
	trans_missing_title = {
		message = '<code style="'..code_style..'">&#124;trans-title=</code> requires <code style="'..code_style..'">&#124;title=</code>',
		anchor = 'trans_missing_title',
		category = 'Pages with citations using translated terms without the original',
		hidden = false },
	vancouver = {
		message = 'Vancouver style error',
		anchor = 'vancouver',
		category = 'CS1 errors: Vancouver style',
		hidden = false },
	wikilink_in_url = {
		message = 'Wikilink embedded in URL title',
		anchor = 'wikilink_in_url',
		category = 'Pages with citations having wikilinks embedded in URL titles',
		hidden = false },
}

--[--------------------------< I D _ H A N D L E R S >--------------------------------------------------------

The following contains a list of values for various defined identifiers.  For each identifier we specify a
variety of information necessary to properly render the identifier in the citation.

	parameters: a list of parameter aliases for this identifier
	link: Wikipedia article name
	label: the alternate name to apply to link
	mode: 	'manual' when there is a specific function in the code to handle the identifier;
			'external' for identifiers that link outside of Wikipedia;
	prefix: the first part of a url that will be concatenated with a second part which usually contains the identifier
	encode: true if uri should be percent encoded; otherwise false
	COinS: into rft.id
	separator: character or text between label and the identifier in the rendered citation](https://second-renaissance.fandom.com/wiki/--------------------------<_I_D___H_A_N_D_L_E_R_S_>--------------------------------------------------------

The_following_contains_a_list_of_values_for_various_defined_identifiers.__For_each_identifier_we_specify_a
variety_of_information_necessary_to_properly_render_the_identifier_in_the_citation.

	parameters:_a_list_of_parameter_aliases_for_this_identifier
	link:_Wikipedia_article_name
	label:_the_alternate_name_to_apply_to_link
	mode:_	'manual'_when_there_is_a_specific_function_in_the_code_to_handle_the_identifier;
			'external'_for_identifiers_that_link_outside_of_Wikipedia;
	prefix:_the_first_part_of_a_url_that_will_be_concatenated_with_a_second_part_which_usually_contains_the_identifier
	encode:_true_if_uri_should_be_percent_encoded;_otherwise_false
	COinS:_into_rft.id
	separator:_character_or_text_between_label_and_the_identifier_in_the_rendered_citation)

local id_handlers = {
	['ARXIV'] = {
		parameters = {'arxiv', 'ARXIV', 'eprint'}, 
		link = 'arXiv',
		label = 'arXiv',
		mode = 'manual',
		prefix = '//arxiv.org/abs/', 						-- protocol relative tested 2013-09-04
		encode = false,
		COinS = 'info:arxiv',
		separator = ':',
	},
	['ASIN'] = {
		parameters = { 'asin', 'ASIN' },	   
		link = 'Amazon Standard Identification Number',
		label = 'ASIN',
		mode = 'manual',
		COinS = 'info:asin',
		separator = '&nbsp;',
		encode = false;
	},
	['BIBCODE'] = {
		parameters = {'bibcode', 'BIBCODE'}, 
		link = 'Bibcode',
		label = 'Bibcode',
		mode = 'external',
		prefix = 'http://adsabs.harvard.edu/abs/',
		encode = false,
		COinS = 'info:bibcode',
		separator = ':',
	},
	['DOI'] = {
		parameters = { 'doi', 'DOI' },
		link = 'Digital object identifier',
		label = 'doi',
		mode = 'manual',
		prefix = '//dx.doi.org/',
		COinS = 'info:doi',
		separator = ':',
		encode = true,
	},
	['ISBN'] = {
		parameters = {'isbn', 'ISBN', 'isbn13', 'ISBN13'}, 
		link = 'International Standard Book Number',
		label = 'ISBN',
		mode = 'manual',
		prefix = 'Special:BookSources/',
		COinS = 'rft.isbn',
		separator = '&nbsp;',
	},
	['ISMN'] = {
		parameters = {'ismn', 'ISMN'}, 
		link = 'International Standard Music Number',
		label = 'ISMN',
		mode = 'manual',
		prefix = '',															-- not currently used; 
		COinS = 'info:ismn',
		separator = '&nbsp;',
	},
	['ISSN'] = {
		parameters = {'issn', 'ISSN'}, 
		link = 'International Standard Serial Number',
		label = 'ISSN',
		mode = 'manual',
		prefix = '//www.worldcat.org/issn/',
		COinS = 'rft.issn',
		encode = false,
		separator = '&nbsp;',
	},
	['JFM'] = {
		parameters = {'jfm', 'JFM'}, 
		link = 'Jahrbuch über die Fortschritte der Mathematik',
		label = 'JFM',
		mode = 'external',
		prefix = '//zbmath.org/?format=complete&q=an:',
		COinS = 'rft.jfm',
		encode = true,
		separator = '&nbsp;',
	},
	['JSTOR'] = {
		parameters = {'jstor', 'JSTOR'}, 
		link = 'JSTOR',
		label = 'JSTOR',
		mode = 'external',
		prefix = '//www.jstor.org/stable/', 				-- protocol relative tested 2013-09-04
		COinS = 'rft.jstor',
		encode = false,
		separator = '&nbsp;',
	},
	['LCCN'] = {
		parameters = {'LCCN', 'lccn'}, 
		link = 'Library of Congress Control Number',
		label = 'LCCN',
		mode = 'manual',
		prefix = 'http://lccn.loc.gov/',
		COinS = 'rft.lccn',
		encode = false,
		separator = '&nbsp;',
	},
	['MR'] = {
		parameters = {'MR', 'mr'}, 
		link = 'Mathematical Reviews',
		label = 'MR',
		mode = 'external',
		prefix = '//www.ams.org/mathscinet-getitem?mr=', 	-- protocol relative tested 2013-09-04
		COinS = 'rft.mr',
		encode = true,
		separator = '&nbsp;',
	},
	['OCLC'] = {
		parameters = {'OCLC', 'oclc'}, 
		link = 'OCLC',
		label = 'OCLC',
		mode = 'external',
		prefix = '//www.worldcat.org/oclc/',
		COinS = 'info:oclcnum',
		encode = true,
		separator = '&nbsp;',
	},
	['OL'] = {
		parameters = { 'ol', 'OL' },
		link = 'Open Library',
		label = 'OL',
		mode = 'manual',
		COinS = 'info:olnum',
		separator = '&nbsp;',
		endode = true,
	},
	['OSTI'] = {
		parameters = {'OSTI', 'osti'}, 
		link = 'Office of Scientific and Technical Information',
		label = 'OSTI',
		mode = 'external',
		prefix = '//www.osti.gov/energycitations/product.biblio.jsp?osti_id=',	-- protocol relative tested 2013-09-04
		COinS = 'info:osti',
		encode = true,
		separator = '&nbsp;',
	},
	['PMC'] = {
		parameters = {'PMC', 'pmc'}, 
		link = 'PubMed Central',
		label = 'PMC',
		mode = 'manual',									-- changed to support unlinking of PMC identifier when article is embargoed
		prefix = '//www.ncbi.nlm.nih.gov/pmc/articles/PMC', 
		suffix = " ",
		COinS = 'info:pmc',
		encode = true,
		separator = '&nbsp;',
	},
	['PMID'] = {
		parameters = {'PMID', 'pmid'}, 
		link = 'PubMed Identifier',
		label = 'PMID',
		mode = 'manual',									-- changed from external manual to support PMID validation
		prefix = '//www.ncbi.nlm.nih.gov/pubmed/',
		COinS = 'info:pmid',
		encode = false,
		separator = '&nbsp;',
	},
	['RFC'] = {
		parameters = {'RFC', 'rfc'}, 
		link = 'Request for Comments',
		label = 'RFC',
		mode = 'external',
		prefix = '//tools.ietf.org/html/rfc',
		COinS = 'info:rfc',
		encode = false,
		separator = '&nbsp;',
	},
	['SSRN'] = {
		parameters = {'SSRN', 'ssrn'}, 
		link = 'Social Science Research Network',
		label = 'SSRN',
		mode = 'external',
		prefix = '//ssrn.com/abstract=', 					-- protocol relative tested 2013-09-04
		COinS = 'info:ssrn',
		encode = true,
		separator = '&nbsp;',
	},
	['USENETID'] = {
		parameters = {'message-id'},
		link = 'Usenet',
		label = 'Usenet:',
		mode = 'manual',
		prefix = 'news:',
		encode = false,
		COinS = 'info:usenet',
		separator = '&nbsp;',
	},
	['ZBL'] = {
		parameters = {'ZBL', 'zbl'}, 
		link = 'Zentralblatt MATH',
		label = 'Zbl',
		mode = 'external',
		prefix = '//zbmath.org/?format=complete&q=an:',
		COinS = 'info:zbl',
		encode = true,
		separator = '&nbsp;',
	},
}

return 	{
	aliases = aliases,
	defaults = defaults,
	error_conditions = error_conditions,
	id_handlers = id_handlers,
	maint_cats = maint_cats,
	messages = messages,
	presentation = presentation,
	prop_cats = prop_cats,
	title_types = title_types,
	uncategorized_namespaces = uncategorized_namespaces,
	uncategorized_subpages = uncategorized_subpages,
	}
```

## Provenance

Raw source: `bronze/pages/623/864.wikitext` · revision `864` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3ACitation/CS1/Configuration)
