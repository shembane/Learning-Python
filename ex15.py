from sys import argv
# This associates the argv function with the script and the filename variable #
script, filename = argv
# The open command targets the filename variable in conjunction with txt #
txt = open(filename)
# Line 7 adds the filename I specified in the execution command into the output #
print "Here's your file %r:" % filename
print txt.read()

# This next part prompts to type the filename so it can print the text again #
print "Type the filename again:"
file_again = raw_input("> ")
# This uses another variable txt_again to use with a secondary process - opening the file #
txt_again = open(file_again)
# This then prints the same text file but in a secondary process #
print txt_again.read()
