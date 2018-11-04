=================
Lesson 08 Content
=================

.. raw:: html

   <div id="menuheading">

.. rubric:: NOSQL databases
   :name: nosql-databases
   :class: caH2

.. raw:: html

   <div id="navbar" class="caNav grid-row around-md clearunderlinestyle"
   role="navigation">

`Introduction <%24WIKI_REFERENCE%24/pages/lesson-08-introduction>`__ \|
`Content <%24WIKI_REFERENCE%24/pages/lesson-08-content>`__ \|
`Quiz <%24CANVAS_OBJECT_REFERENCE%24/assignments/ibe91f0cc09bbecc290b2f8a417d1cf9d>`__ \|
`Activity <%24CANVAS_OBJECT_REFERENCE%24/assignments/i85a67f5992214211e1422f618383b5da>`__
\|
`Assignment <%24CANVAS_OBJECT_REFERENCE%24/assignments/i10247fb9255383751f912e986d6fd289>`__
\| `Code
Talk <%24CANVAS_OBJECT_REFERENCE%24/discussion_topics/ie7fce6e6c072d03b675b6796a45e3c25>`__

.. raw:: html

   </div>

.. raw:: html

   </div>

Introduction
============

Relational databases remain the type of database you are most likely to
encounter as a Python developer, at least for the time being. But over
the last few years, in all applications, data volumes have increased to
previously unheard of proportions. Distributed systems have become the
norm. And the pace of business change has increased, causing the need
for software development pace to continue to accelerate.

In this lesson we are going to look at some alternatives to the RDBMS.
We are going to learn how to use them with Python, and we are also going
to consider where these alternatives are most suited. However, we are
just scratching the surface here. There will be much left to learn when
we are done.

We’ll start by considering the characteristics of databases. And then
we’ll move on to look at how the evolution of the use of hardware and
software enables new techniques. Next, we examine database products that
exploit these new techniques. And we’ll learn how to use them from
Python. And along the way, we’ll also show how you can avoid a database
all together for simple data management scenarios.

So lets get started!

Nosql - Why?
============

One of the main weaknesses of the RDBMS is that it does not usually
perform well when data is distributed across multiple locations.
Oversimplifying a bit, the RDBMS is essentially a single server-based
data storage device, and although it can cope with multiple locations
things get awkward quickly.

To address this, we need to look at scaling. Scaling refers to adapting
technology to deal with reducing, or more usually, increasing processing
volumes.

Traditionally in technology projects we have scaled vertically; that is,
by continually replacing servers with other increasingly powerful
servers. However, that is expensive, wasteful and inflexible, as much
financial and implementation planning is needed, and we usually have to
over-specify to allow for growth. Nosql databases allow horizontal
scaling, which means that when more capacity is needed, you just add
another server. There can be many, cheaper servers that can support
massive work volumes across widely dispersed geographic locations. And
it is no coincidence that this model is the way that the cloud works. 

The RDBMS is less than ideal for horizontal scaling. Although, it must
be said, before moving away from the RDBMS there should be at least one
good reason to do so. For many or even most systems the RDBMS is still
perfectly suitable.

Nosql databases are much better at horizontal scaling. These types of
database are called nosql databases because originally (and even now)
they did not use SQL for data definition and management. However, it’s
hard to define something by saying what it isn’t! So now nosql is
starting to mean “Not Only SQL”. That is because some of the databases
can use SQL, but have other means for data definition and management
too.

There are tradeoffs though, and while this gets complex and is beyond
this class, you can read more at the links using the links identified
later in this lesson

Next we’ll look at an overview of some representative types of nosql
database.

 

NOSQL Databases: Tradeoffs
==========================

 

{{VIDEO HERE}}

Nosql database types 
---------------------

+--------------------+--------------------+--------------------+--------------------+
| Database           | Strengths          | Weaknesses         | Good uses          |
+--------------------+--------------------+--------------------+--------------------+
| Mongodb :          | Easy to scale      | No built in        | Web applications,  |
|                    |                    | transaction        | general business   |
| Document database. | High availability  | support: requires  | applications where |
|                    |                    | manual effort      | query flexibility  |
|                    | Flexible data      |                    | is important, and  |
|                    | model, easy to     | Not good for       | where data         |
|                    | program            | modeling data with | definition need to |
|                    |                    | lots of            | evolve.            |
|                    | Excellent query    | relationships.     |                    |
|                    | capabilities       |                    | Applications that  |
|                    |                    |                    | may grow rapidly - |
|                    | Performs           |                    | horizontal scaling |
|                    | exceptionally well |                    | works very well.   |
|                    | with the right     |                    |                    |
|                    | data (that is,     |                    |                    |
|                    | where there are    |                    |                    |
|                    | not lots of        |                    |                    |
|                    | relationships)     |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| Redis :            | Rapid access where | Querying           | Look up data       |
|                    | data size can be   |                    | (reference data).  |
| Data structure     | predetermined (all | All data needs to  |                    |
| server, message    | data held in       | fit in RAM         | Caching.           |
| queuing, caching   | memory).           |                    |                    |
|                    |                    | Security very      | Very fast access   |
|                    | Realtime           | basic              | to data - real     |
|                    | applications -     |                    | time apps          |
|                    | “instant” access   |                    |                    |
|                    | to data by its     |                    |                    |
|                    | key.               |                    |                    |
|                    |                    |                    |                    |
|                    | Easily store sets  |                    |                    |
|                    | and lists.         |                    |                    |
|                    |                    |                    |                    |
|                    | High availability  |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| Neo4j :            |                    |                    | Applications that  |
|                    |                    |                    | emphasize          |
| Graph database     | Powerful querying  | Scaling can be a   | maintaining and    |
|                    |                    | problem in certain | tracking complex   |
|                    | Very fast          | situations (very   | relationships      |
|                    |                    | high end).         | between data, such |
|                    | Flexible data      |                    | as master data     |
|                    | structures,        | Doesn’t offer an   | management, and    |
|                    | handles            | advantage if data  | analyzing business |
|                    | complexity.        | structure and      | events.            |
|                    |                    | relationships are  |                    |
|                    | Fully ACID         | simple.            | Investigative      |
|                    | compliant          |                    | applications       |
|                    | (protects data     |                    | (stock trades).    |
|                    | quality and        |                    |                    |
|                    | integrity)         |                    |                    |
|                    |                    |                    |                    |
|                    |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+

| So, that’s a quick overview of these databases. Next, we are going to
  prepare to run Python code against these databases.
| 

Preparation
===========

In this part of the lesson we are going to walk through setting up
security to ensure our databases are protected from unauthorized access.

Security Setup
==============

{{VIDEO HERE}}

Reminder: The databases we will be using require secure access; that is,
entry of a user name and password. Storing these details for use in
Python code can present security problems if we don’t keep at least our
passwords safe from unwanted viewing.

If we embed our password in our Python code, and we then push that code
to Github, we will have compromised out security, since the password
will be available for anyone to see.

We will address this by storing the password in a file that we place in
a directory which we will add to our .gitignore file. We will then read
that file from within our Python program, get the password and use it to
access the database. As long as the file is not checked in to Github,
all is well and our database is safe.

*NOTE: this still puts your password in plain text on your computer! So
not really secure for really critical use!*

Here’s how we do this:

Create a new local project for each database. Then, follow these steps
for each repository:

First, edit your .gitignore file and add the following 2 lines at the
end of the file, exactly as shown:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    # secrets
    .config/

.. raw:: html

   </div>

| Now, in the parent directory of your local project, make a new
  directory called “.config”. Note the leading period, and don’t enter
  the quotes.
| 

In the newly create .config directory create a new file called “config”.
Note no leading period. Again, don’t enter the quotes.

Edit the config file using your preferred editor, creating lines as
follows:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    [configuration]
    user =
    pw = 
    connect =

.. raw:: html

   </div>

| At the end of the line containing user = enter a space after the =,
  and then a user name (for now just enter any name. When you sign up
  for each database you will enter the correct name).
| 

It will look something like this:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    user = andy

.. raw:: html

   </div>

| Now, enter a password as above, remembering the correct one will be
  entered after database signup. Also, leave connect blank after the =.
  Save the file.
| 

| Your user name and password are now safely store where Python can
  access them. The .gitignore change will prevent the .config files from
  being pushed to github.
| 

Signup
------

Our next step is to signup for the database services we are going to
use. The PowerPoint file used in the video is included below so you can
work along without the video after watching.

{{VIDEO HERE}}

Here is the
`PowerPoint <%24IMS-CC-FILEBASE%24/signup.pptx?canvas_download=1&canvas_qs_download_frd=1>`__.
It starts on the third slide.

Now we are all setup, and can move on to Python development with the
databases.

nosql examples with Python
--------------------------

We will get into more detail as we look at the activities in this class,
and the assignments too. But for now let's look at some simple
illustrations how of how Python works with the databases we have setup.
For now you can just follow along with the code below.

mongodb
-------

For this application we are going to use the example of a furniture
rental business. We will use mongodb to manage product data. Let’s take
a look at part of this program, which fully annotated with log
statements:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    """
        Mongodb #1
        test and learn mongodb
        for this to work in macos you must run from bash:
            open "/Applications/Python 3.6/Install Certificates.command"

    """
    # code intentionally omitted - see git for complete module

        logger.info('Setup the connection to mongodb')
        with src.login_database.login_mongodb_cloud() as client:

            logger.info('We are going to use a database called dev')
            db = client['dev']

            logger.info('And in that database create a collection called furniture')

            furniture = db['furniture']

            logger.info('Now we add data from the dictionary')
            results = furniture.insert_many([
            {
                'product': 'Red couch',
                'in_stock_quantity': 10
            },
            {
                'product': 'Blue couch',
                'in_stock_quantity': 3
            }])

            logger.info('Find the products that are described as plastic')
            query = {'product': 'Red couch'}
            results = furniture.find_one(query)

    if __name__ == '__main__':
        main()

.. raw:: html

   </div>

Notice how we used a dictionary to represent the data in Python, and
passed the dictionary to insert\_many() to store the data in mongodb.

What about the schema? In this case there isn’t really a concept of a
database schema. This makes things much more straightforward for the
programmer than when using SQL in a relational database. The data items
are defined in Python, and while some (mainly RDBMS die-hards) may say
this is a problem, it does mean that there is no need to repeat data
definition in the program and database. 

You should also study the simple query above, where we use find\_one()
to retrieve an item of furniture based on a query. Notice how a
dictionary defines this most simple of queries.

We’ll now study how we connect to mongodb. Here is the function that
gets us wired up, which we call in the code above:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    def login_mongodb_cloud():
        """
            connect to mongodb and login
        """

        log.info('Here is where we use the connect to mongodb.')
        log.info('Note use of f string to embed the user & password (from the tuple).')
        try:
            config.read(config_file)
            user = config["mongodb_cloud"]["user"]
            pw = config["mongodb_cloud"]["pw"]

        except Exception as e:
            print(f'error: {e}')

        client = pymongo.MongoClient(f'mongodb://{user}:{pw}'
                                     '@cluster0-shard-00-00-wphqo.mongodb.net:27017,'
                                     'cluster0-shard-00-01-wphqo.mongodb.net:27017,'
                                     'cluster0-shard-00-02-wphqo.mongodb.net:27017/test'
                                     '?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin')

        return client

.. raw:: html

   </div>

 Notice how we read the config file, and then use the information we
obtained to login.

More about mongodb
------------------

Here's some more information you can read to learn more before we start
the mongodb activity.

https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb 

 

Redis
-----

We are now going to review a Python program that will create and read
some data into our Redis database. We are going to cache some product
data from the furniture rentals example so that we can obtain
lightening performance! Let’s take a look at this program:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    """
        demonstrate use of Redis
    """

    # code intentionally omitted - see git for complete module

        try:
            log.info('Step 1: connect to Redis')
            r = src.login_database.login_redis_cloud()
            log.info('Step 2: cache some data in Redis')
            r.set('andy', 'andy@somewhere.com')

            log.info('Step 2: now I can read it')
            email = r.get('andy')
            log.info('But I must know the key')
            log.info(f'The results of r.get: {email}')

        except Exception as e:
            print(f'Redis error: {e}')

.. raw:: html

   </div>

This is a partial and trivial Redis program that shows how we can
populate and then read from a Redis cache. Notice it is essential to
write and read using a key.

And here is how we connect to Redis: 

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    def login_redis_cloud():
        """
            connect to redis and login
        """
        try:
            config.read(config_file)
            host = config["redis_cloud"]["host"]
            port = config["redis_cloud"]["port"]
            pw = config["redis_cloud"]["pw"]


        except Exception as e:
            print(f'error: {e}')

        log.info('Here is where we use the connect to redis.')

        try:
            r = redis.StrictRedis(host=host, port=port, password=pw, decode_responses=True)

        except Exception as e:
            print(f'error: {e}')

        return r

.. raw:: html

   </div>

More about Redis
----------------

Here's some more information you can read to learn more before we start
the Redis activity.

Neo4J
=====

In computing, a graph database is a database that uses graph concepts
and theory from math to represent and store data.

This is in contrast to RDBMSs, where the data are stored in individual
tables, with the relationships between the tables maintained via primary
and foreign keys, and the actual relationships determined on the fly by
searching multiple tables during “join” queries. RDBMSs are well
optimized for these kinds of queries, but Graph Databases can be much
more efficient for data retrieval when the records have complex
relationships.

For more detail see:

https://en.wikipedia.org/wiki/Graph_database

We are now going to review a Python program that will create and read
some data into our Neo4J database. For this application we are going to
continue to use the example of a furniture rental business. We will use
Neo4J to manage product data and customer. Let’s take a look at this
partial program, which fully annotated with log statements:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    """
        neo4j example
    """

    # code intentionally omitted - see git for complete module


        with driver.session() as session:

            log.info('Adding a few Person nodes')
            for first, last in [('Bob', 'Jones'),
                                ('Nancy', 'Cooper'),
                                ('Alice', 'Cooper'),
                                ('Fred', 'Barnes'),
                                ('Mary', 'Evans'),
                                ('Marie', 'Curie'),
                                ]:
                cyph = "CREATE (n:Person {first_name:'%s', last_name: '%s'})" % (
                    first, last)
                session.run(cyph)

            log.info("Get all of people in the DB:")
            cyph = """MATCH (p:Person)
                      RETURN p.first_name as first_name, p.last_name as last_name
                    """
            result = session.run(cyph)
            print("People in database:")
            for record in result:
                print(record['first_name'], record['last_name'])

.. raw:: html

   </div>

` <https://en.wikipedia.org/wiki/Graph_database>`__

Here we add some data, and use the Neo4J cyph language to create and
retrieve our Person records.

And here is how we connect to Neo4J:

 

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    def login_neo4j_cloud():
        """
            connect to neo4j and login

        """

        log.info('Here is where we use the connect to neo4j.')
        log.info('')

        config.read(config_file)

        graphenedb_user = config["neo4j_cloud"]["user"]
        graphenedb_pass = config["neo4j_cloud"]["pw"]
        graphenedb_url = 'bolt://hobby-opmhmhgpkdehgbkejbochpal.dbs.graphenedb.com:24786'
        driver = GraphDatabase.driver(graphenedb_url,
                                      auth=basic_auth(graphenedb_user, graphenedb_pass))

        return driver

.. raw:: html

   </div>

 

More about Neo4J
----------------

Here's some more information you can read to learn more before we start
the Neo4J activity.

For more details, here is a nice Python based tutorial about graph
databases and neo4j (Talking About your Data Relationships): 

https://medium.com/labcodes/graph-databases-talking-about-your-data-relationships-with-python-b438c689dc89

| And here is the documentation for the Python driver:
| 

https://neo4j.com/developer/python/ 

| There are a lot of other great docs and tutorial on the neo4j web site
  – well worth checking out if you want to really learn how to use it.
| 

Persistence and Serialization
=============================

Beyond using databases there are various simple ways to store data in
our Python programs. We refer to these as persistence and serialization,
which are closely related. Serialization means taking a potentially
complex data structure and converting it into a single string of
bytes. Persistence is storing data simply in a way that it will persist
beyond the run-time of your program.

Serialization:
`h <https://en.wikipedia.org/wiki/Serializa_on%20>`__\ `ttps://en.wikipedia.org/wiki/Serializa\_on  <https://en.wikipedia.org/wiki/Serializa_on%20>`__

Persistance: \ https://en.wikipedia.org/wiki/Persistence_(computer_science) 

They are closely related, because most forms of persistent storage –
simple text files, databases, etc, require that it be turned into a
simple string of bytes first. After all, everything done with computers
is ultimately a serial string of bytes. And serialization is also very
useful for transmiting information between systems, such as
over a network.

Examples
--------

We are going to illustrate persistence using Pickle, Shelve, CSV files
and JSON.

Pickle is a simple way to store and retrieve the contents of a Python
object. Pickle serializes the data before writing it to disk, and
deserializes it when reading from disk. Here is a good article that
summarized Pickle: 

https://pythontips.com/2013/08/02/what-is-pickle-in-python/

Shelve stores objects too, but the objects must be associated with a
key. This kety is used to retrieve the shelved object. See:

https://pythontips.com/2013/08/02/what-is-pickle-in-python/

CSV, or comma separated files, are used for data interchange between a
very wide range of software products, including most notably
spreadsheets. There are many forms of CSV file, but all share the common
property of using the comma to delimit field values, and end of line to
separate records. See:

https://en.wikipedia.org/wiki/Comma-separated_values

Finally, JSON files, which stands for javascript object notation, are
used in many modern web applications. They are easier to read and write
(both for humans and computers) than the interchange format they often
replace, which is XML. See:

https://en.wikipedia.org/wiki/JSON 

Here is  an example of a partial program that uses each of these:

.. raw:: html

   <div
   style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">

::

    """
    pickle etc
    """

    # code intentionally omitted - see git for complete module


    def run_example(furniture_items):
        """
        various persistence and serialization scenarios

        """

        def run_pickle():
            """
            Write and read with pickle
            """
            log.info("\n\n====")
            log.info('Demonstrate persistence with pickle')
            log.info('Write a pickle file with the furniture data')

            pickle.dump(furniture_items, open('data/data.pkl', 'wb'))

            log.info('Now read it back from the pickle file')
            read_data = pickle.load(open('data/data.pkl', 'rb'))
            log.info('Show that the write and read were successful')
            assert read_data == furniture_items
            log.info("and print the data")
            pprint.pprint(read_data)

        def run_shelve():
            """
            write and read with shelve

            """
            log.info("\n\n====")
            log.info("Demonstrate working with shelve")
            shelf_file = shelve.open('data/shelve.dat')
            log.info("store data at key")
            shelf_file['key'] = furniture_items

            log.info("Now retrieve a COPY of data at key")
            read_items = shelf_file['key']

            log.info("Check it worked")
            assert read_items == furniture_items

            log.info("And now print the copy")
            pprint.pprint(read_items)

            log.info("delete data stored at key to cleanup and close")
            del shelf_file['key']
            shelf_file.close()

        def run_csv():
            """
            write and read a csv
            """
            log.info("\n\n====")
            peopledata = [
                ('John', 'second guitar', 117.45),
                ('Paul', 'bass', 22.01),
                ('George', 'lead guitar', 45.99),
                ('Ringo', 'drume', 77.0),
                ('Roger', 'vocals', 12.5),
                ('Keith', 'drums', 6.25),
                ('Pete', 'guitar', 0.1),
                ('John', 'bass', 89.71)
            ]
            log.info("Write csv file")
            with open('data/rockstars.csv', 'w') as people:
                peoplewriter = csv.writer(people)
                peoplewriter.writerow(peopledata)

            log.info("Read csv file back")
            with open('data/rockstars.csv', 'r') as people:
                people_reader = csv.reader(people, delimiter=',', quotechar='"')
                for row in people_reader:
                    pprint.pprint(row)

        def run_json():
            log.info("\n\n====")
            log.info("Look at working with json data")
            furniture = [{'product': 'Red couch','description': 'Leather low back'},
            {'product': 'Blue couch','description': 'Cloth high back'},
            {'product': 'Coffee table','description': 'Plastic'},
            {'product': 'Red couch','description': 'Leather high back'}]

            log.info("Return json string from an object")
            furniture_string = json.dumps(furniture)

            log.info("Print the json")
            pprint.pprint(furniture_string)

            log.info("Returns an object from a json string representation")
            furniture_object = json.loads(furniture_string)
            log.info("print the string")
            pprint.pprint(furniture_object)

        run_pickle()
        run_shelve()
        run_csv()
        run_json()

        return

.. raw:: html

   </div>

 

Conclusion 
-----------

{{VIDEO HERE}}
