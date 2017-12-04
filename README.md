# News_Database_Reporting_Tool

##Introduction

This application queries data from the `news` database and neatly organizes answers to complex questions in a data reporting tool
The application uses postgresql for querying the data, and it uses python 2.7 for post processing of the data
Three distinct answers are answered by this application:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?
        
##Content

newsdata.zip:
newsdata.sql - sql file holding the news database
logsdb.py - python file holding the queries and organizing them as plain text deliverables
Vagrantfile - virtual machine
README.md - readme file detailing application specifics
output.txt - txt file that displays output of running logsdb.py
    
##Operating Instructions

Install and/or load linux os virtual machine or other virtual machine that can operate on postgresql database
Pull fullstack-nanodegree-vm github repository
Change directory to the vagrant directory: use command `cd vagrant/`
Run the virtual machine: use command `vagrant up`
Log into virtual machine: use command `vagrant ssh`
Once inside of the virtual machine, cd back into vagrant: `cd /vagrant`
Open newsdata.zip - this will unzip newsdata.sql
Connect to the news database: use command `psql -d news -f newsdata.sql`
The logsdb.py file will query the news database and deliver the answers to the questions
Run the logsdb.py file: `python logsdb.py`



