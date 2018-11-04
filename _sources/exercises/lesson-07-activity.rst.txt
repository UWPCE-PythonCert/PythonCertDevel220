==============================
Assignment: Lesson 07 Activity
==============================

.. raw:: html

   <div id="menuheading">

.. rubric:: Relational Databases
   :name: relational-databases
   :class: caH2

.. raw:: html

   <div id="navbar" class="caNav grid-row around-md clearunderlinestyle"
   role="navigation">

`Introduction <%24WIKI_REFERENCE%24/pages/lesson-07-introduction>`__ \|
`Content <%24WIKI_REFERENCE%24/pages/lesson-07-content>`__ \|
`Quiz <%24CANVAS_OBJECT_REFERENCE%24/assignments/ie39542f4274b1ba93a37a8b75f9011ef>`__ \|
`Activity <%24CANVAS_OBJECT_REFERENCE%24/assignments/idd62db3e72b3f43a8a85b8633adf4461>`__
\|
`Assignment <%24CANVAS_OBJECT_REFERENCE%24/assignments/i0296493f505e23900bda7d7da2d96776>`__
\| `Code
Talk <%24CANVAS_OBJECT_REFERENCE%24/discussion_topics/i5023a80264163ea8cad0130f8d2b92b6>`__

.. raw:: html

   </div>

.. raw:: html

   </div>

Warm up for the assignment
==========================

Before we launch into the assignment, let's be sure that you have
everything you need to get started. We'll enhance the modules from the
video along the way.

Preparing
=========

Be sure to

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    pip install peewee

.. raw:: html

   </div>

 first.

Also, be sure that  

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    sqlite3 -version

.. raw:: html

   </div>

returns the sqlite3 version number, indicating it is installed. It
should be, as it's bundled with Python 3.

Clone the repo at 

::

    git@github.com:milesak60/RDBMS.git

although you should already have that from earlier in this lesson.

Make sure everything runs before proceeding to the next step.

Let's add a department
======================

We have details of Persons. We have details of Jobs. Now we need to
track in which Department a Person held a Job. For a Department, we need
to know it's department number, which is 4 characters long and start
with a letter. We need to know the department name (30 characters), and
the name of the department manager (30 characters). We also need to know
the duration in days that the job was held. Think about this last one
carefully.

Make the necessary changes, annotating the code with log statements to
explain what's going on. Also, draw a digram to help think through how
you will incorporate Department into the programs.

Finally, produce a list using pretty print that shows all of the
departments a person worked in for every job they ever had. 

Instructions
============

Once you've completed the activity from the lesson content, commit your
changes and submit:

-  a link to your repository on GitHub
-  the relevant .py file(s)

We'll be grading this activity purely on the percentage of included
tests that pass.

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
