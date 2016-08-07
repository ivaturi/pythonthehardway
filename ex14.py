# exercise 14: prompting and passing

# import sys
from sys import argv

# unpack
script, user_name, lives = argv
prompt = "> "

print "Hi %s, I'm the %s script." % (user_name,script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "What kind of a computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %s. Not sure where that is.
And you have a %s computer.
Nice.
""" % (likes, lives, computer)
