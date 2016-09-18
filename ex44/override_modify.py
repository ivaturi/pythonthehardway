#! /usr/bin/env python


# Altering inherited functions


class Parent(object):
    def altered(self):
        print "PARENT altered"

class Child(Parent):
    def altered(self):
        print "CHILD, before alterations"
        super(Child,self).altered()
        print "CHILD, after PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()
