=====================
Lesson 02.02 Currying
=====================

https://rriehle.github.io/FP3/build/html/index.html#currying

{{VIDEO HERE}}

.. raw:: html

   <div id="currying" class="section">

.. rubric:: Currying\ ` <https://rriehle.github.io/FP3/build/html/index.html#currying>`__
   :name: currying

“Currying” is a special case of closures:

The idea behind currying is that you may have a function with a number
of parameters, and you want to make a specialized version that function
with a couple parameters pre-set.

.. raw:: html

   <div id="real-world-example" class="section">

.. rubric:: Real world
   Example\ ` <https://rriehle.github.io/FP3/build/html/index.html#real-world-example>`__
   :name: real-world-example

I was writing some code to compute the concentration of a contaminant in
a river, as it was reduced by exponential decay, defined by a half-life:

https://en.wikipedia.org/wiki/Half-life

So I wanted a function that would compute how much the concentration
would reduce as a function of time – that is:

.. raw:: html

   <div class="highlight-python">

.. raw:: html

   <div class="highlight">

::

    def scale(time):
        return scale_factor

.. raw:: html

   </div>

.. raw:: html

   </div>

The trick is, how much the concentration would be reduced depends on
both time and the half life. And for a given material, and given flow
conditions in the river, that half life is pre-determined. Once you know
the half-life, the scale is given by:

scale = 0.5 \*\* (time / (half\_life))

So to compute the scale, I could pass that half-life in each time I
called the function:

.. raw:: html

   <div class="highlight-python">

.. raw:: html

   <div class="highlight">

::

    def scale(time, half_life):
        return 0.5 ** (time / (half_life))

.. raw:: html

   </div>

.. raw:: html

   </div>

But this is a bit klunky – I need to keep passing that half\_life
around, even though it isn’t changing. And there are places, like
``map`` that require a function that takes only one argument!

What if I could create a function, on the fly, that had a particular
half-life “baked in”?

*Enter Currying* – Currying is a technique where you reduce the number
of parameters that function takes, creating a specialized function with
one or more of the original parameters set to a particular value. Here
is that technique, applied to the half-life decay problem:

.. raw:: html

   <div class="highlight-python">

.. raw:: html

   <div class="highlight">

::

    def get_scale_fun(half_life):
        def half_life(time)
            return 0.5 ** (time / half_life)
        return half_life

.. raw:: html

   </div>

.. raw:: html

   </div>

**NOTE:** This is simple enough to use a lambda for a bit more compact
code:

.. raw:: html

   <div class="highlight-python">

.. raw:: html

   <div class="highlight">

::

    def get_scale_fun(half_life):
        return lambda time: 0.5 ** (time / half_life)

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="using-the-curried-function" class="section">

.. rubric:: Using the Curried
   Function\ ` <https://rriehle.github.io/FP3/build/html/index.html#using-the-curried-function>`__
   :name: using-the-curried-function

Create a scale function with a half-life of one hour:

.. raw:: html

   <div class="highlight-ipython">

.. raw:: html

   <div class="highlight">

::

    In [8]: scale = get_scale_fun(1)

    In [9]: [scale(t) for t in range(7)]
    Out[9]: [1.0, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625]

.. raw:: html

   </div>

.. raw:: html

   </div>

The value is reduced by half every hour.

Now create one with a half life of 2 hours:

.. raw:: html

   <div class="highlight-ipython">

.. raw:: html

   <div class="highlight">

::

    In [10]: scale = get_scale_fun(2)

    In [11]: [scale(t) for t in range(7)]
    Out[11]:
    [1.0,
     0.7071067811865476,
     0.5,
     0.3535533905932738,
     0.25,
     0.1767766952966369,
     0.125]

.. raw:: html

   </div>

.. raw:: html

   </div>

And the value is reduced by half every two hours…

And it can be used with ``map``, too:

.. raw:: html

   <div class="highlight-ipython">

.. raw:: html

   <div class="highlight">

::

    In [13]: list(map(scale, range(7)))
    Out[13]:
    [1.0,
     0.7071067811865476,
     0.5,
     0.3535533905932738,
     0.25,
     0.1767766952966369,
     0.125]

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="functools-partial" class="section">

.. rubric:: ``functools.partial``\ ` <https://rriehle.github.io/FP3/build/html/index.html#functools-partial>`__
   :name: functools.partial

The ``functools`` module in the standard library provides utilities for
working with functions:

https://docs.python.org/3.5/library/functools.html

Creating a curried function turns out to be common enough that the
``functools.partial`` function provides an optimized way to do it:

What functools.partial does is:

    .. raw:: html

       <div>

    -  Makes a new version of a function with one or more arguments
       already filled in.
    -  The new version of a function documents itself.

    .. raw:: html

       </div>

Example:

.. raw:: html

   <div class="highlight-python">

.. raw:: html

   <div class="highlight">

::

    def power(base, exponent):
        """returns based raised to the give exponent"""
        return base ** exponent

.. raw:: html

   </div>

.. raw:: html

   </div>

Simple enough. but what if we wanted a specialized ``square`` and
``cube`` function?

We can use ``functools.partial`` to *partially* evaluate the function,
giving us a specialized version:

.. raw:: html

   <div class="highlight-python">

.. raw:: html

   <div class="highlight">

::

    square = partial(power, exponent=2)
    cube = partial(power, exponent=3)

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>
