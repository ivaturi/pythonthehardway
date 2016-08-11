# exercise 15: reading files

from sys import argv

# pass the file to be read as an argument to the script
script, filename = argv

# open the file
txt = open(filename)

print "Here is your file *%s*: " % filename
print txt.read()
txt.close()


print "Type the filename again:"
file_again = raw_input(">> ")

txt_again = open(file_again)
print txt_again.read()
txt_again.close()
