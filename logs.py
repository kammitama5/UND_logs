# ! /usr/bin/env python

# import psycopg2
import psycopg2
# using Python 2
DBNAME = "news"


# connect to database and make a query
# open connection to database
# execute query, fetch and close database request

def connect_query(query):
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()
# list queries
# Query 1: What are the three most popular articles of all time?

query_1 = """


select title, count(*) as views from articles inner join
log on concat('/article/', articles.slug) = log.path
where log.status like '%200%'
group by log.path, articles.title order by views desc limit 3;
"""


# function for first query
def query_one(query):
    # function connects to database and runs first query
    queries_ = connect_query(query)
    print "What are the most popular three articles of all time?"
    print "The 3 most popular articles of all time are: "
    for query_ in queries_:
        print "{} - {} views".format(query_[0], query_[1])
# Query 2
# Who are the most popular article authors of all time?

query_2 = """


select authors.name, count(*) as views from articles inner join
authors on articles.author = authors.id inner join
log on concat('/article/', articles.slug) = log.path where
log.status like '%200%' group by authors.name order by views desc
"""

# query_2 function


def query_two(query):

    """
    function connects to database and runs second query
    """
    queries_ = connect_query(query)
    print "Who are the most popular article authors of all time?"
    print "The most popular article authors of all time are : "
    for query_ in queries_:
        print "{}-{}views".format(query_[0], query_[1])
# Query 3
# On Which days did more than 1% of requests lead to errors?

query_3 = """


select * from (
select request1.day,
round(cast((100*request2.req) as numeric) /
cast(request1.req as numeric), 2)
    as err from
    (select date(time) as day,
    count(*) as req from log group by day) as request1
        inner join
        (select date(time) as day, count(*) as req from log where status
        like '%404%' group by day) as request2
    on request1.day = request2.day)
as threshold where err > 1.0;
"""

# query_3 function


def query_three(query):
    # function to find 1 percent of requests leading to errors
    # function connects to database and runs third query
    queries_ = connect_query(query)
    print "On which days did more than 1 percent of requests lead to errors?"
    print "These days had more than 1 percent of requests lead to errors: "
    for query_ in queries_:
        print "{} - {} views".format(query_[0], query_[1])

# run  and print queries


print query_one(query_1)
print query_two(query_2)
print query_three(query_3)
