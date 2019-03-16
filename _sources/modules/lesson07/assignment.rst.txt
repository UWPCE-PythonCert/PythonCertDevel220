##########
Assignment
##########
    
HP Norton is having success with their new computer system written in Python.
So much success, in fact, that the way they have had some of their systems
written is starting to introduce processing bottlenecks, and therefore delays for users.

In this lesson's assignment, we are going to apply techniques beyond
vertical scaling (upgrading servers) to help maximize their application performance.

You should address the following general requirements:
======================================================
#. As a user of the HP Norton systems, I need to be confident that the system will perform
   sufficiently rapidly that responses are almost instantaneous, and I am not kept waiting
   for the system to complete its processing. I feel the system now is too slow, and I want 
   to see if improvements can be made without having to upgrade our hardware.

Here is what you need to do:
============================
#. Demonstrate with real profile data the time taken to run your existing import logic from lesson 5
#. Amend the import logic so that 
   it can process the imports in parallel. Your module should launch the imports 
   simultaneously. Provide real timing data for your new approach.
#. Compare and contrast parallel vs. linear performance and recommend to management
   if a change is worthwhile.
#. To show you have thought through your design, create and provide an example of 
   where the program fails due to contention and explain why in code comments, and how
   that will be avoided when the system is running.
#. You will submit two modules: linear.py and parallel.py
#. Each module will return a list of tuples, one tuple for customer and one for products.
   Each tuple will contain 4 values: the number of records processed (int),
   the record count in the database prior to running (int), the record count after running (int),
   and the time taken to run the module (float).
#. You will also submit a text file containing your findings.


Other requirements:
-------------------
- Your code should not trigger any warnings or errors from Pylint.

Testing
-------
- Make sure your tests run as expected.

Submission
----------
- You will need to submit *linear.py*, *parallel.py*, your brief bullet point notes on 
  findings and recommendations called findings.txt, and any test files you develop.

Tips
----
- Amend some of the previously provided data to create 1,000 records.
