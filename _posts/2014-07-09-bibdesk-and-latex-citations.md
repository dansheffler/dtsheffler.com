---
title: BibDesk and LaTeX Citations
tags: [BibDesk, LaTeX]
summary: Using BibDesk to keep all your bibliographic info for automatically generated footnotes in LaTeX.
---

[Yesterday], I promised to address [LaTeX] citations using
[BibDesk] and [Pandoc].  LaTeX can be a little scary to set up
initially, but once you do it makes life a lot easier and PDFs a
lot prettier.  I do not usually interact with LaTeX directly,
instead preferring to write everything in Pandoc-flavor markdown
and using Pandoc to create PDFs via LaTeX.  In a normal month of
writing, I never actually look at my LaTeX set-up.  Instead, it
operates in the background every time I create a PDF version of a
paper.  I will be sharing all the pieces to make this work in a
future series of posts, but for now I just want to present one
feature of the Pandoc-plus-LaTeX workflow that makes citations from
BibDesk awesome.

In BibDesk, the first field in every catalog entry is called a
citekey (see screen-shot from yesterday's post).  Every catalog
entry has a unique citekey, so referencing a citekey is a sure-fire
pointer to the specific bibliographic information you want.  You
can reference a citekey in a Pandoc file like this: `[@mccabe94]`.
Pandoc will recognize that this is a citation, and when you use
Pandoc to convert your markdown file into a LaTeX file, it will end
up looking like this: `\autocite{mccabe94}`.  To accomplish this,
you will need to include the `--biblatex` flag when you call
Pandoc, so on the command line you would run something like this:
`pandoc --biblatex -o MyOutput.tex MyFile.md`.  The nice thing
about `\autocite` is that you can put text before or after the
citation and `\autocite` will figure out what to do with that text
based on your preferred citation style, whether it be footnotes or
parentheses.  For example, `[See @mccabe94 ch. 2 for an interesting
discussion of concrete particulars.]` turns into `\autocite[See][
ch.~2 for an interesting discussion of concrete
particulars.]{mccabe94}` and rendered in a PDF, the footnote looks
like this:

![Formated Footnote using BibDesk and \autocite](/images/Screen2014-07-091.png)

This method is very powerful because I can fill many papers with
hundreds of references to McCabe's book and these all point to a
single bibliographic entry in BibDesk.  Suppose that I realize in
two years that some detail of my bibliographic record is wrong.  It
would be a pain to go back through every one of my hundreds of
references to McCabe's book in who knows how many papers to change
this detail.  With citekeys, I change the reference in BibDesk once
and all the automatically formatted footnotes everywhere are
changed.

So far, Pandoc does all this without interacting with BibDesk.
After generating the LaTeX file, it is relying on you to set up
LaTeX to do this.  But you can also tell Pandoc where you keep your
bibliography file and Pandoc can generate pretty citations in other
formats without ever calling on LaTeX---including HTML and Word
documents.  To do this you need to add the `--bibliography` flag
when you call Pandoc, followed by the path to your bibliography
file.  When I call Pandoc the flag looks like this:
`--bibliography=~/Library/texmf/bibtex/bib/mybib.bib`.  In the last
post, I mentioned that this is one of the nice things about
BibDesk.  It stores all its data natively as a `.bib` file in the
BibTex format which Pandoc can read.  This means that you just save
in BibDesk and your bibliographic information is right there ready
for Pandoc to use.

Let's demonstrate how this works for HTML output.  I am going to
put a citation that looks like `[@mccabe94]` at the end of this
sentence.[@mccabe94]  Notice that we have a nicely formatted
footnote without needing to go and specify all that information.
You can click on the source link at the bottom of this post to see
what this looks like in markdown.  Now let's follow that reference
with another citation to the same work.  I am going to put a
citation that looks like `[@mccabe94 56]` at the end of this
sentence (notice I added a page number).[@mccabe94 56]  Now the
automatic formating is smart and makes this next footnote use
"Ibid."  To accomplish this fanciness, I need to override Pandoc's
default style of parenthetical author-year citations.  To do this,
you need to add the `--csl` flag when you call Pandoc followed by a
path to your preferred citation style.  Mine looks like this:
`--csl ~/.pandoc/my-chicago.csl`.  If you want to duplicate the way
my footnotes look you can steal [my CSL file].  Alternatively, you
can look for one to suit your own tastes and learn more about CSL
specification at [citationstyles.org].

Again using citekeys can be quite powerful.  Suppose that I submit
a book to a publisher that prefers an author-date citation format.
It would be a lot of work to go through a 300 page document and
change all my footnotes to parenthetical citations.  By using
citekeys, all I need to do is call a different CSL format when I
build the Word file to give to the publisher.

[citationstyles.org]: http://citationstyles.org/styles/
[my CSL file]: /files/my-chicago.csl
[Yesterday]: http://www.dtsheffler.com/blog/2014-07-08-intro-to-bibdesk.md
[LaTeX]:    http://www.latex-project.org
[Pandoc]:   http://johnmacfarlane.net/pandoc/
[BibDesk]:  http://bibdesk.sourceforge.net

