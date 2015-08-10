---
title: Search BibDesk
---

Often I want to just do a quick check of whether I have a book in
[BibDesk] already, or I want to find a PDF quickly.  BibDesk has a
nice search field, but you need to select the `Library` first to
get a global search.  Otherwise, you will only search within
selected groups.  Most of the time, I also want to perform these
searches from another application when BibDesk isn't even running.
So I wrote a quick little script that (i) opens BibDesk, (ii)
clears all search limitations, and (iii) puts the cursor in the
search field:


{% gist dansheffler/d7d862546cff0c95918e %}

Notice that you will need to change `mybib.bib` after `theTitle` to
the name of your `.bib` file.

Then I set up a [Quicksilver] trigger to run the script when I
press `^⌘<space>`.  Think of it like a Spotlight search just for
your bibliography---quite helpful when you have several hundred
bibliographic references.

![Quicksilver Trigger for Searching BibDesk](/images/Screen2014-07-121.png)

This concludes my Skim/BibDesk series of posts, so look tomorrow
for a summary post that pulls all the pieces together.


[Quicksilver]: http://qsapp.com
[BibDesk]: http://bibdesk.sourceforge.net
