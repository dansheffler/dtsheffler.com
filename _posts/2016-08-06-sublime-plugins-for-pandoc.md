---
title: Sublime Plugins for Pandoc
tags: [Note Taking, Sublime, Pandoc]
summary: My recommendations for Sublime slugins for writers who use Pandoc.
sharing:
  twitter: My recommendations for Sublime slugins for writers who use Pandoc.
  facebook: My recommendations for Sublime slugins for writers who use Pandoc.
---



In the [last post](http://dansheffler.com/blog/2016-07-11-pandoc/), I gave a brief introduction to using Pandoc.  There are a few plugins for Sublime Text that I have installed that make it much easier to use Pandoc.  On any Sublime Text installation, the first plugin to add should be [Package Control](https://packagecontrol.io/).  This allows you to easily install more plugins from within Sublime Text with an easy-to-use interface.  While there are many plugins out there geared toward Markdown in general and Pandoc in particular, these are the ones that I use:

[Markdown Editing](https://packagecontrol.io/packages/MarkdownEditing)
:   This markdown plugin trumps all the others and provides a base
    color scheme that I really like.

[Academic Markdown](https://packagecontrol.io/packages/AcademicMarkdown)
:   This requires Markdown Editing and extends its features to
    include some of the things academics would be interested in,
    like highlighting for Pandoc's version of citations and
    [CriticMarkup](http://criticmarkup.com/).

[Citer](https://packagecontrol.io/packages/Citer)
:   Just tell this plugin where your BibTeX file is and it will
    handle all your citation needs.  I especially use the fuzzy
    filterable list of all my bibliography entries to add citations
    extremely quickly even when I only half remember a title or the
    name of an author.

[WordCount](https://packagecontrol.io/packages/WordCount)
:   This does what it says with lots of reconfigurability and minimal
    overhead.

[Wrap Plus](https://packagecontrol.io/packages/Wrap%20Plus)
:   This hard wraps selections and best of all it intelligently
    handles markdown-style block quotes and lists.  (As an added
    bonus it handles a variety of block comment styles in different
    programming languages.)

Also take a look at the little tweaks that I have added myself [for Academic Markdown](http://dansheffler.com/blog/2015-08-03-sublime-syntax-definition/) and [creating footnotes with a consistent numbering scheme across multiple files](http://dansheffler.com/blog/2015-05-13-my-footnote-plugin/).