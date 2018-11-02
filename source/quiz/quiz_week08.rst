=======================
Python 220 Week 08 Quiz
=======================




#. Closures can carry mutable state.
True
False

Like objects (or classes) closures can and often do carry mutable state.

#. Closures encourage direct, external access of their internal attributes.
False
True

Closures, unlike objects (or classes), discourage external access of their internal attributes.  They close around their internal state -- hence their name.  The internal attributes of closures are accessible via the __closure__ dunder, but doing so can lead to hard to understand code and is thus discouraged.

#. What is arity?
Arity relates to the number and types of arguments expected by a function.
Arity is a condition that describes the over-inflation of a call to functools.partial.
Arity is when too few closures have been defined within a system.


#. What is the purpose of currying?
To reduce the number of arguments to a function and thereby make it more composable.
To add spice to your code.
To hide values inside objects.

Currying closes values into the curried function thereby making it more composable.

#. Python offers a library function to facilitate currying.  What is it called?
functools.partial()
__closure__()
__init__()
