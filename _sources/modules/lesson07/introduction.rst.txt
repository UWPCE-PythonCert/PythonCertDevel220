############
Introduction
############

This lesson introduces the concepts of concurrent and asynchronous
programming and the python tools available for their implementation. Concurrency is doing multiple things at the same time -- in
Python, this can be accomplished through several approaches:
multi-threading, multi-processing and asynchronous programming.

Threading and multi-processing support true parallelism, while
asynchronous techniques allow tasks to be completed in unknown order.
Python recently added features to support async, this lesson will
explain how to use it.

These techniques can be applied to allow interfaces to be responsive
while work is being done, and/or to boost performance with
parallelizable tasks.

 

Learning Objectives
===================

Upon successful completion of this lesson, you will be able to: 

-  Identify when to apply each of the core techniques:

   -  multi-threading.
   -  multi-processing.
   -  async.

-  Create a simple multi-threaded program with a message queue.
-  Create a simple multi-processing program with a message queue.
-  Create a web-api client with the asyncio package.

New Words, Concepts, and Tools
==============================

-  Concurrency.
-  Threading.
-  Multi-processing.
-  Message Queues.
-  Coroutines.
-  Async.

Required Reading
================

-  `Concurrent
   Programming <https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Concurrency.html>`__
-  `Threading and
   multiprocessing <https://uwpce-pythoncert.github.io/PythonCertDevel/modules/ThreadingMultiprocessing.html>`__
-  `Asychronous
   Programming <https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Async.html>`__

Optional Reading
================

*Fluent Python:*

-  Ch. 16: Coroutines
-  Ch. 17: Concurrency with Futures
-  Ch. 18: Concurrency with asyncio

Threading:
----------

`Grok the
GIL <https://emptysqua.re/blog/grok-the-gil-fast-thread-safe-python/>`__

Async:
------

-  `Unyielding: a take on threads vs
   async <https://glyph.twistedmatrix.com/2014/02/unyielding.html>`__
-  `The Asyncio Cheat
   Sheet <http://cheat.readthedocs.io/en/latest/python/asyncio.html>`__:
   This is a pretty helpful, how to do it guide.
-  Nathanial Smith's `Some thoughts on asynchronous API
   design <https://vorpus.org/blog/some-thoughts-on-asynchronous-api-design-in-a-post-asyncawait-world/>`__
-  The built in asyncio suffers from a lot of legacy -- for a new take
   without any pre- 3.5 legacy: \ `The Trio async
   package <https://trio.readthedocs.io/en/latest/index.html>`__
