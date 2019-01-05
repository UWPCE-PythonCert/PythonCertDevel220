###################
Lesson 06.03 Cython
###################

{{VIDEO HERE}} {{VIDEO HERE}}

Cython is Python’s bridge to C. In allows you to continue to work
largely in Python, albeit Python with a few extensions, and yet produce
fast, statically compiled libraries to link into your Python code.

Cython provides a keyword, cdef which provides access to C types such as
char, int, long, float, double, struct and enum. It also enables type
delectations for function or method return values. Take for instance the
following function declaration.

.. raw:: html

   <div class="highlight-python">

.. raw:: html

   <div class="highlight">

::

    cdef double great_circle(double lon1, double lat1, double lon2, double lat2):
        cdef double a, b, c, radius, theta, x

.. raw:: html

   </div>

.. raw:: html

   </div>

The great_circle function above is defined by specifying double as the
type of its return value. Each argument is declared to be of type
double, and a series of symbols which will be used later in the function
are all defined to be of type double. The cython compiler uses this
information to produce a statically compiled library which is called
from Python. Since this is no longer standard Python we do not save
the code in files with .py extensions, instead by convention we use .pyx.

Cython involves a different workflow, because it is a statically
compiled environment. Statically compiled programming environments,
including C and Cython, have separate compile, link and run steps. You
can’t simply type your code into an interpreter and get an immediate
result. Statically compiled programming environments also have tooling
to support the static build workflow. These tools include Python’s
distutils used by cython setup files and optionally Gnu Make used to
manage the build dependencies of projects large and small.

This is \ ``great_circle_setup_v1.py``\  which is one of the cython
setup files for use with the Great Circle code.

.. raw:: html

   <div class="highlight-python">

.. raw:: html

   <div class="highlight">

::

    from distutils.core import setup
    from Cython.Build import cythonize

    setup(
        name='Great Circle v1',
        ext_modules=cythonize("great_circle_v1.pyx"),
    )

.. raw:: html

   </div>

.. raw:: html

   </div>

The setup file tells Python how to have Cython build a statically
compiled library to call from within Python.

.. raw:: html

   <div class="highlight-bash">

.. raw:: html

   <div class="highlight">

::

    $ python great_circle_setup_v1.py build_ext --inplace

.. raw:: html

   </div>

.. raw:: html

   </div>

There are two main hurdles in learning to use Cython. The first involves
the extensions to the Python language which are for the most part
borrowed directly from C. Without familiarity with C it may not be clear
what these new language elements mean, or how or why they are used. The
second hurdle involves the build process associated with statically
compiled languages — i.e., the separate compile, link and run steps
which will feel foreign to someone coming strictly from an interpreted
language like Python. In both cases, programmers familiar with C will
have an advantage over those who are not. As with any new worthwhile
programming strategy, it will take an investment in time and effort to
learn this new tool.

The video links start to pull this information together. Arm yourself
with the sample code when you watch Part 2.

https://github.com/rriehle/ProfilingPerformance/tree/master/source/solutions/cython

{{VIDEO HERE}}
