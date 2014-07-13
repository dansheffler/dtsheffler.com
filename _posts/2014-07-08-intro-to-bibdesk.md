---
title: Intro to BibDesk
---

In several of the scripts I use to interact with [Skim], I have mentioned that they receive bibliographic information from [BibDesk].  BibDesk is an excellent bibliography management tool similar to [Mendeley] or [Zotero].  I like BibDesk for three main reasons: (i) like Skim, it is a free and open source project created by academics for other academics, (ii) it stores all its data in a flat BibTex file, and (iii) it can interact easily with Skim via AppleScript.  In another post I will talk more about the implications of (ii), but for now just know that this means BibDesk talks easily with [Pandoc] and [LaTeX] without the need to export anything.  Both Mendeley and Zotero can achieve the same result, but one needs to export every time a change is made to the bibliography.

Several of my colleagues have asked me to recommend a good bibliography manager, but they have not wanted to dive headlong into LaTeX citations (the learning curve is admittedly quite steep).  In this post, I would like to simply introduce BibDesk as a stand-alone bibliography manager.  When working with BibDesk, every bibliographic reference gets an entry---think of this like the old catalog cards at the library.  When filling out the entry it looks like this:

![BibDesk Catalog Entry](/images/Screen2014-07-081.png)

Just at this stage, BibDesk has already become useful: rather than pick a book off the shelf to look for the bibliographic information or search ten clicks deep in the university library's arcane catalog, you enter your info once and it is here for you to reference in the future.  If you have a PDF associated with the entry, then you can set up BibDesk to automatically file the PDF based on this bibliographic data---no more cluttered downloads folder with a mysterious `3978503409348.pdf`!

Without getting into compiled citations, BibDesk can still be quite useful.  It uses templates to generate pre-formated output for a given catalog entry.  If you make sure that `View > Bottom Preview > Default RTF template` is checked you will see something like this at the bottom of your main screen:

![BibDesk default RTF template](/images/Screen2014-07-082.png)

This is useful for copying and pasting into other applications like Word.  But how many times do you really want your bibliographic data in *that* format?  I prefer to use Chicago-style footnotes and it is a pain to format each note individually much less remember where to put that pesky comma.  So I created an RTF template that automatically arranges the relevant data in the Chicago way, being sensitive to whether we are dealing with a book, a journal article, or an article from a book.  With this template selected the output looks like this:

![My Chicago Footnote Template in BibDesk](/images/Screen2014-07-083.png)

Now when I am working in Word (God forbid!) and I want a footnote, I can just select this pre-formatted version and paste it into my footnote.  If you want this same template just download this [file] to your `~/Library/Application\ Support/BibDesk/Templates` folder and add it in the BibDesk `Templates` preference pane.  You can even do multiple catalog entries at once by selecting more than one.  If you want to create your own templates I suggest taking a look at the [BibDesk Wiki page].

But wait, it gets better!  You can skip the step of selecting the text at the bottom and instead simply drag and drop the catalog entry into Word, or select a citation and press `⌘C`.  To do so simply select your new Chicago footnote template in the BibDesk `Citations` preference pane:

![BibDesk Preference Pane Citations](/images/Screen2014-07-084.png)

In a later post we will come to find out that this is *still* way more work than you need to do, but leveraging the full power of BibDesk will require working with LaTeX, and this (understandably) scares many people away.


[BibDesk Wiki page]: https://sourceforge.net/p/bibdesk/wiki/Templates/
[file]:     /files/ChicagoFootnote.rtf
[LaTeX]:    http://www.latex-project.org
[Pandoc]:   http://johnmacfarlane.net/pandoc/
[Zotero]:   https://www.zotero.org
[Mendeley]: http://www.mendeley.com
[Skim]:     http://skim-app.sourceforge.net/
[BibDesk]:  http://bibdesk.sourceforge.net


