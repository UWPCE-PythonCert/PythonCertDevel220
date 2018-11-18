######################
Lesson 10 Introduction
######################

Introduction
============

Metaprogramming is a programming technique in which computer programs
have the ability to treat programs as their data. In other words: A
metaprogram is a program that writes (or modifies) programs.  As a
dynamic language, Python is very well suited to metaprogramming, as it
allows objects to be modified at runtime. 

In this lesson, we will learn about the tools Python provides for
metaprogramming, and the structure of objects that can be manipulated.
We will also answer the question "why would I want to do this"!

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

-  Metaprograming
-  ``getattr()`` and ``setattr()``
-  The ``type()`` constructor
-  Metaclasses
-  Class Decorators 

 

Required Reading
================

-  `Metaprogramming
   Notes <https://uwpce-pythoncert.github.io/PythonCertDevel/modules/MetaProgramming.html>`__
-  https://realpython.com/python-metaclasses/


Optional Reading
================

*Fluent Python*\ : Chapters 19 – 21

-  `Concept overview
   <https://www.geeksforgeeks.org/metaprogramming-metaclasses-python/>`_

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

-  https://realpython.com/python-metaclasses/
-  https://medium.com/@guoxing/brief-intro-to-metaprogramming-with-python-a278fc104b3b
-  https://stackabuse.com/python-metaclasses-and-metaprogramming/
-  https://www.ibm.com/developerworks/library/ba-metaprogramming-python/index.html
