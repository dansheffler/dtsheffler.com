---
title: Exporting Skim Notes
tags: [Skim, Markdown]
summary: A little script I wrote for getting all your Skim notes into a single nicely formated markdown file.
---


After I have entered marginal and anchored notes in [Skim], I need
some way to export those notes and format them nicely for reading.
Skim has some built-in tools for exporting notes, but I wanted (i)
to format these notes nicely with markdown, (ii) to incorporate
bibliographic information from [BibDesk], and (iii) to include my
custom [Skim URLs] so that a track-back link to the original page
follows each note.

The following script accomplishes all this by first identifying
which BibDesk entry owns the PDF currently open in Skim, second
iterating through all the pages of the PDF to get the note text,
and third concatenating all the notes into a nicely formated
markdown document with track-back links.

{% gist a552f6ee1558079a2067 %}

As a bonus, the script used [PDFtk] to find bookmarks in the PDF
(which are usually used for a table of contents) and uses these to
create appropriate section headers.  If you do not want to install
PDFtk, you could simply comment out this portion of the script.
Finally, the script writes the output to a temp file and opens that
file in [Marked].  The final output looks like this:

{% gist 03cbb182632b622b6610 %}

In Marked it ends up looking like this:

![Marked Screen with Sample Skim
Notes](/images/Screen2014-07-071.png)

Remember that putting this in `~/Library/Application\
Support/Skim/Scripts` will make it available from within Skim's
script menu.


[Marked]:       http://markedapp.com
[pdftk]:        http://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/
[Skim URLs]:    http://www.dtsheffler.com/blog/2014-07-02-custom-skim-urls/
[Skim]:          http://skim-app.sourceforge.net
[BibDesk]:       http://bibdesk.sourceforge.net
