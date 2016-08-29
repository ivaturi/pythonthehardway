#! /usr/bin/env python

## Exercise 39: Notes on dictionaries

##
##
## A dictionary is an associative array that maps hashable values to objects
## The keys of a dictionary should be hashable
## (the immutable basic types that are supported by python)
##
##  - The ordering of elements is not important within a dictionary
##  - The keys used for different elements within a dictionary must be unique
##

#
# Different ways to create an empty dictionary
# --------------------------------------------
#
print "-" * 40
print "Creating dictionaries"
print "-" * 40

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

# Using tuples
heroes = dict([
    ('north' , 'Jon Snow'),
    ('south' , 'Unknown'),
    ( 'east' , 'Varys' ),
    ( 'west' , 'Jaime')
])
print "heroes: ", heroes

# If the keys are simple strings, we can use assignments within the definition
my_dict = dict(a=1, b=2, c=3, d=4)
print my_dict
#
# Interacting with dictionaries
# -----------------------------
#
print "\n"
print "-"*40
print "Interacting with dictionaries"
print "-"*40

# Retrieving elements...
print "westeros[north] = ", westeros['north']

# Using a tuple as a key (A tuple is immutable, and therefore, hashable)
westeros[('writer','GRRM')] = "Awesome"
print westeros

# Printing the list of keys in a dictionary
print "Keys to westeros: ", westeros.keys()
print "  Keys to heroes: ", sorted(heroes.keys())  # <<< sorting the keys


# Looping through a dictionary
print "westeros loop-through:"
for key in westeros.keys():
    print "%r : %r" % (key, westeros[key])

print "heroes loop-through, with keys and values"
for key, value in heroes.items():
    print "%r : %r" % (key, value)

# deleting keys
# > This seems to be the preferred way
westeros.pop(('writer', 'GRRM'))
print westeros

# what happens if we try to pop a key that isn't in the dict?
try:
    element = westeros.pop("essos")
    print element
except:
    print "Exception! Can't pop a nonexistent key!"

# we can handle this in an easier way...
element = westeros.pop("essos", None)
print "Trying to pop a nonexistent key...the answer is",element
