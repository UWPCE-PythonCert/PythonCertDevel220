sqlite3 Windows install
=======================
.. todo::
    Find correct home for sqlite install on windows

On Windows, unlike Linux and Mac, sqlite is not installed with Python. As always, there are many ways to install sqlite, but the easiest way is with pip.
Open a command prompt (press the Windows key, type cmd and press enter).

At the command prompt enter the following command:
.. cdoe::
    pip install pysqlite3

Now, type the following command:
.. cdoe::
    sqlite3

And you should see the sqlite prompt. Type the quit command to return to the command prompt:
.. cdoe::
    .quit
