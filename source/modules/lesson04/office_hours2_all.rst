Office Hours : This weeks' content
==================================
Agenda
------
#. Q+A This week's content
#. Student Demos: This week's content
#. Instructor Demos: This week's content


Functional Programming
======================

Additional information
----------------------

Functional programming
----------------------
Some links for you that may help with the concepts (in no particular order):

* https://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming

* https://www.dataquest.io/blog/introduction-functional-programming-python/

* https://www.vinta.com.br/blog/2015/functional-programming-python/

* https://marcobonzanini.com/2015/06/08/functional-programming-in-python/

* https://github.com/sfermigier/awesome-functional-python

Things to think about
---------------------
* What's easy?
* What's hard?
* Where are you struggling?
* Where do you need more information?

Let us know! Use Slack or post a question on Canvas.

Know of others? Clone and branch / amend / push and send a PR.



From last week:
===============
Iterators
---------
* https://anandology.com/python-practice-book/iterators.html
* https://www.programiz.com/python-programming/iterator

Programming paradigms
---------------------
* https://en.wikipedia.org/wiki/Comparison_of_programming_paradigms
* https://dev.to/ericnormand/programming-paradigms-and-the-procedural-paradox

Functional programming
----------------------
Some links for you that may help with the concepts (in no particular order):
* https://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming
* https://www.dataquest.io/blog/introduction-functional-programming-python/
* https://www.vinta.com.br/blog/2015/functional-programming-python/
* https://marcobonzanini.com/2015/06/08/functional-programming-in-python/
* https://github.com/sfermigier/awesome-functional-python


This week
=========
Questions?
----------
* What's easy?
* What's hard?
* Where do oyu need help?
* Where do you need more information?

Iterator
--------
An iterator is a stateful helper object that will produce the next value when you call
next() on it. Any object that has a __next__() method is therefore an iterator. How it produces a
value is irrelevant.
Think of an iterator is a value factory. Each time you ask it for "the next" value, it knows how to compute it
because it holds internal state.

Iterables
---------
Iterable objects are objects that conform to the "Iteration
Protocol" and can hence be used in a loop. They always return an iterator.

This protocol consists in two methods:
* the "__iter__" method that returns the object we would to iterate over and
* the "__next__" method that is called automatically on each iteration

and that returns the value for the current iteration.

Often, for pragmatic reasons, iterable classes will implement both __iter__() and __next__() in
the same class, and have __iter__() return self , which makes the class both an iterable and its
own iterator. It is perfectly fine to return a different object as the iterator though.

```
# here range() is an iterable object...
# at each iteration i is given a different value
# values returned one value at a time

for i in range(50):
    print(i)
```
You can create your own iterable by implementing the iteration protocol.

```
class fibonacci:
    def __init__(self, max=1000000):
        self.a, self.b = 0, 1
        self.max = max
    def __iter__(self):
        # Return the iterable object (self)
        return self
    def __next__(self):
        # To stop the iteration we just need to raise
        # a StopIteration exception
        if self.a > self.max:
            raise StopIteration
        # save the value that has to be returned
        value_to_be_returned = self.a
        # calculate the next values of the sequence
        self.a, self.b = self.b, self.a + self.b
        return value_to_be_returned

if __name__ == '__main__':
    MY_FIBONACCI_NUMBERS = fibonacci()
    for fibonacci_number in MY_FIBONACCI_NUMBERS:
        print(fibonacci_number)
```
and now let's prove an iterator is stateful...
```
"""
Simple iterator examples
"""

class IterateMe_1:
    """

    returns a sequence of numbers
    ( like range() )
    """

    def __init__(self, start, increment, stop):
        self.start = start
        self.increment = increment
        self.stop = stop
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.increment
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration

if __name__ == "__main__":

    iter = IterateMe_1(5,2,17)
    for i in iter:
        if i >10: break
        print(i)
    # it's stateful
    for i in iter:
        print(i)

    # reinitialize "loses state"
    iter = IterateMe_1(5,2,17)
    for i in iter:
        print(i)
```
Generators
----------
Generators in Python are just another way of creating iterable objects.
They are usually used when you need to create iterable object quickly,
without the need of creating a class and adopting the iteration protocol. They are "just a function" (or a comprehension).
They are used once; to use subsequent times you have to call the generator again.
An iterator is usually more memory-efficient than a generator, though. And, somewhat related, generators can be faster. BUT MEASURE!

```
def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b

if __name__ == '__main__':
    # Create generator of fibonacci numbers
    fibonacci_generator = fibonacci(1000000)
    # print out all the sequence
    for fibonacci_number in fibonacci_generator:
        print(fibonacci_number)
```
This has one yield statement, but a generator can have several. For each yield the state of the generator is saved.
All generators are iterators (but not vice versa); that is, Generator in Python is a subclass of Iterator. Try to prove this (hint issubclass() function).

See also
--------
https://stackoverflow.com/questions/2776829/difference-between-pythons-generators-and-iterators

Discuss
=======
1. Why not always use generators (rather than iterators)?
1. How to make an iterator stateless?

Next class
==========
PLEASE let me know ASAP if lesson 2 concepts need more explanation. Some of this work is challenging!
https://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming
https://codesachin.wordpress.com/2016/04/03/a-practical-introduction-to-functional-programming-for-python-coders/
https://www.dataquest.io/blog/introduction-functional-programming-python/

STOP PRESS
==========

To install the xcode command lines tools ONLY (and not needed if you already have xcode installed) type the following at the command prompt:

xcode-select --install

Also, see here: http://osxdaily.com/2014/02/12/install-command-line-tools-mac-os-x/

The book I mentioned on refactoring, if anyone is interested (this is not Python speicifc):
https://martinfowler.com/books/refactoring.html
See also http://blog.thedigitalcatonline.com/blog/2017/07/21/refactoring-with-test-in-python-a-practical-example/ (but we may be getting ahead here!)


Closures
========
Purpose
-------
Closures fulfill these purposes:
* replacing hardcoded constants
* a simple way to implement information hiding (https://en.wikipedia.org/wiki/Information_hiding) in programs that don't justify a full object oriented approach
* reduce the use of global variables

Closures in many ways are like functions, but closures preserve their internal state between calls (hence redution in global variable use). Closures also "hide" their internal state, preventing clients from accessing that internal state directly.

A closure is created using the following approach:
* A function is created inside another function (in other words, we have a nested function).
* The function that is enclosed (nested) needs to reference variables that are defined in the function in which it is enclosed).
* And finally, the enclosing function returns the nested function.

Example: a closure
------------------
```
def make_addings():
    results = []
    for i in range(10):
        def add(x, i=i):
            return i + x
        results.append(add)
    return results


for add in make_addings():
    print(add(3))
```
And another (making functions):
```
def make_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

multiply9 = make_multiplier(9)

print(multiply9(8))
```

External sources
----------------
* https://www.geeksforgeeks.org/python-closures/
* https://www.codevoila.com/post/51/python-tutorial-python-function-and-python-closure

Currying
========
Purpose
-------
Currying allows you to make new, specialized versions of an existing, multi-parameter function by pre-setting some of those parameters. Thus, you create more specialized functions from more general ones.

Currying allows little pieces of functionality to be setup and reused with ease, without clutter;

Example
-------
Uncurried:
```
def func(x, y):
  return 2 * x + y
```
Curried:
```
def func2(x):
  def inner(y):
    return 2 * (x + y)
  return inner

print(func2(7)(3))
```

External sources
----------------
* https://unpythonic.com/01_05_currying/
* https://mtomassoli.wordpress.com/2012/03/18/currying-in-python/
* https://hackernoon.com/ingredients-of-effective-functional-javascript-closures-partial-application-and-currying-66afe055102a

Itertools
=========
Purpose
-------
Itertools provides a set of memory efficient but fast tools, that can be used to provide comprehnsive looping features in pure Python. Examples include counting, repatition and grouping.

Example
-------
chain:
```
import itertools
for i in itertools.chain('ABC', 'DEF'):
    print(i)
```
count:
```
from itertools import *
for i in islice(count(), 5, 10):
    print(i)
```
permutations:
```
from itertools import *
for i in permutations("ABC"):
    print(i)
```

External sources
----------------
* https://medium.com/@mr_rigden/a-guide-to-python-itertools-82e5a306cdf8
* https://docs.python.org/3.1/library/itertools.html

