#! /usr/bin/env python

# A simple game engine

class Engine(object):
    def __init__(self, scene_map):
        self.map = scene_map
        pass

    def play(self):
        self.map.opening_scene()
        pass

# The superclass for scenes
# A scene does the following:
#    - present itself to the player (enter)
#    - pose a question and offer choices (ask)
#    - retrieve the user's choice
#    - point to the next scene
class Scene(object):
    def __init__():
        pass
    
    def enter(self):
        pass

    def do(self):
        pass

 
class Opening(self):
    def enter(self):
        pass

    
class Death(Scene):
    def enter(self):
        pass

class CentralCorridor(Scene):
    def enter(self):
        print "Central corridor!"

class LaserWeaponArmory(Scene):
    def enter(self):
        pass

class TheBridge(Scene):
    def enter(self):
        pass

class EscapePod(Scene):
    def enter(self):
        pass

# The map 
class Map(object):
    def __init__(self, start_scene):
        self.scenes = [
            EscapePod,
            TheBridge,
            Death,
            LaserWeaponArmory,
            CentralCorridor
        ]
        import random
        
    def next_scene(self):
        # pick a random scene
        random.choice()().enter()
        

    def opening_scene(self):
        CentralCorridor().enter()     
        pass

a_map = Map('central corridor')
a_game = Engine(a_map)
a_game.play()
