#!/usr/bin/python
# exercise 19: practice

# define a function
def greet(firstname = "john", lastname = "doe"):
    print "Hello, %s %s." % (lastname, firstname)

# --------
# TASK - call this function in 10 different ways
# ---------

#1 - pass values directly
greet("Leo","McCoy")

#2 - pass values through variables
f = "James"
l = "Kirk"
greet(f,l)

#3 - prompt for user input
f_prompt = "Enter a first name >> "
l_prompt = "Enter a last name >> "
greet(raw_input(f_prompt),raw_input(l_prompt))

#4 - use the default values
greet()

#5 - use the default first name
greet(lastname="wayne")

#6 - use the default last name
greet("jane")

#7 - assign the function to another variable
hello_greeting = greet
hello_greeting("sarah")

#8 - assign the result to another variable
var = greet("Thomas")
print "%r" % var # this is 'none', because the function returns nothing

#9 - use the default first name and ask the user for a last name
greet(lastname = raw_input("Please enter a last name >> "))

#10 - use a variable and a default
greet(lastname = l)
