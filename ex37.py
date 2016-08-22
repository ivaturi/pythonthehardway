#! /usr/bin/python

# Exercise 37: symbol review

## Keywords:
print "-- Keywords (logical operators and booleans) --"
print "True and False is >>> ", True and False
print "True or False is >>> ", True or False
print "True and not False is >>> ", True and not False

# conditional flow
print "-- Keywords (conditional) --"
a = 10
b = 12

if a < b:
    print "a is lesser than b"
elif a==b:
    print "a is equal to b"
else:
    print "a is greater than b"

# Loops    
print "-- Loops --"
for count in range(0,3):
    print "count is %d" % count

##### BREAK #####
#    'break' terminates the nearest enlosing loop.
#    It should only be used under 'for' or 'while' loops
#
#    Within a try-except block, 'break' doesn't immediately
#    break flow; it moves the flow to 'finally' before exiting.
print "-- Break --"
for loop_counter in range(0,20):
    print "%d" % loop_counter,
    if loop_counter == 11:
        print "\nUh oh. I met a 11. Peace out."
        break


##### ASSERT ######
#     Assert statements are used to insert debugging assetions into a program
#     They help to ascertain that the internal state of a program is as we expect
#     it to be.

#    If an assert fails, an AssertionError is thrown; unless this is handled by
#    an 'except' block, the program will terminate.

print "-- Assert --"
def check_square(num, num_square):
    """This function checks if you have guessed the square of a number correctly"""
    assert num_square == num**2
    return num_square

print "check_square(2,4) >>> ", check_square(2,4)
#print "check_square(3,6) >>> ", check_square(3,6)  # <--- This will throw an AssertionError

from types import *
def test_assert(x,y):
    """this function accepts numeric inputs, and checks if the inputs are really numerical"""
    assert type(x) is IntType, "The first input should be an integer!"
    return x + y

test_assert(1, 2.2)
#test_assert(2.2, 1)  # <--- This will throw an AssertionError, because the first input is not an integer     

