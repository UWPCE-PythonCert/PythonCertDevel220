
.. _concurrency:

======================
Concurrent Programming
======================

..todo::
  Embed {{video}} tags into Lesson 7 concurrency (Luis)

What does it mean to do something "Concurrently" ? It means multiple tasks are being done at the same time. Is Concurrency the same thing as "parallelism"? Not exactly:

 - Parallelism is about processing multiple things at the same time -- true parallelism requires multiple processors (or cores).
 - Concurrency is about handling multiple things at the same time -- things that may or may not actually be running in the processor at the same time (such as network requests).
 
So, parallelism needs concurrency, but concurrency needs not be in parallel.

"Concurrency is not parallelism" -- Rob Pike:  https://vimeo.com/49718712

Despite Rob Pike using an example about burning books, I recommend listening to at least the first half of his talk.

In that talk, Rob makes a key point: Breaking down tasks into concurrent subtasks only allows parallelism, it’s the scheduling of these subtasks that creates it.

Once you have a set of subtasks, they can be scheduled in a truly parallel fashion, or managed asynchronously in a single thread (concurrent, but not parallel).

Asynchrony
--------------------

We now know parallelism is not the same as concurrency. What about "asynchrony"?

**Concurrency:**

Having different code running at the same time, or *kind* of the same time.

**Asynchrony:**

The occurrence of events independent of the main program flow and the ways in which such events are dealt with.

Asynchrony and Concurrency are really two different things -- you can do either one without the other -- but they are closely related, and often used together. They solve different problems, but the problems they solve 
and the solutions tend to overlap.

Types of Concurrency
--------------------
There are different ways to implement concurrency in Python:

**Multithreading:**

  Multiple code paths sharing memory -- one Python interpreter, one set of Python objects.

**Multiprocessing:**

  Multiple code paths with separate memory space -- completely separate Python interpreter.

**Asyncronous programming:**

  Multiple "jobs" run at "arbitrary" times -- but usually in one thread -- i.e. only one code path, one interpreter.

Several different packages for these, both in the standard library and 3rd party libraries.

Which one should you use?

 - IO bound vs. CPU bound -- CPU bound requires multiprocessing (at least with pure Python).
 - Event driven cooperative multitasking vs. preemptive multitasking.
 - Callbacks vs coroutines + scheduler/event loop.

Motivations for parallel execution
----------------------------------

Why would you want your code to use excute in parallel?

-  Performance
   -  Limited by "Amdahl's Law": http://en.wikipedia.org/wiki/Amdahl%27s_law

   -  CPUs aren't getting much faster.

-  Event handling
   - If a system handles asynchronous events, a separate thread of execution could handle those events and let other threads do other work.

   - Examples:
      -  Network applications.
      -  User interfaces.

Parallel programming can be hard!

If your problem can be solved sequentially, consider the costs and
benefits before going parallel.


Parallelization Strategy for Performance
----------------------------------------
Once you have determined that you want to execute your code in parallel, there are certain steps you need to complete to take
advantage of parallel execution:

| 1. Break the problem down into chunks.
| 2. Execute chunks in parallel.
| 3. Reassemble output of chunks into a result.

.. image:: /_static/OPP.0108.gif
      :align: right
      :height: 450px
      :alt: multitasking flow diagram


|
|

-  Not every problem is parallelizable.
-  There is an optimal number of threads for each problem in each
   environment, so make it tunable.
-  Working concurrently opens up synchronization issues.
-  Methods for synchronizing threads:

   -  locks.
   -  queues.
   -  signaling/messaging mechanisms.

Other alternatives
------------------

Traditionally, concurency has been achieved through multiple process
communication and in-process threads, as we've seen.

Another strategy is through micro-threads, implemented via coroutines
and a scheduler.

A coroutine is a generalization of a subroutine which allows multiple
entry points for suspending and resuming execution.

The threading and the multiprocessing modules follow a
`preemptive multitasking model <http://en.wikipedia.org/wiki/Preemption_(computing)>`_

Coroutine based solutions follow a
`cooperative multitasking model: <http://en.wikipedia.org/wiki/Computer_multitasking#Cooperative_multitasking.2Ftime-sharing>`_

Threads versus processes in Python
----------------------------------

Threads are lightweight processes_, run in the address space of an OS
process, true OS level threads.

Therefore, a component of a process.

.. _processes: https://en.wikipedia.org/wiki/Light-weight_process

This allows multiple threads access to data in the same scope.

Threads can not gain the performance advantage of multiple processors
due to the Global Interpreter Lock (GIL).

But the GIL is released during IO, allowing IO bound processes to
benefit from threading.

Processes
---------

A process contains all the instructions and data required to execute
independently, so processes do not share data!

Mulitple processes are best to speed up CPU bound operations.

The Python interpreter isn't lightweight!

Communication between processes can be achieved via:

``multiprocessing.Queue``

``multiprocessing.Pipe``

and regular IPC (inter-process communication)

Data moved between processes must be pickleable (it can be serialized).


Advantages / Disadvantages of Threads
-------------------------------------

Advantages:
...........

They share memory space:

 - Threads are relatively lightweight -- shared memory means they can be created fairly quickly without much memory use.

 - Easy and cheap to pass data around (you are only passing a reference).

Disadvantages:
..............

They share memory space:

 - Each thread is working with the *same* python objects.
 - Operations often take several steps and may be interrupted mid-stream
 - Thus, access to shared data is also non-deterministic

   (race conditions)

Creating threads is easy, but programming with threads is difficult.

  Q: Why did the multithreaded chicken cross the road?

  A: to To other side. get the

  -- Jason Whittington

GIL
---

**Global Interpreter Lock**

(**GIL**)

This is a lock which must be obtained by each thread before it can
execute, ensuring thread safety

.. image:: /_static/gil.png
    :width: 100.0%


The GIL is released during IO operations, so threads which spend time
waiting on network or disk access can enjoy performance gains

The GIL is not unlike multitasking in humans, some things can truly be
done in parallel, others have to be done by time slicing.

Note that potentially blocking or long-running operations, such as I/O, image processing, and NumPy number crunching, happen outside the GIL. Therefore it is only in multithreaded programs that spend a lot of time inside the GIL, interpreting CPython bytecode, that the GIL becomes a bottleneck. But: it can still cause performance degradation.

Not only will threads not help cpu-bound problems, they can actually make things *worse*, especially on multi-core machines!

Python threads do not work well for computationally intensive work.

Python threads work well if the threads are spending time waiting for something:

 - Database Access.
 - Network Access.
 - File I/O.

Some alternative Python implementations such as Jython and IronPython
have no GIL.

cPython and PyPy have one.

More about the gil

More on the GIL:

https://emptysqua.re/blog/grok-the-gil-fast-thread-safe-python/

If you really want to understand the GIL -- and get blown away -- watch this one:

http://pyvideo.org/pycon-us-2010/pycon-2010--understanding-the-python-gil---82.html


-  http://wiki.python.org/moin/GlobalInterpreterLock

-  https://docs.python.org/3/c-api/init.html#threads

-  http://hg.python.org/cpython/file/05e8dde3229c/Python/pystate.c#l761


**NOTE:** The GIL *seems* like such an obvious limitation that you have to wonder why it's there. Indeed, there have been multiple efforts to remove it. But it turns out that Python's design makes that very hard (maybe even impossible) without severely reducing performance on single threaded programs.

The current "Best" effort is Larry Hastings' `gilectomy <https://speakerdeck.com/pycon2017/larry-hastings-the-gilectomy-hows-it-going>`_

But that may be stalled out at this point, too. No one should count on it going away in cPython.


Posted without comment
----------------------
.. figure:: /_static/killGIL.jpg
   :class: fill


Advantages / Disadvantages of Processes
---------------------------------------

Processes are heavier weight -- each process makes a copy of the entire interpreter (mostly...) -- uses more resources.

You need to copy the data you need back and forth between processes.

Slower to start, slower to use, more memory.

But as the entire python process is copied, each subprocess is working with the different objects -- they can't step on each other. So there is:

 **no GIL**

Multiprocessing is suitable for computationally intensive work.

Works best for "large" problems with not much data to pass back and forth, as that's what's expensive.

Note that there are ways to share memory between processes, if you have a lot of read-only data that needs to be used. (see `Memory Maps <https://docs.python.org/3/library/mmap.html>`_)



Synchronization options:

 - Locks (Mutex: mutual exclusion, Rlock: reentrant lock).
 - Semaphore.
 - BoundedSemaphore.
 - Event.
 - Condition.
 - Queues.


Mutex locks (``threading.Lock``)
--------------------------------

 - Probably most common.
 - Only one thread can modify shared data at any given time.
 - Thread determines when unlocked.
 - Must put lock/unlock around critical code in ALL threads.
 - Difficult to manage.

Easiest with context manager:

.. code-block:: python

    x = 0
    x_lock = threading.Lock()

    # Example critical section
    with x_lock:
        # statements using x


Only one lock per thread! (or risk mysterious deadlocks).

Or use RLock for code-based locking (locking function/method execution rather than data access).


Subprocesses (``subprocess``)
-----------------------------

Subprocesses are completely separate processes invoked from a master process (your python program).

Usually used to call non-python programs (shell commands). But of course, a Python program can be a command line program as well, so you can call either your or other python programs this way.

Easy invocation:

.. code-block:: python

    import subprocess

    subprocess.run('ls')

The program halts while waiting for the subprocess to finish. (unless you call it from a thread!)

You can control communication with the subprocess via:

``stdout``, ``stdin``, ``stderr`` with:

``subprocess.Popen``

Lots of options there!


Pipes and ``pickle`` and ``subprocess``
.......................................

 - Very low level, for the brave of heart.
 - Can send just about any Python object.

For this to work, you need to send messages, as each process runs its own independent Python interpreter.


When to Use What
================

.. image:: /_static/proc_thread_async.png




