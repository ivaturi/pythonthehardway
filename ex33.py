#! /usr/bin/python

# Exercise 33: While loops


# A while loop will keep executing as long as the loop
# condition evaluates to True

# loop counter
counter = 0

# initialize an array
numbers = []

while counter < 6:
    print "Counter:  %d >>>" % counter,
    numbers.append(counter)
    counter += 1
    print "%d" % counter
    print "The array is now ", numbers

# print out the elements of the array
for number in numbers:
    print number


## Study drill 1 ##
print "<<< Study drill 1 >>>"

def num_array(lower_limit = 0, upper_limit = 5, increment  = 1):
    """This function returns a range of values within the specified limits, using the specified increment"""
    numbers = []
    while lower_limit < upper_limit:
        numbers.append(lower_limit)
        lower_limit += increment
    return numbers

# calling num_array with defaults
print num_array()
# array with default increment
print num_array(4, 10)
# array with specified increment
print num_array(50,70,2)
