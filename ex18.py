#!/usr/bin/python
# exercise 18: names, variables, code, functions

# -- a function names a piece of code --

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1,arg2)

# explicitly take two arguments
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# no arguments
def print_none():
    print "I got nothin'"


# let's use these functions...
print_two("Tiberius","Kirk")
print_two_again("James, T.", "Kirk")
print_one("Spock")
print_none()
