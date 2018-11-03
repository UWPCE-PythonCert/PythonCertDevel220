==============================
Assignment: Lesson 01 Activity
==============================

.. todo::
    Lesson 1 activity needs rework

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

Your assignment is to complete testing and linting on the calculator
from the lesson content. As a first step, review the videos and writing
on that page. Then find the calculator project directory in the course
repository.

Your goals:
===========

Note that all of the command examples below should be run from inside
the project root which contains the *unit-test.py*
and \ *integration-test.py* files.

#. Provide a *MultiplierTests* and \ *DividerTests* test classes in
   the \ *unit-test.py* file.
#. *python -m unittest unit-test.py*\  and *python -m unittest
   integration-test.py* should have no failures.
#. Running \ *coverage run --source=calculator -m unittest unit-test.py;
   coverage report*\ * *\ shows 90%+ coverage..
#. Satisfy the linter such that \ *pylint calculator* gives no errors
   and *flake8 calculator* gives no errors. You can achieve this by some
   combination of editing your code and editing the \ *.pylintrc* file
   to ignore certain violations

Submitting Your Work 
=====================

Put the file(s) (ex: a\_new\_file.py) in your student directory in a new
subdirectory named for this lesson, and add it to your clone early (git
add a\_new\_file.py). Make frequent commits with good, clear messages
about what you're doing and why.

When you're done and ready for the instructors to review your work, push
your changes to your GitHub fork (git push) and then go to the GitHub
website and make a pull request. Copy the link to the pull request.

Click the *Submit Assignment* button in the upper right.

**Part 1: File(s)**

Use the \ *Choose File* button to find and select the saved .py file or,
if there are multiple files for the assignment, the .zip file.

**Part 2: GitHub Link**

Paste the GitHub link to the pull request in the comments area.

Click the \ *Submit Assignment* button.
