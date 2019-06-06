##########
Assignment
##########
    
In this lesson's assignment we are going to apply the functional
programming techniques we have learned to improve code that we have
written in earlier lessons for the case study.
As important as learning the syntax for iterables, iterators and generators
is understanding the context in which they are best used.
This assignment will allow you to reflect on that as you apply your learning.

Here is what you need to do:
----------------------------
We are not going to develop new functionality in this assignment. Rather,
we are going to refactor existing code to improve it and make it more Pythonic.
This is a very common activity in application development.

You will already have tests from the lesson 3 assignment that verify data is being
written to the HP Norton databases. Although we are going to change the way
data is written to and read from the databases, the tests should not need to change.
We are amending the functionality the tests use to make them easier to maintain and be
more Pythonic.

This development process, where we change internal behavior while preserving how
that behavior is called, is named *refactoring*.

So here is our refactoring assignment:

#. Using comprehensions, iterators / iterables, and generators appropriately,
   and the assignment 3 data, write data to your customer
   database and read / display it.
#. Verify existing unit tests still function correctly.
#. If necessary, update your tests to show the data is being maintained correctly in the database.
#. Add code to log all database data changes (adds, amends, deletes) to a file called db.log.

Be sure to consult the lesson 3 assignment for details of the functionality.

Other requirements:
-------------------
- Your code should not trigger any warnings or errors from Pylint.

Testing
-------
- Make sure your existing tests run as expected.

Submission
----------
- You will need to submit *basic_operations.py* plus any test files you develop.

Tips
----
- Remember to think about system features, not web pages or the UI.
- Tests first!
- Think about the right techniques to use given the volumes of data.
- Be sure you make the best use of your existing tests.
