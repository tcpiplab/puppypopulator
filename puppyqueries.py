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
from datetime import date
from dateutil.relativedelta import relativedelta
from sqlalchemy import create_engine, desc
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
def allPuppyNames():
  """
  Query the Puppy table and print the puppy names in alphabetical order
  """
  # Create an object containing a list of all rows in the Puppy table, 
  # and sort by name.
  puppies = session.query(Puppy).order_by(Puppy.name).all()
  
  # Iterate through the object to print all names.
  for puppy in puppies:
    print puppy.name

# Query 2
def puppiesUnder6Months():
  """
  Query the Puppy table for all puppies < 6 months old. Then print the puppy 
  names and dateOfBirth, sorted by youngest first.
  """
  # Grab today's date
  today = date.today()
 
  # Calculate the date six months ago using the dateutil module.
  six_months = today + relativedelta(months=-6)

  # Create an object containing a list of all rows in the Puppy table, 
  # and sort by dateOfBirth.
  puppies = session.query(Puppy.name, Puppy.dateOfBirth, Puppy.dateOfBirth < 
                          six_months).order_by(desc(Puppy.dateOfBirth)).all()

  # Iterate through the object to print name and dateOfBirth
  for puppy in puppies:
    print puppy.name, puppy.dateOfBirth


# Query 3
def puppyWeights():
  """
  Query the Puppy table for all names and weights, sorted by ascending weight. 
  """
  # Query all puppies by ascending weight
  puppies = session.query(Puppy.name, Puppy.weight).order_by(Puppy.weight).all()

  # Iterate through the object to print name and weight
  for puppy in puppies:
    # weight is stored as a string, but sqlalchemy converts to a float
    # requiring us to recast as a string. Then we truncate to 5 characters. 
    print puppy.name, str(puppy.weight)[:5]


# Query 4
def puppiesByShelter():
  """
  Query the database for all puppy names and shelter names, printing each 
  shelter name once and indenting puppy names below their respective shelters.
  """
  # Query the Puppy and Shelter tables, filtering to match Shelter.id with the 
  # foreign key Puppy.shelter_id so we can get the name of each puppy's shelter.
  # Order by the shelter name.
  puppies = session.query(Puppy, Shelter).filter(Puppy.shelter_id == 
                          Shelter.id).order_by(Shelter.name).all()

  # Keep track of which shelter the previous puppy lives in. Initialize empty.
  prev_shelter = ''

  # Iterate through the oject to print puppy names indented under their 
  # respective shelter names.
  for puppy in puppies:
    # Strip any trailing whitespace
    this_shelter = str(puppy.Shelter.name).rstrip()
    # Only print shelter name if it differs from that of the previous puppy.
    if prev_shelter != this_shelter: 
      print this_shelter
      # Remember the most recent shelter name.
      prev_shelter = this_shelter
    # Always print the puppy name.
    print "  " + puppy.Puppy.name


# only show the menu if invoked as a command line tool
if __name__ == '__main__':
  while 1:
    print("""

    1) Show all puppy names in alphabetical order.

    2) Show all puppies under six months old, youngest to oldest.

    3) Show all puppies by ascending weight.

    4) Show all puppies grouped by their shelters.

    5) Exit.

    """)

    selection = int(input('Select a menu item: '))
    if selection == 1:
        allPuppyNames()
    elif selection == 2:
        puppiesUnder6Months()
    elif selection == 3:
        puppyWeights()
    elif selection == 4:
        puppiesByShelter()
    elif selection == 5:
        exit()
