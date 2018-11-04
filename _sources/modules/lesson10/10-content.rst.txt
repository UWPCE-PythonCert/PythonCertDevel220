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

Why metaprogramming?
====================

Developers are always looking for ways to make the development process
faster, while developing better quality code that is easier to understand,
test and maintain.
Metaprogramming allows a program to modify itself, effectively adding
functionality that another developer using that functionality will get
"for free". Remember the lesson on relational databases, using PeeWee?
Remember how certain functionality appeared without us having to do anything?
That was metaprogramming working for us.

Now, metaprogramming is another of those techniques, like OO and functional
programming, that requires a shoft in mindset to really make it work
effectively. Understanding the syntax is one thing; understanding the right
way to apply the syntax is another altogether.

In this lesson we will certaonly cover the sytax, and you will start to
understand how metaprogramming works. But you may feel lost or confused
about why you would even want to use this technique. For now, as long as you
 understand the syntax, that is the minimum necessary. Then, later, you
 should be able to spot development problems for which metaprogramming is
a good solution. That's great! Then you work out how, maybe wiht the help of
 books or another developer.

So let's get started. But before we launch into metaprogramming itself, it's
 important you understand the concept of namespaces.


Namespaces
==========

Python makes great use of namespaces. Namespaces can be thought of as
sections of a program, such as classes, functions and modules, in which
variables live and retain their values. They are thus places in which
variable names are valid and in scope.

Many of these namespaces (class instances, etc) are stored
internally as Python dictionaries, which makes it very easy to introspect
and manipulate the names in objects. And that is a hint that will help you
to start to understand metaprogramming.
 

{{VIDEO HERE}}

Metaprogamming
==============

Metaprogramming is the process of writing programs that write programs
-- that is, programs that manipulate the code objects themselves. Python
provides a number of tools that allow introspection, or determining the
nature of objects at runtime, as well as tools to change code at runtime.
These are the tools of metaprogramming.


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

Quick Recap
===========

How do metaclasses work?
------------------------
To understand how Python metaclasses work, you need to be very comfortable
with the notion of types in Python.

.. code::python
    >>> name = "andy"
    >>> print(type(name))
    <class 'str'>
    >>> print(type(str))
    <class 'type'>
    >>> print(type(type))
    <class 'type'>

Remember: every type in Python is defined by a class.

.. code::python
    >>> class Person:
        pass
    >>> andy = Person()
    >>> print(type(andy))
    <class '__main__.Person'>

A class is just another object and can be modified:

.. code::python
    >>> andy.dob = "2/27/1960"
    >>> print(andy.dob)
    2/27/1960

Hence, Metaclasses modifying classes.


Creating custom Metaclass
-------------------------
In Python you can assign a metaclass to the creation of a new class by
passing in the intended masterclass to the new class definition.

The type type, as the default metaclass in Python, defines special methods
that new metaclasses can override to implement unique code generation
behavior. Here is a brief overview of these "magic" methods that exist on
metaclass:

* ```__new__```: This method is called on the Metaclass before an instance of a class based on the metaclass is created
* ```__init__```: This method is called to set up values after the instance/object is created
* ```__prepare__```: Defines the class namespace in a mapping that stores the attributes
* ```__call__```: This method is called when the constructor of the new class is to be used to create an object

These are the methods to override in your custom metaclass to give your
classes behavior different from that of type, which is the default metaclass.

To create our custom metaclass, it must inherit type and will often override:
* ```__new__()```: It’s a method which is called before ```__init__()```. It creates the object and return it. We can override this method to control how the objects are created.
* ```__init__()```: This method initializes the created object passed as parameter


.. code::python
    # our metaclass
    class MultiBases(type):
        # overriding __new__ method
        def __new__(cls, clsname, bases, clsdict):
            # if no of base classes is greator than 1
            # raise error
            if len(bases)>1:
                raise TypeError("Inherited multiple base classes!!!")

            # else execute __new__ method of super class, ie.
            # call __init__ of type class
            return super().__new__(cls, clsname, bases, clsdict)

    # metaclass can be specified by 'metaclass' keyword argument
    # now MultiBase class is used for creating classes
    # this will be propagated to all subclasses of Base
    class Base(metaclass=MultiBases):
        pass

    # no error is raised
    class A(Base):
        pass

    # no error is raised
    class B(Base):
        pass

    # This will raise an error!
    class C(A, B):
        pass

Note: Decorators can achieve the same code-transformation behavior of
metaclasses, but are much simpler.

A quote by Tim Peters
-----------------------
"Metaclasses are deeper magic that 99% of users should never worry about. If
 you wonder whether you need them, you don’t (the people who actually need
 them know with certainty that they need them, and don’t need an explanation
  about why)."


An example
==========

.. code::python

    # This metaclass adds a 'hello' method to classes that use the metaclass
    # Such classes get a 'hello' method with no extra effort
    # The metaclass takes care of that for us

    class HelloMeta(type):
        # A hello method
        def hello(cls):
            print("greetings from %s, a HelloMeta type class" % (type(cls())))

        # Call the metaclass
        def __call__(self, *args, **kwargs):
            # create the new class as normal
            cls = type.__call__(self, *args)

            # define a new hello method for each of these classes
            setattr(cls, "hello", self.hello)

            # return the class
            return cls

    # Try out the metaclass
    class TryHello(object, metaclass=HelloMeta):
        def greet(self):
            self.hello()

    # Create an instance of the metaclass. It should automatically have a hello method
    # even though one is not defined manually in the class
    # in other words, it is added for us by the metaclass
    greeter = TryHello()
    greeter.greet()


The result of running this code is that the new TryHello class is able to
printout a greeting that says:

.. code::python
    greetings from <class '__main__.TryHello'>, a HelloMeta type class


The method responsible for this printout is not declared in the declaration
of the class. Rather, the metaclass, which is HelloMeta in this case,
generates the code at run time that automatically affixes the method to the
class.

Rather than get an error for calling a method that does not exist, TryHello
gets such a method automatically affixed to it due to using the HelloMeta
class as its metaclass.

Metaclasses give us the ability to write code that transforms, not just
data, but other code, e.g. transforming a class at the time when it is
instantiated. In the example above, our metaclass adds a new method
automatically to new classes that we define to use our metaclass as their
metaclass.



