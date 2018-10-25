================================
Assignment: Lesson 04 Assignment
================================

Instructions
============

From: \ `Mailroom – metaprogramming
it! <https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/mailroom-meta.html#exercise-mailroom-meta>`__

Mailroom – metaprogramming it!
==============================

So far, your mailroom program may not have any way to save or re-load
the donor data. Some of you may have added code to save and load the
data in a text file or JSON, but even if you have, you might want a more
flexivle and extensible system once your data gets more complicated.

.. raw:: html

   <div id="json" class="section">

.. rubric:: JSON
   :name: json

`JavaScript Object Notation (JSON) <https://www.json.org/>`__\  is a
format borrowed from the Web – Javascript being the de-facto scripting
language in browsers. It is a great format for communicating with
browsers, but it has become a common serialization format for many other
uses: it is simple, flexible, and human-readable and writable.

It also maps pretty much directly to (some of) the core Python
datatypes: lists, dictionaries, strings, and numbers.

So JSON is a nice way to save data for a program like Mailman.

.. raw:: html

   </div>

.. raw:: html

   <div id="goal" class="section">

.. rubric:: Goal
   :name: goal

Your goal is to use a JSON-save system started in the Metaprogramming
Lesson
(`Metaprogramming <https://uwpce-pythoncert.github.io/PythonCertDevel/modules/MetaProgramming.html#metaprogramming>`__)
to make your model classes saveable and loadable as JSON.

YOu can download the package here:

```json_save.zip`` <https://uwpce-pythoncert.github.io/PythonCertDevel/_downloads/json_save.zip>`__

And it may also be in your class repo solutions dir:

``solutions/metaprogramming/json_save/``

You can use either the decorator-based or meta-class based approach.

You may need to extend the JSON-save module a bit to make it work for
you!

When you are done, your class that holds the database of donors and
their data should have \ ``save``\ and \ ``load``\  methods that will,
naturally, save and load the entire dataset.

**Make sure it’s tested!**

.. raw:: html

   </div>

Submitting Your Work 
---------------------

Put the file(s) (ex: a\_new\_file.py) in your student directory in a new
subdirectory named for assignment, and add it to your clone early (git
add a\_new\_file.py). Make frequent commits with good, clear messages
about what you're doing and why.

When you're done and ready for the instructors to review your work, push
your changes to your GitHub fork (git push) and then go to the GitHub
website and make a pull request. Copy the link to the pull request.

Click the *Submit Assignment* button in the upper right.

**Part 1: File(s)**

Use the \ *Choose File* button to find and select the saved .py file or,
if there are multiple files for the assignment, the .zip file.

**Part 2: GitHub Link**

Paste the GitHub link to the pull request in the comments area.

Click the \ *Submit Assignment* button.
