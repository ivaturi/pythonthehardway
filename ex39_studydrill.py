#! /usr/bin/env python

# Exercise 39: Notes on dictionaries

###
# A dictionary is an associative array that maps hashable values to objects
# The keys of a dictionary should be hashable
# (the immutable basic types that are supported by python)


# Different ways to create an empty  dictionary:
#----------------------------------------------

my_dict  = {}
my_dict2 = dict()

# a little more complicated (probably unnecessary):
import types
my_dict3 = types.DictType.__new__(types.DictType, (), {})




# Using key-value pairs
westeros  = {
    'north' : 'winterfell',
    'south' : 'dorne',
     'east' : 'the vale',
     'west' : 'the iron islands'
}
print "westeros: ", westeros


#
