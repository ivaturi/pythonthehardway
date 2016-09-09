#! /usr/bin/env python

# A simple game engine

class User(object):
    def __init__(self):
        # start with perfect health
        self.health = 100
        # start with a random name
        self._name   = "John Doe"
        # kill count
        self.kills  = 0
        # how many rooms have I gone through?
        self.num_rooms = 0

    def say(self,thing = ""):
        print thing

    def ask(self, thing = ""):
        if len(thing) > 1:
            print thing
        return(raw_input("> "))
    
    def set_name(self):
       self._name = self.ask("What is your name?") 

    def get_name(self):
        return self._name
       
# Scene
class Scene(object):
    def __init__(self):
        """
        Base class for scenes
        """
        self.description = "Scene description goes here"
        self.monsters = []
        self.objects  = []
    
# Let's build a few locations for the map
scene_descriptions = {
    "first" : "Welcome to the game, %s."
    "last"  : "Goodbye, %s. It was fun knowing you."
}


# The map 
class Map(object):
    def __init__(self):
        pass
  


class Engine(object):
    def __init__(self, scene_map):
        self.map = scene_map
        pass

    def play(self):
        self.map.opening_scene()
        pass


    
user = User()
user.set_name()
print user.get_name()
