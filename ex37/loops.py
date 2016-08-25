#! /usr/bin/python

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
