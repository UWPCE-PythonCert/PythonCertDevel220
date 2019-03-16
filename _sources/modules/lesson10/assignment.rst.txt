##########
Assignment
##########

Here is what you need to do:
============================

HP Norton has experienced explosive growth as a result of the excellent
system that has been developed for the company. However, that has brought
its own problems. Periodically the system is running slow. Initial
investigations have have not been able to identify a root cause. But the
database is suspected to be a culprit (although whether it is customers or
products is not clear.

In order to diagnose the issues the HP Norton developer want to easily as
some timing information to record what the system is actually
doing and to help identify the bottlenecks. And metaprogramming seems to be a
good way to unobtrusively add this functionality to the existing application.

For this assignment, you will use metaprogramming to add timing
information to the HP Norton application, using the code samples from
lesson 5.

Your program, called database.py, must output details of timing for all functions
in the program. Gather this data and write it to a file called timings.txt. The file should contain 
function name, time taken, and number of records processed.

Be sure to demonstrate how the timing changes with differing number of records
(you can copy and duplicate the data provided in the lesson 5 csv files so you
have more data to deal with. It's easy to do that. Be sure to show widely different
numbers of records). Make some notes on your conclusions.

Submission
----------
Submit your revised database.py, the output file and your conclusions.


Tips
----
- Remember to write the code from the perspective of another developer who
  will use it.
- Such a developer needs to use your features transparently.
