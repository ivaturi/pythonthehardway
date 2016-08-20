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
    # we start at the main door
    main_door()

def main_door():
    """The beginning"""
    description = "You are at a door. It seems unlocked, but there is a faint light behind the door."
    actions = ("Turn away", "Knock the door", "Open the door")
    consequences = (end,knock,enter)
    # send to the user 
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
    """Enter the house"""
    description = "You open the door and enter the house. A faint TV plays in the other room, but there doesn't seem to be anyone else home."
    actions = ("Look around", "Go outside")
    consequences = (main_door_look, end)
    # send to the user
    say(description, actions, consequences)
 
def main_door_look():
    """Looking into the house"""
    description = "You are at one end of a dimy lit corridor. A few feet away, there seems to be a door on your right.\nThe walls are a dull green, and lined by what seem to be really old family photos.\nThe floor is creaky in places, and sounds surprisingly hollow."
    actions = ("Look at the photos", "Walk towards the door", "Inspect the floor")
    consequences = (boring, to_storage_door, inspect_floor)
    #send to the user
    say(description, actions, consequences)

def boring():
    end("TBD")

def to_storage_door():
    end("TBD")

def inspect_floor():
    end("TBD")

# let's play a game
start()
