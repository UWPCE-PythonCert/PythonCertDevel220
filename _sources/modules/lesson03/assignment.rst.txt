=====================
Lesson 3 : Assignment
=====================

As part of the Norton Furniture project, we are going to store customer data from HP
Norton in a relational database (sqlite3). We are also going to amend our
functional tests (or create new ones) so that we can verify the customer
data meets HP Norton's needs.

You should address the following general requirements, specific to three user types:

#. As a *salesperson* at HP Norton I need to be able to store details of
   customers so that I can manage how I contact them to sell furniture.
#. As an *accountant* at HP Norton I need to be able to store and retrieve
   customers credit limits.
#. As a *manager* at HP Norton I need to be able to produce monthly counts of
   the total number of active customers so that I can assess if the business is
   growing or shrinking.

Here is what you need to do:
----------------------------

Note:
   We are just developing the backend here. Imagine your module(s) will be called
   from a web app (which is outside the scope of this project).

#. Create a customer model and database that can be used at HPNorton.
    - At a minimum, the following information needs to be stored:
        - Customer ID.
        - Name.
        - Lastname.
        - Home address.
        - Phone number.
        - Email address.
        - Status (active or inactive customer).
        - Credit limit.
#. Create a file called *basic_operations.py*.
    - This file will need to have the following functions:
        - *add_customer(customer_id, name, lastname, home_address, phone_number, email_address, status, credit_limit)*: This function will add a new customer to the sqlite3 database.
        - *search_customer(customer_id)*: This function will return a dictionary object with name, lastname, email address and phone number of a customer or an empty dictionary object if no customer was found.
        - *delete_customer(customer_id)*: This function will delete a customer from the sqlite3 database.
        - *update_customer_credit(customer_id, credit_limit)*: This function will search an existing customer by *customer_id* and update their credit limit or raise an exception if the customer does not exist.
        - *list_active_customers()*: This function will return an integer with the number of customers whose status is currently active.
    - Note: You can have other functions and code as required, but the five functions oultined above should be present and using the same amount of parameters. This is important, as those functions are how your code gets integrated into other sections of the project (such as the Web frontend).
#. Create some functional and unit tests for the model.
#. Develop functionality to deliver the requirements listed above.
#. Develop tests, and show some tests passing. Show other tests failing.

Other requirements:
-------------------
- Your code should not trigger any warnings or errors from Pylint.

Testing
-------
- Make sure your tests run as expected.

Submission
----------
- You will need to submit *basic_operations.py* plus any test files you develop.

Tips
----
- Remember to think about system features, not web pages or the UI.
- Tests first!
- Be creative! Think about what else the furniture store might need regarding customer information.
- Be careful when selecting your primary keys, many people can have the same name and lastname!

