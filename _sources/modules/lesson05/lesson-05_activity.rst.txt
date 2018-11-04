==============================
Assignment: Lesson 05 Activity
==============================

.. todo:: rework activity lesson 5

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

 nosql exercise
===============

Let's now get our "hands dirty" with some Python code. Start by cloning
the repo at:

https://github.com/milesak60/nosql

| 
| You will need to install three modules for this program to run
  successfully. Here's a list:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    pip install neo4j-driver

    pip install pymongo

    pip install redis

.. raw:: html

   </div>

This program uses all three nosql databases we have looked at so far, as
well as Pickle, Shelve, CSV and JSON files. The code should look very
familiar, but not necessarily the way it is structured. It explains
itself with logging messages at all appropriate spots.

The main module is leanrnosql.py

It runs examples for each of the above in turn. For mongodb it sets up
some data first.

Each of the database specific scripts deals with getting the relevant
login information prior to running the example code.

There is also some dictionary based logger setup, the intent of which is
to drown some of the noisy logging messages that some of the database
drivers themselves generate.

Take a look at the flow of the code and get a good understanding of the
structure and what is going on. Try changing the logger values and
seeing the affect it has on the logging messages.

When you are familiar with the code, try the following exercises:

mongodb
-------

Add some extra furniture items for mongodb. And while you're doing that,
separate the product field in to 2 fields; one called product type, one
called color. Start by amending the data, then change the Mongodb
program to store and retrieve using these new values.

Next, write a mongodb query to retrieve and print just the red products,
an the just the couches. 

Redis
-----

Add some customer data to the cache, Have Redis store a customer name,
telephone and zip for 6 or so customers. Then show how you can retrieve
a zip code, and then a phone number, for a known customer.

Neo4J
-----

Add some new people to the database. Then add some colors. Create
associations between people and their favorite colors (they can have
more than one). Then list all of the people who have each color as their
favorite. Can you also list all of the everyones favorite colors?

Simple persistence and serialization
------------------------------------

Pick one of the 4 formats only. Create some data (at least 10 rows with
about 5 fields in each). Show how you can read and write data in that
format. For an extra assignment, write a program that reads form one
format and converts to another.


