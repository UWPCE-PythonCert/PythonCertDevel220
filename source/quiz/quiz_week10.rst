=======================
Python 220 Week 10 Quiz
=======================


#. Which of these types are not "regular objects" in Python?
Integers
Strings
Functions created with "def"
Class Instances
Classes created with "class"

All of them! Everything in Python is an object -- they can be assigned
names, passed to functions, introspected, etc.

#. setattr(object, att_name, att_value) Is exactly the same as
object.att_name = att_value

True
False

Not quite!
#. setattr(object, att_name, _att_value) lets you use ANY string as an
   att_name -- even ones that aren't legal python names.

#. An object's: __dict__ Is always an actual dictionary
True
False

#. What is the class of a class object (created with the class keyword)?
type: class
type: object
type: metaclass
type: type
The type of a class object is "type" -- "class" and "type" mean the same
thing in Python.

#. Which of these special methods is run first when you create a new class
   object with a metaclass?&lt;/p&gt;

__new__
__init__

#. Using metaclasses or class decorators can impact performance, as there is
   extra code being run every time you make a new instance of a  class.
True
False
metaclasses and class decorators are both applied at module import time:
when the class object is created. So there is no real overhead at runtime,
when new instances are created -- or when instances are used.
