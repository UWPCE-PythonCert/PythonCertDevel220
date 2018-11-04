======================
Lesson 05 Introduction
======================

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

Introduction
============

{{video 1}}

.. code-block:: python
   class BaseModel(Model):
       class Meta:
           database = database

   class Person(BaseModel):
       """
         This class defines Person, which maintains details of someone
         for whom we want to research career to date.
       """

       person_name = CharField(primary_key = True, max_length = 30)
       lives_in_town = CharField(max_length = 40)
       nickname = CharField(max_length = 20, null = True)

   class Job(BaseModel):
       """
         This class defines Job, which maintains details of past Jobs
         held by a Person.
       """
       job_name = CharField(primary_key = True, max_length = 30)
       start_date = DateField(formats = 'YYYY-MM-DD')
       end_date = DateField(formats = 'YYYY-MM-DD')
       salary = DecimalField(max_digits = 7, decimal_places = 2)
       person_employed = ForeignKeyField(Person, related_name='was_filled_by', null = False)
   new_person = Person.create(
      person_name = 'Fred',
      lives_in_town = 'Seattle',
      nickname = 'Fearless')
       new_person.save()

   aperson = Person.get(Person.person_name == 'Fred')

.. todo::
  Add git links for rdbms code (Andy)

Learning Objectives
===================

Upon successful completion of this lesson, you will be able to:

-  Augment the Python modules you develop by consuming APIs.
-  Discover the details of APIs and how to apply them in Python
-  Use the API of a NoSQL database to store and retrieve data
-  Identify when to use a NoSQL database instead of a relaional database

New Words, Concepts, and Tools
==============================

-  APIs, NoSQL, MongoDB.
-  Using document databases.
-  Using third party documentation

Required Reading
================
.. todo::
   Verify all required and optional reading links for lesson 5 mongo API (Andy)

-  `Background <https://www.fullstackpython.com/no-sql-datastore.html>`__
   on databases
-  `Mongodb <https://realpython.com/blog/python/introduction-to-mongodb-and-python/>`__
-  http://wiki.python.org/moin/PersistenceTools 

Optional Reading
================

-  Excellent `guide <http://nosql-database.org>`__ for future reference
-  A
   `list <http://bigdata-madesimple.com/a-deep-dive-into-nosql-a-complete-list-of-nosql-databases/>`__ of
   databases and database characteristics
-  `Simple <https://docs.python.org/3/library/persistence.html>`__
   persistence.
-  https://realpython.com/introduction-to-mongodb-and-python/
-  https://www.bogotobogo.com/python/MongoDB_PyMongo/python_MongoDB_pyMongo_tutorial_installing.php
-  https://gearheart.io/blog/how-do-you-use-mongodb-with-python/


