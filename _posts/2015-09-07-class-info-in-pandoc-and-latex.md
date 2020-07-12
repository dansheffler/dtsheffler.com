---
title: Class Info in Pandoc and LaTeX
tags: [LaTeX, Markdown]
summary: How to get typical student info into your LaTeX output using Pandoc's metadata.
---


So I have a colleague who is using the LaTeX template that I
developed to go from Markdown to PDF using Pandoc and he wants to
put his name and class information at the top of an essay.  Pandoc
expects metadata like this to be at the top of your markdown file
in a YAML block like this:

    ---
    author:     Dan Sheffler
    title:      Example Title
    class:      PHI 735
    semester:   Fall 2015
    ---

So how do we get this to render in the PDF via LaTeX?  I used
Pandoc's conditional template tags to check and see if each piece
of the metadata is there (that way you could leave something blank
and it won't choke).  If a piece of the metadata is there, then it
goes into the document on a new line with no paragraph indent.

    \noindent $if(author)$$author$$endif$\\
    $if(title)$$title$$endif$\\
    $if(class)$$class$$endif$\\
    $if(semester)$$semester$$endif$\\

Make sure you copy and paste this LaTeX bit into your
`default.latex` template somewhere **below** the `\begindocument`
command and above the `\doublespace` command (if you are using the
spacing package).  If you wanted to extend this it would be simple
to add another variable to both the YAML and the template with
something like `$if(teacher)$$teacher$$endif$\\`.

When all is done, this should produce something at the top of the
PDF that looks like this:

![Sample PDF](http://dansheffler.com/images/Screenshot 2015-09-07 12.27.51.png)

Hope this helps!

