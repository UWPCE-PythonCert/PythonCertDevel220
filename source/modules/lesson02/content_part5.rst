#################
Part 5: Debugging
#################

We said that logging and debugging are a step up from the print
statements that many new programmers use to debug their code.

The first half of this lesson presented logging as a direct evolution to
print statement debugging: a logging statement is like a print statement
that can be hidden, or have extra information attached to it, or can be
sent to somewhere else other than the console.

Debugging your code with an interactive debugger is another thing
entirely; although both practices help you answer the same question of
what's going in your code, interactive debugging is not at all like
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
interpreter when a certain condition on a certain line of code is met.

{{VIDEO HERE}}

Complicated Example and Exercise
--------------------------------

Here's an exercise where the error in our code is not entirely obvious.

{{VIDEO HERE}}

Take some time to try to figure out what values of \ *i*, \ *j*,
and \ *k* give rise to the zero division error. Focus on trying to
create a breakpoint condition for line 19 that will be met if the
interpreter is \ *about* to divide by zero.

{{VIDEO HERE}}

Recursion Error Exercise
------------------------

Here's an exercise that finally does not involve a ZeroDivisionError!
Instead, we'll be investigating a RecursionError.

For the `lesson
activity <%24CANVAS_OBJECT_REFERENCE%24/assignments/i89c943e0018a913b1c51e640fa38f289>`__,
you'll be required to copy your debugger output from this recursion
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
