#! /usr/bin/env python

# A dictionary example

# create a mapping of state to abbreviation:
states = {
       'Oregon'  : 'OR',
      'Florida'  : 'FL',
      'New York' : 'NY',
      'Michigan' : 'MI',
    'California' : 'CA'
}

# create a basic set of states and some cities in them cities.
cities = {
    'MI' : 'Flint',
    'FL' : 'Jacksonville',
    'CA' : 'Sacramento',
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'


# print out some cities
print '-' * 10
print "Michigan is abbreviated to ", states['Michigan']
print "Florida is abbreviated to ", states['Florida']

# cities in a given state
print '-' * 10
print "Michigan has these states: ", cities[states['Michigan']]
print " Florida has these states: ", cities[states['Florida']]

# print the abbreviation for every state
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated to %s" % (state, abbrev)

# print every city in state
print "-"*10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)
