==================================
Office Hours : This weeks' content
==================================
Agenda
------
#. Q+A This week's content
#. Student Demos: This week's content
#. Instructor Demos: This week's content


Processes are running programs. Threads are the unit of execution within a program.


#Thread example

```
import threading

mydata = threading.local()
mydata.x = 1

x=100

print(f"mydata.x is {mydata.x}, x is {x}")


def hello(thread):
    print()
    print(f"hello world from {thread}")

t1 = threading.Timer(3.0, hello, args=('t1',))
t2 = threading.Timer(2.0, hello, args=('t2',))

t1.start()
t2.start()

```


#Process example

```
# run from command prompt
from multiprocessing import Pool
from multiprocessing import Process
import os

def f1(x):
    return x*x

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f2(name):
    info('function f2')
    print('hello', name)


if __name__ == '__main__':

    #part 1 Pool
    with Pool(5) as p1:
        print(p1.map(f1, [10, 11, 12]))
    print()

    # part 2 Process

    info('main line')
    p2 = Process(target=f2, args=('bob',))
    p2.start()
    p2.join()
```


# async coroutines (stop and start again)
An asynchronous program takes one execution step at a time and can move on to the next if the previous one is not finished.

This means we are continuing onward through execution steps of the program, even though a previous execution step (or multiple steps) is running ìelsewhereî. This also implies when one of those execution steps is running ìelsewhereî completes, our program code somehow has to handle it.


##Async example

```
import asyncio

async def say(what, when):
    await asyncio.sleep(when)
    print(what)

async def stop_after(loop, when):
    await asyncio.sleep(when)
    loop.stop()


loop = asyncio.get_event_loop()

loop.create_task(say('first hello', 2))
loop.create_task(say('second hello', 1))
loop.create_task(say('third hello', 4))
loop.create_task(stop_after(loop, 3))

loop.run_forever()
loop.close()

```
