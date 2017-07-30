# Defines the function cheese_and_crackers as well as its arguments
def cheese_and_crackers(cheese_count, box_of_crackers):
    # Prints a string with a formatted variable (the argument cheese_count)
    print "You have %d cheeses!" % cheese_count
    # Does the same for the formatted variable box_of_crackers
    print "You have %d boxes of crackers!" % box_of_crackers
    # Prints a string
    print "Man that's enough for a party!"
    # Prints another string
    print "Get a blanket.\n"

# Prints a string
print "We can just give the function numbers directly:"
# Takes the function defined above and passes 20 into the cheese_count argument and 30 into the box_of_crackers argument
cheese_and_crackers(20, 30)

# Prints a string
print "OR, we can use variables from our script:"
# Defines two variables separate from the arguments above
amount_of_cheese = 10
amount_of_crackers = 50

# Takes the original function and places the variables just defined as the cheese_count and box_of_crackers arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Prints a string
print "We can even do math inside too:"

# Takes the function and defines cheese_count and box_of_crackers as mathematical equations
cheese_and_crackers(10 + 20, 5 + 6)

# Prints a string
print "And we can combine the two, variables and math:"

# Takes the function and takes the two arguments as combinations of the defined variables and integers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
