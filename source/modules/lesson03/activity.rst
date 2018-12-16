########
Activity
########

Warm up for the assignment
==========================

Before we launch into the assignment, let's be sure that you have
everything you need to get started. We'll enhance the modules from the
video along the way.

Preparing
=========

Be sure to

.. code:: bash

    pip install peewee

first. Also, be sure that  

.. code:: bash

    sqlite3 -version

returns the sqlite3 version number, indicating it is installed. It
should be, as it's bundled with Python 3. If you are using Windows and you
get an error revisit the lesson content for instructions on how to install
sqlite.

Clone the lesson 3 code repo at 

.. TODO: Missing link for lesson 3 code repo


although you should already have that from earlier in this lesson.

Make sure everything runs before proceeding to the next step.

Let's add a department
======================

We have details of Persons. We have details of Jobs. Now we need to
track in which Department a Person held a Job. For a Department, we need
to know it's department number, which is 4 characters long and starts
with a letter. We need to know the department name (30 characters), and
the name of the department manager (30 characters). We also need to know
the duration in days that the job was held. Think about this last one
carefully.

Make the necessary changes, annotating the code with log statements to
explain what's going on. Also, draw a digram to help think through how
you will incorporate Department into the programs.

Finally, produce a list using pretty print that shows all of the
departments a person worked in for every job they ever had. 

Prepare the results, and prepare to demo them!
