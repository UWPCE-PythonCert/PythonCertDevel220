######################
Part 5: Using Unittest
######################

Our first example showed the system that you would have to come up with
if you wanted an automated way to assure that the Squarer class was working
correctly.

Python also includes a built-in library for creating automated software tests:
unittest. We can create tests in unittest that are very similar to the
test_positive_numbers and test_negative_numbers tests that we
created above, with unittest adding a few extra features. Let's create a
test2.py file:

.. raw:: html

   <div
   style#"background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

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


These test methods are just a little different than the test script we
created for ourselves above. Here are the key differences:

.. raw:: html

   <div
   style#"background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    import unittest                       # <---

    from squarer import Squarer

    class SquarerTest(unittest.TestCase): # <---
        ....


We import the unittest library, and our SquarerTest class inherits from
unittest.TestCase. Next:

.. raw:: html

   <div
   style#"background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    class SquarerTest(unittest.TestCase):
                                          # <---
        def test_positive_numbers(self):  # <---

.. raw:: html

   </div>

Our test class methods *are not static*: they do not include
a *@staticmethod* decorator, and they also accept *self* as their
initial, implicit argument. Also, and this is very important, it is a *unittest requirement* that all
of our test methods begin with the word "test", as in
*test* _positive_numbers. Next:

.. raw:: html

   <div
   style#"background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

            for num, square in squares.items():
                self.assertEqual(square, Squarer.calc(num), "Squaring {}".format(num));  # <---

.. raw:: html

   </div>
