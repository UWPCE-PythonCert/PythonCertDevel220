"""
    Learning persistence with Peewee and sqlite
    delete the database file to start over
        (but running this program does not require it)

        protect data integrity dangling add
"""

from peewee import *
from src.v00_personjob_model import Job


import logging


def show_integrity_add():
    """
        demonstrate how database protects data inegrity : add
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('../data/personjob.db')

    job_name = 0
    start_date = 1
    end_date = 2
    salary = 3
    person_employed = 4

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        with database.transaction():
            logger.info('Try to add a new job where a person doesnt exist...')

            addjob = ('Sales', '2010-04-01', '2018-02-08', 80400, 'Harry')

            logger.info('Adding a sales job for Harry')
            logger.info(addjob)
            new_job = Job.create(
                job_name = addjob[job_name],
                start_date = addjob[start_date],
                end_date = addjob[end_date],
                salary = addjob[salary],
                person_employed = addjob[person_employed])
            new_job.save()

    except Exception as e:
        logger.info('Add failed because Harry is not in Person')
        logger.info(f'For Job create: {addjob[0]}')
        logger.info(e)


if __name__ == '__main__':
    show_integrity_add()
