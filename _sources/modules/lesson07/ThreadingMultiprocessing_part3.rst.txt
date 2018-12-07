######################################################
Threading and multiprocessing Part 3: Locking Exercise
######################################################

:download:`lock_exercise.zip <../examples/threading-multiprocessing/lock_exercise.zip>`

In: ``lock/stdout_writer.py``

Multiple threads in the script write to stdout, and their output gets
jumbled

1. Add a locking mechanism to give each thread exclusive access to
   stdout.

2. Try adding a Semaphore to allow 2 threads access at once.

.. TODO:: 
    Review lock_exercise.zip

