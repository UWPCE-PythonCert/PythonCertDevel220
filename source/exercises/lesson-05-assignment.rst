================================
Assignment: Lesson 05 Assignment
================================

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

Instructions
============

 

Your assignment is a continuation of the \ **logging** exercise that we
completed in the course content. We last left the code like so:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    #simple.py
    import logging

    format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"

    formatter = logging.Formatter(format)

    file_handler = logging.FileHandler('mylog.log')
    file_handler.setLevel(logging.WARNING)           
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()        
    console_handler.setLevel(logging.DEBUG)          
    console_handler.setFormatter(formatter)          

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)                   
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)               

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

.. raw:: html

   </div>

 

For this assignment, you'll be making some modifications to the code.
The biggest modification is that we'll be adding the ability to send our
log messages to a remote server somewhere on the internet. This can be
useful if you have a lot of copies of your code running in production
and you want all of them to send messages to a single logging server
from which you can monitor the health of all of the running copies.

Look into the assignment directory for this lesson. I have provided a
syslog server that you will run on your own machine to receive these log
messages. Although you'll be running the server locally on your own
machine, in practice the server could receive these messages from
anywhere on the internet because the messages are being sent over
UDP/IP.

To complete this assignment, modify simple.py to satisfy the following
goals:

-  You want ALL log messages logged to the console. The format of these
   messages should include the current time.
-  You want WARNING and higher messages logged to a file named {
   todays-date }.log. The format of these messages should include the
   current time.
-  You want ERROR and higher messages logged to a syslog server. The
   syslog server will be appending its own time stamps to the messages
   that it receives, so DO NOT include the current time in the format of
   the log messages that you send to the server.

Some of these goals may already be accomplished or partially
accomplished by the existing code.

To complete this assignment, you will need to create:

-  A second instance of Formatter. Because the three different
   destinations for your log messages require two different formats (one
   with time stamps and one without), you'll need two different
   instances of Formatter.
-  A third Handler, to send messages to the syslog server.

Hints
-----

Look at the list of Handler classes in the Python logging
documentation. The code above instantiates a FileHandler and a
StreamHandler, and you'll need to instantiate a new handler type in
order to complete this assignment. Specifically, you'll need to create a
SysLogHandler.

If you're completing this assignment on Windows, then you may have to
use a DatagramHandler instead of a SysLogHandler. The address and port
will be '127.0.0.1' and 514, respectively. The DatagramHandler will
produce uglier output than the SysLogHandler, but it will suffice for
the purposes of this assignment.

Testing
-------

To test your completed work, open a terminal window and run the included
syslogserver.py.

In another terminal window, run simple.py. As the program runs, you
should see all of the logging messages from the program appear,
including the DEBUG messages. The terminal window containing the server
should show only the ERROR messages generated by the system. And after
the program has completed, it should generate a file { todays-date
}.log, containing the program's WARNING and ERROR messages.

Submitting Your Work 
=====================

Put the file(s) (ex: a\_new\_file.py) in your student directory in a new
subdirectory named for this lesson, and add it to your clone early (git
add a\_new\_file.py). Make frequent commits with good, clear messages
about what you're doing and why.

When you're done and ready for the instructors to review your work, push
your changes to your GitHub fork (git push) and then go to the GitHub
website and make a pull request. Copy the link to the pull request.

Click the *Submit Assignment* button in the upper right.

**Part 1: File(s)**

Use the \ *Choose File* button to find and select the saved .py file or,
if there are multiple files for the assignment, the .zip file.

**Part 2: GitHub Link**

Paste the GitHub link to the pull request in the comments area.

Click the \ *Submit Assignment* button.
