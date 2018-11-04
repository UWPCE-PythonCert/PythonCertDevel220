=====================
Lesson 02.01 Closures
=====================

 

{{VIDEO HERE}}

.. raw:: html

   <div id="menuheading">

.. rubric:: Closures 
   :name: closures
   :class: caH2

.. raw:: html

   <div style="padding-left: 30px;" role="navigation">

The venerable master Qc Na was walking with his student, Anton. Hoping
to prompt the master into a discussion, Anton said "Master, I have heard
that objects (and classes) are a very good thing - is this true?" Qc Na
looked pityingly at his student and replied, "Foolish pupil - objects
are merely a poor man's closures."\*
Chastised, Anton took his leave from his master and returned to his
cell, intent on studying closures. He carefully read the entire "Lambda:
The Ultimate..." series of papers and its cousins, and implemented a
small Scheme interpreter with a closure-based object system. He learned
much, and looked forward to informing his master of his progress.\*
On his next walk with Qc Na, Anton attempted to impress his master by
saying "Master, I have diligently studied the matter, and now understand
that objects are truly a poor man's closures." Qc Na responded by
hitting Anton with his stick, saying "When will you learn? Closures are
a poor man's object." At that moment, Anton became enlightened.

.. raw:: html

   </div>

From: http://wiki.c2.com/?ClosuresAndObjectsAreEquivalent

What exactly are Closures, these mysterious things that offer
programming enlightenment? Let's continue to compare and contrast
closures with objects.

-  Objects have methods.
-  Closures \*are\* methods --- they are defined and behave like
   functions, but like object methods they carry internal state and take
   it into account when returning results.
-  Objects can, and generally do, carry mutable state.
-  Closures can, and often do, carry mutable state.
-  Objects control access to their attributes --- their internal state
   --- through Properties and Python's lexical scoping rules. By default
   however object attributes are externally accessible.
-  Closures by nature tend to close around their internal state and
   thereby prevent external access, thus in terms of access to internal
   state, internal attributes, this is the opposite of the default
   behavior of an object. In accordance with Python's Consenting Adults
   policy a closure's internal state is still accessible via its
   \_\_closure\_\_() dunder, but this violates the spirit of a closure
   --- so do so at your own risk.

Thus, objects (or classes) and closures are similar, but different.

This is the general form of a closure:

::

         def closure(internal_state):  # line 1
             def return_function(arguments):  # line 2
                 return internal_state combined with arguments  # line 3
             return return_function  # line 4

Let's unpack that line by line.

#. The closure is defined like any other function with a name and
   arguments. In this case the name of the function is closure and its
   arguments are internal\_state.
#. Inside the closure another function is defined. It too takes
   arguments. In this case its name is return\_function, because *this
   internally defined function itself will be returned by the closure*.
#. When calculating a return value the internal function,
   return\_function, uses both the internal state passed into the
   closure on line 1 when the closure was first defined, and also the
   arguments that will be passed into it later when it is used as a
   stand-alone function.
#. The closure uses the *internally defined* function, return\_function,
   for its return value.  Thus, just as a class is a template or factory
   for creating stateful objects, a closure is a template or factory for
   creating stateful functions, that is, stand-alone methods.

.. raw:: html

   </div>
