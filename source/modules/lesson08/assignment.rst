=====================
Lesson 8 : Assignment
=====================

Norton Furniture has been using comma-separated files (.CSV extension) to keep track of which furniture they have rented out to which
customer. This currently requires them to use a spreadsheet program. Your Project Manager wants you to get the spreadsheet program out
of the equation by creating a Python function that will create and update an inventory CSV file with all the information that is currently
entered through the spreadsheet program. Additionally, you will need to, using closures and currying, add the necessary functionality
to bulk-process a list of items, coming from another CSV file, that have been rented out to a single customer. 


Here is what you need to do:
----------------------------

#. Create a python module called *inventory.py*. This file will contain all the functions used for this assignment.
#. Create a function called *add_furniture* that takes the following input parameters:
    - *invoice_file*
    - *customer_name*
    - *item_code*
    - *item_description*
    - *item_monthly_price*

    This function will create *invoice_file* if it doesn't exist or append a new line to it if it does. After adding a few items to the
    same file, the file created by *add_furniture* should look like this:

    ::

        Elisa Miles,LR04,Leather Sofa,25.00
        Edward Data,KT78,Kitchen Table,10.00
        Alex Gonzales,BR02,Queen Matress,17.00


#. Create a function called *single_customer*:
    - Input parameters: *customer_name*, *invoice_file*.
    - Output: Returns a function that takes one parameter, *rental_items*.
    
    *single_customer* needs to use *functools.partial* and closures, in order to return a function that will iterate through 
    *rental_items* and add each item to *invoice_file*. 

Other requirements:
-------------------
- Your code should not trigger any warnings or errors from Pylint.

Testing
-------
You can use the included *test_items.csv* file for testing of your *single_customer* function. *add_furniture* can be tested manually,
as shown below.

.. code-block:: python

    from inventory import *
    add_furniture("invoice01.csv", "Elisa Miles", "LR04", "Leather Sofa", 25)
    add_furniture("invoice01.csv", "Edward Data", "KT78", "Kitchen Table", 10)
    add_furniture("invoice01.csv", "Alex Gonzales", "Queen Matress", 17)   

    create_invoice = single_customer("Susan Wong", "SW_invoice.csv")
    create_invoice("test_items.csv")

Submission
----------

Your submission should include a single file, *inventory.py* with two functions, *add_furniture* and *single_customer*. You can
include other functions but all testing for the purpose of grading your assignment will use only those two functions.


