#! /usr/bin/env python

# NOTES:
#
# Prefix private variables within a class with a double underscore (__)
# See: http://stackoverflow.com/a/5690920
#
#

# A simple game engine
class Player(object):
    """
    Player handler
    """
    def __init__(self):

        self.__name   = "John Doe"

    def __console(self):
        """
        Template for accepting user input
        """
        return raw_input("> ")
    
    def say(self,message = ""):
        """
        Prints a message to the console
        """
        print message

    def ask(self, thing = ""):
        if len(thing) > 1:
            print thing
        return self.__console()
    
    def set_name(self,name = ""):
       self.__name = name 

    def get_name(self):
        return self.__name
       
# Scene
class Scene(object):
    def __init__(self, description = ""):
        """
        Base class for scenes
        """
        self.__description = description
        
        
    
# Let's build a few locations for the map
scene_descriptions = {
    "first" : "Welcome to the game, %s.",
    "room"  : "Welcome to room %s",
    "last"  : "Goodbye, %s. It was fun knowing you."
}


# The map 
class Map(object):
    def __init__(self, num_scenes = 3):
        """
        Initiates a map with a given number of scenes
        The minimum number of scenes is 3, so if a lesser number
        is given, the map still chooses 3 scenes.
        """
        if num_scenes < 3:
            num_scenes = 3

        # build a room-name array:
        self.__scenes = ["first"]
        for count in range(1,num_scenes-1):
            self.__scenes.append("room")

        self.__scenes.append("last")
        print self.__scenes


class Engine(object):
    def __init__(self, scene_map):
        self.map = scene_map
        pass

    def play(self):
        self.map.opening_scene()
        pass
