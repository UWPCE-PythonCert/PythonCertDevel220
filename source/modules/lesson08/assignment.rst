##########
Assignment
##########

HP Norton has been using comma-separated files (.CSV extension) to keep track of which furniture they have rented out to which
customer. This is currently generated from a spreadsheet called inventory.

Your Project Manager wants you to get the spreadsheet program out
of the equation by creating a Python function that will create and update an inventory CSV file with all the information that is currently
entered through the spreadsheet program. You have decided to use closures and currying to develop the necessary functionality. 

You will also develop functionality to
to bulk-process a list of items, coming from a separate CSV file, that have been rented out to a single customer. This functionality will thus update the inventory list by adding that customer's rentals.

To summarize:
1. You will create a program to initially create, and subsequently update, a CSV file that lists which furniture is rented to which customer (to replace use of the spreadsheet mentioned above).
2. You will create additionally functionality that will load individual customers rentals.


Here is what you need to do:
----------------------------

#. Create a python module called *inventory.py*, to replace the existing spreadsheet. This file will contain all the functions used for this assignment.
#. Create a function called *add_furniture* that takes the following input parameters:
    - *invoice_file*
    - *customer_name*
    - *item_code*
    - *item_description*
    - *item_monthly_price*

    This function will create *invoice_file* (to replace the spreadsheet's data) if it doesn't exist or append a new line to it if it does. After adding a few items to the
    same file, the file created by *add_furniture* should look something like this:

    ::

        Elisa Miles,LR04,Leather Sofa,25.00
        Edward Data,KT78,Kitchen Table,10.00
        Alex Gonzales,BR02,Queen Mattress,17.00


    You can create a starter file in this format for testing, or you can have your add function do it.

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
You can create the *test_items.csv* file for testing of your *single_customer* function. 
The layout of the csv will be something like this:

    ::

        LR04,Leather Sofa,25.00
        KT78,Kitchen Table,10.00
        BR02,Queen Mattress,17.00



*add_furniture* can be tested manually,
as shown below.

The idea is for the single_customer() function to return a new function (with a fixed customer name and destination inventory file) that will add all items in a source file to the overall inventory under a single customer name. Internally, single_customer() should leverage add_furniture() by fixing the first two parameters.


.. code-block:: python

    from inventory import *
    add_furniture("rented_items.csv", "Elisa Miles", "LR04", "Leather Sofa", 25)
    add_furniture("rented_items.csv", "Edward Data", "KT78", "Kitchen Table", 10)
    add_furniture("rented_items.csv", "Alex Gonzales", "Queen Mattress", 17)
    create_invoice = single_customer("Susan Wong", "rented_items.csv")
    create_invoice("test_items.csv")

So, using create_invoice() will, in this case, add all items in test_items.csv to rented_items.csv under the name “Susan Wong”.

Submission
----------

Your submission should include a single file, *inventory.py* with two functions, *add_furniture* and *single_customer*. You can
include other functions but all testing for the purpose of grading your assignment will use only those two functions.
