---
title: Chicago CSL
tags: [LaTeX, markdown]
summary: How to get nicely styled Chicago footnotes in your LaTeX output with Pandoc.
---

Yesterday, I was helping another colleague get set up with markdown
for his dissertation and realized that I did not have a convenient
way of giving him the CSL file that I use to automagically format
my footnotes according to the *Chicago Manual of Style*.  So here
is a [link](https://gist.githubusercontent.com/dansheffler/1524f545c1b4e01978d0/raw/ebcf0fdaf6b011aad97a1761399e53b52b915057/chicago.csl) to this file posted to Gist.

[CSL](http://citationstyles.org/) is an open standard that defines
how bibliographic elements are put together (e.g. parentheses
versus footnotes).  You can use this with many tools, but I use it
with Pandoc.  To get it to work, you need to define two files when
you run Pandoc:

1. You need the `--bibliography` flag to point to a BibTeX file
   with your bibliographic information so that Pandoc knows which
   author wrote which book.  (This is the format that BibDesk and
   JabRef save in automatically.)
2. You need the `--csl` flag to point to the CSL file so that
   Pandoc knows how you want things to look.

An example command might look like this:

    pandoc --bibliography=~/Dropbox/mybib.bib --csl=~/Dropbox/chicago.csl -o test.html test.md

You can have multiple CSL files for different formats, say one for
author--date and one for footnotes.  Then, on a project-by-project
basis you can easily switch between them without having to change
your source document.  The source will just contain a Pandoc
citation that looks like this `[@gerson03 67]` and it will get
formatted differently based on which CSL you use.