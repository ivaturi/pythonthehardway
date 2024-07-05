#! /usr/bin/env python


# create a list of things
ten_things = "car bus rocket phone chair stool pen"
print(ten_things)

# are these really ten things?
print("Hm. There are supposed to be ten things in that list...")

# let's keep a bunch of things on hand, to add to our list
more_things = ["bowl", "box", "zebra", "hyena", "bread", "dumpster"]

# make a real list out of the ten_things string
my_stuff = ten_things.split(" ")

# how many things are supposed to be on this list?
required_number_of_things = 10

# add things to my_stuff until we have the requisite amount
while len(my_stuff) < required_number_of_things:
    latest = more_things.pop()
    print("Adding ", latest)
    my_stuff.append(latest)
    print("There are %d things now" % len(my_stuff))



print("my_stuff : ", my_stuff)
print("\n-----")
print("Accessing things...")
print("-----")

# zero-based index, second element
print("      [1] : ", my_stuff[1])

# last element
print("     [-1] : ", my_stuff[-1])

# last in, first out (also modifies the list)
print("   .pop() : ", my_stuff.pop())

# concatenate into a string, using a specified separator
print("  .join() : ", ' '.join(my_stuff))

# concatenate a subset of the list, using a specified operator
print(" .join(3:5) with # : ", ' # '.join(my_stuff[3:5]) )
