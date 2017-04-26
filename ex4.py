# This defines the variable "cars"
cars = 100
# This defines the variable "space_in_a_car"
space_in_a_car = 4
# This defines the variable "drivers"
drivers = 30
# This defines the variable "passengers"
passengers = 90
# This defines the variable "cars_not_driven" by reference to the defined variables of "cars" and "drivers"
cars_not_driven = cars - drivers
# This defines the cariable "cars_driven" as being the equivalent of the variable "drivers"
cars_driven = drivers
# This defines the variable "carpool_capacity" as a multiple of the variables "cars_driven" and "space_in_a_car"
carpool_capacity = cars_driven * space_in_a_car
# This defines the variable "average_passengers_per_car" as being the equivalent of "cars_driven" divided by "passengers"
average_passengers_per_car = passengers / cars_driven

# This next section runs various calculations using the defined variables instead of re-inserting the actual figures again.
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
