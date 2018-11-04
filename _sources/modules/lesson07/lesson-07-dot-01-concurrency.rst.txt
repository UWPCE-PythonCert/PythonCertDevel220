=========================
Lesson 07.01: Concurrency
=========================

Video Tutorials: Concurrency
============================

 

Simple Threading
----------------

Threading is the ability run multiple pieces of code at the same time in
the same process. Doing threading safely and properly is tricky
business, but it's Python makes it easy to get started.

  

{{VIDEO HERE}}

Race Conditions
---------------

Race conditions are one of the tricky bits with concurrent programming
-- here's a simple example that will help you understand what they are
all about, and why they can catch you unaware.

 

{{VIDEO HERE}}

Threading and the GIL
---------------------

The Global Interpreter Lock (GIL) can keep processor intesive code from
gaining full advantage of multiple threads. But there are ways around
it.

 

{{VIDEO HERE}}

Multiprocessing
---------------

Multiprocessing means running code in a separete process -- since the
code is not sharing a single python intrpeter, there are no issues with
the GIL. But there is other overhead.

 

{{VIDEO HERE}}

Optional Videos
===============

 David Beazley's "Grok the GIL"

` Grok the GIL Pycon
Talk <https://www.youtube.com/watch?time_continue=150&v=7SSYhuk5hmc>`__
