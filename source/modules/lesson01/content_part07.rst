##########################
Lesson 01 Advanced Testing
##########################

==============================
Part 7: A more complex example
==============================

.. toctree::
    :maxdepth: 1

    content_part01
    content_part02
    content_part03
    content_part04
    content_part05
    content_part06
    content_part08
    content_part09
    content_part10
    content_part11

As you watch this video, bear in mind that part of your assignment is
going to be to complete the calculator that's presented here. Type along
if you wish, but there will also be a code repository for you to clone.

{{VIDEO HERE}}

What could go wrong with addition and subtraction? Well, at the end of
this example we found something that could go wrong! I was expecting
that with 11 in the calculator, entering a 2 and then subtracting would
produce 9, not -9.

At this point, let's \ **define**\  what it means for our
module's behavior to be correct:

#. An \ **operator**\  is a class instance which provides a method
   named \ *calc*. The \ *calc*\  method shall accept two arguments and
   operate on its arguments in the usual order:
   *Adder().calc(a, b) # a + b
   Subtracter().calc(a, b) # a - b
   *\ etc...
#. A \ **calculator**\  is a class instance which provides
   an \ *enter\_number*\  method and \ *add, subtract,
   multiply, *\ and \ *divide*\  methods.
#. The constructor of a \ *calculator* shall accept four \ *operators*:
   an \ *adder, subtracter, multiplier, *\ and \ *divider*. The
   calculator shall use these operators to perform its \ *add, subtract,
   multiply*, and \ *divide*\  methods.
#. *enter\_number(a)*, \ *enter\_number*\ (*b), operator*\  should be
   the same as \ *a operator b*. In other words:
   *enter\_number(a), enter\_number(b), add() # a + b
   enter\_number(a), enter\_number(b), subtract() # a - b
   etc...*
#. The \ *add, subtract, multiply, *\ and \ *divide*\  methods shall
   both:

   #. Return the result of the operation
   #. Enter the result of the operation back into the calculator

   This makes it possible to perform the following sequences of
   operations:

   #. *calculator.enter\_number(2)*
   #. *calculator.enter\_number(3)*
   #. *calculator.add()                      # Returns 5, and 5 is
      now 'in the calculator' *
   #. *calculator.enter\_number(1)*
   #. *calculator.subtract()               # Returns 4 because 5 - 1 #
      4 *

#. What should happen if a user enters only one number and then tries to
   perform an operation? Let's decide that the calculator should throw
   an \ **InsufficientOperands** exception if there are fewer than two
   numbers in the stack.

Based on this definition, we can see that the final result of our
calculation in the video should have been 9!

There are some situations that our definition above doesn't explicitly
cover:

-  What should a \ *calculator* do if two numbers have already been
   entered onto the stack and the user enters a third?
-  What if there are more than two numbers "in the calculator" when the
   user performs an operation?
-  When a user adds 2 and 3, that enters 5 into the calculator. But are
   2 and 3 still in the calculator, or do they get removed?
-  Etc..

For the purposes of this exercise, we'll leave the behavior in these
circumstances \ *undefined*. Any person who wants to program
a \ *calculator* could choose to write their code such that:

-  a\ * calculator* throws an error when a third number gets entered
   into the calculator
-  or it could just ignore any new numbers entered if it already has two
   numbers
-  or it could replace one of the two numbers with the third

Any of these choices would be OK in that they would not explicitly
violate the six behavioral rules we defined above.

Our next step is to add tests that can automatically tell us if our
classes are conforming to those six behavioral rules.
