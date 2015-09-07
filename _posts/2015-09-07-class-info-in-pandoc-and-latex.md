---
Title: Class Info in Pandoc and LaTeX
---


So I have a colleague who is using the LaTeX template that I developed to go from Markdown to PDF using Pandoc and he wants to put his name and class information at the top of an essay.  Pandoc expects metadata like this to be at the top of your markdown file in a YAML block like this:

    ---
    Author:     Dan Sheffler
    Title:      Example Title
    Class:      PHI 735
    Semester:   Fall 2015
    ---

So how do we get this to render in the PDF via LaTeX?  I used Pandoc's conditional template tags to check and see if each piece of the metadata is there (that way you could leave something blank and it won't choke).  If a piece of the metadata is there, then it goes into the document on a new line with no paragraph indent.

    \noindent $if(author)$$author$$endif$\\
    $if(title)$$title$$endif$\\
    $if(class)$$class$$endif$\\
    $if(semester)$$semester$$endif$\\

Make sure you copy and paste this LaTeX bit into your `default.latex` template somewhere **below** the `\begindocument` command and above the `\doublespace` command (if you are using the spacing package).  If you wanted to extend this it would be simple to add another variable to both the YAML and the template with something like `$if(teacher)$$teacher$$endif$\\`.


