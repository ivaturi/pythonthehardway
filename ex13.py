# exercise 13: parameters, unpacking, variables

# import lets us add features to our scripts from a
# Python pre-defined feature set (a.k.a, a module, a.k.a library)
# In this case, we're importing the 'sys' module

# argv hold the arguments that we pass to the script
from sys import argv

# this assignment unpacks argv; it assigns the contents of
# argv to the four variables
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third


print "The sum of %d, %d, and %d is %d" % (int(first),int(second),int(third),int(first) + int(second) + int(third))
