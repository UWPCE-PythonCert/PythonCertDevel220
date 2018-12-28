###########
Assignments
###########

Introduction
============
An important part of your success on this class is the work you do on
the class assignments. Here we describe the approach we are using for
stroing and submitting you assignment work.

As with every part of Python 220 we are going to get as close as we can
to replicating the way that we work in a professional setting.

So now let's go through all of the steps.

Prior to starting, be sure you have your Git repo url from your instructor.

Part 1 - Setup
--------------
You will do this once, at the start of class.

1. Your repository url will look something like this:

    git@github.com:UWPCE-PythonCert/py220yyyymmxxx.git

 with the name being this part:

    py220yyyymmxxx

yyyy and mm are the start of the class, and xxx is your initials.

2. Start by making a repo directory on your development computer. The directory 
should be exactly the same as the name provided by your instructor. For example,
my repo name would be py220201901akm.

3. Ina terminsal session, make your new repo the default directory (using cd) 
and then clone the repo from GitHub as follows. For me I will type:

    git clone git@github.com:UWPCE-PythonCert/py220201901akm.git .

Note the ending period; it must be entered. Substitute the correct details for
you and press enter.

Now you are all set up!

Part 2 - Working on assignments
-------------------------------
Point your editor or IDE at the project directory above. You will
see a directory for each lesson, and then in each lesson, one for activities (ungraded) 
and one for assignments (which are graded).

You will also see a tests directory, that contains automated tests you can run
to verify if your assignment is complete and ready to submit.
You can also lint and run coverage tests, but we're getting to far ahead!

Remember to create a branch in which to do your work. Then, all you need to do is 
save your work in the correct directory. Remember to commit often, with good 
commit messages.

Part 3 - Submitting
-------------------
When you are ready to submit your work, push your working branch to the remote repo,
and then create a pull request for master, assigned to your instructor team.

And that's it!