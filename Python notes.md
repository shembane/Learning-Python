# Introduction to Python

## Useful Python references

* [Learn Python the Hard Way - Read for Free](https://learnpythonthehardway.org/book/)
* [BeginnersGuide at the Python Wiki](https://wiki.python.org/moin/BeginnersGuide)
* [Python Tips](https://pythontips.com)
* [Python Resources at Python Tips](https://pythontips.com/python-resources/), especially [Python Resources](https://pythontips.com/python-resources/#beginners-delight)
* [The Hitchhiker’s Guide to Python! — The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/)

## Comments

Comments have two purposes:

* Explain a function in plain language; and
* Temporarily disable parts of a program.

Comments use the octothorpe or hash - `#`. Here is an example of how the code is used:

```
# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.

print "I could have code like this." # And the comment after is ignored.

# You can also use a comment to "disable" or comment out a piece of code:
# print "This won't run."

print "This will run."
```

## Maths functions

| **Function** | **Description** |
| --- | --- |
| `+` | plus |
| `-` | minus |
| `/` | slash |
| `*` | asterisk |
| `%` | percent |
| `<` | less-than |
| `>` | greater-than |
| `<=` | less-than-equal |
| `>=` | greater-than-equal |
| `=` | single equal |
| `==` | double equal - to test equivalence |

### Questions from the book about % (modulus)

>Why is the `%` character a ”modulus” and not a ”percent”? Mostly that’s just how the designers chose to use that symbol. In normal writing you are correct to read it as a ”percent.” In programming this calculation is typically done with simple division and the `/` operator. The `%` modulus is a different operation that just happens to use the `%` symbol.
>
>How does `%` work? Another way to say it is, ”X divided by Y with J remaining.” For example, ”100 divided by 16 with 4 remaining.” The result of `%` is the J part, or the remaining part.

The order that Python applies the maths functions is "**PEMDAS** which stands
for Parentheses Exponents Multiplication Division Addition Subtraction".

## Variables

A variable is a name for something.

### Question from the book about "=" and "=="

> What is the difference between `=` (single-equal) and `==` (double-equal)? The `=` (single-equal) assigns the value on the right to a variable on the left. The `==` (double-equal) tests if two things have the same value

## Strings

>Every time you put `”` (double-quotes) around a piece of text you have been making a string. A string is how you make something that your program might give to a human. You print strings, save strings to files, send strings to web servers, and many other things.

"This is a string"

> You embed variables inside a string by using specialized format sequences and then putting the variables at the end with a special syntax that tells Python, ”Hey, this is a format string. Put these variables in there.”

When expressing multiple variables, place the variables in parentheses. For example:

`print "He's %d pounds heavy or %d kilograms." % (weight, weight_kg)`

For reference purposes: "[2.3.6.2 String Formatting Operations](https://docs.python.org/2.4/lib/typesseq-strings.html)"

### Further explanation of strings from the book

>A string is usually a bit of text you want to display to someone, or ”export” out of the program you are writing. Python knows you want something to be a string when you put either `”` (double-quotes) or `’` (single-quotes) around the text. You saw this many times with your use of print when you put the text you want to go inside the string inside `”` or `’` after the print to print the string.

>Strings may contain the format characters you have discovered so far. You simply put the formatted variables in the string, and then a `%` (percent) character, followed by the variable. The only catch is that if you want multiple formats in your string to print multiple variables, you need to put them inside `( )` (parenthesis) separated by `,` (commas). It’s as if you were telling me to buy you a list of items from the store and you said, ”I want milk, eggs, bread, and soup.” Only as a programmer we say, ”(milk, eggs, bread, soup).”

Question about variables from the book:

> **What does `%s`, `%r`, and `%d` do again?** You’ll learn more about this as you continue, but they are ”formatters.” They tell Python to take the variable on the right and put it in to replace the `%s` with its value.

> **What is the difference between `%r` and `%s`?** Use the `%r` for debugging, since it displays the ”raw” data of the variable, but the others are used for displaying to users.

### A note about the `formatter` attribute

From "[34.1. formatter — Generic output formatting — Python 2.7.13 documentation](https://docs.python.org/2/library/formatter.html)"

>This module supports two interface definitions, each with multiple implementations. The formatter interface is used by the HTMLParser class of the `htmllib` module, and the writer interface is required by the formatter interface.
>
>Formatter objects transform an abstract flow of formatting events into specific output events on writer objects. Formatters manage several stack structures to allow various properties of a writer object to be changed and restored; writers need not be able to handle relative changes nor any sort of “change back” operation. Specific writer properties which may be controlled via formatter objects are horizontal alignment, font, and left margin indentations. A mechanism is provided which supports providing arbitrary, non-exclusive style settings to a writer as well. Additional interfaces facilitate formatting events which are not reversible, such as paragraph separation.
>
>Writer objects encapsulate device interfaces. Abstract devices, such as file formats, are supported as well as physical devices. The provided implementations all work with abstract devices. The interface makes available mechanisms for setting the properties which formatter objects manage and inserting data into the output.

Also check out this question and answers in Stack Overflow regarding exercise 8 in the book: "[formatter in python - Stack Overflow](http://stackoverflow.com/questions/15280004/formatter-in-python)". Some responses that help clarify `formatter`:

>The formatter acts as a template, each `%r` acting as a place holder for the values in the tuple on the right-hand side.

>That's the classic format for string formatting, `print "%r" % var` will print the raw value of var, four `%r` expects 4 variables to be passed after the `%`.

>formatter is a string. so, the first line is the same as: `"%r %r %r %r" % (1, 2, 3, 4)`

When using the ``\n`` syntax to create new lines, remember that using it with a `%r` formatter changes its behaviour:

>**Why do the `\n` newlines not work when I use `%r`?** That’s how `%r` formatting works; it prints it the way you wrote it (or close to it). It’s the ”raw” format for debugging.

### A note about the `import` statement

Python notes: "[6. Simple statements — Python 2.7.13 documentation](https://docs.python.org/2.7/reference/simple_stmts.html#the-import-statement)"

### Escape sequences

From the book:

>This `\` (backslash) character encodes difficult-to-type characters into a  string. There are various ”escape sequences” available for different characters you might want to use. We’ll try a few of these sequences so you can see what I mean.
>
>An important escape sequence is to escape a single-quote `’` or double-quote `”`. Imagine you have a string that uses double-quotes and you want to put a double-quote inside the string. If you write ”I ”understand” joe.” then Python will get confused because it will think the `”` around ”understand” actually ends the string. You need a way to tell Python that the `”` inside the string isn’t a real doublequote.
>
>To solve this problem you escape double-quotes and single-quotes so Python knows to include in the string. Here’s an example:
```
” I am 6’2\” tall. ” # escape double-quote inside string
’ I am 6\’2” tall. ’ # escape single-quote inside string
```
>The second way is by using triple-quotes, which is just `”””` and works like a string, but you also can put as many lines of text as you want until you type `”””` again.

| Escape | What it does. |
| --- | --- |
| `\\` | Backslash () |
| `\’` | Single-quote (’) |
| `\”` | Double-quote (”) |
| `\a` | ASCII bell (BEL) |
| `\b` | ASCII backspace (BS) |
| `\f` | ASCII formfeed (FF) |
| `\n` | ASCII linefeed (LF) |
| `\N{name}` | Character named name in the Unicode database (Unicode only) |
| `\r` | ASCII Carriage Return (CR) |
| `\t` | ASCII Horizontal Tab (TAB) |
| `\uxxxx` | Character with 16-bit hex value xxxx (Unicode only) |
| `\Uxxxxxxxx` | Character with 32-bit hex value xxxxxxxx (Unicode only) |
| `\v` | ASCII vertical tab (VT) |
| `\ooo` | Character with octal value ooo |
| `\xhh` | Character with hex value hh |

### Parameters and variables

A note about `argv` in the book:

>The argv is the ”argument variable,” a very standard name in programming, that you will find used in
many other languages. This variable holds the arguments you pass to your Python script when you run
it. In the exercises you will get to play with this more and see what happens.
>
>Line 3 ”unpacks” argv so that, rather than holding all the arguments, it gets assigned to four variables you can work with: script, first, second, and third. This may look strange, but ”unpack” is probably the best word to describe what it does. It just says, ”Take whatever is in argv, unpack it, and assign it to all of these variables on the left in order.”
>
>After that we just print them out like normal.

Note: Another word for "modules" is "features". Programmers also call them "libraries".

## Commands (really functions)

From the book (page 77):

>You give a file a command by using the `.` (dot or period), the name of the command, and parameters. Just like with open and raw_input. The difference is that `txt.read()` says, ”Hey txt! Do your read command with no parameters!”

Commands are also called ”functions” and ”methods".

Great explanation of the `open` command at Python Tips titled "[The open function explained](https://pythontips.com/2014/01/15/the-open-function-explained/)".

>Let’s start with the basics: The return of open is a file handle, given out from the operating system to your Python application. You will want to return this file handle once you’re finished with the file, if only so that your application won’t reach the limit of the number of open file handle it can have at once.

### Commands (or functions) to remember

* `close` – Closes the file. Like File->Save.. in your editor.
* `read` – Reads the contents of the file. You can assign the result to a variable.
* `readline` – Reads just one line of a text file.
* `truncate` – Empties the file. Watch out if you care about the file.
* `write(’stuff’)` – Writes ”stuff” to the file.

Useful article about the `open` command and opening text files: "[Reading and Writing Files in Python](http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python)".

Also take a look at "[7. Input and Output — Python 2.7.13 documentation](https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files)". It is a bit dense but has a lot of formatting information.

Modifiers for file modes (from the book, page 82):

> **What modifiers to the file modes can I use?** The most important one to know for now is the + modifier, so you can do ’w+’, ’r+’, and ’a+’. This will open the file in both read and write mode, and depending on the character use position the file in different ways.

### Simplifying commands with strings

In exercise 16, the original code used the following to write lines from the user to a text file:

```
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
```

One of the study drills called for a simplification of these lines of the code. This simplified string works:

```
target.write("%s\n%s\n%s\n" % (line1, line2, line3))
```

## Functions

Functions do three things:

* They name pieces of code the way variables name strings and numbers.
* They take arguments the way your scripts take `argv`.
* Using 1 and 2 they let you make your own "mini-scripts" or "tiny commands."

You can create a function by using the word `def` in Python.

### About `def` and `args`

From exercise 18:

```
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
```

Explanation from the book:

>1. First we tell Python we want to make a function using `def` for "define".
>2. On the same line as def we give the function a name. In this case we just called it "print_two" but it could also be "peanuts". It doesn't matter, except that your function should have a short name that says what it does.
>3. Then we tell it we want `*args` (asterisk args) which is a lot like your `argv` parameter but for functions. This *has* to go inside `()` parentheses to work.
>4. Then we end this line with a `:` colon, and start indenting.
>5. After the colon all the lines that are indented four spaces will become attached to this name, `print_two`. Our first indented line is one that unpacks the arguments the same as with your scripts.
>6. To demonstrate how it works we print these arguments out, just like we would in a script.
>
>The problem with `print_two` is that it's not the easiest way to make a function. In Python we can skip the whole unpacking arguments and just use the names we want right inside ().

### Function checklists

* Did you start your function definition with `def`?
* Does your function name have only characters and `_` (underscore) characters?
* Did you put an open parenthesis `(` right after the function name?
* Did you put your arguments after the parenthesis `(` separated by commas?
* Did you make each argument unique (meaning no duplicated names)?
* Did you put a close parenthesis and a colon `):` after the arguments?
* Did you indent all lines of code you want in the function four spaces? No more, no less.
* Did you "end" your function by going back to writing with no indent (`dedenting` we call it)?

When you run ("use" or "call") a function, check these things:

* Did you call/use/run this function by typing its name?
* Did you put the `(` character after the name to run it?
* Did you put the values you want into the parenthesis separated by commas?
* Did you end the function call with a `)` character?

**To 'run,' 'call,' or 'use' a function all mean the same thing.**

From the book:

>In a way, the arguments to a function are kind of like our = character when we make a variable. In fact, if you can use = to name something, you can usually pass it to a function as an argument.

### Using `int()` with `raw_input()` in functions to get values from users

Example string formats:

`cheeses1 = int(raw_input("> "))`

You have to store after you call `int()`. Like `cheeses1 = int(cheeses1)`

Longer feedback from Stack Overflow:

>`int` does not mutate the user input (a string, which is in fact immutable), but constructs an integer and then returns it.
>
>Since you don't assign any name to the return value, it is lost.
>
>Demo:
```
>>> user_input = raw_input('input integer > ')
input integer > 5
>>> type(user_input)
<type 'str'>
>>> input_as_int = int(user_input)
>>> input_as_int
5
>>> type(input_as_int)
<type 'int'>
>>> type(user_input) # no change here
<type 'str'>
```

### Another note about `raw_input` and entering values into a formula

This relates to exercise 21. The question was about using `raw_input` to capture values to feed into the functions.

>The problem with that is then you can't enter floating point, so also try using `float(raw_input())` instead.

### Understanding the `f` notation in exercise 20

From the book:

>**What is f in the print_all and other functions?** The `f` is a variable just like you had in other functions in Exercise 18, except this time it’s a file. A file in Python is kind of like an old tape drive on a mainframe, or maybe a DVD player. It has a ”read head,” and you can ”seek” this read head around the file to positions, then work with it there. Each time you do `f.seek(0)` you’re moving to the start of the file. Each time you do `f.readline()` you’re reading a line from the file, and moving the read head to right after the `\n` that ends that file. This will be explained more as you go on.

Also read the explanation here: "[Learn Python the Hard Way ex20, how does this function work? - Stack Overflow](http://stackoverflow.com/questions/20969536/learn-python-the-hard-way-ex20-how-does-this-function-work)"

### Running functions in Python in the terminal

We started this in exercise 25. One of the functions was `word.pop`. This question and answer from the book discuss how it works in relation to the `words` variable:

> **How can the `words.pop` function change the words variable?**
>
>That's a complicated question, but in this case `words` is a list, and because of that you can give it commands and it'll retain the results of those commands. This is similar to how files and many other things worked when you were working with them.

The exercise also used `return` instead of `print` in some parts. Here is an explanation of the differences between the two functions:

>**When should I `print` instead of `return` in a function?**
>
>The `return` from a function gives the line of code that called the function a result. You can think of a function as taking input through its arguments, and returning output through `return`. The `print` is *completely* unrelated to this, and only deals with printing output to the terminal.

## Code writing best practices

* Try keep lines to 80 characters in length (exercise 7 comments).
