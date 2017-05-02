from sys import argv

print "What is your file called?"
filename = raw_input("> ")

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
