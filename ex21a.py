def addition(a, b, c):
    print "Adding %d + %d + %d" % (a, b, c)
    return a + b + c

print "What is the cumulative ages of me and the kids?"

age1 = float(raw_input('How old are you? '))
age2 = float(raw_input('How old is your first child? '))
age3 = float(raw_input('How old is your second child? '))

print "So your age is %d, your first child is %d years old and your second child is %d years old." % (age1, age2, age3)

ages = addition(age1, age2, age3)

print "So that means your accumulative ages are ", ages, "\nThat's not so much."

# Hah! this worked the first time!
