=================
Lesson 04 Content
=================

.. raw:: html

   <div id="menuheading">

.. rubric:: Metaprogramming Tutorial Videos
   :name: metaprogramming-tutorial-videos
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

Namespaces
==========

Python makes great use of namespaces: different scopes and places to
store names. Many of these namespaces (class instances, etc) are stored
as Python dictionaries which makes it very easy to introspect and
manipulate the names in objects.

 

{{VIDEO HERE}}

Metaprogamming
==============

Metaprogramming is the process of writing programs that write programs
-- that is, programs that manipulate the code objects themselves. Python
provides a number of tools that allow introspection, or determining the
nature of objects at runtime, as well as tools to change code at runtime
-- these are the tools of metaprogramming.

 

{{VIDEO HERE}}
==============

Class Objects
=============

Classes are how you create custom types in Python. If you want to
manipulate how classes work and are created, you need to have a
understanding of how class objects themselves are put together.

{{VIDEO HERE}}
==============

Metaclasses
===========

Metaprogramming is writing programs that create programs, so metaclasses
are classes that make classes.  Here’s another way to think about it:

Objects get created from classes. So what is the class of a class?

The class of a Class is a metaclass.


{{VIDEO HERE}}
==============

.. todo::
    Add metaprogramming example code

