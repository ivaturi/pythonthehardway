# variables and names

cars = 100              # initialize the number of cars
space_in_a_car = 4.0    # how many passengers?
drivers = 30            # total number of drivers
passengers = 90         # total number of passengers

cars_not_driven = cars - drivers    # free cars
cars_driven = drivers               # busy cars

carpool_capacity = cars_driven * space_in_a_car         # how many people can carpool?
average_passengers_per_car = passengers / cars_driven   # avg per car


# print things to the console
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "we can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
