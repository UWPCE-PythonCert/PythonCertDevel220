z=================
Lesson 02 Content
=================

.. raw:: html

   <div id="menuheading">

.. rubric:: Logging and Debugging
   :name: logging-and-debugging
   :class: caH2

.. raw:: html

   <div id="navbar" class="caNav grid-row around-md clearunderlinestyle"
   role="navigation">

`Introduction <%24WIKI_REFERENCE%24/pages/lesson-05-introduction>`__ \|
`Content <%24WIKI_REFERENCE%24/pages/lesson-05-content>`__ \|
`Quiz <%24CANVAS_OBJECT_REFERENCE%24/quizzes/ie7895b971d4a0e2e35b415eb863435b0>`__ \|
`Activity <%24CANVAS_OBJECT_REFERENCE%24/assignments/i89c943e0018a913b1c51e640fa38f289>`__
\|
`Assignment <%24CANVAS_OBJECT_REFERENCE%24/assignments/i6935f2eba782af5becab9aa3ea3829ca>`__
\| `Code
Talk <%24CANVAS_OBJECT_REFERENCE%24/discussion_topics/i72c5561508c841b38aa31c3d12c9e1c7>`__

.. raw:: html

   </div>

.. raw:: html

   </div>

Logging
=======

We'll be talking about both logging and debugging in this lesson. In the
introduction, I said that logging and debugging are a great step up from
the print statements that beginning programers often like to use to
debug their code.

Your assignment for this week will be the culmination of the logging
exercises that we complete in this lesson. I encourage you to actually
create and modify each of the exercise scripts that I demonstrate below.

Print Statement Debugging
-------------------------

Let's start off by writing a simple Python script with an obvious
problem. Begin by creating simple.py:

.. code:: Python

    # simple.py
    def my_fun(n):
        for i in range(0, n):
            100 / (50 - i)

    if __name__ == "__main__":
        my_fun(100)

You can probably already see the problem that we'll encounter when we
run simple.py. Let's run it in python:

.. code:: Python

    $ python simple.py
    Traceback (most recent call last):
      File "simple.py", line 7, in <module>
        my_fun(100)
      File "simple.py", line 4, in my_fun
       100 / (50 - i)
    ZeroDivisionError: division by zero

As you might have expected, we get a ZeroDivisionError! At some point,
for some value of \ *i*, the instruction 100\ * / (50 - i)* causes our
program to attempt to divide by zero.

I'm sure that you can see what value of \ *i* would cause this problem,
but let's pretend that we didn't know, and we were trying to figure it
out. If you had no better tools, you might try to investigate this
problem by adding print statements to the loop. You could print out the
value of \ *i* just before the problem-fraught division statement. Make
the following modification to simple.py:

.. code:: Python

    for i in range(0, n):
        print(i)           # <-- Add this line
        100 / (50 - i)


Now running simple.py will give us some clue about for the faulting
value of \ *i*:

.. code:: Python

    $ python simple.py
    0
    1
    2
    ...
    48
    49
    50
    Traceback (most recent call last):
     File "simple.py", line 2, in <module>
     100 / (50 - i)
    ZeroDivisionError: division by zero

If we didn't know it already, then we know it now! The value
of \ *i *\ just before the ZeroDivisionError is 50. This is the faulting
value of \ *i*.

This "print statement debugging" is how a lot of new programmers begin
trying to understand problems in their code. And many advanced
programmers will still use a print statement when they're writing simple
scripts.

But what are the problems with print statement debugging?

Here are a few problems with using a print statement to debug your code:

-  You have to go back in and take them out, otherwise they produce
   distracting output when you're running your program.
-  If you have more than a couple of print statements, it becomes hard
   to keep track of where they all are and what each one specifically is
   reporting on.
-  Print statements don't help you when your code is being run in
   production: you can only use print statements when you're running the
   code on your own machine from your console.

To fix all of these problems, we're going to use \ *logging*. Logging is
a practice that's used in similar ways across a lot of different
languages: you'll be able to apply these lessons about logging to your
entire programming career.

We'll practice logging statements that:

-  You can choose to hide or show with each run of your code.
-  You can automatically add extra information to, like the line number
   and file that they're invoked in.
-  You can send from any Internet connected device to a centralized
   server, to monitor your code as it works in production.

If you like using print statements to debug your code, you'll enjoy
logging: message logging is a direct step up from print statements in
your programming skills.

The Print Statement You Can Hide
--------------------------------

Let's make a couple of changes to our code:

.. code:: Python

    import logging

    logging.basicConfig(level=logging.DEBUG)
    def my_fun(n):
        for i in range(0, n):
            logging.debug(i)
            100 / (50 - i)

    if __name__ == "__main__":
        my_fun(100)


We've imported the logging library, set some kind of logging
configuration, and then replaced our print statement with
a \ *logging.debug* statement.

Now running simple.py produces the following output:


.. code:: Python
    
    $ python simple.py
    DEBUG:root:0
    DEBUG:root:1
    DEBUG:root:2
    ...
    DEBUG:root:48
    DEBUG:root:49
    DEBUG:root:50
    Traceback (most recent call last):
      File "simple.py", line 10, in <module>
        my_fun(100)
      File "simple.py", line 7, in my_fun
        100 / (50 - i)
    ZeroDivisionError: division by zero

So far, this doesn't look very different from the print statement that
we were using before. But let's change one line of the script:

.. code:: Python

    import logging

    logging.basicConfig(level=logging.WARNING)  # Change the level to logging.WARNING
    def my_fun(n):
        for i in range(0, n):
            logging.debug(i)
            100 / (50 - i)

    if __name__ == "__main__":
        my_fun(100)


Now try running the script again:

.. code:: Python

    $ python simple.py
    Traceback (most recent call last):
      File "simple.py", line 10, in <module>
        my_fun(100)
      File "simple.py", line 7, in my_fun
        100 / (50 - i)
    ZeroDivisionError: division by zero

What happened?

The logging library includes the idea of various \ *levels* of logging
messages: some messages are more important than others. For example, if
you were curious to know the values that a function was being called
with, then you might put a logging statement into that function to help
you understand when it was being called, and with what arguments. For
example:

.. code:: Python

    def my_fun(n):
        logging.info("Function my_fun called with value {}".format(n))
        do_something(n)
        ...


This logging statement is just giving us some information about how the
function is being used, so we've used the *logging.info* method.

In our example script, when we were trying to figure out what value
of \ *i* was causing our script to crash, we were debugging our code.
That's why we used a \ *logging.debug* statement. Now that we know that
the value 50 causes our code to crash, we could put in
a \ *logging.warning* statement that will warn us of dangerous
conditions:

.. code:: Python

    import logging

    logging.basicConfig(level=logging.WARNING)
    def my_fun(n):
        for i in range(0, n):
            logging.debug(i)
            if i == 50:                                   # Add this line
                logging.warning("The value of i is 50.")  # Add this line
            100 / (50 - i)

    if __name__ == "__main__":
        my_fun(100)


If we wanted to handle the division by zero error gracefully, then we
could modify the code to attempt the \ *100 / (50 - i)* operation inside
of a try, except block. Then we would log an \ *error* if our script did
attempt to divide by 0:

.. code:: Python

    import logging

    logging.basicConfig(level=logging.WARNING)

    def my_fun(n):
        for i in range(0, n):
            logging.debug(i)
            if i == 50:
                logging.warning("The value of i is 50.")
            try:
                100 / (50 - i)
            except ZeroDivisionError:
                logging.error("Tried to divide by zero. Var i was {}. Recovered gracefully.".format(i))

    if __name__ == "__main__":
        my_fun(100)


You can see all of the logging levels in the `logging
documentation <https://docs.python.org/3/library/logging.html#levels>`__.
Each level has an associated logging method,
like \ *logging.error*, \ *logging.warning*, etc.

Now what do we get when we run our code?

.. code:: Python

    $ python simple.py
    WARNING:root:The value of i is 50.
    ERROR:root:Tried to divide by zero, i was 50. Recovered gracefully.

Why is it not showing the \ *logging.debug* statements?

The statement \ *logging.basicConfig(level=logging.WARNING) *\ tells the
logger to \ *only* display log messages with level WARNING and above.
Look back to the logging levels documentation. You'll see that the DEBUG
level is below the WARNING level, so it won't be displayed. When we were
debugging this code, the debug statements were helping us understand why
our code was failing, but now it would be overwhelming to see them every
time we run our code. We've \ *hidden* the statements by making a single
configuration change.

The idea is that you might be working on a project with a lot of Python
files. You may have put debugging or information statements into several
of these files. While you're authoring the project, these messages are
useful. And once you think you've worked out all of the bugs in your
code, you don't have to go through all of your files and find every
logging statement: you can just turn off the unimportant ones by setting
the log level in your main script.

What is the default log level? If you don't specify a log level, then
will you see \ *all* log messages, or is there some default level that
the logging library will choose for you? To answer that, try running the
following script:

.. code:: python

    # loggingtest.py
    import logging

    logging.critical("This is a critical error!")
    logging.error("I'm an error.")
    logging.warning("Hello! I'm a warning!")
    logging.info("This is some information.")
    logging.debug("Perhaps this information will help you find your problem?")


Although I used the \ *logging.basicConfig* method to set the logging
level in these examples, there are other ways to set this value. We'll
learn about this later in the lesson.

The Print Statement You Can Add More Information To
---------------------------------------------------

Sometimes, it's not enough just to see the error, warning, or
information message that you would put into a print statement to debug
your code. Other information can be useful, such as:

-  when the log message was generated;
-  what Python file the log message was generated in;
-  what line number the log message was generated on; or
-  The name of the function that the log message was generated in.

It's easy to see how knowing the file name, line number, and function
name that the log message was generated on can be useful: you might
create a lot of messages and it can be easy to lose track of where all
of your log statements are.

Why would you possibly want to know \ *when* a log message was
generated? One reason is that you might want to time how long it takes
your code to get to a particular log message. But the real usefulness of
knowing \ *when* a log message was generated will come in the next
session: we'll be saving log messages to files instead of printing them
at the console. When you open up a saved log file, you might not even
know \ *what day* the message was generated on unless you include a
timestamp!

Let's try it out! Make the following changes to your code:

.. code:: python

    import logging

    log_format = "%(asctime)s %(filename)s:%(lineno)-4d %(levelname)s %(message)s"  # Add/modify these
    logging.basicConfig(level=logging.WARNING, format=log_format)                   # two lines

    def my_fun(n):
        for i in range(0, n):
            logging.debug(i)
            if i == 50:
                logging.warning("The value of i is 50.")
            try:
                100 / (50 - i)
            except ZeroDivisionError:
                logging.error("Tried to divide by zero. Var i was {}. Recovered gracefully.".format(i))

    if __name__ == "__main__":
        my_fun(100)


Let's look at these two lines:

.. code:: python

    log_format = "%(asctime)s %(filename)s:%(lineno)-4d %(levelname)s %(message)s"
    logging.basicConfig(level=logging.WARNING, format=log_format)


We begin by defining a *log_format* for our log messages. All of the
characters inside of the parentheses specify a different piece of
information that we want to include inside of our messages. Please see
the `full list of these LogRecord
attributes <https://docs.python.org/3/library/logging.html#logrecord-attributes>`__,
and look for each of the attributes we included above, to get a guess
for what information this formatter will include. For
example, \ *asctime* produces a human-readable time string.

The formatting characters to the left and right of the parentheses are
borrowed from \ *printf* formatting. For example, \ *%(asctime)s* means
to include the time string in the log message as a string.
The \ *-4d* in *%(lineno)-4d* means to include the line number of the
log statement as a 4 character integer, padding the output on the right
with spaces.

Now, what do you imagine running simple.py will produce? Here is the
output:

.. code:: python

    $ python simple.py
    2018-03-12 17:39:17,567 simple.py:10   WARNING The value of i is 50.
    2018-03-12 17:39:17,567 simple.py:14   ERROR Tried to divide by zero. Var i was 50. Recovered gracefully.

As expected, we see the time that the log message was produced, the file
name and line number that the message was produced on, and the log
message and its level.

If we were using print statements to debug our code, then we could have
included this information manually in each print statement. But it's
much less work to specify this format in one line at the top of our
code, and if we want to change it later then we only have to change it
in one location in our script.

The Print Statement You Can Send Somewhere Else
-----------------------------------------------

Every print statement you include in your code writes its message to the
console, but what if it could be sent somewhere else?

The simplest place that you can send log messages to is a file. Edit
the \ *logging.basicConfig*\ statement in your \ *simple.py*.

.. code:: python

    logging.basicConfig(level=logging.WARNING, format=log_format, filename='mylog.log')


Now run simple.py:

.. code:: python

    $ python simple.py

    $

There should now be no output sent to the console. Instead, the logging
messages have been sent to a new file: mylog.log. Open this newly
created file to take a look at the contents.

What happens when you run the script again? Will the contents of
mylog.log be appended to, or will they be overwritten? Try it out and
find the answer. What's in the log file after running simply.py two or
three times?

We're really starting to show off the power of logging. Now you no
longer have to wait patiently at the console for your print statements
to be displayed: you can just send them to a file and read them later.

Logging is even more powerful than that. We're about to learn how to
send our logging messages to multiple places. In preparation for that, I
want you to make the following changes to your code:

.. code:: python

    import logging

    log_format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"

    # BEGIN NEW STUFF
    formatter = logging.Formatter(log_format)

    file_handler = logging.FileHandler('mylog.log')
    file_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.addHandler(file_handler)
    # END NEW STUFF

    def my_fun(n):
        for i in range(0, n):
            logging.debug(i)
            if i == 50:
                logging.warning("The value of i is 50.")
            try:
                i / (50 - i)
            except ZeroDivisionError:
                logging.error("Tried to divide by zero. Var i was {}. Recovered gracefully.".format(i))

    if __name__ == "__main__":
        my_fun(100)


Python, and the logging library, are so easy to read that you can
probably guess at the meaning of all of these new lines. The first thing
to notice is that we've eliminated that \ *logging.basicConfig* line!
We're manually building a logging configuration, consisting of
a \ *formatter* and a \ *handler*.

Let me add a bit of explaination to each new line in following comments:

.. code:: python

    # Create a "formatter" using our format string
    formatter = logging.Formatter(log_format)

    # Create a log message handler that sends output to the file 'mylog.log'
    file_handler = logging.FileHandler('mylog.log')
    # Set the formatter for this log message handler to the formatter we created above.
    file_handler.setFormatter(formatter)

    # Get the "root" logger. More on that below.
    logger = logging.getLogger()
    # Add our file_handler to the "root" logger's handlers.
    logger.addHandler(file_handler)


What does this new configuration do? Well, it does exactly what our code
did before: it sends warning messages and above to a file named
'mylog.log'.

Log message handlers answer the question, "What should the system do
with log messages?" Here are a few possible things that we can do with
log messages:

-  We could print them to the console.
-  We could send them to a file.
-  We could send them to a remote server.
-  We could send them in an email.
-  We could just ignore them.

Take a brief look at each of the `handler classes available in the
logging
library <https://docs.python.org/3/library/logging.handlers.html>`__.
Each of the above ways to handle log messages, and more, is represented
by a handler class in the logging library.

In the newest iteration of our code, we create a logging.FileHandler log
message handler to send our log messages to a file. Unlike
the \ *logging.basicConfig* command, we can't provide the log message
format to our file handler as a string. We have to create an instance of
the logging.Formatter class and use \ *file_handler.setFormatter* to
instruct our handler to use this formatter.

Next, we have to tell the logger to use this handler that we've created.
We first get a reference to the "root" or global logger
using \ *logging.getLogger()*. It turns out that you can have multiple
loggers running in a system, although we're not going to explore that in
this lesson. Instead, we're going to use a single logger and add
multiple log message handlers to that logger. But if you're curious, you
can look at the documentation
for \ `logging.getLogger() <https://docs.python.org/3/library/logging.html#logging.getLogger>`__

Now that we have a reference to the "root" or global logger, we can add
our message handler to it using \ *logger.addHandler*. Now, our root
logger will send all of its messages to the file_handler log message
handler, and these messages get written to the file 'mylog.log'.

Run the script and confirm!

Now, let's add another handler! Imagine that you wanted to see ALL
logging messages at the console while you were running your program, but
only log the most important messages (WARNING and above) to your log
file. You could accomplish that with this code:

.. code:: python

    import logging

    log_format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"

    formatter = logging.Formatter(log_format)

    file_handler = logging.FileHandler('mylog.log')
    file_handler.setLevel(logging.WARNING)           # Add this line
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()        # Add this line
    console_handler.setLevel(logging.DEBUG)          # Add this line
    console_handler.setFormatter(formatter)          # Add this line

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)                   # Add this line
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)               # Add this line

    def my_fun(n):
        for i in range(0, n):
            logging.debug(i)
            if i == 50:
                logging.warning("The value of i is 50.")
            try:
                i / (50 - i)
            except ZeroDivisionError:
                logging.error("Tried to divide by zero. Var i was {}. Recovered gracefully.".format(i))

    if __name__ == "__main__":
        my_fun(100)


You might have a few questions about this code:

-  What is a StreamHandler?
-  Why do we set the log level on both of the log message
   handlers \ **and also** set the log level on the root logger?

A rigorous definition of a s\ *tream* is outside the scope of this
assignment; but in rough terms, a stream is a very general concept in
computer science of a store or source of information. The StreamHandler
constructor will accept a stream as its first argument; but if we don't
provide an argument, then it will use its default: the sys.stderr
stream. That's one of two system streams that get printed directly to
the console. So by default, the StreamHandler will send log messages to
the console.

As for the second question, loggers and handlers maintain separate
settings for their minimum log level. By default, a logger will not pass
any messages lower than WARNING on to its handlers. Because we want the
console_logger to handle DEBUG messages, we have to set the level of the
root logger to DEBUG in order for these messages to be sent on to its
handlers at all. Because we also set the level of the console_handler to
DEBUG, the console_handler will print out these low-level messages. The
root logger will also send DEBUG messages and above to the file_handler,
but because we have set the log level of the file_handler to WARNING it
will only log WARNING messages and above to its log file.

Run the script, and confirm that it now runs as expected!

Lesson Assignment
-----------------

The lesson assignment makes use of the materials in this lesson on
logging. Refer back to this section when you're ready to complete the
assignment.

Debugging
=========

We said that logging and debugging are a step up from the print
statements that many new programmers use to debug their code.

The first half of this lesson presented logging as a direct evolution to
print statement debugging: a logging statement is like a print statement
that can be hidden, or have extra information attached to it, or can be
sent to somewhere other than the console.

Debugging your code with an interactive debugger is another thing
entirely; although both practices help you answer the same question of
what's going in in your code, interactive debugging is not at all like
inserting print statements.

Interactive debugging allows you to run the Python interpreter
line-by-line through your code, pausing to print out the values of
particular variables, or to evaluate other statements inside of the
interpreter. And it includes tools that can help you "zoom through" the
execution of many statements to get right to trouble-raising conditions
in your code.

Basic Debugging Commands
------------------------

Let's begin by understanding the basic commands of the interactive
debugger. We'll begin by debugging the file simple.py in the debugging
exercises code repository:

.. code:: python

    # simple.py
    def my_fun():
        for i in range(1, 500):
             123/ (50 - i)

    if __name__ == '__main__':
        my_fun()


Try running the script. You probably expected to receive a
ZeroDivisionError. Let's use this code to begin exploring the Python
interactive debugger.

{{VIDEO HERE}}

Breakpoints
-----------

It could take a lot of 's' and 'n' commands to get to that
ZeroDivisionError condition in simple.py! Breakpoints and conditions
allow you to "zoom through" the execution of your code, pausing the
interpretter when a certain condition on a certain line of code is met.

{{VIDEO HERE}}

Complicated Example and Exercise
--------------------------------

Here's an exercise where the error in our code is not entirely obvious.

{{VIDEO HERE}}

Take some time to try to figure out what values of \ *i*, \ *j*,
and \ *k* give rise to the zero division error. Focus on trying to
create a breakpoint condition for line 19 that will be met if the
interpretter is \ *about* to divide by zero.

{{VIDEO HERE}}

Recursion Error Exercise
------------------------

Here's an exercise that finally does not involve a ZeroDivisionError!
Instead, we'll be investigating a RecursionError.

For the `lesson
activity <%24CANVAS_OBJECT_REFERENCE%24/assignments/i89c943e0018a913b1c51e640fa38f289>`__,
you'll be required to copy and your debugger output from this recursion
exercise and paste it into the activity submission text box. Before
beginning this video, visit the lesson activity to make sure that you
understand what will be required.

{{VIDEO HERE}}

Use the interactive debugger to analyze the error in our program. In a
couple of sentences, describe our error in the following terms:

-  What is wrong with our logic?
-  Why doesn't the function stop calling itself?
-  What's happening to the value of 'n' as the function gets deeper and
   deeper into recursion?

Once you're satisfied with your answer, see the next video:

{{VIDEO HERE}}

Conclusion
==========

Logging and interactive debugging are excellent tools to keep in your
Python toolbox, and the syntax and semantics of logging and debugging
are so similar across so many different languages that these lessons may
help you no matter what programming language you're using.
