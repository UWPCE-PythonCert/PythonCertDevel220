########
Activity
########

Your assignment is to complete testing and linting on the calculator
from the lesson content. As a first step, review the videos and writing
on that page. Then find the calculator project directory in the course
repository.

Your goals:
===========

Note that all of the command examples below should be run from inside
the project root which contains the *test_unit.py*
and *test_integration.py* files.

#. Provide a *MultiplierTests* and *DividerTests* test classes in
   the *test_unit.py* file.
#. *python -m unittest test_unit.py*  and *python -m unittest
   test_integration.py* should have no failures.
#. Running *coverage* run --source=calculator -m unittest test_unit.py;
   coverage report* * * shows 90%+ coverage..
#. Satisfy the linter such that *pylint calculator* gives no errors
   and *flake8 calculator* gives no errors. You can achieve this by some
   combination of editing your code and editing the *.pylintrc* file
   to ignore certain violations

Prepare the results, and prepare to demo them!
