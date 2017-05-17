# Exercise version

>>> import ex25
>>> sentence = "All good things come to those who wait."
>>> words = ex25.break_words(sentence)
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
>>> sorted_words = ex25.sort_words(words)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_word(words)
All
>>> ex25.print_last_word(words)
wait.
>>> words
['good', 'things', 'come', 'to', 'those', 'who']
>>> ex25.print_first_word(sorted_words)
All
>>> ex25.print_last_word(sorted_words)
who
>>> sorted_words
['come', 'good', 'things', 'those', 'to', 'wait.']
>>> sorted_words = ex25.sort_sentence(sentence)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_and_last(sentence)
All
wait.
>>> ex25.print_first_and_last_sorted(sentence)
All
who
>>>

# Modified exercise version with more efficient script import

# This first line obviates the need to type `ex25` for each function
>>> from ex25 import *
>>> sentence = "All good things comes to those who wait."
>>> words

# This next error was because I jumped ahead and didn't define the parameters of the `words` variable correctly
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'words' is not defined

# Here I defined the parameters for the `words` variable correctly and could continue executing the script.
>>> words = break_words(sentence)
>>> words
['All', 'good', 'things', 'comes', 'to', 'those', 'who', 'wait.']
>>> sorted_words = sort_words(words)
>>> sorted_words
['All', 'comes', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> print_first_word(words)
All
>>> print_last_word(words)
wait.
>>> words
['good', 'things', 'comes', 'to', 'those', 'who']
>>> print_first_word(sorted_words)
All
>>> print_last_word(sorted_words)
who
>>> sorted_words
['comes', 'good', 'things', 'those', 'to', 'wait.']
>>> sorted_words = sort_sentence(sentence)
>>> sorted_words
['All', 'comes', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> print_first_and_last(sentence)
All
wait.
>>> print_first_and_last_sorted(sentence)
All
who
>>>
