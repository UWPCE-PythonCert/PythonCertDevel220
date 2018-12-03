======================
Lesson 10 : Assignment
======================

Here is what you need to do:
============================

HP Norton has experienced explosive growth as a result of the excellent
system that has been developed for the company. However, that has brought
its own problems. Periodically the system is running slow. Initial
investigations have have not been able to identify a root cause. But the
database is suspected to be a culprit (akthough whether it is customers or
products is not clear.

In order to diagnose the issues the HP Norton developer want to easily ass
some logging and timing infomration to record what the system is actually
doing and to help identify the bottlnecks. And metaprogramming seems to be a
good way to unobtrusively add this functionality to the existing applcation.

For this assigment, you will use metaprogramming to add logging and timing
information to the HP Norton application, using the code samples from
lessons 3 and 5.

Provide an elegant way to output details of what the system is doing and
the associtaed timing. Just write it to a file. DOnt bother with fancy
report formatting, although the data should be preented in such a way that
command line tools can easily view it.

.. todo::
    Lesson 10 add links to code for assignment (RDBMS and mongo)

Tips
----
- Remember to write the code from the perspective of another developer who
  will use it.
- Such a developer needs to use your fetaures transprently.
