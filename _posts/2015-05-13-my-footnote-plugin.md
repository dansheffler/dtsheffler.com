---
title: My Footnote Plugin
tags: [Sublime, Writing, LaTeX, markdown]
summary: A plugin I wrote for Sublime that makes unique footnote references across multiple files.
---

While writing my dissertation I was getting tired of coming up with
reference names for my markdown footnotes.  Further, since the
project is getting big and spans multiple files I wanted to have a
good way to ensure that I never used the same reference twice.  So
I created a quick and dirty plugin this morning that stores the
last footnote number in a global settings file.  In order to keep
all the footnote references to just two characters, it keeps this
number in a custom base-62 format that uses digits, uppercase
letters, and lowercase letters.[^2X]  When I press `ctrl+alt+f` it
will: (i) iterate this number and update the settings file, (ii)
insert a new footnote reference at the current cursor position
(looks like `[^aY]`), and creates the footnote just after the
current paragraph with the cursor in position to start typing the
footnote.


Here it is in a Gist:

{% gist dansheffler/46fd6d6c71d5d9d4fe6a %}

[^2X]: Thanks to Wolph's answer [here](http://stackoverflow.com/a/2549514).  (I just made this footnote using my new plugin!)