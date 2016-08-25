#! /usr/bin/python

##### LAMBDA #####

print "\n"
print "-- lambda --"

def multiplier(x):
    return lambda n: n * x

times3 = multiplier(3)
times20 = multiplier(20)

print "4 times 3 is %d" % times3(4)
print "4 times 20 is %d" % times20(4)
