======================
Lesson 04 Introduction
======================

.. raw:: html

   <div id="menuheading">

.. rubric:: Metaprogramming
   :name: metaprogramming
   :class: caH2

.. raw:: html

   <div id="navbar" class="caNav grid-row around-md clearunderlinestyle"
   role="navigation">

`Introduction <%24WIKI_REFERENCE%24/pages/lesson-04-introduction>`__ \|
`Content <%24WIKI_REFERENCE%24/pages/lesson-04-content>`__ \|
`Quiz  <%24CANVAS_OBJECT_REFERENCE%24/quizzes/i13b71605c62c3cd78ebd595c20e90e67>`__\ \|
Activity \|
`Assignment <%24CANVAS_OBJECT_REFERENCE%24/assignments/ie56dae8f75ae35df42a7bc6747d8c572>`__
\| `Code
Talk <%24CANVAS_OBJECT_REFERENCE%24/discussion_topics/i4df1858495d80dbc0637bfdc8f754051>`__

.. raw:: html

   </div>

.. raw:: html

   </div>

Introduction
============

Metaprogramming is a programming technique in which computer programs
have the ability to treat programs as their data. In other words: A
metaprogram is a program that writes (or modifies) programs.  As a
dynamic language, Python is very well suited to metaprogramming, as it
allows objects to be modified at runtime. 

In this lesson, we will learn about the tools python provides for
metaprogramming, and the structure of objects that can be manipulated.

Learning Objectives
===================

Upon successful completion of this lesson, you will be able to:

-  Use the core getattr() and setattr() functions to manipulate object's
   attributes.
-  Access the namespaces of various objects to inspect or update them.
-  Use the type() function to create a new class from scratch.
-  Write a basic metaclass to create custom classes on the fly.
-  Write a class decorator that can customize class definitions.

 

New Words, Concepts, and Tools
==============================

-  metaprograming
-  getattr() and setattr()
-  The type() constructor
-  metaclasses
-  class decorators 

 

Required Reading
================

-  `Metaprogramming
   Notes <https://uwpce-pythoncert.github.io/PythonCertDevel/modules/MetaProgramming.html>`__

 

Optional Reading
================

*Fluent Python*\ : Chapters 19 – 21

-  `About
   metaclasses <http://blog.thedigitalcatonline.com/blog/2014/09/01/python-3-oop-part-5-metaclasses>`__

-  `What is a metaclass in
   Python? <http://stackoverflow.com/a/6581949/747729>`__

-  `Python metaclasses by
   example: <http://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example/>`__

-  `A Primer on Python
   Metaclasses: <http://jakevdp.github.io/blog/2012/12/01/a-primer-on-python-metaclasses/>`__

-  `Advanced use of Python decorators and
   metaclasses <http://blog.thedigitalcatonline.com/blog/2014/10/14/decorators-and-metaclasses>`__
