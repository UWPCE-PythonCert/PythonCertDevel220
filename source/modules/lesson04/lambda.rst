=================
Lesson 4.1 Lambda
=================

{{VIDEO HERE}}

 

.. raw:: html

   <div id="menuheading">

The Lambda special form is Python's syntax for creating an unnamed
function --- a function without a name.  This is its general form:

.. raw:: html

   </div>

::

        lambda arguments: expression

The function evaluates to the result of the expression.  Here is a
lambda that adds one to its argument:

::

        lambda x: x + 1

Here is a lambda that adds its two arguments together:

::

        lambda x, y: x + y

Compare this syntax to that of a standard function definition:

::

        def my_sum(x, y):
            return x + y

This simple function does nothing more than return the value of the
expression in the 'return', so it is viable written on a single line.

::

        def my_sum(x, y): return x + y

Notice how this named function maps directly to its unnamed, lambda
equivalent:

::

        lambda x, y: x + y

Now, unlike most code snippets, if you were to type these examples into
your favorite python interpreter by themselves they would not accomplish
much.

::

        >>> lambda x, y: x + y
        <function <lambda> at 0x104f61e18>

You can't call that, because it has no name.  For all intents and
purposes the anonymous functions were defined, recognized by the python
interpreter as valid, syntactically correct python code, and then
discarded, never to be seen or used again.  You could, however, use the
function immediately by calling it with its required arguments:

::

        >>> (lambda x, y: x + y)(2, 3)
        5

| In this case python defines the anonymous function, calls it with the
  supplied arguments and prints the result, but this feels like we're
  using the python interpreter as little more than a calculator; we are
  not writing useful code.  Indeed simply entering '2 + 3' in the
  interpreter provides the same result with a lot less typing.  So
  what's the point?  Where are lambdas useful?
| Lambdas are only useful within larger code constructs --- specifically
  when defined inline --- and generally as an argument to a function or
  method which is expecting a function.

|
| What is so special about Lambda?  Here is the secret about Lambda:
  there is no secret to lambda.  There is nothing it can do that a
  standard named function cannot do.  It has no special powers aside
  from its ability to be defined inline.  Wherever you can use a Lambda
  you could instead choose to use a standard named function.
| What use is Lambda?  According to Python's creator, not much.

|
| "About 12 years ago, Python aquired lambda, reduce(), filter() and
  map(), courtesy of (I believe) a Lisp hacker who missed them and
  submitted working patches. But, despite of the PR value, I think these
  features should be cut from Python 3000.
| Why drop lambda? Most Python users are unfamiliar with Lisp or Scheme,
  so the name is confusing; also, there is a widespread misunderstanding
  that lambda can do things that a nested function can't -- I still
  recall Laura Creighton's Aha!-erlebnis after I showed her there was no
  difference! Even with a better name, I think having the two choices
  side-by-side just requires programmers to think about making a choice
  that's irrelevant for their program; not having the choice streamlines
  the thought process. Also, once map(), filter() and reduce() are gone,
  there aren't a whole lot of places where you really need to write very
  short local functions; Tkinter callbacks come to mind, but I find that
  more often than not the callbacks should be methods of some
  state-carrying object anyway (the exception being toy programs).
| Update: lambda, filter and map will stay (the latter two with small
  changes, returning iterators instead of lists). Only reduce will be
  removed from the 3.0 standard library. You can import it from
  functools. "
|  -- Guido van Rossum
| http://www.artima.com/weblogs/viewpost.jsp?thread=98196

|
| Why would we teach the Lambda special form if even if Python's creator
  has a low opinion of it?
| You need to understand it, because you are going to see it in the
  wild.
| As to whether you decide to propagate its use, we leave that to you.
