##########################
Lesson 01 Advanced Testing
##########################

=========================================
Part 8: Unit testing Adder and Subtracter
=========================================

Let's begin our tests with unit testing the Adder and Subtracter
classes. Recall that unit testing involves testing a \ *single unit* of
code. This usually means testing a single class all by itself: without
involving any other class.

If we can define the correct behavior of a single class and test it in
isolation from any other code, then if our unit test fails we know it's
because of a failure in that specific class: if we've written a test
that only uses Adder and not Subtracter, then we know that if that test
fails it is because of a problem in the Adder class, something that is not
related with its interaction with other classes (interaction between
classes is covered by integration testing).

{{VIDEO HERE}}

Unit testing Calculator
=======================

Unit testing is a good solution for the Adder and Subtracter classes: Adder and Subtracter
don't make use of any other classes. But just *creating* a Calculator instance
requires creating an Adder, a Subtracter, a Multiplier, and a Divider:
how can we possible devise unit tests for Calculator that don't involve
those other classes at all, so that the class can be kept isolated for testing purposes?

To answer this question, we introduce a new tool library: \ *mock*.

{{VIDEO HERE}}

Testing Calculator in isolation from all of the other classes is
difficult, but we achieve it by strictly defining the responsibilities
of Calculator, separate from the responsibilities of the other classes,
and testing those responsibilities in isolation using dummy versions of Adder,
Subtracter, Multiplier, and Divider methods. The Mock library will also come
in handy in situations in which you need input from a networked location or a
physical sensor (for example, a temperature reading).
