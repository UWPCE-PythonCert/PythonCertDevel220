##########
Assignment
##########

In this lesson's assignment we are going to apply language features 
like decorators, context managers and recursion that can
help to build expressive programs that are easy to understand.

Here is what you need to do:
----------------------------

#. Revisit your logging assignment from lesson 2. We are going to make logging 
   selective, by using decorators.

   Add decorator(s) to introduce conditional logging so that a single
   command line variable can turn logging on or off for decorated classes or functions.
#. Change the lesson 5 assignment to Write a context manager to access MongoDB. 
   There is already
   an example in lesson 5, but build on this example. Try to add useful
   features based on your experience of the Python techniques you have learned.
#. HP Norton keeps pictures of all their furniture in jpg files that are stored 
   on their file server. They have a very crude program that starts by 
   discovering all directories on the server and then looking in each of those
   for the jpg files. They have discovered a problem, though: jpg files are not 
   found when they are stored in directories that are more than one level deep from the 
   root directory.
   Your job is to write a jpg discovery program in Python, using recursion,  
   that works 
   from a named parent directory provided on the command line.
   The program will take the parent directory as input.
   As output, it will return a list of lists structured like this:
   ["full/path/to/files", ["file1.jpg", "file2.jpg",...], "another/path",[], etc]
   The program must be called jpgdiscover.py

Other requirements:
-------------------
- Your code should not trigger any warnings or errors from Pylint.
