---
title: Marginal Note Properties in Skim
tags: [Skim, Notetaking]
summary: A script I wrote for adjusting the width of marginal text notes in Skim.
---

When I am reading a book with the greatest amount of engagement, I
like to write short notes in the margins of the PDF.
Unfortunately, when I create a new text note in [Skim] the note
uses a default height, width, and font-size, and produces something
looking like this:

[Skim]: http://skim-app.sourceforge.net

![New text note in Skim with default settings](/images/Screen2014-07-041.png)

I can adjust this, of course, but that involves manually shrinking
the width of the note to the book's margin width and setting the
font size for every single note.  Fortunately, Skim has a
preference setting for the default text note font size and a
*hidden* preference setting for the default dimensions of new
notes.  Unfortunately, books come in various sizes, so the values I
set for these need to be adjusted every time I start reading a new
book, and opening terminal just to adjust Skim's hidden preferences
at every reading session is too much.

So I wrote a script that does all this for me.  When I am facing a
new book that I want to read closely, I create a new text note,
adjust it to fit the margins of the book and select an appropriate
font size.  Then, with the note selected, I run the following
script.  This grabs the values I want from this note, sets them as
Skim's defaults, and restarts Skim to the PDF and page where I left
off.

{% gist 4f8e7ee2c91c5f6ddbe6 %}

Now every new note that I create will be uniform and fit nicely in
the margin.  Remember that putting this in `~/Library/Application\
Support/Skim/Scripts` will make it available from within Skim's
script menu.

