##################################
Part 2: NOSQL Databases: Tradeoffs
##################################

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

