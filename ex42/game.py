#! /usr/bin/env python

# A simple game engine

class Engine(object):
    def __init__(self, scene_map):
        pass

    def play(self):
        pass

# The superclass for scenes
class Scene(object):
    def enter(self):
        pass

class Death(Scene):
    def enter(self):
        pass

class CentralCorridor(Scene):
    def enter(self):
        pass

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
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central corridor')
a_game = Engine(a_map)
a_game.play()
