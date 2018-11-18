=====================
Lesson 5 : Assignment
=====================

.. todo::
    Make this assignment consistent with the case study.


As mentioned before, HP Norton has been using a mix of different of file formats
to keep track of their business. One of those formats is called *comma-separated file*
which can be distinguished by the *.csv* extension. 

This week, you will work on a prototype migration of product data from a sample csv
file into MongoDB. You will use the MongoDB API while exploiting mongo's ability to
allow the Python module, not the database, to specify the schema for the data to
be stored.

You implementation should address the following requirements:
#.  As a HP Norton *customer* I want to see a list of all products available for
    rent so that I can make a rental choice.
#. As a HP Norton *salesperson* I want to see a list of all of the different
   types of a product, showing a product ID, name, product type and
   description.
#. As a HP Norton salesperson I want to see a list of the names and contact
   details (address, phone number and email) of all customers who have rented products, as well as the name, description
   and type of product that they rented.

.. todo::
    Create product CSV file (Andy)


Here is what you need to do:
----------------------------

#. Create a product database with attributes that reflect the content ofthe
   csv file.
#. All data in the csv file needs to be incorporated into your MongoDB implementation.
#. Make sure you add a field to indicate if an item is available (i.e., not currently rented out).
#. Write queries to retrieve the product data
#. Write a query to integrate customer and product data
#. Update tests to show the data is being maintained correctly in the database.

.. todo::
    Add function stubs for automated testing (Luis)


