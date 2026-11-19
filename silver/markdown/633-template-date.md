---
page_id: 633
revision_id: 876
source_url: https://second-renaissance.fandom.com/wiki/Template%3ADate
raw_sha256: e65c078779bd93c5ed69d8a08a38014895d6f4c4a5dfbe42061241584fb55292
---

# Template:Date

## Preserved source

```wikitext
{{{{{|safesubst:}}}#switch:none
 |{{{{{|safesubst:}}}#iferror: {{{{{|safesubst:}}}#time:Y_M_d|{{{1|}}} }} | none }} <noinclude><!-- #time: can't handle --></noinclude>
 |{{{{{|safesubst:}}}#iferror: {{{{{|safesubst:}}}#expr: {{{1|}}}+0 }}
    |<noinclude><!--not a pure number--></noinclude>
    |{{{{{|safesubst:}}}#ifexpr: {{{1|}}}+0 > 10000000000000
       |<noinclude><!-- a yyyymmddhhmmss timestamp --></noinclude>
       |{{{{{|safesubst:}}}#ifeq: {{{{{|safesubst:}}}#expr:{{{1|}}}+0}} | {{{1|}}}
          | none <noinclude><!-- pure number eg 123.456 --></noinclude>
          | <noinclude><!-- assume yy-mm-dd --></noinclude>
        }}
     }}
  }}
 |{{{{{|safesubst:}}}#switch:  {{lc:{{{2|}}}}} | none | asis | link | lnone =none }}
 |{{{{{|safesubst:}}}#ifexpr:  {{{{{|safesubst:}}}#time:Y|{{{1|}}} }} < 1000 | none }}
 |{{{{{|safesubst:}}}#switch:  {{{{{|safesubst:}}}#time:Ynj|{{{1|}}} }}|100031|110031|130031|140031|150031=none}}
 |= {{{{{|safesubst:}}}#if:{{{1|}}}
      |{{{{{|safesubst:}}}#switch:{{{2}}}
         |link|lnone|l=[{{{1}}}](https://second-renaissance.fandom.com/wiki/{{{1}}})
         |{{{1}}}
       }}
    }}<noinclude><!-- error or "none", so no formatting --></noinclude>
 |<noinclude><!-- continue with formatting --></noinclude>
  {{{{{|safesubst:}}}#ifeq:<noinclude><!--
    --></noinclude>{{{{{|safesubst:}}}#time:Y|{{{1}}} 2008}}<noinclude><!--
    --></noinclude>{{{{{|safesubst:}}}#iferror: {{{{{|safesubst:}}}#ifexpr: {{{1}}}>10000000000000 | no }} | }}<noinclude><!--
    --></noinclude>{{{{{|safesubst:}}}#time:Y|{{{1}}} 2004}}
  |20082004
  |<noinclude><!-- no year --></noinclude>
    {{{{{|safesubst:}}}#ifeq:{{{{{|safesubst:}}}#time:d|{{{1}}} 2036}}|{{{{{|safesubst:}}}#time:d|{{{1}}} }}
    |<noinclude><!-- month+day --></noinclude>{{{{{|safesubst:}}}#time:
      {{{{{|safesubst:}}}#switch: {{lc: {{{{{|safesubst:}}}#ifeq:{{{3|}}}|y|L}}{{{2|}}} }}
      | lmdy | liso | lymd      = [:F j](https://second-renaissance.fandom.com/wiki/:F_j)
      | mdy  | iso  | ymd       = F j
      | ldmy | l                = [:j F](https://second-renaissance.fandom.com/wiki/:j_F)
      | #default                = j F
      }}|{{{1}}} 2000 }}<noinclude><!-- default='dmy' or null or "" or unsupported option --></noinclude>
    |<noinclude><!-- month only --></noinclude>{{{{{|safesubst:}}}#time:
      {{{{{|safesubst:}}}#switch: {{lc: {{{{{|safesubst:}}}#ifeq:{{{3|}}}|y|L}}{{{2|}}} }}
      | lmdy | liso | lymd 
      | ldmy | l                = [F](https://second-renaissance.fandom.com/wiki/F)
      | #default                = F
      }}|{{{1}}} 2000 }}<noinclude><!-- default='dmy'/'mdy'/'ymd'/'iso'/null/""/unsupported opt --></noinclude>
    }}
  |<noinclude><!-- with year--></noinclude>
    {{{{{|safesubst:}}}#if: {{{{{|safesubst:}}}#iferror:{{{{{|safesubst:}}}#time:j|2 {{{1|}}}}}|*D*|{{{{{|safesubst:}}}#iferror:{{{{{|safesubst:}}}#time:j|2000 {{{1|}}}}}|*D*| }}}}
    |<noinclude><!-- day+month+year --></noinclude>{{{{{|safesubst:}}}#time:
      {{{{{|safesubst:}}}#switch: {{lc: {{{{{|safesubst:}}}#ifeq:{{{3|}}}|y|L}}{{{2|}}} }}
      | lmdy                    = [:F j](https://second-renaissance.fandom.com/wiki/:F_j), [Y](https://second-renaissance.fandom.com/wiki/Y)
      | mdy                     = F j, Y
      | liso                    = [Y-](https://second-renaissance.fandom.com/wiki/Y)[m-d](https://second-renaissance.fandom.com/wiki/F_j)<noinclude><!-- i.e. [Y-m-d](https://second-renaissance.fandom.com/wiki/Y-m-d) --></noinclude>
      | iso                     = Y-m-d
      | lymd                    = [Y](https://second-renaissance.fandom.com/wiki/Y) [:F j](https://second-renaissance.fandom.com/wiki/:F_j)
      | ymd                     = Y F j
      | ldmy | l                = [:j F](https://second-renaissance.fandom.com/wiki/:j_F) [Y](https://second-renaissance.fandom.com/wiki/Y)
      | #default                = j F Y
      }}|{{{1|}}} }}<noinclude><!-- #default='dmy' or null or "" or unsupported option --></noinclude>
    |<noinclude><!-- month+year --></noinclude>{{{{{|safesubst:}}}#time:
      {{{{{|safesubst:}}}#switch: {{lc: {{{{{|safesubst:}}}#ifeq:{{{3|}}}|y|L}}{{{2|}}} }}
      | lmdy | liso | lymd | ldmy | l  = [:F Y](https://second-renaissance.fandom.com/wiki/:F_Y)
      | #default                = F Y
      }}|{{{1|}}} }}<noinclude><!-- default='dmy'/'iso'/'mdy'/null/""/unsupported option --></noinclude>
    }}
  }}    
}}<noinclude>
{{documentation}}
</noinclude>
```

## Provenance

Raw source: `bronze/pages/633/876.wikitext` · revision `876` · [upstream](https://second-renaissance.fandom.com/wiki/Template%3ADate)
