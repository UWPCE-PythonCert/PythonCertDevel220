##################
Part 1: Background
##################

Here we are going to cover the background to why we use databases, and
set the stage for later, when we will start to develop a Python database
application.

You will probably wish to clone the repository you can find on
`GitHub <https://github.com/UWPCE-PythonCert/PythonCertDevel220/tree/master/source/code/lesson03>`__. 
These are the files we refer to in the videos
and they are included here, below the video:

|v1files.png|

Windows only
============

Note: If you are using Windows, you will need to install sqlite. Here's how:

  On Windows, unlike Linux and Mac, sqlite is not installed with Python. As
  always, there are many ways to install sqlite, but the easiest way is with pip.
  Open a command prompt (press the Windows key, type cmd and press enter).

  At the command prompt enter the following command:

  .. code:: bash

      pip install pysqlite3

  Now, type the following command:

  .. code:: bash

      sqlite3

  And you should see the sqlite prompt. Type the quit command to return to the command prompt:

  .. code:: bash
  
      .quit

Storing data
============


{{VIDEO HERE}} 

People file:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    """
    write a csv file
    data is "anonymous" (no schema)

    Creates a file that looks like this:

    John,502-77-3056,2/27/1985,117.45

    """

    import csv

    peopledata = ['John', '502-77-3056', '2/27/1985', 117.45]

    with open('simple_data_write.csv', 'w') as people:
        peoplewriter = csv.writer(people)
        peoplewriter.writerow(peopledata)

.. raw:: html

   </div>

Schema file:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    'Person Name','SSN','BirthDate','Account Balance'
    'John','502-77-3056','2/27/1985','117.45'

.. raw:: html

   </div>


We have covered the basis of data definition, and why it is important.
We now know what a schema is and why it is important. Now we can start
to write a Python program that uses a database.

