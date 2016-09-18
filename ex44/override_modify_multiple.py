#! /usr/bin/env python

# What about multiple inheritances? How does alteration with inheritance work then?

class Parent1(object):
    def say(self):
        print "Hi, this is Parent1"

class Parent2(object):
    def say(self):
        print "Hi, this is Parent2"

class Child1(Parent1, Parent2):
    def say(self):
        print "Hi, this is Child1"
        super(Child1, self).say()

class Child2(Parent2, Parent1):
    def say(self):
        print "Hi, this is Child2"
        super(Child2,self).say()



Child1().say()
Child2().say()


# Method Resolution Order for multiple inheritance: C3 (oversimplified: left > up > right)
