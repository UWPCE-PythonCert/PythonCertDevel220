======================
Lesson 06 Introduction
======================

.. raw:: html

   <div id="menuheading">

.. rubric:: Profiling and Performance
   :name: profiling-and-performance
   :class: caH2

.. raw:: html

   <div id="navbar" class="caNav grid-row around-md clearunderlinestyle"
   role="navigation">

`Introduction <%24WIKI_REFERENCE%24/pages/lesson-10-introduction>`__ \|
`Content <%24WIKI_REFERENCE%24/pages/lesson-content-10-dot-01-profiling>`__\ \|
`Quiz <%24CANVAS_OBJECT_REFERENCE%24/assignments/i7f8f602a176f2f9bcad10fc458fab73c>`__ \|
`Activity <%24CANVAS_OBJECT_REFERENCE%24/assignments/ia6afcfdf074c64ed04482edb4da51fd9>`__
\|
`Assignment <%24CANVAS_OBJECT_REFERENCE%24/assignments/if1e2fbc9a48ac648d2ff823b52519597>`__
\| `Code
Talk <%24CANVAS_OBJECT_REFERENCE%24/discussion_topics/ica2f1e64bf72f3df5256abc73efd92b4>`__

.. raw:: html

   </div>

.. raw:: html

   </div>

Introduction
============

In this module we cover strategies, tools and pitfalls around
understanding the performance of a python code base. We mention or
demonstrate analysis tools built into specific operating systems or
available via python itself. We then we look at techniques for improving
performance, including coding techniques, alternate Python interpreters,
and interaction with C.

Keep in mind that the material presented herein is not the last word on
this topic, rather, as is often the case with the material in the
program, it is merely the first. There are related topics covered
elsewhere in the curriculum, such as concurrency and asynchronous
programming; both topics are about improving the performance or
responsiveness of systems. Also keep in mind that related topics are
covered more deeply in other areas of the curriculum, so that for
instance it might be worthwhile referencing the material on map/filter,
comprehensions, lambdas and other functional programming constructs from
their respective lessons while or before continuing with this lesson.

Learning Objectives

Upon successful completion of this lesson, you will be able to:

-  use profiling strategies to identify bottlenecks in Python code.
-  use timing strategies to assess code constructs.
-  use PyPy to run simple Python scripts to improve their performance.
-  refactor Python code to use Cython for performance improvement.

 

New Words, Concepts, and Tools
==============================

-  Profiling
-  cProfile
-  time (GNU Time)
-  timeit
-  Great Circle
-  memoization
-  PyPy
-  Cython
-  cdef

 

 

Required Reading
================

-  Profiling & Timing

   .. raw:: html

      <div class="line-block">

   .. raw:: html

      <div class="line">

   https://docs.python.org/3.6/library/debug.html

   .. raw:: html

      </div>

   .. raw:: html

      <div class="line">

   https://docs.python.org/3.6/library/profile.html

   .. raw:: html

      </div>

   .. raw:: html

      <div class="line">

   https://docs.python.org/3.6/library/timeit.html

   .. raw:: html

      </div>

   .. raw:: html

      </div>

-  PyPy

   .. raw:: html

      <div class="line-block">

   .. raw:: html

      <div class="line">

   http://pypy.org/

   .. raw:: html

      </div>

   .. raw:: html

      </div>

-  Cython

   .. raw:: html

      <div class="line-block">

   .. raw:: html

      <div class="line">

   `http://cython.org <http://cython.org/>`__

   .. raw:: html

      </div>

   .. raw:: html

      </div>

Optional Reading
================

-   Profiling

   .. raw:: html

      <div class="line-block">

   .. raw:: html

      <div class="line">

   https://pypi.python.org/pypi/memory_profiler

   .. raw:: html

      </div>

   .. raw:: html

      <div class="line">

   https://www.jetbrains.com/help/pycharm/profiler.html

   .. raw:: html

      </div>

   .. raw:: html

      </div>

-  https://wiki.python.org/moin/PythonSpeed/PerformanceTips
-  https://www.codementor.io/satwikkansal/python-practices-for-efficient-code-performance-memory-and-usability-aze6oiq65
-  https://nyu-cds.github.io/python-performance-tips/
-  https://pypy.org/performance.html


