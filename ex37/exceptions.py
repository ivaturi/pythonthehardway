#! /usr/bin/python

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
