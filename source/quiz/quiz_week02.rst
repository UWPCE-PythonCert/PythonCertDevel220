##############
Lesson 02 Quiz
##############

1. In Python development, a log file is a file that records:
The work a developer needs to do to complete their work
Only errors that may occur when a program is running
Evidence that software works as intended
A record of activity deemed important, produced when a program is running

2. The main use of logging is to:
Help developers understand their code
Provide more flexible output than print statements
Help track down issues and diagnose problems when a program is running


3. Put the log levels in order from most critical to least critical.
The value 50 corresponds to the most critical level and 10 corresponds
to the least critical level.

CRITICAL
ERROR
WARNING
INFO
DEBUG
UNIMPORTANT

40
CRITICAL
ERROR
WARNING
INFO
DEBUG
UNIMPORTANT

30
CRITICAL
ERROR
WARNING
INFO
DEBUG
UNIMPORTANT

20
CRITICAL
ERROR
WARNING
INFO
DEBUG
UNIMPORTANT

10
CRITICAL
ERROR
WARNING
INFO
DEBUG
UNIMPORTANT

4. You are using the interactive debugger to debug the following Python

def my_function(x):
        print(x + 2)
if __name__ == "__main__":
    my_function(1)
    my_function(2)

5. What debugger command would bring the debugger arrow up to the
definition of my_function?
s
n
c

6. You are using the interactive debugger to debug the following Python
script:

def my_function(x):
    print(x + 2)
if __name__ == "__main__"
    my_function(1)
    my_function(2)

7. What debugger command would bring the debugger arrow down to line 6?
n
s
c

8. Suppose you are debugging the following code:

from some_library import some_function
    def my_function():
        for i in range(500):
            some_function(i)
if __name__ == '__main__':
    my_function()

9. You've found that some_function will encounter an exception when 
i is equal to 387. What debugger command could help you speed through
execution and bring the debugger arrow immediately to line 5 when i is
equal to 387, rather than stepping through every single iteration of the 
for loop?

b
n
