=================
Lesson 2 Activity
=================

.. raw:: html

   <div id="menuheading">

.. rubric:: Logging and Debugging
   :name: logging-and-debugging
   :class: caH2

.. raw:: html

   <div id="navbar" class="caNav grid-row around-md clearunderlinestyle"
   role="navigation">

`Introduction <%24WIKI_REFERENCE%24/pages/lesson-05-introduction>`__ \|
`Content <%24WIKI_REFERENCE%24/pages/lesson-05-content>`__ \|
`Quiz <%24CANVAS_OBJECT_REFERENCE%24/quizzes/ie7895b971d4a0e2e35b415eb863435b0>`__ \|
`Activity <%24CANVAS_OBJECT_REFERENCE%24/assignments/i89c943e0018a913b1c51e640fa38f289>`__
\|
`Assignment <%24CANVAS_OBJECT_REFERENCE%24/assignments/i6935f2eba782af5becab9aa3ea3829ca>`__
\| `Code
Talk <%24CANVAS_OBJECT_REFERENCE%24/discussion_topics/i72c5561508c841b38aa31c3d12c9e1c7>`__

.. raw:: html

   </div>

.. raw:: html

   </div>

 
In the lesson content, we asked you to spend 5-10 minutes on your own
debugging the recursion error exercise code. After doing so, do the following:

#. In very general terms, use a couple of sentences to address the
   problem with our code. For example, give your best guess or insight
   on the following questions:

   -  What is wrong with our logic?
   -  Why doesn't the function stop calling itself?
   -  What's happening to the value of 'n' as the function gets deeper
      and deeper into recursion?

#. A copy-and-paste of your terminal debugging activity.

Demstrating your work 
=====================

Either gring your work to class or office hours, or show your instructor.
 For example, you might produce:

::

    The function keeps calling itself and calling itself and it can't stop because
    it's a Tuesday today and Tuesdays are bad for recursion.

    Below is my debugging log:
    $ python -m pdb recursive.py
    > c:\users\jschilz\onedrive\py300\debugging\recursive.py(1)<module>()
    -> import sys
    (Pdb) ll
     1 -> import sys
     2
     3
     4 def my_fun(n):
     5 if n == 2:
     6 return True
     7
     8 return my_fun(n/2)
     9
     10
     11 if __name__ == '__main__':
     12 n = int(sys.argv[1])
     13 print(my_fun(n))
    (Pdb) n
    > c:\users\jschilz\onedrive\py300\debugging\recursive.py(4)<module>()
    -> def my_fun(n):
    (Pdb)

Of course, your answer will be more insightful and your debugging log
will be longer.
