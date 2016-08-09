# exercise 16: reading and writing files

# import stuff
from sys import argv

# get the name of the file from the command line
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want this to happen, press CTRL+C."
print "If you do want that, press ENTER."

raw_input("?")

print "Opening the file..."

# create a file object, in write mode
target = open(filename,'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1 >> ")
line2 = raw_input("Line 2 >> ")
line3 = raw_input("Line 3 >> ")

print "I'm going to write these to the file."

target.write("%s\n%s\n%s"%(line1, line2, line3))

print "And finally, we close the file."
target.close()
