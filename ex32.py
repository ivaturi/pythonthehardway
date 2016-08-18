#! /usr/bin/python

# Exercise 32: Loops and lists

# How to make a list:
# list_name = [comma-separated list contents]

the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# go through the list with a for-loop:
for number in the_count:
    print "This is the count: %d" % number

for fruit in fruits:
    print "A fruit of type: %s" % fruit
