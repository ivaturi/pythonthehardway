#! /usr/bin/env python

# NOTES:
#
# Prefix private variables within a class with a double underscore (__)
# See: http://stackoverflow.com/a/5690920
#
#

from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()"
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she was smarter.",
        "What a loser.",
        "I have a small puppy that is better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(Death.quips)-1)]
        exit(1)
