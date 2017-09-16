---
title: Git for Zettelkasten
tags: [Zettlekasten, Notetaking, Sublime]
summary: Using Git with my zettlekasten
---

TheClearHorizon asked an interesting question in a [comment
thread](http://zettelkasten.de/posts/getting-started/) over at
[Zettelkasten.de](http://zettelkasten.de/) about a particular
advantage of Luhmann's index card system.  While responding to his
post, I realized that there was a certain structural feature that I
had reproduced using Git without reflecting that I had done this.
I would like to make two points, first a theoretical point about
the architecture of a Zettelkasten and second a practical point
about using Git to achieve this.

#### Theoretical Point ####

There are different kinds of association between ideas, and the
architecture of a note-taking system can be better or worse at
capturing these connections.  Luhmann's Zettelkasten system is
brilliant because it captures many types of association very
efficiently.  Each index card has an ID that looks something like
this `143b/3c/2`.  The first number `143` stands for a particular
topic, say *Sartre*. Letters indicate branching within that topic.
So `143b` may stand for *Sartre > No Exit*.  A slash followed by a
number stands for a continuation (which is necessary because of the
physical size of the index cards).  So `143b/3` would stand for the
third index card of *Satre > No Exit*.  (My apologies if this is
not a strictly accurate representation of Luhmann's actual system.)

The disadvantage of this system is that the numbers are rather
cryptic.  On an electronic version we have the space, so we can
just write `Sartre > No Exit` rather than `143b`.  We can still
capture the two kinds of association between ideas that matter
most: (i) explicit reference and (ii) hierarchical nesting.
Subtly, however, we have just lost an important form of
association: (iii) the sequential relationship between 142 and 143.
`142` might stand for *Drama* and we would not immediately think to
associate *Drama* and *Sartre*.  They are associated in the
numbering system because the person creating the cards first opened
a new topic for *Drama* and then opened a new topic for *Sartre*.
The two ideas are associated *for the researcher* because of the
chronological nearness of the work.


#### Practical Point ####

One of the great advantages of working in a plain-text format like
Markdown is that you can use powerful tools like Git rather than
whatever your software happens to ship with.  Many change-tracking
features in software like Word or Dropbox happen automatically.
Each time you save or make a change, the software keeps track of
what you did.  This is fine if all you want is to keep from loosing
your work, and you can make Git work this way too.  But there is a
better way: make intentional commits with brief, descriptive
messages that log what you have done at logical intervals in your
work.  For years, I have been doing this for all my writing as a
matter of course.

Now the realization: I have also been using Git to get the same
kind of association that I thought might be lost by switching from
numbers to descriptive titles.  Each time you make a commit in Git,
you have a group of files that have been changed at the same time.
They are "change neighbors" so to speak.  With a Git plugin in
Sublime Text, it takes only a few keystrokes to pull up a log of
all the times a particular file has been changed.  By selecting one
of these commits, I can---within seconds---see all the "change
neighbors" of this particular file at any stage of its development.
In other words, I can easily see all the notes (whether I would
later think to relate them or not) that I was working on at the
same time as this note.

This method of association is actually *more* powerful that the
association between `142` and `143` above.  Those numbers were
close to each other only because those top-level topics were
*created* at the same time.  Association through Git commits,
however, established nearness *each time the note is changed* not
just at creation.


