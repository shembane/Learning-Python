# This part defines the functions that the variations below will invoke.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man, that's enough for a party!"
    print "Get a blanket.\n"

# This variation allocates numerical values directly to the two variables defined in the function
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# This variation defines two new sets of variables and assigns them values
print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# This part of this variation uses the variables above to pass values to the function at the top
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# This variation uses two sets of calculations to come up with the values for the variables used in the function
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# This variation uses a combination of numerical values and variables defined in a previous variation to come up with values for the function
print "And we can combine the two, variable and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
