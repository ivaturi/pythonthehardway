#! /usr/bin/env python

# Inheritance

class Parent(object):
    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    pass


dad = Parent()
son = Child()

dad.implicit()
son.implicit()
