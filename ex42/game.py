#! /usr/bin/env python


# Zed's version of the game

# imports for the game
from sys import exit
from random import randint


class Scene(object):
    """
    Base class for scenes
    """
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
    """
    The death scene
    """
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she was smarter.",
        "What a loser.",
        "I have a small puppy that is better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(Death.quips)-1)]
        exit(1)


class CentralCorridor(Scene):
    """
    The central corridor
    """
    def enter(self):
        msg = """
        The Gothons of Planet Percal #25 have invaded your ship and destroyed
        your entire crew. You are the last surviving member and your last mission
        is to get the neutron destruct bomb from the Weapons Armory, put it in the
        bridge, and blow up the ship after getting into an escape pod.

        You are running down the central corridor to the Weapons Armory when a 
        Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown
        costume flowing around his hate filled body. He is blocking the door to
        the armory and is about to pull a weapon to blast you.
        """

        print msg
        action = raw_input("> ")

        if action == "shoot":
            msg = """
            Quick on the draw, you yank out your blaster and fire it at the Gothon.
            His clown costume is flowing and moving around his body, which throws off
            your aim. Your laser hits his costume but misses him entirely. 

            This completely ruins his brand new costume his mother bought him, which
            makes him fly into an insane rage and blast you repeatedly in the face until
            you are dead. Then he eats you.
            """
            print msg
            return "death"

        elif action == "dodge":
            msg= """
            Like a world-class boxer you dodge, weave, slip and slide right as
            the Gothon's blaster cranks a laser past your head.

            In the middle of your artful dodge your foot slips and you bang
            your head on the metal wall and pass out.

            You wake up shortly after only to die as the Gothon stomps on
            your head and eats you.
            """
            print msg
            return "death"

        elif action=="joke":
            msg = """
            Lucky for you they made you learn Gothon insults in the academy.
            You tell the one Gothon joke you know:
            'Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur nebhaq
            gur ubhfr.'
            
            The Gothon stops, tries not to laugh, then busts out laughing and can't move.
            While he's laughing, you run up and shoot him square in the head, putting him
            down, then jump through the Weapon Armory door.
            """
            print msg
            return "laser_weapon_armory"

        else:
            print "DOES NOT COMPUTE"
            return "central_corridor"


class LaserWeaponArmory(Scene):
    """
    The armory
    """
    def enter(self):
        msg = """
        You dive into the armory, crouch, and scan the room for more Gothons that might
        be hiding. It is dead quiet, too quiet. You stand up and run to the far side of
        the room and find the neutron bomb in its container. There is a keypad lock on
        the box and you need the code to get the bomb out. If you get the code wrong 
        10 times, the lock closes forever and yo can't get the bomb. The code is 3 digits.
        """
        print msg
        code = "%d%d%d" % (randint(1,9),randint(1,9),randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 1 # 0-index gives us 11 tries, not 10

        while guess != code and guesses < 10:
            print "BZZZZZZZZZZZT"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code or guess == "code":
            msg = """
            The container clocks open and the seal breaks, letting gas out.
            You grab the neutron bomb and run as fast as you can to the bridge
            where you must place it in the right spot.
            """
            print msg
            return "the_bridge"
        else:
            msg = """
            The lock buzzes one last time and then you hear a sickening melting
            sound as the mechanism is fused together.

            You decide to sit there, and finally the Gothons blow up the ship from
            their ship and you die.
            """
            print msg
            return "death"



class TheBridge(Scene):
    """
    The bridge of the ship
    """
    def enter(self):
        msg = """
        You burst onto the Bridge with the neutron destruct bomb under your arm
        and surprise 5 Gothons who are trying to take control of the ship.

        Each of them has an even uglier clown costume than the last. They haven't 
        pulled their weapons out yet, as they seethe active bomb under your arm
        and don't want to set it off.
        """
        print msg
        action = raw_input("> ")

        if action == "throw":
            msg = """
            In a panic you throw the bomb at the group of Gothons and make a leap
            for the door. Right as you drop it a Gothon shoots you right in the 
            back, killing you.

            As you die you see another Gothon frantically trying to disarm the bomb.
            You die knowing they will probably blow up when it goes off. 
            """
            print msg
            return "death"

        elif action == "place":
            msg = """
            You point your blaster at the bomb under your arm. The Gothons put their
            hands up and start to sweat. You inch backward to the door, open it, and
            then carefully place the bomb on the floor, pointing your blaster at it.

            You jump back through the door, punch the close button, and blast the lock
            so the Gothons cannot get out. 

            Now that the bomb is placed you run to the escape pod to get off this tin
            can.
            """
            print msg
            return "escape_pod"

        else:
            print "DOES NOT COMPUTE"
            return "the_bridge"


class EscapePod(Scene):
    """
    The escape pod
    """
    def enter(self):
        msg = """
        You rush through the ship desperately trying to make it to the escape pod
        before the whole ship explodes. It seemslike hardly any Gothons are on the 
        ship, so your run is clear of interference.

        You get to the chamber with the escape pods, and now need to pick one to 
        take. Some of them could be damaged but you don't have the time to look.
        
        There are 5 pods; which one do you take?
        """
        print msg

        # Cheating: there is only one bad pod
        bad_pod = raw_input("[pod]> ")

        if int(guess) == bad_pod:
            msg = """
            You jump into pod %s and hit the eject button. The pod escapes out
            into the void of space, then implodes as the hull ruptures, crushing
            your body into jam jelly.
            """
            print msg % guess
            return "death"
        else:
            msg = """
            You jump into pod %s and hit the eject button. The pod easily 
            slides out into space heading to the planet below. As it flies to the 
            planet, you look back and see your ship implode lije a bright star,
            taking out the Gothon ship at the same time.

            You won!
            """
            print msg %guess
            return "finished"

class Finished(Scene):
    """
    The last scene
    """
    def enter(self):
        print "You won! Good job."
        return "finished"


# The map
class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }


    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


# let's play!
m = Map('central_corridor')
g = Engine(m)
g.play()
