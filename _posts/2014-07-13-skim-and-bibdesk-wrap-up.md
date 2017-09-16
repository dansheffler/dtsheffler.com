---
title: Skim and BibDesk Wrap-up
tags: [Skim, BibDesk]
summary: All my posts on Skim and BibDesk organized in one place.
---

Over the last few weeks, I have posted several snippets of code and
explanations regarding the way I work with [Skim] and [BibDesk].
Initially, I started writing these posts just so that I could have
some documentation for myself lest I forget how all these pieces
work in two years, but I have also had some colleagues in the
philosophy department ask about my system, so I have tried to make
the explanations comprehensible to them as well.  The following is
a list of those posts with a brief description of what they
include.


#### Skim ####

[Intro](http://www.dansheffler.com/blog/2014-07-05-why-i-use-skim)
:   A brief introduction to Skim and an explanation of its
    advantages as a PDF reader.

[Skim URLs](http://www.dansheffler.com/blog/2014-07-02-custom-skim-urls)
:   A system-wide URL scheme so that I can open to a particular
    page of a PDF from anywhere.  Looks like this:
    `sk://mccabe94#57`.

[Skim Links](http://www.dansheffler.com/blog/2014-07-03-skim-links)
:   Using the above URL scheme, a script that automatically
    generates markdown formatted citations or links to the
    current page of the PDF open in Skim.

[Marginal Notes](http://www.dansheffler.com/blog/2014-07-04-marginal-note-properties-in-skim)
:   A script to quickly set Skim's defaults so that all new
    marginal notes fit a book's margins in an appropriate font
    size.

[Export Notes](http://www.dansheffler.com/blog/2014-07-07-exporting-skim-notes)
:   A script that goes through a PDF, gathers all the textual
    notes, and outputs a nicely formatted markdown document
    opened in [Marked].  It even includes table of contents
    information from the PDF and bibliographic information from
    BibDesk.

#### BibDesk ####

[Intro](http://www.dansheffler.com/blog/2014-07-08-intro-to-bibdesk)
:   A brief intro to BibDesk and an explanation of how to
    generate preformated footnotes without using [LaTeX].

[Citations](http://www.dansheffler.com/blog/2014-07-09-bibdesk-and-latex-citations)
:   An explanation with examples of citations using [Pandoc] and
    [LaTeX].

[Search](http://www.dansheffler.com/blog/2014-07-12-search-bibdesk)
:   A simple  script for opening BibDesk and running a search
    from anywhere---like Spotlight for your bibliography.

[Skim]:         http://skim-app.sourceforge.net
[BibDesk]:      http://bibdesk.sourceforge.net
[LaTeX]:        http://www.latex-project.org
[Pandoc]:       http://johnmacfarlane.net/pandoc/
[Marked]:       http://markedapp.com

