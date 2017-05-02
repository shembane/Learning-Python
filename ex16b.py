# This script doesn't work
from sys import argv

script, filename = argv
# I added this next section to first display the file before editing it #
txt = open(filename)
print "Here is your file %r:" % filename
print txt.read()

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file ..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("%s \n %s \n %s \n" % (line1, line2, line3))

print "And finally, we close it."
target.close()
