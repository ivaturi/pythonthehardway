#!/usr/bin/python

# exercise 21: functions can return something

# function to add two input numbers
def add(a,b):
    return a + b

# function to subtract one number from another
def subtract(a,b):
    return a - b

# function to multiply numbers
def multiply(a,b):
    return a*b

# function to divide numbers
def divide(a,b):
    return a/b

print "Let's do some math with just functions!"

age     = add(30,5)
height  = subtract(78,4)
weight  = multiply(90,2)
iq      = divide(100,2)

print """
Age     : %d
Height  : %d
Weight  : %d
I.Q     : %d
""" % (age,height,weight,iq)

# Puzzle?
print "Here is a puzzle:"

what = add (age, subtract(height, multiply(weight,divide(iq,2))))
print "What is {", what, "}?"
