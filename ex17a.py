from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s " % (from_file, to_file)

# we could do these two in one line, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

# The prompt to allow the script to continue was removed to reduce the output and speed up the script's execution

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
