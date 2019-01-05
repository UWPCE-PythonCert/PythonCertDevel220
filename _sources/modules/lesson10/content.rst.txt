#######
Content
#######

Quick Recap
===========

How do metaclasses work?
------------------------
To understand how Python metaclasses work, you need to be very comfortable
with the notion of types in Python.

.. code:: python

    >>> name = "andy"
    >>> print(type(name))
    <class 'str'>
    >>> print(type(str))
    <class 'type'>
    >>> print(type(type))
    <class 'type'>

Remember: every type in Python is defined by a class.

.. code:: python

    >>> class Person:
        pass
    >>> andy = Person()
    >>> print(type(andy))
    <class '__main__.Person'>

A class is just another object and can be modified:

.. code:: python

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


.. code:: python

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

.. code:: python

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

.. code:: python

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
