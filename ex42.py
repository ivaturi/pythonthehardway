#! /usr/bin/env python

# Exercise 42: Objects and classes, practice

## Animal is-a object
class Animal(object):
    pass


## Dog is-a Animal, and has-a init
class Dog(Animal):

    def __init__(self, name):
        self.name = name


## Cat is-a Animal, and has-a init
class Cat(Animal):

    def __init__(self, name):
        self.name = name


## Person is-a object, and has-a init function.
## Person also has-a pet, of some kind
class Person(object):

    def __init__(self, name):
        self.name = name
        self.pet  = None


## Employee is-a Person, and has-a init function
class Employee(Person):

    def __init__(self, name, salary):
        ## invoke the parent class's init function
        super(Employee, self).__init__(name)
        ## set a local variable
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## Rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("satan")

## mary is-a Person
mary = Person("Mary")

## Mary has-a pet called Satan
mary.pet = satan

## Frank is-a Employee with a salary of 120000
frank = Employee("Frank", 120000)

## Frank has-a pet called Rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
