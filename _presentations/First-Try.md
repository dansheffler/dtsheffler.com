---
title: My First Slide Show
theme: league
---

<section>

# Pandoc Jekyll and Reveal.js #

This is my test slide show that I created using the magic of [Pandoc](http://pandoc.org/), [Jekyll](https://jekyllrb.com/) and [Reveal.js](http://lab.hakim.se/reveal-js/#/).  This is awesome because Jekyll will take my `_presentations` folder, which is filled with (mostly) markdown files and transform them into a sweet sideshows like this.

(Use space bar or arrow keys to navigate.)


</section>
<section>
<section>

## I Can Use: ##

1. All the normal markdown like ordered lists and *italics*.
2. All of Pandoc's extensions like subscripts~2~.
3. Reveal's cool features like presentation mode (press `s` to
   check it out) or vertical navigation (press space or down).
4. All the customization flags that I care about in Reveal.js by
   using Jekyll's liquid templates and the YAML front-matter on the
   file.


<aside class=notes>
Here are my speaking notes, which can receive Pandoc's markdown too like *italics* and bold.  I think I can handle this level of html.
</aside>
</section>
<section>

## Limitations ##

- While there is a way to go straight from complete markdown to
  Reveal.js using pandoc, I cannot seem to enable this for just
  files in the presentations collection.  The Jekyll plugin I use
  requires the same pandoc flags for all markdown files site-wide.
- This means that I do need to use the HTML elements `<section>`
  and `<aside>` to designate slides and speaking notes.
- Pandoc puts footnotes at the end and this turns into a nice slide
  all by itself, but the link from footnote number to citation
  doesn't play nice with Reveal.js's slide animations.[@gerson03 57]


</section>
</section>
<section data-background="http://www.reactiongifs.com/wp-content/uploads/2013/08/dr-mccoy-and-captain-kirk-approve.gif">

# I'm Impressed #



</section>
</section>
<section>

## PS ##

I can us it with mathjax too:

$\frac{x + y}{x} = \frac{x}{y}$

$\forall x \exists y (x \leftrightarrow \neg y)$

</section>