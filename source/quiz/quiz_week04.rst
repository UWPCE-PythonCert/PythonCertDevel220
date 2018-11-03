=======================
Python 220 Week 04 Quiz
=======================


#. Lambdas can do things that standard, named functions cannot.
False
True
The only thing that lambdas can do that named functions cannot is that they
can be defined inline.  This is not a functional difference; rather, it is a
 difference in syntax.
False.  There is nothing a lambda can do that a standard named function cannot.

#. Iterators and generators are more memory efficient than instantiated sequences such as lists.
True
False
Keep in mind that if all you need to do with the results of an expression
that generates a sequence is to loop over it, use a generator expression
rather than a list comprehension.  A generator expression will behave
exactly as you would expect in a for loop and it will be more memory
efficient than generating an entire list via a list comprehension.
Iterators and generators are lazy in the sense that they only compute the
next value of a sequence when they are called upon to do so.  This means
that they need not compute an entire list of values.

#. Iterators and generators raise the StopIteration exception when they have no more values to emit
True
False
Note that for loops listen for Stopiteration and take the appropriate action
 for you when an iterator or generator is empty.  In other words, they stop.

#. Between subsequent calls generators pick up from where they left off by
   using this special keyword.
yield
return

#. Generators can create infinite series without using infinite computer
   memory.
True
False
Correct.  Generators are lazy in the sense that they only calculate the next
 value of a sequence when they are called upon to do so.  This makes them
 highly memory efficient.
