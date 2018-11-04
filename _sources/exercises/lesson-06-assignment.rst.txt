================================
Assignment: Lesson 06 Assignment
================================

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

Instructions
============

Your assignment is to program, test, lint, and flake a "water
regulation" module. Begin by finding the water-regulation directory in
the course repository. The README in that directory may be helpful.

Your goals:
-----------

Note that all of the command examples below should be run from the
project root which contains the directories waterregulation, sensor, and
pump.

#. Complete the \ *TODO*\ s
   in \ *waterregulation/controller.py*\  and \ *waterregulation/decider.py*.
#. Complete the \ *TODO*\ s
   in \ *waterregulation/test.py*\  and \ *waterregulation/integrationtest.py*.
   A single integration test may be sufficient. However, your unit tests
   in \ *test.py*\  should include at least one test for each specified
   behavior.
#. *python -m unittest waterregulation/test.py*\  and \ *python -m
   unittest waterregulation/integrationtest.py* should have no failures.
#. Running \ *coverage run
   --source=waterregulation/controller.py,waterregulation/decider.py -m
   unittest waterregulation/test.py; coverage report*\ * *\ shows 90%+
   coverage..
#. Satisfy the linter such that \ *pylint waterregulation* gives no
   errors and and \ *flake8 waterregulation* gives no errors. You may
   have to add docstrings to your test files.

 

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
