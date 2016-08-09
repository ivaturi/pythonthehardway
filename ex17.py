# exercise 17: more files

from sys import argv

# new import!
from os.path import exists

# get file names from the user
script, from_file, to_file = argv

print "Copying from *%s* to *%s*" % (from_file,to_file)

# task: do this in one statement:
in_file = open(from_file)
indata = in_file.read()

# we can count the length of data
print "The input file is %d bytes long." % len(indata)

# we can check if a file exists
print "Does the output file exist? %s" % exists(to_file)
print "Press ENTER to continue, CTRL+C to abort."
raw_input()

# continue if the user hasn't aborted
out_file = open(to_file, 'w')
out_file.write(indata)

print "Done!"

# it is good practice to close files are opening them
out_file.close()
in_file.close()
