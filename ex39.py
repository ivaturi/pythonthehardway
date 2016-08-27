#! /usr/bin/env python

# Exercise 39: Dictionaries, oh lovely dictionaries!

# A dictionary associates one thing to another, no matter what it is

profile = {'name' : 'Matthew Murdock ', 'profession': 'Lawyer', 'alias': 'Daredevil', 'location': 'Hell\'s Kitchen'}

print "profile: ", profile

print "------------------"
print "Numerical indices!"
print "------------------"

# We can also add numerical indices:
profile[1] = "Superheroes!"
print "Updated profile: ", profile


print "------------------"
print "Accessing elements"
print "------------------"

print "           [1] : ", profile[1]
print "        [name] : ", profile['name']
print "       [alias] : ", profile['alias']
print "    [location] : ", profile['location']
print "  [profession] : ", profile['profession']

print "-----------------"
print "Deleting elements"
print "-----------------"

del profile[1]
del profile['alias']
print "Updated profile: ", profile
