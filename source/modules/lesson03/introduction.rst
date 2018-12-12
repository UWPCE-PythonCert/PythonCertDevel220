############
Introduction
############

Introduction
============

In this lesson we are going to look at how to use a relational database
with Python. Using relational databases is a massive subject in its own
right, but we are going to concentrate on how to use these technologies
simply and effectively.

What we learn here will be a foundation on which you can build as your
database needs increase in volume and complexity.

Learning Objectives
===================

Upon successful completion of this lesson, you will be able to:

-  Apply data definition techniques to help assure the quality of the
   data your Python programs use.
-  Store and retrieve single and multiple sets of records in a database
   from your Python programs so that you can leverage data management
   services from a database.
-  Use simple techniques to help model data correctly in a relational
   database, and recognize the trade-offs between different options for
   this. 

New Words, Concepts, and Tools
==============================

-  We are going to learn about relational databases, data definition and
   management, and SQL. We will cover object relational mapping and
   relational database design, but all aligned to simplicity of use with
   Python. 

Required Reading
================

-  Relational database
   `concepts <https://www.tutorialspoint.com/sql/sql-rdbms-concepts.htm>`__.
-  The
   Peewee \ `Quickstart <http://docs.peewee-orm.com/en/latest/peewee/quickstart.html>`__.
-  Query \ `examples <http://docs.peewee-orm.com/en/latest/peewee/query_examples.html>`__.
-  Peewee
   `models <http://docs.peewee-orm.com/en/latest/peewee/models.html>`__.

Optional Reading
================
RDBMS
=====

-  https://docs.python.org/2/library/sqlite3.html
-  https://medium.com/analytics-vidhya/programming-with-databases-in-python-using-sqlite-4cecbef51ab9
-  https://www.pythonlearn.com/html-008/cfbook015.html

-  How to
   `interact <http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html>`__
   with sqlite from Python (does not use Peewee)
-  How to interact with
   `PostgreSQL <http://www.postgresqltutorial.com/postgresql-python/>`__
   from Python.
-  A great reference book for SQL that shows details of SQL for several
   databases is "`SQL in a
   Nutshell <http://shop.oreilly.com/product/9780596518851.do>`__: A
   Desktop Quick Reference Guide"
-  If you really want to understand the details of SQL, then this is an
   excellent book: "`Joe Celko's SQL Programming
   Style <https://www.amazon.com/Celkos-Programming-Kaufmann-Management-Systems/dp/0120887975/ref=mt_paperback?_encoding=UTF8&me=&dpID=51KBLQqsLxL&preST=_SX218_BO1,204,203,200_QL40_&dpSrc=detail>`__
   (The Morgan Kaufmann Series in Data Management Systems)"

-  Data model design is a complex topic that requires lots of knowledge.
   If you do a lot of database work then the three books in the series
   "The Data Model Resource Book" (Vol.
   `1 <https://www.wiley.com/en-us/The+Data+Model+Resource+Book%2C+Volume+1%3A+A+Library+of+Universal+Data+Models+for+All+Enterprises%2C+Revised+Edition-p-9780471380238>`__,
   `2 <https://www.wiley.com/en-us/The+Data+Model+Resource+Book%2C+Volume+2%3A+A+Library+of+Universal+Data+Models+by+Industry+Types%2C+Revised+Edition-p-9780471353485>`__
   and
   `3 <https://www.wiley.com/en-us/The+Data+Model+Resource+Book%3A+Volume+3%3A+Universal+Patterns+for+Data+Modeling-p-9781118080832>`__)
   are invaluable (the links are the numbers).

` <https://github.com/coleifer/peewee/blob/master/docs/peewee/database.rst>`__
