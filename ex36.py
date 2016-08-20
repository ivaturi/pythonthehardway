#! /usr/bin/python
# encoding: UTF-8

# Rules for if-statements:
#  - Every if statement must have an else
#  - In else-statements that 'should never run', use die() 
#  - Never nest if-statements more than two deep 
#  - Blank lines before and after if-elif-else statements
#  - Move complex boolean calculations outside if-checks


# Rules for loops:
#  - Try and never use while-loops
#  - Use for-loops when there are a fixed or limited number of things to loop over

# Debugging
#  - Use print statements to check what is happening in the code 
#  - Code a little, run a little, fix a little


## Homework ##

#                     | - door - |
#                     |          |
#                     |          |
#  ———————————————————   (keys)  |
#  |   Storage       /           |
#  |   (1x torch)                |
#  ———————————————————           |


# door >>> keys >>> storage room >>> box >>> torch


# first, some utility functions
def build_message(description, *args):
    """Provide some description, and a list of things the user can do"""
    print description
    # do we give the user something to do?
    if len(args) > 0:
        print "The following actions are available:"
        action_counter = 0
        for action in args:
            print "%d : %s" % (action_counter+1, action)
            action_counter += 1
        print "What do you want to do?"
        choice = int(raw_input("> "))
        return choice


def start():
    """The beginning"""
    description = "You are at a door. It seems unlocked, but there is a faint light behind the door."
    actions = ("Turn away", "Knock the door", "Open the door")
    
    # what does the user say? 
    user_say = build_message(description, *actions)
    


# let's play a game
start()
