=======================
Python 220 Week 07 Quiz
=======================



You have a lot of independent computations for perform -- CPU heavy. Which
to use?

multithreading
multiprocessing
async
Not a good idea -- the GIL will keep parallel computation from working.
yup -- no GIL, so true parallelism.
doesn't help here -- async only uses one thread.

#. You have a web service using web sockets. Each request is small and fast,
but you may have lots of clients connected at once. Which to use?

multithreading
multiprocessing
async
With a lot of connected clients, you may have too many threads at once.
If each request is small and fast, no need for multiprocessing.
Yes -- with async you can have may open sockets at once. most of them will be waiting for a response most of the time. each individual request is fast, so no blocking issues.

#. You are a traditional web server: plain old http. each request could
   require a fair bit of database lookups, etc. But only a few clients
   requesting pages at any given moment.
Which to use?

multithreading
multiprocessing
async
Yes -- if each request is spending its time in database lookups, then other
threads can run -- no GIL issues. And each request is independent --
even if you have a lot of clients connected at one time, there will still
only be a moderate number of threads running at once.&lt;/The database is
probably in another process already -- no need for each request to have its
own process.
Not real help from async here -- each request is independent -- not a lot of
connections kept open at once.

The GIL means that Python can't do "real" threading.
True
Python threads are "real" OS threads -- and they work fine if the task is
not spending all its time with the CPU -- waiting for IO, etc. Or if the CPU
intensive part releases the GIL (e.g. numpy and C extensions)
