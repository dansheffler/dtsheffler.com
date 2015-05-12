---
title: My Zettelkasten in Sublime
date: 2015-05-11
---


In the [last post][] I talked about the general idea of the Zettelkasten method for taking notes.  In this post I will outline how I implement that method in [Sublime Text][].  First, I should say that I write *everything* in [markdown][], so I won't be going into all the general markdown tools for Sublime Text.  I'll do this in a later post.

All of my notes are in a single folder with one zettel per file.  I have saved a Sublime Text project with only this folder in it as `Notes`.  This means that I can press `ctrl+alt+p` and type `N, O, Enter` and be in my notes project from anywhere.  This will bring up any open tabs and the window arrangement from the last time I was in my notes project.  From here, I can press `ctrl+p` and begin typing the title of any note and I will get a fuzzy-filtered list of notes.  This means that I can go from working on my dissertation to a very specific note in less than ten key strokes.

Each file name describes the topic in the note.  For example: `Plato.md`, `Akrasia.md`, `Principle of Alternate Possibilities.md`.  When I want to split up a note that is getting too big, I create new notes that branch off the parent note by adding a hyphen to the original name.  For instance `Plato - Psyche.md` is a child of `Plato.md`.  This could, in principle, go as many layers deep as I like, but I prefer to keep the hierarchy as flat as possible.  It is often better to add a new top-level note with a more specific title like `Frankfurt-Style Counterexamples.md`.  Here is a sample of what the contents of a note look like:

{% gist dansheffler/94e4838fc0176ff11c19 %}

You will notice that I have surrounded some text in double brackets like this: `[[Free Will Thesis]]`.  These are standard wiki-style links to other notes in the folder.  This is not standard markdown, so I wrote a quick and dirty plugin to make these links work in Sublime Text.  You can get the plugin on GitHub [Here][].  It does two things: (i) whenever I type `[[`, it brings up a filterable list of all my notes and auto-completes the links so that I never misspell them (pressing escape drops you back to the original `[[`); and (ii) when the cursor is inside of a link, pressing `ctrl+enter` will follow the link to the desired note *or* create a new file with the appropriate name if the note does not exist yet.  To get this last part to work I needed to install the [Bracketeer][] plugin.




[last post]: blog/2015-05-05-the-zettelkasten-method/
[Sublime Text]: http://www.sublimetext.com/
[markdown]: http://brettterpstra.com/2011/08/31/why-markdown-a-two-minute-explanation/
[Here]: https://github.com/dansheffler/MyWiki 
[Bracketeer]: https://github.com/colinta/SublimeBracketeer
