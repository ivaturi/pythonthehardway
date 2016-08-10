#!/usr/bin/python
# exercise 20: functions and files

from sys import argv

# get the input file from the user
script, input_file = argv

# print the contents of the file
def print_all(f):
    print f.read()

# move to the beginning of the file
def rewind(f):
    f.seek(0)

# print a line at the specified position
def print_a_line(line_count, f):
    print line_count, f.readline()


# open file for processing
current_file = open(input_file)

print "First, let's print the whole file: \n"
print_all(current_file)

print "Now, let's rewind to the beginning.\n"
rewind(current_file)

print "Let's print 3 lines:"
current_line = 1 
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

