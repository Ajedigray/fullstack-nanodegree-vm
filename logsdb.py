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
	print (b + "\nReporting Tool for the News Database\n" + r)


def popularArticles():
	print (b + "1. What are the most popular three articles of all time?" + r)
	db = psycopg2.connect(database=DBNAME)
	c = db.cursor()
	c.execute('''select path, count(*) as num_of_hits from log
				group by path order by num_of_hits desc limit 4;''')
	rows = c.fetchall()
	form_row = rows[1:]
  
  for row in form_row:
		value = row[1]
		num_of_hits = format(value, ',d')
		string = row[0].title()
		cut_str = string[9:]
		reform_str = cut_str.replace('-', ' ')
		print (bullet + '"' + reform_str + '"' + " - " + num_of_hits + views)
	db.close()
  
  
  def init():
	  header()
	  popularArticles()
  
  
  init()
