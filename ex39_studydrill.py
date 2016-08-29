#! /usr/bin/env python

## Exercise 39: Notes on dictionaries

##
##
## A dictionary is an associative array that maps hashable values to objects
## The keys of a dictionary should be hashable
## (the immutable basic types that are supported by python)
##
##

#
# Different ways to create an empty dictionary
# --------------------------------------------
#

my_dict  =     {}  # <<< this is more common
my_dict2 = dict()  # <<< this is slower 

# a little more complicated (probably unnecessary):
import types
my_dict3 = types.DictType.__new__(types.DictType, (), {})


#
# Different ways to initialize a non-empty dictionary
# ---------------------------------------------------
#

# Using key-value pairs
westeros  = {
    'north' : 'winterfell',
    'south' : 'dorne',
     'east' : 'the vale',
     'west' : 'the iron islands'
}
print "westeros: ", westeros

# Using the dict constructor
lords = dict(
    lannister = 'tywin',
        stark = 'ned',
      greyjoy = 'balon',
    baratheon = 'robert'
)
print "lords: ", lords

