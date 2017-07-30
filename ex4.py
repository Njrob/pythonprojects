# How many cars there are
cars = 100

# How much space is in one car
space_in_a_car = 4

# How many available drivers there are
drivers = 30

# How many passengers need to be driven
passengers = 90

# How many cars will not be driven; take the total number of cars - the total number of available drivers
cars_not_driven = cars - drivers

# The number of cars driven will equal the amount of available drivers
cars_driven = drivers

# The capacity for any car to include multiple passengers, which is calculated by multiplying the number of cars driven by the amount of space in a car
carpool_capacity = cars_driven * space_in_a_car

# The average number of passengers per car, which is found by dividing the total number of passengers to be driven by the number of cars driven
average_passengers_per_car = passengers / cars_driven

# Each line will print out two strings, split up by variables storing numerical information; this line prints out how many cars are available.
print "There are", cars, "cars available."

# This line prints out how many drivers are available.
print "There are only", drivers, "drivers available."

# This line prints out the number of empty cars today.
print "There will be", cars_not_driven, "empty cars today."

# This line prints the carpool capacity, or how many people can be transported today.
print "We can transport", carpool_capacity, "people today."

# This line prints out how many passengers need to be carpooled today.
print "We have", passengers, "to carpool today."

# This line prints out the average number of passengers per car, or how many passengers should be allotted to each car.
print "We need to put about", average_passengers_per_car, "in each car."
