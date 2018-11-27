=====================
Lesson 2 : Assignment
=====================

.. todo::
    Complete code for charges_calc.py (Luis)

One of the challenges with the existing code base at HP Norton is the lack
of the necessary debug information when issues occur.

One such case is the *charges_calc* script. Its purpose is to convert a list of
existing rentals of individual inventory items (for example, table lamps),
including number of units rented, price charged per day and rental start / end dates,
and return the same list with the total cost of the rental (based on the number of
days the item or items have been rented), as well as total cost per item (in the 
case of multiple items). Both the input and the output of the script are JSON files.

The problem at this point is that, using the included JSON input file, the script 
is not working. There is no error message or anything else indicating what is
going on and no output file is being produced.

Your goal this week is twofold: You need to use the Python debugger to figure out
why the script is not working, you also need to incorporate logging into the script
so that someone doing debug can follow the flow of the script.

Here is what you need to do:
----------------------------

#. Download the charges_calc.py code and review it. Make sure you also download source.json, which contains the sample source data.
#. Try as best as you can to understand what the code is doing.
#. Using the debugger, try to understand what is going on with the
   expected command line parameters. See if from the code and through
   watching variables and creating dummy parameters you can infer enough
   to get the program to run. Capture your debug work to a text file.
#. Now, enable logging and start inserting logging statements to track the code's execution.
#. Add comments that describe your discoveries, additional things you need.
#. Add warnings for things missing in the source data that are expected but impeded some of the calculations (for example, unreturned items do not have a *rental_end* value).
#. Add error messages for inconsistencies in the source data that could make your program crash or return incorrect data.

Requirements:
-------------

#. You cannot change the source data, your script needs to deal with data inconsistencies that could make it crash or return incorrect data and issue warnings for missing data. 
#. Capture you debug work in a text file, you will need that for your submission.
#. Setup logging messages so that they are disabled by default and can by enabled by using *-d 1* or *--debug 1* from the command line. Use the *argparse* module for this. You will have the following debug levels:
    #. 0: No debug messages or log file.
    #. 1: Only error messages.
    #. 2: Error messages and warnings.
    #. 3: Error messages, warnings and debug messages.
#. You need to implement three types of logging messages:
    #. Debug: General comments, indicating where in the script flow we are. Should be shown on screen only.
    #. Warning: Used for missing elements in the source data that force a change in the flow. Shown on screen and on the log file.
    #. Error: Used for inconsistencies in the source data that will cause the script to crash or report incorrect results. Shown on screen and on the log file.
#. Use the following format for your log messages: 

    ..

    log_format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"

#. Use the following filename format to timestamp your log files:

    ..

    log_file = datetime.datetime.now().strftime("%Y-%m-%d")+'.log'

Submission:
-----------

Your submission should include the following:

- Updated version of *charges_calc.py* (keep the same filename).
- Your Python debugger logfile. Include it as *debugger_log.txt*.
- Logfile created by running your updated script on the source data.
- Output JSON file created with the updated script.

Tips
----
- Think about what a developer would need by way of logging to help trace what
  has happened and gone wrong when the module is running.
- Add details of your approach to logging to the module docstring to assist
  anyone who maintains the module.
- Be sure to document details of your fix from the debugging activity in
  your pull request.

