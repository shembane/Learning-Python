from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "What is your favourite book, %s?" % user_name
book = raw_input(prompt)

print """
Alright, so you said %r, you like me.
You live in %r. I think I know where that is.
And you have a %r computer. Nice.
Your favourite book is %r. I like it too.
""" % (likes, lives, computer, book)
