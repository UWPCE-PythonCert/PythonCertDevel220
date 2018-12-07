#############################################
Threading and multiprocessing Part 6: Pooling
#############################################

A processing pool contains worker processes with only a configured
number running at one time.

.. code-block:: python

    from multiprocessing import Pool
    pool = Pool(processes=4)

The Pool module has several methods for adding jobs to the pool.

``apply_async(func[, args[, kwargs[, callback]]])``

``map_async(func, iterable[, chunksize[, callback]])``


Pooling example
---------------

.. code-block:: python

    from multiprocessing import Pool
    def f(x):
        return x*x
    if __name__ == '__main__':
        pool = Pool(processes=4)

        result = pool.apply_async(f, (10,))
        print(result.get(timeout=1))
        print(pool.map(f, range(10)))

        it = pool.imap(f, range(10))
        print(it.next())
        print(it.next())
        print(it.next(timeout=1))

        import time
        result = pool.apply_async(time.sleep, (10,))
        print(result.get(timeout=1))

http://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.pool


ThreadPool
----------

Threading also has a pool.

Confusingly, it lives in the multiprocessing module.

.. code-block:: python

    from multiprocessing.pool import ThreadPool
    pool = ThreadPool(processes=4)


.. Threading versus multiprocessing, networking edition
.. ----------------------------------------------------

.. :download:`server.zip <../examples/threading-multiprocessing/server.zip>`

.. We're going to test making concurrent connections to a web service in:

.. ``server/app.py``

.. It is a WSGI application which can be run with Green Unicorn or another WSGI server

.. ``$ gunicorn app:app --bind 0.0.0.0:37337``

.. ``client-threading.py`` makes 100 threads to contact the web service

.. ``client-mp.py`` makes 100 processes to contact the web service

.. ``client-pooled.py`` creates a ThreadPool

.. ``client-pooled.py`` contains a results Queue, but doesn't use it. Can you collect all the output from the pool into a single data structure using this Queue?