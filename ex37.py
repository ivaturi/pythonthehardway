#! /usr/bin/python

# Exercise 37: symbol review

## Keywords:
print "-- Keywords (logical operators and booleans) --"
print "True and False is >>> ", True and False
print "True or False is >>> ", True or False
print "True and not False is >>> ", True and not False

# conditional flow
print "\n"
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
print "\n"    
print "-- Loops --"
for count in range(0,3):
    print "count is %d" % count

##### BREAK #####
#    'break' terminates the nearest enlosing loop.
#    It should only be used under 'for' or 'while' loops
#
#    Within a try-except block, 'break' doesn't immediately
#    break flow; it moves the flow to 'finally' before exiting.
print "\n"
print "-- Break --"
for loop_counter in range(0,20):
    print "%d" % loop_counter,
    if loop_counter == 11:
        print "\nUh oh. I met a 11. Peace out."
        break

        
##### CONTINUE #####
#    This keyword is used in for and while loops, to continue with
#    the next cycle of the loop
print "\n"
print "-- Continue --"
for count in range(1,20):
    if count%2 != 0:
        print "%d" % count
    elif count%5 == 0:
        # if a number is even and a multiple of 5, print it
        print "%d (even multiple of 5!)" % count
    else:
        # don't print even numbers
        continue
print "\n"

##### EXEC #####
#    This keyword is used to execute other python statements
#    Try to avoid using this, because it introduces (usually) unnecessary complexity
print "-- Exec --"
list_builder = "exec_list = [1,2,3,4,5,6,7]"
exec list_builder
print "exec_list: ", exec_list

function_builder = """
def exec_function():
\tprint "This function is created within an exec block"
"""

exec function_builder
exec_function()

##### ASSERT ######
#     Assert statements are used to insert debugging assetions into a program
#     They help to ascertain that the internal state of a program is as we expect
#     it to be.

#    If an assert fails, an AssertionError is thrown; unless this is handled by
#    an 'except' block, the program will terminate.
print "\n"
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



##### TRY-EXCEPT-FINALLY #####

#  The try statement is used to specify exception handlers.
#  An exception is a point in the program where normal flow
#  of control breaks. A 'try' block helps us handle these
#  exceptions by providing exception handlers (except).

#  An exception raised by a 'try' block should be handled by
#  a corresponding 'except' block. The except block can either
#  handle specific kinds of exceptions (TypeError/DivideByZeroError)
#  or it can just catch all generic exceptions (not a very good idea)

#  If a try-except block is followed by a 'finally' block. the 'finally'
#  block is executed *no matter what happens* in the try block.

# If an exception is raised and isn't caught by any 'except' statement
#  the program is terminated.
print "\n"
print "-- try-except-finally --"
global a

try:
    a = 1/0
# we can catch specific exceptions like this:
except ZeroDivisionError:
    print "ERROR! You tried to divide by zero!"
    # we can catch generic exceptions like this:
except:
    print "ERROR! You did something wrong!"
finally:
    a = 1/2.0

print "a = %f" % a


##### LAMBDA #####

print "\n"
print "-- lambda --"

def multiplier(x):
    return lambda n: n * x

times3 = multiplier(3)
times20 = multiplier(20)

print "4 times 3 is %d" % times3(4)
print "4 times 20 is %d" % times20(4)
