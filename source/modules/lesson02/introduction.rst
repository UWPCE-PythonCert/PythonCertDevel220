=====================
Lesson 2 Introduction
=====================

Introduction
============

When something goes wrong in your code, most programmers' first
intuition is to insert a print statement. A print statement can help you
answer questions like, "What is the value of variable \ *x* just before
my code crashes? Does my code crash only when \ *x* has that value, or
does it crash all the time?" This "print statement debugging" is how
most new programmers begin investigating failures in their code.

This lesson will teach you two new, awesome and professional ways to
debug your code: logging and debugging.

Logging takes the idea of printing statements from your code and brings
it to the next level. You'll be able to selectively hide or show
different logging messages, and send them to the console, into log
files, or across the internet into log servers.

Then we'll use the interactive Python debugger. The debugger lets you
"get into the head" of the Python interpreter. We will step through each
line of code as it's executed by Python, with an extra opportunity to
print out the values of variables or evaluate extra statements before
moving on to the next line of code. And you can transfer the skills you
learn in Python's debugger into the debuggers of many other languages.

Learning Objectives
===================

Upon successful completion of this lesson, you will be able to:

-  Create log messages of different importance levels.
-  Selectively hide or show log messages based on their importance.
-  Send log messages to a log file.
-  Send log messages across the internet to a central logging server.
-  Step through program execution in Python's interactive debugger.
-  Set breakpoints and conditional breakpoints within a program's
   execution.
-  Use a debugger to diagnose, describe, and correct the failure of a
   Python script.

 

New Words, Concepts, and Tools
==============================

-  logging
-  log levels
-  syslog
-  debugger
-  pdb
-  breakpoint
-  "step in"
-  continue

 

Required Reading
================

-  `Python's logging library
    <https://docs.python.org/3/library/logging.html>`__\ Spend five to
   ten minutes scanning the text for basic \ *familiarity* with the
   logging library.
-  `PDB
   commands <https://docs.python.org/3/library/pdb.html#debugger-commands>`__
   Read over just the debugger commands.
