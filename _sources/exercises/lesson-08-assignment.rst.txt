================================
Assignment: Lesson 08 Assignment
================================

.. raw:: html

   <div id="menuheading">

.. rubric:: Non-Relational Databases
   :name: non-relational-databases
   :class: caH2

.. raw:: html

   <div id="navbar" class="caNav grid-row around-md clearunderlinestyle"
   role="navigation">

`Introduction <%24WIKI_REFERENCE%24/pages/lesson-08-introduction>`__ \|
`Content <%24WIKI_REFERENCE%24/pages/lesson-08-content>`__ \|
`Quiz <%24CANVAS_OBJECT_REFERENCE%24/assignments/ibe91f0cc09bbecc290b2f8a417d1cf9d>`__ \|
`Activity <%24CANVAS_OBJECT_REFERENCE%24/assignments/i85a67f5992214211e1422f618383b5da>`__
\|
`Assignment <%24CANVAS_OBJECT_REFERENCE%24/assignments/i10247fb9255383751f912e986d6fd289>`__
\| `Code
Talk <%24CANVAS_OBJECT_REFERENCE%24/discussion_topics/ie7fce6e6c072d03b675b6796a45e3c25>`__

.. raw:: html

   </div>

.. raw:: html

   </div>

Instructions
============

Part 1: MONGODB
===============

**Goal:**

As with the RDBMS assignment, refactor the object oriented mailroom
program so that the data is persisted in mongodb. The approach you used
in the OO exercise will naturally lend itself to this.

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
,much difference!

Part 2: Redis
=============

**Goal:**

Refactor the mailroom program so that you can lookup data for validation
purposes using Redis. You will need to populate a cache, and show how
you use the Redis cache to read the data.

**Suggestions**
---------------

Examples of the lookup data you may use include the email addresses of
donors. What else can you think of?  Try to come up with 2 or 3 more
examples.

 

Part 3: Neo4j
=============

**Goal:**

And finally, refactor the mailroom program so that the data is persisted
in Neo4J. 

Be sure to think about how you can compare and contrast the ease of
development, and the value delivered by each database. Submit
some comments to reflect this thinking with your assignment.

Submitting Your Work 
---------------------

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
