##################################
Part 2: Inreacting with a database
##################################

Be sure you cloned the repository we mentioned prior to video 1
from \ `GitHub <https://github.com/milesak60/RDBMS>`__\ . In this video
we will be using the modules in the "src" directory We start
with \ `v00\_personjob\_model.py <https://github.com/milesak60/RDBMS/blob/master/src/v00_personjob_model.py>`__. 

Key fragments are included here too, below the video.


Using the Model, Using the Person Class, Using the Job Class
============================================================

{{VIDEO HERE}}

 Here is the model code:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    class Person(BaseModel):
        """
            This class defines Person, which maintains details of someone
            for whom we want to research career to date.
        """

        person_name = CharField(primary_key = True, max_length = 30)
        lives_in_town = CharField(max_length = 40)
        nickname = CharField(max_length = 20, null = True)


    class Job(BaseModel):
        """
            This class defines Job, which maintains details of past Jobs
            held by a Person.
        """

        job_name = CharField(primary_key = True, max_length = 30)
        start_date = DateField(formats = 'YYYY-MM-DD')
        end_date = DateField(formats = 'YYYY-MM-DD')

        salary = DecimalField(max_digits = 7, decimal_places = 2)
        person_employed = ForeignKeyField(Person, related_name='was_filled_by', null = False)

.. raw:: html

   </div>

