======================
Lesson 06 Introduction
======================

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

   </div>

Introduction
============

This week's topics step beyond *programming* into a central question
of \ *software engineering*: how do you manage code that is too big to
fit inside your own head?

Up until now, most of the programs that you've written for this course
have probably been 200 lines or fewer, and you wrote them on your own. A
single programmer can completely understand a program this small. As
programs get bigger and you begin working in teams, it becomes difficult
to understand or remember how the changes you make on line 523 of your
program will effect the operation of code written on lines 10, 200, or
2000.

There are tools that can help us manage the complexity of a large
codebase. And the tools that we'll explore for this lesson are testing,
linting, and flaking. While exploring these tools, we'll introduce a
software design pattern that makes it easier to write maintainable code:
dependency injection.

Learning Objectives

Upon successful completion of this lesson, you will be able to:

-  Use dependency injection and mocking to create easily testable code.
-  Differentiate between unit testing and acceptance testing.
-  Create a file for your project that defines a code style standard,
   and run an automatic analysis of your code to test whether it
   conforms to that standard.
-  Automatically identify areas of your code that might be difficult to
   maintain or test.

New Words, Concepts, and Tools
==============================

-  unittest
-  unittest.TestCase
-  dependency injection
-  TestCase.setUp
-  mock
-  mock.MagicMock
-  flake8
-  pylint
-  coverage

Required Reading
================

-  `Managing Software
   Complexity <http://oberheim.github.io/complexity/2016/05/18/managing-software-complexity.html>`__
-  `Technical
   Debt <https://en.wikipedia.org/wiki/Technical_debt>`__ (wiki) for
   discussions on the types of problems we'll be addressing.
-  ONLY the first 3 minutes and 44 seconds of
   this \ `video <https://www.youtube.com/watch?v=HhwElTL-mdI>`__
   STOP at 3:44! After 3:44 it introduces Test Driven Development which
   we will circle back to at the end of the lesson but will confuse our
   discussion right now.
