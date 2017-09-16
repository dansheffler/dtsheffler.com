---
title: Definition Lists
tags: [LaTeX, markdown]
summary: Using markdown's definition lists in LaTeX output.
---

After telling someone that they should use definition lists, I
noticed that I had ignored them in my papers because I was too lazy
back then to set up a nice format in LaTeX.  Definition lists are
great for philosophers (especially analytic philosophers) because
it provides a good semantic structure for defining a proposition or
example.  So I updated the source of my papers to reflect my own
advice.  A good example of this is in my paper "Why Molinism Does
not Help with the Rollback Argument."  You can see the raw source
of this paper [here](https://raw.githubusercontent.com/dansheffler/dansheffler.com/master/_papers/Molinism-and-Rollback.md), the PDF
output [here](http://dansheffler.com/pdfs/Molinism-and-Rollback.pdf), and the HTML output [here](http://dansheffler.com/papers/Molinism-and-Rollback.html).

To get the PDF output to style nicely, I added this to the header of the LaTeX template that I use for Pandoc:

{% gist dansheffler/d32dbbaede6150b087e1 %}

To get the HTML output for this site to style nicely, I used this CSS:

{% gist dansheffler/c5714b4a1e9d3dc7b35e %}

Hope this helps!

