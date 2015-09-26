---
title: The Why and the Wherefore
---


[Sascha Fast said](https://twitter.com/SaschaFast/status/644437872737693696)
that I should write up a blog post explaining why I find my
[association of notes through Git](http://dansheffler.com/blog/2015-09-10-git-for-zettelkasten/)
useful.  Admittedly, I only use this kind of association rarely.
When I do, however, it proves to be just what I need.

I tend to work on my notes in creative bursts during which my mind
is deeply immersed in the material.  While I am putting all the
notes and citations from (e.g.) an article where they go, I'm also
opening totally fresh topics and thinking about seemingly unrelated
things.  For example, thoughts about Socrates's comments about the
real self, the soul, and conversation in the *Alcibiades*, will
make me think about something connected to Martin Buber and Gabriel
Marcel.  When I'm done with a burst I commit in Git.

Most of the time, I navigate around my notes by either:

1. using the quick panel in Sublime because I know exactly where I
   want to go,
2. using direct links between explicitly associated notes, or
3. searching for words or citekeys because I know the general topic
   I am looking for.

But these ways of moving from one note to others will not capture
the association between Socrates and Martin Buber---there is no
citekey in the later note since the article I was reading had
nothing to do with Martin Buber; there are no obvious key words to
search between the two files; and the random inspiration during the
burst did not cause me to explicitly associate the notes with a
hard link.  Nevertheless, a year later I start to see the deep
pattern that initially led me to think of Martin Buber while
reading about Socrates.  When I had the original inspiration, my
grasp of this underlying pattern was totally inchoate.  But now,
I'm starting to see many little ideas across years of reading form
one big constellation.  As I work on this, it is *super* helpful to
pull up a list---in under ten keystrokes---of all the notes I
edited when I was working on *this particular sentence* of my note
on the *Alcibiades*.

Christian Tietze had this to say [on Twitter](https://twitter.com/ctietze/status/643868436800667648):

> Date-based IDs in the file name do the same but only upon
> creation---the tech hurdle for Git is high, though.

I wanted to point out that I think everyone should be using Git
anyway if they are doing anything in plain text.  With an
appropriate plugin, there is really very little to learn (no need
to get into the CLI or any advanced features for our purposes).  I
also want to point out that Christian is exactly right.  With date-of-creation
timestamps or date-of-modification timestamps, you only get one
point at which to place this note near others.  With Git, you get
nearness based on *each* change---both to the starting note and to
its "change neighbors."