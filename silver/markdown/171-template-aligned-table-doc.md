---
page_id: 171
revision_id: 228
source_url: https://second-renaissance.fandom.com/wiki/Template%3AAligned_table/doc
raw_sha256: d91debd463d726f47517712bac1383565df8c9d6dcb8f54a2f18bffb767ba80e
---

# Template:Aligned table/doc

## Preserved source

```wikitext
{{Documentation subpage}}
{{Lua|icononly=on |Module:Aligned table}}
<!----Please place categories where indicated at the bottom of this page and interwikis in Wikidata---->
The purpose is of this template is for generating simple tables in locations where [standard table markup](https://second-renaissance.fandom.com/wiki/Help:Table) is either not possible, without significant use of the {{tld|!}} magic word (e.g., with a {{tl|sidebar}} template), or cumbersome (due to the repetitive use of specification of the same style statement in each row). This template should <u>not</u> be used to replace [standard table markup](https://second-renaissance.fandom.com/wiki/Help:Table) in articles.  This template is meant to be complimentary to {{tl|infobox}} or {{tl|sidebar}}, and <u>not</u> a replacement for {{tl|infobox}} or {{tl|sidebar}}.

A simpler method to include a table in a template that does not directly support table markup is to create the table in a sub-template using standard markup and transclude it.

# Full syntax
For parameter explanations, see table below.

<pre style="overflow:auto;">
{{Aligned table
| cols =
| fullwidth =
| class =
| style =
| colwidth =
| leftright =
| colstyle =
| rowstyle =

<!--for Cth column:-->
| colCwidth =
| colCclass =
| colCalign =
| colCstyle =
| colCnowrap =

<!--for Rth row:-->
| rowRclass =
| rowRstyle =
| rowRheader =

<!--for cell R,C:-->
| classR.C =
| styleR.C =

| (cell 1,1) | (cell 1,2) | ... | ...
| (cell 2,1) | (cell 2,2) | ... | ...
}}
</pre>

# Parameters
{{Aligned table
 |cols=4 |class=wikitable |style=line-height:1.35em;
 |colstyle=padding-right:1.0em;
 |col2width=40.0em
 |col4style=padding-left:1.0em;text-align:center;

 |row1header=on
 | Parameter
 | Description
 | Examples
 | Default

 <!-------Overall-------->
 | cols
 | Number of columns in the table.
 | <code><nowiki> |cols=4 </nowiki></code>
 | 2

 | fullwidth
 | {{nowrap|Set to anything ("on", "true", "yes", etc) to ensure table spans entire width available.}}<br />(Effect is to remove border-spacing and add width:100% to the table's styling.)
 | <code><nowiki> |fullwidth=on </nowiki></code>
 | ''not set''

 | class
 | CSS/[HTML class](1043-html-attribute.md)/es applied to the table.
 | <code><nowiki> |class=wikitable &nbsp; |class=infobox</nowiki><br /><nowiki>|class=sortable nowrap &nbsp; |class=sidebar</nowiki></code>
 | ''none''

 | style
 | [CSS styling](https://second-renaissance.fandom.com/wiki/CSS_styling) applied to the table.
 | <code>{{nowrap|<nowiki> |style=width:80%;background:transparent; </nowiki>}}</code>
 | ''none''

 | colwidth
 | Width of each column (or include "width:...;" in <kbd>colstyle</kbd>).
 | <code><nowiki> |colwidth=6.0em &nbsp; |colwidth=25%</nowiki></code>
 | ''not set''

 | colstyle
 | CSS styling applied to each column.
 | <code><nowiki> |colstyle=background:transparent; </nowiki></code>
 | "

 | rowstyle
 | CSS styling applied to each row.
 | <code><nowiki> |rowstyle=text-align:center; </nowiki></code>
 | "

 <!-------Columns-------->
 | leftright
 | Set to anything ("on", "true", "yes", etc) in place of <kbd><nowiki>|col1align=left</nowiki></kbd> and <kbd><nowiki>|col2align=right</nowiki></kbd>
 | <code><nowiki> |leftright=on </nowiki></code>
 | ''not set''

 | col{{var|C}}width
 | Width of column number {{var|C}} (or include "width:...;" in <kbd>col{{var|C}}style</kbd>).
 | <code><nowiki> |col2width=9.0em &nbsp; |col3width=35%</nowiki></code>
 | ''none set''

 | col{{var|C}}class
 | Class/es applied to column number {{var|C}}.
 | <code><nowiki> |col1class=navbox-group </nowiki></code>
 | "

 | col{{var|C}}align
 | Alignment (left{{\}}right{{\}}center) for column {{var|C}}'s cell contents (or include "text-align:...;" in <kbd>col{{var|C}}style</kbd>).
 | <code><nowiki> |col4align=right </nowiki></code>
 | ''none set''

 | col{{var|C}}nowrap
 | Set to anything ("on", "true", "yes", etc) to add "white-space:nowrap;" to column {{var|C}}'s cell styling (i.e. to prevent lines within its cells from wrapping; or include "nowrap" in <kbd>col{{var|C}}class</kbd> or "white-space:nowrap;" in <kbd>col{{var|C}}style</kbd>).
 | <code><nowiki> |col5nowrap=on </nowiki></code>
 | "

 | col{{var|C}}style
 | CSS styling applied to column number {{var|C}}.
 | <code><nowiki> |col4style=font-style:italic; </nowiki></code>
 | "


 | col{{var|C}}header
 | Set to any value (e.g. <code>Y</code>) to change col's cells from data cells to table headers (headings).
 | <code><nowiki> |col1header=on </nowiki></code>
 | ''not set''

 <!--------Rows---------->
 | row{{var|R}}class
 | Class/es applied to row number {{var|R}}.
 | <code><nowiki> |row10class=navbox-abovebelow </nowiki></code>
 | ''none set''

 | row{{var|R}}style
 | CSS styling applied to row number {{var|R}}.
 | <code><nowiki> |row2style=font-weight:bold; </nowiki></code>
 | "

 | row{{var|R}}header
 | Set to any value (e.g. <code>Y</code>) to change row's cells from data cells to table headers (headings).
 | <code><nowiki> |row1header=on </nowiki></code>
 | ''not set''

 <!--------Cells--------->
 | class{{var|R}}.{{var|C}}
 | Class/es applied to cell in row {{var|R}}, column {{var|C}}. Overrides any other class attributions (<kbd>row{{var|R}}class</kbd>, <kbd>col{{var|C}}class</kbd>).
 | <code><nowiki> |class1.2=adr </nowiki></code>
 | ''none set''

 | style{{var|R}}.{{var|C}}
 | CSS styling applied to cell in row {{var|R}}, column {{var|C}}. Overrides any more general styling (<kbd>leftright</kbd>, <kbd>col{{var|C}}align</kbd>, <kbd>row{{var|R}}style</kbd>, etc).
 | <code><nowiki> |style5.3=text-align:right; </nowiki></code>
 | "

 | {{sans-serif|''Unnamed parameters''}}
 | Each unnamed parameter is taken to be the next cell in the table, starting at the table's top left corner and working left to right from top to bottom.
 | <code>{{!}} Azerbaijan {{!}} Malta {{!}} Zaire</code>
 | empty
}}

# Examples
<pre>
{{Aligned table
|cols=3 |class=wikitable
| A | 1 | a
| B | 2 | b
}}
</pre>
{{Aligned table
|cols=3 |class=wikitable
| A | 1 | a
| B | 2 | b
}}

<pre>
{{Aligned table
|cols=4 |class=wikitable
|col1align=center |col2align=center
|col3align=right  |col4align=right
| AAA | aa    | 123  | 12345
| B   | bbbbb | 1234 | 2
}}
</pre>
{{Aligned table
|cols=4 |class=wikitable
|col1align=center |col2align=center
|col3align=right  |col4align=right
| AAA | aa    | 123  | 12345
| B   | bbbbb | 1234 | 2
}}

<pre>
{{Aligned table
|class=wikitable |style=width:20em;
|col1align=center |col2align=right
| AAA | 123
| B   | 2
}}
</pre>
{{Aligned table
|class=wikitable |style=width:20em;
|col1align=center |col2align=right
| AAA | 123
| B   | 2
}}

<pre>
{{Aligned table
|cols=3 |class=wikitable sortable
|row1header=y
| U | # | l
| A | 1 | a
| B | 2 | b
}}
</pre>
{{Aligned table
|cols=3 |class=wikitable sortable
|row1header=y
| U | # | l
| A | 1 | a
| B | 2 | b
}}

<includeonly>{{#ifeq:{{SUBPAGENAME}}|sandbox |
| <!-- Categories below this line, please; interwikis to Wikidata. -->
[Category:Table and column templates](https://second-renaissance.fandom.com/wiki/Category:Table_and_column_templates)
}}</includeonly>
```

## Provenance

Raw source: `bronze/pages/171/228.wikitext` · revision `228` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3AAligned_table/doc)
