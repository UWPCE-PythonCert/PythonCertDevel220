##########
Assignment
##########

Welcome to the HP Norton Project! The first thing our development team is trying to accomplish is to improve some of Norton Furniture's existing code. Your first assignment will
be to look at a prototype inventory management system they had been working on internally, align the code to the best practices outlined in PEP8 and implement both unit and integration testing.

Here is what you need to do:
----------------------------

#. Download the code for the inventory management system and place it in a folder called *inventory_management*.
#. Evaluate the code using Pylint by running the following command from *outside* of the *inventory_management* folder. Use this command:

    .. code-block:: python

        python -m pylint ./inventory_management

#. Fix all of the issues reported by Pylint up to the point where Pylint gives the code a grade of 10.
#. Create a file called *test_unit.py* that will be outside of the *inventory_management* directory. You will need to add unit tests for all classes in the inventory management system to this file.
#. Run coverage analysis on the *inventory_management* code using *test_unit.py*. Coverage must be 90% or higher for each individual file. Use the following commands.
    - Coverage run:
        .. code-block:: python

            python -m coverage run --source=inventory_management -m unittest test_unit.py

    - Coverage report:
        .. code-block:: python

            python -m coverage report

        Update *test_unit.py* as required to attain 90% coverage.

#. Create a file called *test_integration.py*.

Other requirements:
-------------------
- For Pylint, remember to use the standardized *pylintrc* file provided for the class.
- Although already stated, both of your unit and integration tests files should be placed outside of the *inventory_management* folder.
- Remember that the 90% coverage requirement applies to each individual file in the project, not overall coverage.
- You cannot modify the *market_prices* module. That means you will need to use *Mock* or *MagicMock* to simulate values returned by it.
- When coding unit testing for *main.py*, it has to be in isolation from the project's classes, so will need to use *Mock* or *MagicMock* to simulate their return values.

Testing
-------

Passing pylint, unit and integration tests and coverage analysis should be enough to give you confidence that your code will be accepted by the Project Manager.

Submission
----------
You will need to submit the *inventory_management* folder will all your improvements, as well as the *test_unit.py* and *test_integration.py* files.
