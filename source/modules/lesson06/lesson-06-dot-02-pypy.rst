=================
Lesson 06.02 PyPy
=================

PyPy is an alternative Python interpreter focused on performance. It
uses an optimizing just-in-time compiler which is particularly well
suited to long-running programs.

With very large data sets Python sometimes chokes whereas PyPy keeps
going.

PyPy is best evaluated directly vis-a-via the standard CPython reference
interpreter. Profile code under standard Python and then under PyPy.

PyPy can improve code that is factored out to functions, the more
granular the better in some cases. Note that in the video, during the
last timing test with a large number of iterations, PyPy runs faster
with the factored code than the unfactored code. Remember to rely on
timing and profiling to determine the best structure for your use case.

https://github.com/rriehle/ProfilingPerformance/tree/master/source/scripts

{{VIDEO HERE}}
