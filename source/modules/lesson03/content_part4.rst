##############
Part 4: Design
##############

Now we are going to learn about the best way to design the data in our
database.  We will use the digram in the "stuff" directory, which is
also included below, along with the SQL code:
 

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
