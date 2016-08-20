#! /usr/bin/python
# encoding: UTF-8

#
#                     | - door - |
#                     |          |
#                     |          |
#  ———————————————————   (keys)  |
#  |   Storage       /           |
#  |   (1x torch)                |
#  ———————————————————           |
#


# door >>> keys >>> storage room >>> box >>> torch

from sys import exit


#  A helper to provde the user with a description and some actions
def say(description, actions = (), consequences = ()):
    """Provide a description, a list of things the user can do, and the consequences of each action"""
    print description
    # do we give the user something to do?
    if len(actions) > 0:
        action_counter = 0
        for action in actions:
            print "%d : %s" % (action_counter+1, action)
            action_counter += 1
        choice = int(raw_input("> "))
        consequences[choice-1]()


def start():
    """The beginning"""
    description = "You are at a door. It seems unlocked, but there is a faint light behind the door."
    actions = ("Turn away", "Knock the door", "Open the door")
    consequences = (end,knock,enter)

    # what does the user say? 
    say(description, actions, consequences)
   

def end(message = "You have left the game"):
    """Leave the game"""
    say(message)
    exit(0)


def knock():
    """What happens if you knock the door?"""
    description = "You knock the door, but nothing happens."
    actions = ("Turn away","Open the door")
    consequences = (end, enter)
    # send to the user
    say(description, actions, consequences)

def enter():
    end("TBD")

# let's play a game
start()
