from sys import argv
#This next line informs the argv function by defining which file to use
script, filename = argv
# This next line opens the file I named when executing the script
txt = open(filename)
# These next two lines tell me which file was opened and then prints the contents of the file
print "Here's your file %r:" % filename
print txt.read()
#In the next two lines, the script asks me to tell it which file to open instead of using the initial argv import method
print "Type the filename again:"
file_again = raw_input("> ")
# In this next line, the script opens the file I specified at the prompt.
txt_again = open(file_again)
# In this next line, the script prints the contents of the file I named at the prompt.
print txt_again.read()
