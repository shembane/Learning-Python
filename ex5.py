name = 'Zed A. Shaw'
age = 35 # Not a lie
height = 74 # inches
height_cm = 74 * 2.54
weight = 180 # lbs
weight_kg = 180 * 0.45
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
# This next line is a statement of the height to centimeters
print "In centimeters, his height is %s." % height_cm
# This next line is a statement of weight in kilograms
print "In kilograms, his weight is %s." % weight_kg
print "He's %d pounds heavy or %d kilograms." % (weight, weight_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
