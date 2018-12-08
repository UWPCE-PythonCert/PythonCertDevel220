=====================
Lesson 5 : Assignment
=====================

As mentioned before, HP Norton has been using a mix of different file formats
to keep track of their business. One of those formats is called *comma-separated file*
which can be distinguished by the *.csv* extension. 

This week, you have been assigned to work on a prototype migration of product data from a sample csv
file into MongoDB. You will use the MongoDB API while exploiting mongo's ability to
allow the Python module, not the database, to specify the schema for the data to
be stored.

You implementation should address the following requirements:

#. As a HP Norton *customer* I want to see a list of all products available for
   rent so that I can make a rental choice.
#. As a HP Norton *salesperson* I want to see a list of all of the different
   products, showing product ID, description, product type and quantity available.
#. As a HP Norton salesperson I want to see a list of the names and contact
   details (address, phone number and email) of all customers who have rented a certain product.

Here is what you need to do:
----------------------------

#. Create a product database with attributes that reflect the contents of the
   csv file.
#. Import all data in the csv files into your MongoDB implementation.
#. Write queries to retrieve the product data.
#. Write a query to integrate customer and product data.


Other requirements:
-------------------
- Your code should not trigger any warnings or errors from Pylint.
- You can have a specific field to indicate if a product is available, however, a *quantity_available* of 0 is understood as "not available".

Testing
-------
In order for your code to be evaluated, you need to create a file called *database.py* with the following functions:

- *import_data(directory_name, product_file, customer_file, rentals_file)*: This function takes a directory name three csv files as input, one with product data, one with customer data and the third one with rentals data and creates and populates a new MongoDB database with the these data. It returns 2 tuples: the first with a record count of the number of
products, customers and rentals added (in that order), the second with a count of any errors that occured, in
the same order. 

.. todo::
    create product, customer, rental files for l5 Assignment

- *show_available_products()*: Returns a Python dictionary of products listed as *available* with the following fields:
    - product_id.
    - description.
    - product_type.
    - quantity_available.

    For example:

    ..

    {'prd001':{'description':'60-inch TV stand','product_type':'livingroom','quantity_available':'3'},'prd002':{'description':'L-shaped sofa','product_type':'livingroom','quantity_available':'1'}}

- *show_rentals(product_id)*: Returns a Python dictionary with the following user information from users that have rented products matching *product_id*: 
    - user_id.
    - name.
    - address.
    - phone_number.
    - email.

    For example:

    ..

    {'user001':{'name':'Elisa Miles','address':'4490 Union Street','phone_number':'206-922-0882','email':'elisa.miles@yahoo.com'},'user002':{'name':'Maya Data','address':'4936 Elliot Avenue','phone_number':'206-777-1927','email':'mdata@uw.edu'}}


Submission
----------

Your submission should include all files necessary to create and access your database, as well as *test_database.py* in order to test your submission.

