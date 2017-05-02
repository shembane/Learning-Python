from sys import argv
# This next line tells the script that, when running it, I'll need to name the file I'll be working with
script, filename = argv
# This next part creates the two options for dealing with the file.
print "We are going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# This is just a prompt for the choice mentioned above.
raw_input("?")
# This part creates and opens the file I named when running the script.
print "Opening the file..."
target = open(filename, 'w')
# This part erases the contents of the file.
print "Truncating the file. Goodbye!"
target.truncate()
# In this next part, the script asks for 3 lines of text to write to the emptied file.
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
# Now the script takes the 3 lines and writes them to the file.
print "I'm going to write these to the file."
# In this section, the script takes each line input and writes it to the file. The \n string creates a new line break.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# In this part, the script saves and closes the file.
print "And finally, we close it."
target.close
