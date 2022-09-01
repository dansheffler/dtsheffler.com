---
title: Bayesian Reasoning
tags: [Philosophy]
summary: Bayesian reasoning often shows us that the likelihood of something being true given our evidence is lower than we think.  In this post, however, I examine what happens when we have multiple lines of converging evidence, which often turns out to raise the probability higher than we might guess.
banner: puttiarch.jpg
---

*I wrote the following in response to a class I just taught on arguments for the existence of God.  A student asked about what happens to the strength of probabilistic arguments when they are combined. Bayesian reasoning often shows us that the likelihood of something being true given our evidence is lower than we think.  In this post, however, I examine what happens when we have multiple lines of converging evidence, which often turns out to raise the probability higher than we might guess.*

I thought I would write up a brief further explanation of this kind of probabilistic reasoning since it came up in class, and it seemed that most people were unfamiliar with how to think through such problems. (Human intuition is actually really bad at guessing probabilities, which is why pro poker players can clean you out.) It's also pretty hard to understand without seeing it written out.

Suppose you go in for a cancer screening and the doctor brings you the unfortunate news that the test is positive. Suppose he also tells you the following facts:

1. Only 1% of people in general have cancer.
2. If someone has cancer, the test gives a positive result 80% of the time.
3. If someone does not have cancer the test gives a false positive 10% of the time.

What are the chances that you actually have cancer? Seems pretty scary, right? Wouldn't you guess that your chances are pretty high? The answer, however, is that they aren't actually that high at all.<!--more-->

Call the probability that you have cancer P(C), and the probability that you have cancer given the positive test result P(C|T).

P(C|T) = P(C)P(T|C)/P(T)

In plain English, this means that the probability you have cancer equals the proportion of true positive test results divided by the total positive test results including all the false ones.  This last bit is the crucial thing to see.  There are actually many many more false positive test results than true positive test results even though the false positive rate is only 10% and the true positive rate is 90%.

Why is this?  It happens because its so unlikely that you have cancer in the first place. Let's do the math.

True positives = 1% * 80% = 0.008.

In a population of 10,000 people 1% have cancer, so that's 100 people.  If all of those took the test, 80 of them would test positive.

But how many people would test positive who don't have cancer?

False positives = 99% * 10% = .099.

In a population of 10,000 people 99% don't have cancer, so that's 9,900 people.  If all of those took the test, 990 would test positive.

So given that you have a positive test result, what are the chances that you are in the first group rather than the second group?

Well, we take the ratio of the true positives by all the positives, which equals,

80/(80+990) = 0.747663

So you have a roughly 7.5% chance of having cancer given the test result.  Surprisingly low right?

Now here's the real zinger regarding converging lines of evidence that I explained to Micah above in abbreviated fashion.  Suppose that you took a second test with similar numbers:

4. If a person has cancer, then test 2 gives a true positive 90% of the time.
5. If a person does not have cancer, then test 2 gives a false positive 10% of the time.

Unfortunately, this second test also comes back positive.  What are the chances that you have cancer now?  You might think that it's just the union of the two probabilities P(C|T1) ∪ P(C|T2), but you would be wrong.  That number would actually be way too low, now.  (That comes out to 15.18% if you're curious.)

The trick is to see that given the first test result you have to update the likelihood that you have cancer from 1% likely to 7.5%.  (The other, shorter but less intuitive way is just to do an additive version of the Bayes' Theorem.)

So now we go through the same steps we did above, but instead of multiplying 1% * 80% to get the number of true positives, we have to multiply 7.5% * 90%, which is obviously much higher.  We also need to lower the number of false positives.  Instead of multiplying 99% * 10% we are now multiplying 92.5% * 10%.

When we run the numbers, we get a result of approximately 42.2% likely that you have cancer given two separate positive results.  Interestingly, it is still more likely than not that you don't have cancer because of how rare cancer actually is, but that second number is way higher than you might think given the low likelihood of either test result independently indicating that you have cancer.  This is the power of converging lines of evidence.  You can see that if we add a third and fourth test, this likelihood would shoot up pretty fast.

Similarly, lines of argument that on their own only raise the probability of God's existence slightly can combine to make a very powerful total case, just like multiple pieces of evidence in a trial, provided that they are actually independent pieces of evidence and not just recycling the same evidence in a circular fashion.
