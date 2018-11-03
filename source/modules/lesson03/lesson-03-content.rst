=================
Lesson 03 Content
=================

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

Here we are going to cover the background to why we use databases, and
set the stage for later, when we will start to develop a Python database
application.

You will probably wish to clone the repository you can find on
`GitHub <https://github.com/milesak60/RDBMS>`__. For this first video,
the files are in the "stuff" directory. These are the files we refer to,
and they are included here, below the video:

|v1files.png|

Note: If you are using Windows, you will need to install sqlite. Here's how:


On Windows, unlike Linux and Mac, sqlite is not installed with Python. As
always, there are many ways to install sqlite, but the easiest way is with pip.
Open a command prompt (press the Windows key, type cmd and press enter).

At the command prompt enter the following command:

.. code:: bash
    pip install pysqlite3

Now, type the following command:

.. code:: bash
    sqlite3

And you should see the sqlite prompt. Type the quit command to return to the command prompt:

.. code:: bash
    .quit


{{VIDEO HERE}} 

People file:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    """
    write a csv file
    data is "anonymous" (no schema)

    Creates a file that looks like this:

    John,502-77-3056,2/27/1985,117.45

    """

    import csv

    peopledata = ['John', '502-77-3056', '2/27/1985', 117.45]

    with open('simple_data_write.csv', 'w') as people:
        peoplewriter = csv.writer(people)
        peoplewriter.writerow(peopledata)

.. raw:: html

   </div>

Schema file:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    'Person Name','SSN','BirthDate','Account Balance'
    'John','502-77-3056','2/27/1985','117.45'

.. raw:: html

   </div>

 

We have covered the basis of data definition, and why it is important.
We now know what a schema is and why it is important. Now we can start
to write a Python program that uses a database.


Be sure you cloned the repository we mentioned prior to video 1
from \ `GitHub <https://github.com/milesak60/RDBMS>`__\ . In this video
we will be using the modules in the "src" directory We start
with \ `v00\_personjob\_model.py <https://github.com/milesak60/RDBMS/blob/master/src/v00_personjob_model.py>`__. 

Key fragments are included here too, below the video.

Tutorial Videos:
================

Using the Model, Using the Person Class, Using the Job Class
============================================================

{{VIDEO HERE}}

 Here is the model code:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

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

.. raw:: html

   </div>

 

Now we have looked at the model, lets look at how we create, read, and
delete data from the database, using the Person class. Here we use the
following
code: `v3\_p1\_populate\_db.py <https://github.com/milesak60/RDBMS/blob/master/src/v3_p1_populate_db.py>`__,
then \ `v3\_p1\_populate\_db.py <https://github.com/milesak60/RDBMS/blob/master/src/v3_p1_populate_db.py>`__ and
finally \ `v3\_p3\_add\_and\_delete.py <https://github.com/milesak60/RDBMS/blob/master/src/v3_p3_add_and_delete.py>`__.

{{VIDEO HERE}}

 

Working with one class is not typical. Usually we will have several.
We'll illustrate this by working with the Job class. He we will use all
the Python modules for the repository that start with v4:

{{VIDEO HERE}}

 

Now we are going to learn about the best way to design the data in our
database.  We will use the digram in the "stuff" directory, which is
also included below, along with the SQL code:

 

Behind the scenes
=================

{{VIDEO HERE}}

 

Database diagram:

 |DatabaseDiagram.jpeg| 

Code samples from the video:

SQL statement

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    select * from person ;

.. raw:: html

   </div>

Start sqlite3 database (from the command line):

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    sqlite3 personjob.db

.. raw:: html

   </div>

The sqlite> prompt indicates we are ready to enter sqlite commands.

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    sqlite> .tables
    job person personnumkey

.. raw:: html

   </div>

  Here is how sqlite sees the schema:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    sqlite> .schema

    CREATE TABLE IF NOT EXISTS "person" ("person_name" VARCHAR(30) NOT NULL PRIMARY KEY, "lives_in_town" VARCHAR(40) NOT NULL, "nickname" VARCHAR(20));

    CREATE TABLE IF NOT EXISTS "job" ("job_name" VARCHAR(30) NOT NULL PRIMARY KEY, "start_date" DATE NOT NULL, "end_date" DATE NOT NULL, "salary" DECIMAL(7, 2) NOT NULL, "person_employed_id" VARCHAR(30) NOT NULL, FOREIGN KEY ("person_employed_id") REFERENCES "person" ("person_name"));

    CREATE INDEX "job_person_employed_id" ON "job" ("person_employed_id");

    CREATE TABLE IF NOT EXISTS "personnumkey" ("id" INTEGER NOT NULL PRIMARY KEY, "person_name" VARCHAR(30) NOT NULL, "lives_in_town" VARCHAR(40) NOT NULL, "nickname" VARCHAR(20));

.. raw:: html

   </div>

 

 

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    sqlite> .mode column
    sqlite> .width 15 15 15 15 15
    sqlite> .headers on

.. raw:: html

   </div>

 

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    sqlite> select * from person;
    sqlite> select * from job;

.. raw:: html

   </div>

Enter .quit to leave sqlite.

Lesson Summary
==============

In this lesson we have learned about how we define, store and retrieve
data in a relational database using Python, Peewee and sqlite.

 

Conclusion
----------

{{VIDEO HERE}}

 ` <https://github.com/coleifer/peewee/blob/master/docs/peewee/database.rst>`__

 

.. |v1files.png| image:: %24IMS-CC-FILEBASE%24/v1files.png?canvas_download=1
.. |DatabaseDiagram.jpeg| image:: %24IMS-CC-FILEBASE%24/Lesson%207%20scripts/DatabaseDiagram.jpeg?canvas_download=1
