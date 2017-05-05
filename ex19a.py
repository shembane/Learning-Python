# The idea with this exercise is to come up with 10 variations of function inputs. I didn't get that far.

def cheeses_and_crackers(cheeses, crackers):
    print "You have %d types of cheeses." % cheeses
    print "You have %d types of crackers." % crackers
    print "That is a lot of cheese and crackers!\n"

# Variation 1
print "In this variation, the script uses pre-defined values for the variables."
cheeses1 = 6
crackers1 = 7
cheeses_and_crackers(cheeses1, crackers1)

# Variation 2 with user input
print "In this variation, I'll ask you to give me the values."
print "How many cheeses do you have?"
cheeses2 = int(raw_input("> "))

print "How many types of crackers do you have?"
crackers2 = int(raw_input("> "))

cheeses_and_crackers(cheeses2, crackers2)

# Variation 3
print "This variation takes values from the previous two variations and adds them up."
cheeses_and_crackers(cheeses1 + cheeses2, crackers1 + crackers2)

# Variation 4
print "In this one I'm just going to supply values for the cheeses_and_crackers variable directly."
cheeses_and_crackers(9, 11)

# Variation 5
print "This variation uses some pre-define calculations."
cheeses_and_crackers(5 + 9, 6 + 12)

# Variation 6
print "This 6th variation blends variables and pre-define values. In this case, the variables are %s and %s from Variation 2." % (cheeses2, crackers2)
cheeses_and_crackers(cheeses2 + 7, crackers2 + 10)
