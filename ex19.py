#!/usr/bin/python

# exercise 19: functions and variables

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses and %d boxes of crackers!" % (cheese_count, boxes_of_crackers)
    print "Man, that's enough for a party!"
    print "Get a blanket. \n"

# passing values directly to the function
cheese_and_crackers(10,50)

# passing values through variables
count1 = 12
count2 = 24

cheese_and_crackers(count1,count2)

# doing math...
cheese_and_crackers(count1 + 12, count2 / 2)
