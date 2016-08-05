# more variables and printing

#--- format strings

my_name = "abhi"
my_age = 33
my_height = 186
my_weight = 93
my_eyes = "Black"
my_teeth = "White"
my_hair = "Black"

print "Let's talk about %s." % my_name
print "He is %d cms tall." % my_height
print "He weighs %d kilos." % my_weight
print "That might be a little too heavy."
print "He has %s eyes and %s hair." % (my_eyes,my_hair)
print "He also has %s teeth." % my_teeth

# math inside strings?
print "The sum of %d and %d is %d." % (my_age, my_height, my_age + my_height)

# using variable names
print "The sum of %(age)d and %(height)d is %(total)d." % {"age":my_age,"height":my_height,"total":my_age+my_height}

# we can specify the number of characters in a number type
print "This will print three characters : %03d." % 2
