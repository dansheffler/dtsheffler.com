---
title: Custom Skim URLs
---

I wanted to be able to link to any page of a PDF in my Markdown
notes, and I knew that I could do it by appending `#35`, for
example, to the end of a `file://` URL in my browser.  But I use
[Skim][], and reading PDFs in a browser is no good.  Further, the
URLs end up being super long with ugly things like `%20` for spaces
and this seemed unnecessary because all my PDFs are carefully
organized with [BibDesk][].  So I set up a little AppleScript that
would parse a custom URL starting with `sk://` for a BibDesk
citekey and a page index, then figure out which PDF I want from
BibDesk and open that PDF in Skim to the right page index.

  [Skim]: http://skim-app.sourceforge.net
  [BibDesk]: http://bibdesk.sourceforge.net

{% gist dansheffler/ff35af3059a66b004f35 %}

To get this to work I need to save this using Apple's Script Editor
as an independent App called `Skimmer`. Then in the `info.plist`
for this App, I put this:

{% gist dansheffler/a82305c57695f91eafc0 %}

This makes OS X recognize that URLs starting with `sk://` are
Skimmer URLs.

So when I put a citation reference like `[@mccabe94 [page
41](sk://mccabe94#57)]` in my markdown source, I end up with a
footnote that looks like this:[@mccabe94 [page
41](sk://mccabe94#57)].  Clicking on the link in this citation
takes me to page 41 of *Plato's Individuals*.  The script first
pulls out the citekey `mccabe94` and finds the entry with this key
in Bibdesk.  Then it opens the first linked PDF of this entry in
Skim and tells Skim to go to the page index after the `#`.  This
has the advantage that I can decide to reorganize how I store PDFs
in the future and all my links will be unchanged.

Notice that there is a difference between a PDF page's "label" and
its "index" the index is an integer with the first page of the PDF
counting as 1. The page's label is a string and is often used to
label the cover of a book or pages that use roman numerals.  Hence
in McCabe's book, the page with the label "xii" has the index 14,
while the page with the label "4" has the index 20.  URLs to
specific pages always use the index because these are unambiguous,
but when people refer to the "page number" in a book, they usually
mean the page *label*.

I originally got the idea for this from  [drosophiliac](http://webc
ache.googleusercontent.com/search?q=cache:GajblYFF3VQJ:drosophiliac
.com/2012/09/creating-a-custom-url-scheme-via-applescript-and-
python.html), which now appears to only be available through Google
cache.

