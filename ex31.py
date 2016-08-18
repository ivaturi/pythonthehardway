#! /usr/bin/python

# Exercise 31: Making decisions

print "You enter a dark room with two doors. Do you go through door#1 or door#2?"

# which door?
door = raw_input("> ")

# what is behind door 1?
if door == "1":
    print "there's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    # what do you do?
    bear = raw_input("> ")
    
    # Take the cake
    if bear == "1":
        print "The bear eats your face off. Good job!"
    # scream at the bear?!
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    # do something else
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

# what's behind door 2?
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    # what do you do?
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

# there's no other door!!
else:
    print "You stumble around and fall on a knife and die. Good job!"
