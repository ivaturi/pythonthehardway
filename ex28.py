#! /usr/bin/python

# Exercise 28: Boolean practice

# my answers, to check for correctness
aye = True
nay = False
fail_count = 0

# function to check for correctness
def check(my_guess,condition):
    if(eval(condition) != my_guess):
        print "Fail! *%s* evalutes to <%s>, you said <%s>." % (condition, eval(condition), my_guess)
        fail_count+=1

check(aye, "True and True")
check(nay, "False and True")
check(nay, "1 == 1 and 2 == 1")
check(aye, '"test" == "test"')
check(aye, "1 == 1 or 2 != 1")
check(aye, "True and 1==1")
check(nay, "False and 0 != 0")
check(aye, "True or 1==1")
check(nay, '"test" == "testing"')
check(nay, '"test" == 1')
check(aye, 'not(True and False)')
check(nay,'not(1==1 and 0!=1)')
check(nay,'not(10==1 or 1000==1000)')
check(nay,'not(1!=10 or 3==4)')
check(aye,'not("testing" == "testing" and "Zed" == "Cool Guy")')
check(aye, '1==1 and not("testing"==1 or 1==0)')
check(nay,'"chunky"=="bacon" and (not(3==4 or 3==3))')
check(nay,'3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))')


print "Total fails: %d" % fail_count
