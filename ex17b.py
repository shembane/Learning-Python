# This is a shortened version of the file designed to achieve the same purpose in the shortest script I can create. Here is one line of code. It's a long line but it's one line separated by semi-colons.

from sys import argv
from os.path import exists

script, from_file, to_file = argv

in_file = open(from_file) ; indata = in_file.read() ; out_file = open(to_file, 'w') ; out_file.write(indata) ; out_file.close() ; in_file.close()
