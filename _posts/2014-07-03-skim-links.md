---
title: Skim Links
tags: [Skim, Pandoc]
summary: A script I wrote that for generating a Pandoc-style citation with an automatically generated link to the right page in Skim.
---



In the last post, I shared my little script for opening URLs that
look like this: `sk://mccabe94#57`. It is a little irritating,
however, to remember the citekey for a book and look for the page
*index* as opposed to the page *label* every time I want to put a
link to a PDF page in my notes. So I created a script that will
automatically create a proper [Pandoc][]-style citation with a
Skimmer link inside of it. The result looks like this: `[@mccabe94
[page 41](sk://mccabe94#57)]`. This makes sure that the page
*label* is displayed in the actually presented footnote or citation
while the page *index* goes into the link URL.

 [Pandoc]: http://johnmacfarlane.net/pandoc/

{% gist 77d53e6a4b281bb2f534 %}

By saving this script into `~/Library/Application\
Support/Skim/Scripts` you can access it right from inside [Skim].
Skim automatically loads all the scripts it finds in this folder
into its script menu.  Because this makes the script a menu item
you can add a keyboard shortcut to it in System Preferences.  I
chose `^⎇C`.

[Skim]: http://skim-app.sourceforge.net

Sometimes, I just want the URL, though, without the rest.  For this
I have another script based on the same concept:

{% gist 3f1f74ccc883186c0b75 %}

I also put this in Skim's script folder and assigned it the
shortcut `^⌘C`.  This way I can quickly grab either a complete
citation from what I am reading or just the URL to it, tab over to
Vim, drop it in my notes with `⌘V`, and tab back in just a few
seconds.



