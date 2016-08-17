#! /usr/bin/python

# Exercise 28: Boolean practice

# my answers, to check for correctness
aye = True
nay = False

# function to check for correctness
def check(condition, my_guess):
    print condition == my_guess


check(True and True, aye)
check(False and True, nay)
check(1 == 1 and 2 == 1, nay)


