# News_Database_Reporting_Tool

## Introduction

This application queries data from the `news` database and neatly organizes answers to complex questions in a data reporting tool
The application uses postgresql for querying the data, and it uses python 2.7 for post processing of the data
Three distinct answers are answered by this application:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?
        
## Content

newsdata.zip:
newsdata.sql - sql file holding the news database
logsdb.py - python file holding the queries and organizing them as plain text deliverables
Vagrantfile - virtual machine
README.md - readme file detailing application specifics
output.txt - txt file that displays output of running logsdb.py
    
## Operating Instructions

 1. Install and/or load linux os virtual machine or other virtual machine that can operate on postgresql database: [Installing Virtual Box and Vagrant](https://<span></span>drupalize.me/videos/installing-vagrant-and-virtualbox?p=1526)
 2. Pull fullstack-nanodegree-vm github repository: [News Database Reporting Tool](https://github.com/Ajedigray/fullstack-nanodegree-vm.git)
 3. Change directory to the vagrant directory: use command `cd vagrant/`
 4. Run the virtual machine: use command `vagrant up`
 5. Log into virtual machine: use command `vagrant ssh`
 6. Once inside of the virtual machine, cd back into vagrant: `cd /vagrant`
 7. Open newsdata.zip - this will unzip newsdata.sql
 8. Connect to the news database: use command `psql -d news -f newsdata.sql`
 9. The logsdb.py file will query the news database and deliver the answers to the questions
10. Run the logsdb.py file: `python logsdb.py`



