############
Introduction
############

Introduction
============

{{VIDEO HERE}}

| In this second lesson on functional programming, the first having been
  completed in the last class, we look at the lambda special
  form, which can be used in conjunction with map() and filter() and
  also in comprehensions.  We will consider the debates as to lambda's
  effectiveness by looking at its history and the comments of Python's
  creator Guido van Rossum.
| Where we had been avoiding the topic up until now, at long last we
  investigate iterators and iterables, core constructs in Python 3. 
  Both terms are sprinkled throughout the Python programming literature
  and the distinction between them can be subtle.
| Finally we look at generators, powerful programming constructs that
  are lazy by nature (in the functional programming sense of lazy) and
  thus can produce infinite sequences without exhausting the resources
  of real-world computers.

For the functional programming modules, we \ *recommend*\  the
text \ `Functional Python Programming by Steven
Lott. <https://www.packtpub.com/application-development/functional-python-programming>`__

*Each lesson's Optional Readings will draw from this text.*

| Publisher: Packt Publishing
| Pub. Date: January 31, 2015
| Web ISBN-13: 978-1-78439-761-6
| Print ISBN-13: 978-1-78439-699-2
| ***Note: a second edition is out here: ***

https://www.packtpub.com/application-development/functional-python-programming-second-edition

Learning Objectives
===================

Upon successful completion of this lesson, you will be able to:

-  use the lambda special form to define an anonymous function.
-  use lambda expressions with \`map\` and \`filter\` and in
   comprehensions.
-  articulate the difference between an iterator and an iterable.
-  use \`yield\` to create a generator.

New Words, Concepts, and Tools
==============================

-  Anonymous function
-  Lambda
-  Iterator
-  Iterable
-  Generator
-  yield

Required Reading
================

-  Small functions and the lambda expression
   https://docs.python.org/dev/howto/functional.html?highlight=lambda#small-functions-and-the-lambda-expression
-  Iterators
   https://www.codementor.io/milesak60/round-and-round-on-iterables-vs-iterators-lgq2xg62f
   https://docs.python.org/3/glossary.html#term-iterator
   \ https://docs.python.org/3/library/stdtypes.html#iterator-types
   https://docs.python.org/dev/howto/functional.html#iterators
-  Itertools
   https://docs.python.org/3/library/itertools.html
   https://pymotw.com/3/itertools/index.html
-  What exactly are Python's iterator, iterable, and iteration
   protocols?
   https://stackoverflow.com/questions/9884132/what-exactly-are-pythons-iterator-iterable-and-iteration-protocols
-  Generators
   https://wiki.python.org/moin/Generators

Optional Reading
================

-  Lott, S. (2015) Chapter 5. Higher-order Functions. Using Python
   lambda forms. In Functional Python Programming.
-  Lott, S. (2015) Chapter 3. Functions, Iterators, and Generators. In
   Functional Python Programming.
-  The Iterator Protocol: How For Loops Work in Python
   http://treyhunner.com/2016/12/python-iterator-protocol-how-for-loops-work/
-  Chapter 14 in Fluent Python by Luciano Ramalho
   http://www.learningpython.com/2009/02/23/iterators-iterables-and-generators-oh-my/
-  PEP 255 — Simple Generators
   https://www.python.org/dev/peps/pep-0255/
