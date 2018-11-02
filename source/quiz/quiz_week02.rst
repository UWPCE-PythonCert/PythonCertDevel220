=======================
Python 220 Week 02 Quiz
=======================


Put the log levels in order from most critical to least critical.
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

#. You are using the interactive debugger to debug the following Python

def my_function(x):
        print(x + 2)
        if __name__ == "__main__":
            my_function(1)
            6
                    my_function(2)

What debugger command would bring the debugger arrow up to the
definition of my_function?
s
n
c

#. You are using the interactive debugger to debug the following Python
script:&lt;/p&gt;
&lt;pre&gt;1    def my_function(x):&lt;br&gt;2        print(x + 2)&lt;br&gt;3&lt;br&gt;4    if __name__ == "__main__":&lt;br&gt;5 --&amp;gt;    my_function(1)&lt;br&gt;6        my_function(2)&lt;/pre&gt;
&lt;p&gt;What debugger command would bring the debugger arrow down to line 6?&lt;/p&gt;
&lt;/div&gt;
n
s
c

#. Suppose you are debugging the following code:
&lt;pre&gt;1    from some_library import some_function&lt;br&gt;2&lt;br&gt;3    def my_function():&lt;br&gt;4        for i in range(500):&lt;br&gt;5            some_function(i)&lt;br&gt;6   &lt;br&gt;7    if __name__ == '__main__':&lt;br&gt;8 --&amp;gt;    my_function()&lt;br&gt;&lt;br&gt;&lt;/pre&gt;
&lt;p&gt;You've found that &lt;em&gt;some_function&lt;/em&gt; will encounter an exception when &lt;em&gt;i &lt;/em&gt;is equal to 387. What debugger command could help you speed through execution and bring the debugger arrow immediately to line 5 when &lt;em&gt;i &lt;/em&gt;is equal to 387, rather than stepping through every single iteration of the &lt;em&gt;for&lt;/em&gt; loop?&lt;/p&gt;
&lt;/div&gt;
b
n
