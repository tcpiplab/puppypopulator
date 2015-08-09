# Luke Sheppard
# lshep.usc[(at)]gmail.com
# Fullstack Nanodegree at Udacity.
# Problem Set 1 (optional)
# Exercise 2
# August 8, 2015

# The assignment is to use SQLAlchemy to perform the following queries on 
# your database:
# 1. Query all of the puppies and return the results in ascending 
#    alphabetical order.
# 2. Query all of the puppies that are less than 6 months old organized by 
#    the youngest first.
# 3. Query all puppies by ascending weight.
# 4. Query all puppies grouped by the shelter in which they are staying.

# Dependencies
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# From our existing database
from puppies import Base, Shelter, Puppy

# Specify which database engine to communicate with
engine = create_engine('sqlite:///puppyshelter.db')

# Bind the engine to the Base class. This connects our class definitions to
# their corresponding table in the database.
Base.metadata.bind = engine

# Create a sessionmaker object to establish a link of communications between our
# code executions and the engine object create on the previous line.
DBSession = sessionmaker(bind = engine)

# This is our session
session = DBSession()

# Query 1
def query1():
  # Create an object containing a list of all rows in the Puppy table, 
  # and sort by name.
  puppies = session.query(Puppy).order_by(Puppy.name).all()
  
  # Iterate through the object to print all names.
  for puppy in puppies:
    print puppy.name

# Query 2
def query2():
  # Create an object containing a list of all rows in the Puppy table, 
  # and sort by weight.
  puppies = session.query(Puppy).order_by(Puppy.weight).all()

  # Iterate through the object to print name and weight
  for puppy in puppies:
    # weight is stored as a string, but sqlalchemy converts to a float
    # requiring us to recast as a string. Then we truncate to 5 characters. 
    print puppy.name, str(puppy.weight)[:5]

# MAIN()
query1()
query2()

