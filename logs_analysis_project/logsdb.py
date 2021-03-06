#!/usr/bin/env python2.7

from __future__ import division
import datetime
import psycopg2

DBNAME = 'news'
b = "\033[1m"
r = "\033[0;0m"
bullet = "     " + u'\u2022 '
views = ' views'


def header():
    """header prints the header text for the rporting tool"""

    print (b + "\nReporting Tool for the News Database\n" + r)


def execute_query(query):
    """execute_query is a helper function takes an SQL query as a parameter,
        executes the query and returns the results as a list of tuples.
       args:
           query - (string) an SQL query statement to be executed.

       returns:
           A list of tuples containing the results of the query.
    """
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        results = c.fetchall()
        db.close()

        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def popularArticles():
    """popularArticles prints the output from querying the
        database to find the top three most popular articles"""

    print (b + "1. What are the most popular three articles of all time?" + r)
    rows = execute_query('''select articles.title,log.path, count(*) as num_of_hits from
                log, articles where log.path = concat('/article/',
                articles.slug) group by articles.title, log.path
                order by num_of_hits desc limit 3;''')

    for row in rows:
        value = row[2]
        num_of_hits = format(value, ',d')
        title = row[0]
        print (bullet + '"' + title + '"' + " - " + num_of_hits + views)


def popularAuthors():
    """popularAuthors prints the output resulting from querying the database
        to find the top three most popular article authors"""

    print (b + "\n2. Who are the most popular article authors of all time?" +
           r)
    rows = execute_query('''select authors.name as name, count(*) as frequency
                from articles,log, authors where log.path = concat
                ('/article/', articles.slug) and authors.id = articles.author
                group by name order by frequency desc;''')

    for author, value in rows:
        print(bullet + '{} - {:,d} views'.format(author, value))


def errorProne():
    """errorProne prints the output resulting from querying the database
        to find the day(s) with the most bad requests"""
    # print ('\n')

    print(b + "\n3. On which days did more than 1% of requests lead to " +
          "errors?" + r)
    rows = execute_query('''select date_part('month', time) as month,
                date_part('day', time) as day, date_part('year', time) as year,
                sum(case when status = '404 NOT FOUND' then 1 else 0 end)
                as error, count(*) as total_requests from log group by month,
                day, year order by day;''')

    for row in rows:
        error = int(row[3])
        total = int(row[4])
        error_rate = error / total

        if error_rate > 0.01:
            date = datetime.date(int(row[2]), int(row[0]), int(row[1]))
            print(bullet + '{:%B %d, %Y} - {:.2%} errors\n'.
            	  format(date, error_rate))


def init():
    """init runs the program by making individual function calls when the
        file is loaded"""

    header()
    popularArticles()
    popularAuthors()
    errorProne()


# To make sure the main subroutine is only run when this program is executed
# directly, and not when it is imported as a module
if __name__ == '__main__':
    init()
