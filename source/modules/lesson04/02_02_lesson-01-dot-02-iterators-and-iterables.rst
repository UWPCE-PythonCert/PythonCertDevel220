====================================
Lesson 01.02 Iterators and Iterables
====================================

Python used to be all about sequences --- a good chunk of anything you
did was stored in a sequence or involved manipulating a sequence.

-  lists

-  tuples

-  strings

-  dict.keys()

-  dict.values()

-  dict.items()

-  zip()


  In **python2** those are all sequences.  It turns out, however, that
  the most common operation for sequences is to iterate through them:

::

        for item in a_sequence:
            do_something_with_item

| 
| So fairly early in Python2, Python introduced the idea of the
  "iterable".  An iterable is something you can, well, iterate over in a
  for loop, but often does not keep the whole sequence in memory at
  once.  After all, why make a copy of something just to look at all its
  items?
| For example, in python2: \`\`dict.keys()\`\` returns a list of all the
  keys in the dict.  But why make a full copy of all the keys, when all
  you want to do is:
|     for key in dict.keys():
|         do\_something\_with(key)

|  
| Even worse \`\`dict.items()\`\` created a full list of
  \`\`(key,value)\`\` tuples --- a complete copy of all the data in the
  dict.  Yet worse \`\`enumerate(dict.items())\`\` created a whole list
  of
| \`\`(index, (key, value))\`\` tuples --- lots of copies of everything.
| Python2 then introduced "iterable" versions of a number of functions
  and methods:

| 
| itertools.izip
| dict.iteritems()
| dict.iterkeys()
| dict.itervalues()

| 
| So you could now iterate through that stuff without copying anything.

| 
| **Python3** embraces iterables --- now everything that could be an
  iterator is already an iterator --- no unnecessary copies.  An
  iterator is an iterable that has been made more efficient by removing
  as much from memory as possible.  You have to make a list out of them
  explicitly if you really want it:

::


    list(dict.keys())

 

Then there is an entire module: \`\`itertools\`\` that provides nifty
ways to iterate through stuff.  So while we used to think in terms of
sequences we now think in terms of iterables.

| 
| Iterators and Iterables
| Iteration is one of the main reasons Python code is so readable:
| .. code-block:: python
|     for x in just\_about\_anything:
|         do\_stuff(x)
| An iterable is anything that can be looped over sequentially, so it
  does not have to be a "sequence": list, tuple, etc.  For example, a
  string is iterable. So is a set.
| An iterator is an iterable that remembers state. All sequences are
  iterable, but not all sequences are iterators. To make a sequence an
  iterator, you can call it with iter:
| .. code-block:: python
|    my\_iter = iter(my\_sequence)
| Iterables
| ---------
| To make an object iterable, you simply have to implement the
  \_\_getitem\_\_ method.
| .. code-block:: python
|     class T:
|         def \_\_getitem\_\_(self, position):
|             if position > 5:
|                 raise IndexError
|             return position
| iter()
| ------
| How do you get the iterator object from an "iterable"?  The iter()
  function will make any iterable an iterator.  It first looks for the
  \_\_iter\_\_() method, and if none is found, uses get\_item to create
  the iterator.  The \`\`iter()\`\` function:
| .. code-block:: ipython
|     In []: iter([2,3,4])
|     Out[]: <listiterator at 0x101e01350>
|     In []: iter("a string")
|     Out[]: <iterator at 0x101e01090>
|     In []: iter( ('a', 'tuple') )
|     Out[]: <tupleiterator at 0x101e01710>
| List as an Iterator
| -------------------
| .. code-block:: ipython
|     In []: a\_list = [1,2,3]
|     In []: list\_iter = iter(a\_list)
|     In []: next(list\_iter)
|     Out[]: 1
|     In []: next(list\_iter)
|     Out[]: 2
|     In []: next(list\_iter)
|     Out[]: 3
|     In []: next(list\_iter)
|     --------------------------------------------------
|     StopIteration     Traceback (most recent call last)
|     <ipython-input-15-1a7db9b70878> in <module>()
|     ----> 1 next(list\_iter)
|     StopIteration:
| Use iterators when you can
| --------------------------
| Consider the example from the trigrams problem:
| (http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/)
| You have a list of words and you want to go through it, three at a
  time, and match up pairs with the following word.
| The \*non-pythonic\* way to do that is to loop through the indices:
| .. code-block:: python
|     for i in range(len(words)-2):
|         triple = words[i:i+3]
| It works, and is fairly efficient, but what about:
| .. code-block:: python
|     for triple in zip(words[:-2], words[1:-1], words[2:-2]):
| zip() returns an iterable --- it does not build up the whole list, so
  this is quite efficient.  However, we are still slicing: ([1:]), which
  produces a copy --- so we are creating three copies of the list ---
  not so good if memory is tight.  Note that they are shallow copies, so
  this is not terribly bad.  Nevertheless, we can do better.
| The \`\`itertools\`\` module has a \`\`islice()\`\` (iterable slice)
  function.  It returns an iterator over a slice of a sequence --- so no
  more copies:
| .. code-block:: python
|     from itertools import islice
|     triplets = zip(words, islice(words, 1, None), islice(words, 2,
  None))
|     for triplet in triplets:
|         print(triplet)
|     ('this', 'that', 'the')
|     ('that', 'the', 'other')
|     ('the', 'other', 'and')
|     ('other', 'and', 'one')
|     ('and', 'one', 'more')
| The Iterator Protocol
| ----------------------
| The main thing that differentiates an iterator from an iterable
  (sequence) is that an iterator saves state.  An iterable must have the
  following methods:
| .. code-block:: python
|     an\_iterator.\_\_iter\_\_()
| Usually returns the iterator object itself.
| .. code-block:: python
|     an\_iterator.\_\_next\_\_()
| Returns the next item from the container. If there are no further
  items it raises the \`\`StopIteration\`\` exception.
| Making an Iterator
| -------------------
| A simple version of \`\`range()\`\`

::

        class IterateMe_1:
            def __init__(self, stop=5):
                self.current = 0
                self.stop = stop
            def __iter__(self):
                return self
            def __next__(self):
                if self.current < self.stop:
                    self.current += 1
                    return self.current
                else:
                    raise StopIteration

 

| What does for do?
| Now that we know the iterator protocol, we can write something like a
  for loop:
| :download:\`my\_for.py
  <../examples/iterators\_generators/my\_for.py>\`
| .. code-block:: python
|     def my\_for(an\_iterable, func):
|         """
|         Emulation of a for loop.
|         func() will be called with each item in an\_iterable
|         """
|         # equiv of "for i in l:"
|         iterator = iter(an\_iterable)
|         while True:
|             try:
|                 i = next(iterator)
|             except StopIteration:
|                 break
|             func(i)
