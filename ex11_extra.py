name = raw_input("What is your name? ")
print "Hi %s," % name,
home = raw_input("where do you live? ")

print "I hear that %s is a great place to raise a family, %s." % (home, name)

# In this next line, note the variables inside the raw_input string. If you place those variables outside the brackets, the result is an error. Check out <http://stackoverflow.com/questions/43602790/how-do-i-insert-a-variable-into-a-raw-input-query/43602827?noredirect=1#comment74255515_43602827> for more info and explanation.

age = raw_input("How old are you, %s? " % name)
height = raw_input("One more question. How tall are you? ")

print "Ok, thanks for all that information %s. So you live in %s, you are %s tall and you are currently %s years of age." % (name, home, height, age)
