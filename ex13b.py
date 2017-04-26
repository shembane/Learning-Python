from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is called:", first
print "Your second variable is called:", second
print "Your third variable is called:", third

# This next line just adds a prompt for a fourth value after the original input on the command line.

fourth = raw_input("What is your fourth variable? ")
print "Your fourth variable is called:", fourth
