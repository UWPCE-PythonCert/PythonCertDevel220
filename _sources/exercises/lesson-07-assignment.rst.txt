================================
Assignment: Lesson 07 Assignment
================================

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

Instructions
============

**Goal:**

Redesign the object oriented mailroom program from class one using
Peewee classes so that the data is persisted in sqlite. The approach you
used in the OO exercise will naturally lend itself to this.

**Suggestions**

You will need ways to add, update and delete data. Update and delete
will mean that you need to find the data to update / delete. Perhaps you
can do this by allowing a search first, and then selecting the
particular instance to delete.

Remember that you need to read from the database, rather than relying on
data held in variables when your program is running. To show you
understand how this works, run the donor report from a separate program
that read the database.

Generally, be sure to adapt the exception handling so that it helps
identify any database errors, and consider how you may need to adapt
your tests.

Be sure to give a lot of thought to what you should use as the primary
key for your Peewee classes. In doing this, just consider data items
that are unique in the context of the mailroom application. If you have
to resort to generated keys, be sure to note why in the applicable
docstring. And talking of which, be sure to define all your classes, as
you learned in the videos.

The example programs for the videos will be a good starting point for
reminders of syntax, but remember that the primary determinate of the
structure of your solution will be a good object oriented Python
application. The fact that it will now be persistent should not make too
,much difference. 

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
