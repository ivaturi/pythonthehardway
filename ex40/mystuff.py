#! /usr/bin/env python

"""
Defining a module
"""

# Variable
ver = "0.1"

def greet(name = False):
    """
    Print a greeting with a given name.
    If no name is given, simply say Hello.    
    """
    print "Hello",
    if name:
        print name
