=====================
Lesson 4 : Assignment
=====================

.. todo::
    Make this assignment consistent with the case study.
    
In this lesson's assignment we are going to apply the functional
programming techniques we have learned to improve code that we have
written in earlier lessons for the case study.
As important as leanring the syntax for  iterables, iterators and generators
is understanding the context in which they are best used.
This assignment will allow you to reflect on that as you apply your learning.

Here is what you need to do:
----------------------------
We are not going to develop new functionality in this assignment. Rather,
we are going to refactor existing code to improve it and make it more Pythonic.
This is a very common development activity in application development.

You will already have tests from past assignments that verify data is being
written to the HP Norton databases. Although we are going to changes the way
data is written to and read from the databases, the tests should not need to change.
We are amending the functionality the tests use to make them perform better and be
more Pythonic.

This development process, where we change internal behavior while preserving how
that behavior is called is named refactoring.

So here is our refactoring assignment:


#. Using comprehensions, iterators / iterables, and generators appropriately,
   and the instructor-provided customer data, write data to your customer
   database and read / display it.
#. Verify existing tests still function correctly.
#. If necessary, update tests to show the data is being maintained correctly in the database.
#. Log all database data changes (adds, amends, deletes).

.. todo::
    Create a customer csv file to be used for loading data with at least
    1000 records (Andy).

Tips
----
#. Think about the right techniques to use given the volumes of data.
#. Be sure you make the best use of your existing tests
