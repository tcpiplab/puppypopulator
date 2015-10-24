# puppypopulator
An assignment from Udacity's [Full Stack Foundations][1] class

![Screenshot of menu in terminal](https://cloud.githubusercontent.com/assets/816651/10708609/8b7d0a6e-79c3-11e5-83c3-d7a7f661475f.png)

PURPOSE
-------
This was an optional assignment to use the [SQLAlchemy][2] Object Relational
Mapper to perform the following queries against an existing database:

1. Query for all puppies and return the results in ascending alphabetical
order.
1. Query for all puppies that are less than 6 months old organized by the
youngest first.
1. Query all puppies by ascending weight.
1. Query all puppies grouped by the shelter in which they are staying.

FILES
-----
* `puppies.py` - Defines the database structure. Do not run this file manually.
* `puppypopulator.py` - Populates the database with puppies and attributes.
* `puppyqueries.py` - A menu-based command line tool for read-only queries to
the database.

The first two were provided by the instructor. I wrote the latter.

PREREQUISITES
-------------
All code was developed on Ubuntu 14.04.2 LTS, Python 2.7 and
[`PostgreSQL 9.3.6`](http://www.postgresql.org/ftp/source/v9.3.6/). In addition
to installing PostgreSQL, you will also need to install the following Python
modules:

* [`sqlalchemy 0.8.4`](https://pypi.python.org/pypi/SQLAlchemy/0.8.4)
* [`dateutil 1.4.1`](http://labix.org/python-dateutil)

Don't forget to start the [postgres daemon][3].

BUILD
-----
To create the database and its tables, run this command:

    python puppypopulator.py

RUN
---
To run the `puppyqueries.py` script, run this command:

    python puppyqueries.py

This will display a menu in a terminal based interface where you select menu
item numbers to call the various functions, including exiting the script if you
choose. All data is dumped to `STDOUT` and is not paginated.

[1]:https://www.udacity.com/course/full-stack-foundations--ud088
[2]:http://www.sqlalchemy.org/
[3]:http://www.postgresql.org/docs/9.3/static/server-start.html
