#! /usr/bin/python

# Lambdas
# ------
# A lambda (or an anonymous function) is a function that is not bound to any identifier
# Lambdas are often used when we want to return a function as an argument
#
# Unlike in other functional programming languages, python does not let us define
# normal functions anonymously; a lambda can only contain an <expression> that is returned
#
# A lambda function can be used anywhere a function is expected.
#
#
print "\n"
print "-- lambda --"

def multiplier(x):
    return lambda n: n * x

times3 = multiplier(3)
times20 = multiplier(20)

print "4 times 3 is %d" % times3(4)
print "4 times 20 is %d" % times20(4)


# Slightly advanced use-cases:
#
# Lamda functions are useful in list operations...

my_array = [10,15,20,23, 26, 27, 13, 29, 43, 56, 108]
print my_array

# retrieve only the elements that are divisible by 5:
print "Divisible by 5:"
print filter(lambda x:x%5==0, my_array)

# square each element of the array
print "Squared:"
print map(lambda x: x**2, my_array)

# compute the sum of the elements of the array
print "Sum"
print reduce(lambda x,y: x+y, my_array)
