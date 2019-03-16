##########
Assignment
##########
    
In this lesson's assignment, we are going to apply techniques to identify the
right way to find bottlenecks in modules. We will use an evidence
based approach to implement the right improvements.

Here is what you need to do:
----------------------------

1. The assignment repository for this lesson contains a file with 10 records
   and a module that reads that file.
2. Your first task is to take the data file, and expand it (following the format for the 10 records)
   so that it contains one million records. Write some Python code to do this.
   One of the columns is a guid (a unique identity). See if you can find an easy way to 
   generate these (look online?).
3. The module that reads the file is badly written and probably can be made to run more quickly and
   efficiently!
4. You will look at the code and may immediately form a judgment about where
   performance can be improved. Do not be tempted to make immediate changes!
5. Be sure to use an evidence based approach, and show, with data, how you were able
   to make improvements.
6. Rewrite the module to improve performance. Provide evidence to demonstrate
   the improvement. 
7. Your new module should be called good_perf.py, it should use identical input
   and produce identical output to poor_perf.py

Other requirements:
-------------------
As always, you should ensure your code produces no errors or warnings from pylint.

Submission
----------
You submission should include the good_perf.py file, along with notes on your findings, performance 
improvements, and notes on your approach. For notes, you can use regular text format (.txt) or try restructured
text (.rst) format. It should also include the program you write to generate 1 million records.