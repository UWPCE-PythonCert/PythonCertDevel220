=================
Lesson 06 Content
=================

.. raw:: html

   <div id="menuheading">

.. rubric:: Advanced Testing
   :name: advanced-testing
   :class: caH2

.. raw:: html

   <div id="navbar" class="caNav grid-row around-md clearunderlinestyle"
   role="navigation">

`Introduction <%24WIKI_REFERENCE%24/pages/lesson-06-introduction>`__ \|
`Content <%24WIKI_REFERENCE%24/pages/lesson-06-content>`__ \|
`Quiz <%24CANVAS_OBJECT_REFERENCE%24/assignments/i785a5d3880dcadcaa1cd6b716d4d39a6>`__ \|
`Activity <%24CANVAS_OBJECT_REFERENCE%24/assignments/i7d2419227ff2f1b019facc3c9bee85ff>`__
\|
`Assignment <%24CANVAS_OBJECT_REFERENCE%24/assignments/i935731b3c2d005ed6219d01b38544785>`__
\| `Code
Talk <%24CANVAS_OBJECT_REFERENCE%24/discussion_topics/i197968e655e43b6b4981d673c25fbcf2>`__

.. raw:: html

   </div>

.. raw:: html

   <div class="caNav grid-row around-md clearunderlinestyle"
   role="navigation">

.. raw:: html

   </div>

.. raw:: html

   </div>

As you write more lines of code for a programming project, or as the
number of programmers working on a project increase, your code becomes
more complex. Some projects become so complex that programmers have a
difficult time anticipating how the change they want to make on any
given line of code will effect the rest of the program. This lesson will
cover three answers to this challenge of managing complexity in your
software:

-  Testing: defining the expected behavior of your code, and expressing
   that behavior in a software script that can quickly tell you whether
   your code changes have broken existing code, or whether your changes
   have fixed code that wasn't working.
-  Coverage: measuring how much of your code is invoked by your
   automated tests. If only 10% of your code is invoked by your
   automated tests, then your tests will not know if anything is broken
   in the other 90%.
-  Linting: a "report card" on how well your code conforms to typical
   standards of style and syntax. The more closely your code conforms to
   standards of style, the more likely that another programmer will be
   able to read, understand, and maintain it. Linters also often analyze
   your code for complexity: less complex code is easier to read,
   understand, and maintain than more complex code.

We'll also address the following general concepts of software
engineering:

-  Writing testable code: not all styles of code writing lend themselves
   to automated testing. Fortunately, many strategies for making code
   more testable also make code more maintainable. One such method is
   called \ *dependency injection*.
-  Unit tests vs. integration tests: testing each piece of your software
   individually vs testing it as a whole. If you only test your software
   as a whole, then when you find unexpected/broken behavior you may not
   know exactly which piece of your software is responsible for this
   failure. "Unit testing" is the practice of testing each piece
   individually so that you can know exactly which piece to attribute
   failure to. And you also want to test your software as an integrated
   whole to make sure that the pieces are working together correctly.

Why test?
=========

You probably already have some familiarity with software testing in
general, and writing tests in Python specifically. In this section,
we're going to revisit the basic question: why write software tests. Our
discussion here will form the foundation of the rest of the lesson.

I encourage you to type along with these examples, creating the
squarer.py file and the test files!

A Simple Example
----------------

Suppose that you have written a simple class for squaring numbers:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    # squarer.py
    class Squarer(object):

        @staticmethod
        def calc(operand):
            return operand*operand

.. raw:: html

   </div>

Squarer is a simple class, with a single static method: calc. The calc
method calculates the square of its argument in the usual way, and
returns it to the caller.

Let's use the Squarer class from the REPL: 

::

    $ python -i
    >>> from squarer import Squarer
    >>> Squarer.calc(3)
        9
    >>> Squarer.calc(100)
        10000

Squarer works well: squaring 3 yields 9. Squaring 100 yields 10,000. The
Squarer class is working perfectly.

Now imagine that you, or maybe another engineer working on this project
has a "bright idea" about how to improve the Squarer class: squaring
involves powers, therefore the Squarer class should be using the power
operator. They make the following modification to your code:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    # squarer.py
    class Squarer(object):

        @staticmethod
        def calc(operand):
            # return operand*operand  # OLD
            return operand**operand

.. raw:: html

   </div>

Then at some point later you're using the squarer class to square
numbers:

::

    $ python -i
    >>> from squarer import Squarer
    >>> Squarer.calc(3)
        27
    >>> Squarer.calc(100)
        100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

The square of 3 is definitely not 27. And squaring 100 should give
10,000, not
100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000!
Your code is definitely broken: an error has been introduced into the
Squarer class.

Automated Test Script 
----------------------

If you were to sit down and think about this problem, here's the
solution that you would come up with:

-  When I try squaring 3 I expect to get 9, but I got 27. When I try
   squaring 100 I expect to get 10,000, but I got a much larger number.
-  It takes me a minute or two to try these examples at the REPL, and
   getting into the REPL and trying these examples is kind of a hassle.
-  So I could write a Python script that tries using the Squarer class
   to square 3 and 100. Running the script will be easy and only take a
   few seconds, so when I make a change to Squarer it will only take me
   a few seconds to find out whether I've broken it or not.
-  I could make a habit of running this test script every time I make a
   change to Squarer. If I have a colleague who is working on the
   Squarer class, then they should run the script whenever \ *they* make
   a change to Squarer. In this way, we'll know right away if we've
   introduced an error into Squarer.

Here's a suitable test script:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    # test.py
    from squarer import Squarer

    class SquarerTest(object):

        @staticmethod
        def test_positive_numbers():

            squares = {
                1: 1,
                2: 4,
                3: 9,
                12: 144,
                100: 10000,
            }

            for num, square in squares.items():
                result = Squarer.calc(num)

                if result != square:
                    print("Squared {} and got {} but expected {}".format(num, result, square))
        @staticmethod
        def test_negative_numbers():

            squares = {
                -1: 1,
                -2: 4,
                -3: 9,
                -12: 144,
                -100: 10000,
            }

            for num, square in squares.items():
                result = Squarer.calc(num)

                if result != square:
                    print("Squared {} and got {} but expected {}".format(num, result, square))

    if __name__ == "__main__":
        SquarerTest.test_positive_numbers()
        SquarerTest.test_negative_numbers()

.. raw:: html

   </div>

The SquarerTest class has two static methods: test\_positive\_numbers
and test\_negative\_numbers. I'll explain the test\_positive\_numbers
method, and the test\_negative\_numbers method is nearly identical.

The goal of this script is to define the expected behavior of Squarer
and test Squarer against that expected behavior. So we begin by creating
a dictionary that defines that behavior:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

        squares = {
            1: 1,
            2: 4,
            3: 9,
            12: 144,
            100: 10000,
        }

.. raw:: html

   </div>

Each \ *key* in this dictionary is a number. The corresponding \ *value*
is the value that we expect Squarer to produce when we square the key.
So one of the key/value pairs that we are testing is 12 and 144:
squaring 12 should produce 144.

Next we iterate through these number, square pairs:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

        for num, square in squares.items():
            result = Squarer.calc(num)

            if result != square:
                print("Squared {} and got {} but expected {}\n".format(num, result, square))

.. raw:: html

   </div>

We use Squarer to square the number, and capture the result in a
variable named \ *result*. If \ *result* is not equal to the square that
we defined in \ *squares*, then we print a message describing the error.

Finally, we add a \ *\_\_name\_\_ == "\_\_main\_\_"* clause so that we
can run this script from the command line:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    if __name__ == "__main__":
        SquarerTest.test_positive_numbers()
        SquarerTest.test_negative_numbers()

.. raw:: html

   </div>

Running \ *python test.py* will invoke the
SquarerTest.test\_positive\_numbers method and also the
SquarerTest.test\_negative\_numbers method. If our Squarer.calc method
is working as we expect it to, if it conforms to the behavior we defined
in the \ *squares* dictionary, then nothing will be printed to the
console. But if the SquarerTest finds discrepancies in the behavior of
Squarer, then it will print those discrepancies to the console.

Given our latest mistake that we introduced to \ *squarer.py*, here is
the result of running \ *python test.py*:

::

    $ python test.py
    Squared 3 and got 27 but expected 9
    Squared 12 and got 8916100448256 but expected 144
    Squared 100 and got 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 but expected 10000
    Squared -1 and got -1.0 but expected 1
    Squared -2 and got 0.25 but expected 4
    Squared -3 and got -0.037037037037037035 but expected 9
    Squared -12 and got 1.1215665478461509e-13 but expected 144
    Squared -100 and got 1e-200 but expected 10000

    $

Let's go back into squarer.py and fix our mistake:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    # squarer.py
    class Squarer(object):

        @staticmethod
        def calc(operand):
            # return operand*operand   # OLD
            # return operand**operand  # WRONG
            return operand*operand

.. raw:: html

   </div>

Has this actually fixed our code? Let's run our test script to find out:

::

    $ python test.py

    $

Running test.py produces no errors: test.py was not able to find any
discrepancies between the expected behavior that we defined for
Squarer's calc method and the method's actual behiavor. 

Suppose you wanted to revise squarer.py one more time. You want to try
another implementation of the calc method that uses the power operator:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    # squarer.py
    class Squarer(object):

        @staticmethod
        def calc(operand):
            # return operand*operand   # OLD
            # return operand**operand  # WRONG
            # return operand*operand   # OLD
            return operand**2

.. raw:: html

   </div>

By putting our test into a script file that we can run from the command
line, we've made it so that it only takes a few seconds to test whether
we've introduced an error into our code. We run our test script:

::

    $ python test.py

    $

The test script has not found any discrepancies between the \ *expected*
and \ *actual* performance of Squarer.calc: it looks
like \ *operand\*\*2* is an acceptable way to implement squaring!

Using Unittest
==============

Our first example showed exactly the system that you would come up with
if you wanted an automated way assure that the Squarer class was working
correctly.

Python also includes a built-in library for automated software tests:
unittest. We can create tests in unittest that are very similar to the
test\_positive\_numbers and test\_negative\_numbers tests that we
created above, but unittest adds a few extra features. Let's create a
test2.py file:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    # test2.py
    import unittest

    from squarer import Squarer

    class SquarerTest(unittest.TestCase):

        def test_positive_numbers(self):

            squares = {
                1: 1,
                2: 4,
                3: 9,
                12: 144,
                100: 10000,
            }

            for num, square in squares.items():
                self.assertEqual(square, Squarer.calc(num), "Squaring {}".format(num));

        def test_negative_numbers(self):

            squares = {
                -1: 1,
                -2: 4,
                -3: 9,
                -12: 144,
                -100: 10000,
            }

            for num, square in squares.items():
                self.assertEqual(square, Squarer.calc(num), "Squaring {}".format(num));

.. raw:: html

   </div>

These test methods are just a little different than the test script we
created for ourselves above. Here are the key differences:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    import unittest                       # <---

    from squarer import Squarer

    class SquarerTest(unittest.TestCase): # <---
        ....

.. raw:: html

   </div>

We import the unittest library, and our SquarerTest class inherits from
unittest.TestCase. Next:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    class SquarerTest(unittest.TestCase):
                                          # <---
        def test_positive_numbers(self):  # <---

.. raw:: html

   </div>

Our test class methods \ *are not static*: they do not include
a \ *@staticmethod* decorator, and they also accept \ *self* as their
initial, implicit argument. Also, it is a unittest requirement that all
of our test methods begin with the word "test", as in
*test*\ \_positive\_numbers. Next:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

            for num, square in squares.items():
                self.assertEqual(square, Squarer.calc(num), "Squaring {}".format(num));  # <---

.. raw:: html

   </div>

The TestCase class includes instance methods for making assertions about
the behavior of our program. The \ *assertEqual* method is an instance
method defined in the TestCase class: it helps us compare the expected
behavior of a program with its actual behavior. The first argument we
give it is the \ *expected* result of squaring our number \ *num*. Then
we give it the \ *actual* square that's produced by Squarer.calc. We can
also can also specify an optional helpful message for the test library
to print if this test fails: our helpful message will tell us what
number we were trying to square when the test failed.

Here's another difference: note that I didn't include an \ *if
\_\_name\_\_=="\_\_main\_\_"* clause. We \ *wont* be running this script
directly, instead we'll invoke it indirectly through the unittest
library. You'll see that below.

Finally, there's one more difference between unittest and our original
test script that you may or may not care about: unittest will stop
running a test method as soon as it finds a single assertion error. That
is to say, if test\_positive\_numbers finds that Squarer does not
produce 9 when squaring 3, then it \ *will* report that error but then
it won't try any more numbers: it \ *won't *\ also try squaring 12 to
see if it produces 144.

Here's the current content of our squarer.py file:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    # squarer.py
    class Squarer(object):

        @staticmethod
        def calc(operand):
            return operand**2

.. raw:: html

   </div>

I expect that our Squarer.calc method should be working correctly! And
here's the output of running our test:

::

    $ python -m unittest test2
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.000s

    OK
    $

Excellent! Our Squarer.calc method is working correctly. We wrote two
tests, test\_positive\_numbers and test\_negative\_numbers, and our
unittest script found no discrepancies between the expected and actual
behavior of Squarer.calc. Each test method that our code satisfies is
represented by a '.' at the top of the output. The "OK" also signifies
that each test was passed by our code. Finally, if you're a UNIX geek,
you'll be interested to know that this test run produced a zero return
value.

We can also choose which tests to run. Calling \ *python -m unittest
test2* runs all of the tests in the test2.py file. If there were
multiple test classes in the test2 file, we could choose to run only the
SquarerTest tests:

::

    $ python -m unittest test2.SquarerTest
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.001s

    OK

We can also choose to run just a single test within the SquarerTest
class:

::

    $ python -m unittest test2.SquarerTest.test_positive_numbers
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK

Running just a single test at a time can be helpful if all of your tests
together take a long time to run, but you're working on fixing a single
bug that's covered by a single test.

Let's modify our squarer.py file to produce an error and see what how
unittest reports test failures. Modify squarer.py:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    # squarer.py
    class Squarer(object):

        @staticmethod
        def calc(operand):
            return operand**2  # OLD
            return operand**operand

.. raw:: html

   </div>

Running our tests produces:

::

    $ python -m unittest test2

    FF
    ======================================================================
    FAIL: test_negative_numbers (test2.SquarerTest)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
     File "C:\Users\jaschilz\tmp\test2.py", line 32, in test_negative_numbers
     self.assertEqual(square, Squarer.calc(num), "Squaring {}".format(num));
    AssertionError: 1 != -1.0 : Squaring -1

    ======================================================================
    FAIL: test_positive_numbers (test2.SquarerTest)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
     File "C:\Users\jaschilz\tmp\test2.py", line 19, in test_positive_numbers
     self.assertEqual(square, Squarer.calc(num), "Squaring {}".format(num));
    AssertionError: 9 != 27 : Squaring 3

    ----------------------------------------------------------------------
    Ran 2 tests in 0.001s

    FAILED (failures=2)

Each test that failed is represented by an "F" at the top of the output.
If were running multiple tests, with some passes and some failures, then
we would see a mix of "."s and "F"s at the top of the output. In this
case, we ran two tests and both failed. If our code fails \ *any* tests,
then we will also see the word "FAILED" at the bottom of the output,
replacing "OK". If you're a UNIX geek, you might be interested to know
that this test run has produced a non-zero return value.

The unittest library also gives us detailed information about each test
that failed. Let's look at the output for test\_positive\_numbers:

::

    ======================================================================
    FAIL: test_positive_numbers (test2.SquarerTest)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
     File "C:\Users\jaschilz\tmp\test2.py", line 19, in test_positive_numbers
     self.assertEqual(square, Squarer.calc(num), "Squaring {}".format(num));
    AssertionError: 9 != 27 : Squaring 3

    ----------------------------------------------------------------------

We can see that the code failed its assertion on line 19. The unittest
library reports that it the expected value, 9, was not equal to the
actual value 27 produced by our code. We also see the helpful output
message that we created: "Squaring 3". This tells us that the test
failed while attempting our test scenario for squaring the number 3.

And recall that unittest will stop a test method as soon as it
encounters its first assertion error! Our Squarer.calc would
probably \ *also* fail to produce 144 when squaring 12, but our test
method will not move on to that scenario until our code passes the
scenario for squaring 3.

Now that we know that our change to squarer.py has introduced an error,
let's revise our code to fix the error, run the tests again, and see
that our code is working as expected once again.

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    # squarer.py
    class Squarer(object):

        @staticmethod
        def calc(operand):
            return operand**2        # OLD
            return operand**operand  # BAD
            return operand*operand   # This should work

.. raw:: html

   </div>

Running our tests:

::

    $ python -m unittest test2
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.001s

    OK

Great! Our squarer works as expected again!

In practice you'll probably always use unittest or another similar
library instead of your own, completely homegrown test scripts. The
unittest library offers several useful features, and doesn't require
much more typing than the homegrown test script example above. But the
unittest test methods we've written are not much different in \ *intent*
then the scripts you would come up with yourself if you wanted to write
a script to test whether your code was functioning as intended.

A more complex example
======================

As you watch this video, bear in mind that part of your assignment is
going to be to complete the calculator that's presented here. Type along
if you wish, and there will also be a code repository for you to clone.

{{VIDEO HERE}}

What could go wrong with addition and subtraction? Well, at the end of
this example we found something that could go wrong! I was expecting
that with 11 in the calculator, entering a 2 and then subtracting would
produce 9, not -9.

At this point, let's \ **define**\  what it means for our
module's behavior to be correct:

#. An \ **operator**\  is a class instance which provides a method
   named \ *calc*. The \ *calc*\  method shall accept two arguments and
   operate on its arguments in the "typical" order:
   *Adder().calc(a, b) = a + b
   Subtracter().calc(a, b) = a - b
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
   *enter\_number(a), enter\_number(b), add() = a + b
   enter\_number(a), enter\_number(b), subtract() = a - b
   etc...*
#. The \ *add, subtract, multiply, *\ and \ *divide*\  methods shall
   both:

   #. Return the result of the operation
   #. Enter the result of the operation back into the calculator

   This makes it possible to perform the following sequences of
   operations:

   #. *calculator.enter\_number(2)*
   #. *calculator.enter\_number(3)*
   #. *calculator.add()                      # Returns 5, and now 5 is
      now 'in the calculator' *
   #. *calculator.enter\_number(1)*
   #. *calculator.subtract()               # Returns 4 because 5 - 1 =
      4 *

#. What should happen if a user enters only one number and then tries to
   perform an operation? Let's decide that the calculator should throw
   an \ **InsufficientOperands** exception if there are fewer than two
   numbers in the stack.

Based on this definition, we can see that the final result of our
calculation in the video should have been 9!

There are some situations that our definition above don't explicitly
cover:

-  What should a \ *calculator* do if two numbers have already been
   entered onto the stack and the user enters a third?
-  What if there are more than two numbers "in the calculator" when the
   user performs an operation?
-  When a user adds 2 and 3, that enters 5 into the calculator. But are
   2 and 3 still in the calculator, or do they get removed?
-  Etc..

For the purposes of this exercise, we'll leave the behavior in these
circumstance \ *undefined*. Any person who wants to program
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

Unit testing Adder and Subtracter
=================================

Let's begin our tests with unit testing the Adder and Subtracter
classes. Recall that unit testing involves testing a \ *single unit* of
code. This usually means testing a single class all by itself: without
involving any other class.

If we can define the correct behavior of a single class and test it in
isolation from any other code, then if our unit test fails we know it's
because of a failure in that specific class: if we've written a test
that only uses Adder and not Subtracter, then we know that if that test
fails it is because of a problem in the Adder class.

{{VIDEO HERE}}

Unit testing Calculator
=======================

Unit testing was easy for the Adder and Subtracter: Adder and Subtracter
don't make use of any other classes. But just *creating* a Calculator
requires creating an Adder, a Subtracter, a Multiplier, and a Divider:
how can we possible devise unit tests for Calculator that don't involve
those other classes at all?

To answer this question, we introduce a new tool library: \ *mock*.

{{VIDEO HERE}}

Testing Calculator in isolation from all of the other classes is
difficult, but we achieve it by strictly defining the responsibilities
of Calculator, separate from the responsibilities of the other classes,
and testing those responsibilities in isolation using dummy Adder,
Subtracter, Multiplier, and Divider methods.

Integration Testing
===================

For our integration tests, we want to know if all of our code works
together, as a whole. To accomplish this, we create a calculation
scenario where all of our classes are working together, and confirm that
our calculator produces the correct result.

{{VIDEO HERE}}

Linting
=======

Using automated tests to confirm the functioning of your code is not the
only way to manage the complexity of a large code base. There are also
tools which can automatically report on how readable your code is and
how well it follows the conventions of Python programming: flake and
lint.

These tools can help ensure that your code is readable and maintainable
by other programmers.

{{VIDEO HERE}}

Coverage
========

{{VIDEO HERE}}

Test Driven Development
=======================

No discussion of testing is complete without Test Driven Development
(TDD).

TDD is a practice that extends the idea of testing; instead of writing
some cool code and then writing a test to make sure it never gets
broken, first you conceive of what you want your software to accomplish,
you write tests that will pass once you've written your software, and
then you write the software, then you run the tests to make sure that
you have satisfied their behavioral requirements.

To begin with, go back to the \ `TDD
video <https://www.youtube.com/watch?v=HhwElTL-mdI>`__ and watch a few
more minutes of the talk. You're welcome to watch the whole thing; the
guy is a good presenter!

Although proponents of TDD describe it as an essential practice, TDD is
not currently "the standard" practice of test writing. For better or
worse, most software engineers write their tests \ *after* they write
their code, like we did in our videos above, not \ *before*. Even so,
TDD is a valuable tool to explore: trying it in one of your own projects
can be an enlightening experience and improve your coding of tests in
general.

Conclusion
==========

 Brian Kernighan, computer science, and co-author of the famed `K&R *C
Programming
Language* <https://en.wikipedia.org/wiki/The_C_Programming_Language>`__
wrote that, "Controlling complexity is the essence of computer
programming."

Today, you might be focused on the \ *syntax* of computer programming:
how to turn individual bits of logic into control statements in the
Python language. And you might be focused on how to build those
statements up into programs of a few hundred lines of code.

With practice, you'll soon become comfortable with the line-by-line and
method-by-method of constructing Python programming. You'll encounter
the challenge of maintaining and contributing to large, old code bases.
In this lesson, we introduced you to \ *some* of the tools that
engineers use to manage the complexity of large software projects.
