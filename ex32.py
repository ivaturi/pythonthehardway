#! /usr/bin/python

# Exercise 32: Loops and lists

# How to make a list:
# list_name = [comma-separated list contents]

the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
changes = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# go through the list with a for-loop:
for number in the_count:
    print "This is the count: %d" % number

for fruit in fruits:
    print "A fruit of type: %s" % fruit

# for mixed lists, we can't really use %s or %d because not all
# list items are of the same type
for change in changes:
    print "I got %r" % change

# constructing lists:
elements = []

# use the range function for increments:
for count in range(25,33):
    print "Adding %d to the list." % count
    elements.append(count)

for element in elements:
    print "Element was: %d" % element


### Study drill  - 2 ###

# What type is a range?
print "range(0,6) is of type *%s*" % type(range(0,6))

# Assign a range to a list
range_list = range(0,6)
print range_list

### Study drill  - 3 ###

# What things can we do with lists?
# Quite a few, according to help(list)...

my_list = ["first_is", "This", "is", "list", "is"]
print my_list

# we can count the occurrences of an item
print "'is' occurs %d times in my_list" % my_list.count("is")

# we can pop values (default: last, but we can specify an index)
print "Popping from the list: %s" % my_list.pop()
print "Popping from the beginning : %s" % my_list.pop(0)
print my_list

# we can insert values:
my_list.insert(2,"a")
print my_list

# we can extend a list
my_list.extend([1,2,3,4,5])
print my_list

# we can reverse a list
my_list.reverse()
print my_list

# we can sort the items in a list
my_list.sort()
print my_list
