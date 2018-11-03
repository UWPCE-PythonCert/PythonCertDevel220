=================
Lesson 05 Content
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

APIs and MongoDB background
===========================

{{video 2}}


NOSQL Databases: Tradeoffs
==========================

{{video 3}}

Table from video:

+--------------------+--------------------+--------------------+--------------------+
| Database           | Strengths          | Weaknesses         | Good uses          |
+--------------------+--------------------+--------------------+--------------------+
| Mongodb :          | Easy to scale      | Not good for       | Web applications,  |
|                    |                    | modeling data with | general business   |
| Document database. | High availability  | lots of            | applications where |
|                    |                    | relationships.     | query flexibility  |
|                    | Flexible data      |                    | is important, and  |
|                    | model, easy to     |                    | where data         |
|                    | program            |                    | definition need to |
|                    |                    |                    | evolve.            |
|                    | Excellent query    |                    |                    |
|                    | capabilities       |                    | Applications that  |
|                    |                    |                    | may grow rapidly - |
|                    | Performs           |                    | horizontal scaling |
|                    | exceptionally well |                    | works very well.   |
|                    | with the right     |                    |                    |
|                    | data (that is,     |                    |                    |
|                    | where there are    |                    |                    |
|                    | not lots of        |                    |                    |
|                    | relationships)     |                    |                    |
|                    |                    |                    |                    |
|                    | Supports           |                    |                    |
|                    | transactions       |                    |                    |
+--------------------+--------------------+--------------------+--------------------+

 

Python, mongodb and the API
===========================

{{VIDEO 4 HERE}}

MongoDB Installation
--------------------
Here are the steps referred to in the video that will help you to Install
MongodDB on your development computer.

  Note: If you already have access to a MongoDB instance then feel free to use it.
  You will need to know the connection details though, such as IP address, Port and user /
  password.

1. First you will need to download MongoDB for your operating system.
For Mac OSX go to https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/?_ga=2.22696635.1439444876.1541175909-1381738278.1540687301
For Windows go to https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/
For Linux be sure to select the correct distro when yo go to https://docs.mongodb.com/manual/administration/install-on-linux/

2. Follow the instructions at the url you have visited.

Mongodb vs. RDBMS terminology
-----------------------------

+----------+------------+
| MongoDB  | RDBMS      |
+----------+------------+
| Database | Database   |
| Table    | Collection |
| Row      | Document   |
| Column   | Field      |
| Index    | Index      |
+----------+------------+

MongoDB Technical information
-----------------------------

Here's some links for you to consult and read to understand JSON and BSON:
- https://www.json.org/
- http://bsonspec.org/

Python code
-----------
{{video 5 here}}

Python code from video
----------------------

.. code-block:: python

  """"
  must use 127.0.0.1 on windows
  pip install pymongo

  """
  from pymongo import MongoClient


  class MongoDBConnection():
      """MongoDB Connection"""

      def __init__(self, host='127.0.0.1', port=27017):
          """ be sure to use the ip address not name for local windows"""
          self.host = host
          self.port = port
          self.connection = None

      def __enter__(self):
          self.connection = MongoClient(self.host, self.port)
          return self

      def __exit__(self, exc_type, exc_val, exc_tb):
          self.connection.close()


  def print_mdb_collection(collection_name):
      for doc in collection_name.find():
          print(doc)


  def main():
      mongo = MongoDBConnection()

      with mongo:
          # mongodb database; it all starts here
          db = mongo.connection.media

          # collection in database
          cd = db["cd"]

          # notice how easy these are to create and that they are "schemaless"
          # that is, the Python module defines the data structure in a dict,
          # rather than the database which just stores what it is told

          cd_ip = {"artist": "The Who", "Title": "By Numbers"}
          result = cd.insert_one(cd_ip)

          cd_ip = [{
              "artist": "Deep Purple",
              "Title": "Made In Japan",
              "name": "Andy"
          },
                   {
                       "artist": "Led Zeppelin",
                       "Title": "House of the Holy",
                       "name": "Andy"
                   }, {
                       "artist": "Pink Floyd",
                       "Title": "DSOM",
                       "name": "Andy"
                   },
                   {
                       "artist": "Albert Hammond",
                       "Title": "Free Electric Band",
                       "name": "Sam"
                   }, {
                       "artist": "Nilsson",
                       "Title": "Without You",
                       "name": "Sam"
                   }]

          result = cd.insert_many(cd_ip)

          print_mdb_collection(cd)

          # another collection
          collector = db["collector"]

          collector_ip = [{
              "name": "Andy",
              "preference": "Rock"
          }, {
              "name": "Sam",
              "preference": "Pop"
          }]
          result = collector.insert_many(collector_ip)

          print_mdb_collection(collector)

          # related data
          for name in collector.find():
              print(f'List for {name["name"]}')
              query = {"name": name["name"]}
              for a_cd in cd.find(query):
                  print(f'{name["name"]} has collected {a_cd}')

          # start afresh next time?
          yorn = input("Drop data?")
          if yorn.upper() == 'Y':
              cd.drop()
              collector.drop()


  if __name__ == "__main__":
      main()

.. todo::
  Add git links for mongo code


More about mongodb
------------------

Here's some more information you can read to learn more before we start
the mongodb activites.

https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb 

Activities
----------
#. Having thought about the ideas for improving the MongoDB module from the video,
   first of all work through imlementing your ideas. Be prepared to dicuss or
   demonstrate these at office hours, or with your instructor.

Optional
--------
#. MongoDB is not the only NoSQL database in town. There are many others.
   Of particular interest to Python developers are Redis, and Neo4J. They
   offer very useful features, and are well documented.
   Invetsigate their documentation, and try downloading and using either or both
   for situations where you think they offer functionality that is useful
   fro HP Norton. Again, feel free to bring along your results to dicuss or
   demonstrate at office hours, or with your instructor.
   And check out the example we provided in the class repo.
.. todo::
  Add Redis and Neo4J examles to Lesson 5 repo
 

