# Introduction to Python

## Comments

Comments have two purposes:

* Explain a function in plain language; and
* Temporarily disable parts of a program.

Comments use the octothorpe or hash - #. Here is an example of how the code is used:

```
# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.

print "I could have code like this." # And the comment after is ignored.

# You can also use a comment to "disable" or comment out a piece of code:
# print "This won't run."

print "This will run."
```

## Maths functions

```
* + plus
* - minus
* / slash
* * asterisk
* % percent
* < less-than
* > greater-than
* <= less-than-equal
* >= greater-than-equal
```

### Questions from the book about % (modulus)

`` Why is the % character a ”modulus” and not a ”percent”? Mostly that’s just how the designers chose to use that symbol. In normal writing you are correct to read it as a ”percent.” In programming this calculation is typically done with simple division and the / operator. The % modulus is a different operation that just happens to use the % symbol.

How does % work? Another way to say it is, ”X divided by Y with J remaining.” For example, ”100 divided by 16 with 4 remaining.” The result of % is the J part, or the remaining part. ``

The order that Python applies the maths functions is "**PEMDAS** which stands
for Parentheses Exponents Multiplication Division Addition Subtraction".

## Variables

A variable is a name for something.

### Question from the book about "=" and "=="

> What is the difference between = (single-equal) and == (double-equal)? The = (single-equal) assigns the value on the right to a variable on the left. The == (double-equal) tests if two things have the same value

## Strings

>Every time you put ” (double-quotes) around a piece of text you have been making a string. A string is how you make something that your program might give to a human. You print strings, save strings to files, send strings to web servers, and many other things.

"This is a string"

> You embed variables inside a string by using specialized format sequences and then putting the variables at the end with a special syntax that tells Python, ”Hey, this is a format string. Put these variables in there.”

When expressing multiple variables, place the variables in parentheses. For example:

`print "He's %d pounds heavy or %d kilograms." % (weight, weight_kg)`

For reference purposes: "[2.3.6.2 String Formatting Operations](https://docs.python.org/2.4/lib/typesseq-strings.html)"

### Further explanation of strings from the book

>A string is usually a bit of text you want to display to someone, or ”export” out of the program you are writing. Python knows you want something to be a string when you put either ” (double-quotes) or ’(single-quotes) around the text. You saw this many times with your use of print when you put the text you want to go inside the string inside ” or ’ after the print to print the string.

>Strings may contain the format characters you have discovered so far. You simply put the formatted variables in the string, and then a % (percent) character, followed by the variable. The only catch is that if you want multiple formats in your string to print multiple variables, you need to put them inside ( ) (parenthesis) separated by , (commas). It’s as if you were telling me to buy you a list of items from the store and you said, ”I want milk, eggs, bread, and soup.” Only as a programmer we say, ”(milk, eggs, bread, soup).”

Question about variables from the book:

> **What does %s, %r, and %d do again?** You’ll learn more about this as you continue, but they are ”formatters.” They tell Python to take the variable on the right and put it in to replace the %s with its value.

> **What is the difference between %r and %s?** Use the %r for debugging, since it displays the ”raw” data of the variable, but the others are used for displaying to users.

### A note about the `formatter` attribute

From "[34.1. formatter — Generic output formatting — Python 2.7.13 documentation](https://docs.python.org/2/library/formatter.html)"

>This module supports two interface definitions, each with multiple implementations. The formatter interface is used by the HTMLParser class of the htmllib module, and the writer interface is required by the formatter interface.
>
>Formatter objects transform an abstract flow of formatting events into specific output events on writer objects. Formatters manage several stack structures to allow various properties of a writer object to be changed and restored; writers need not be able to handle relative changes nor any sort of “change back” operation. Specific writer properties which may be controlled via formatter objects are horizontal alignment, font, and left margin indentations. A mechanism is provided which supports providing arbitrary, non-exclusive style settings to a writer as well. Additional interfaces facilitate formatting events which are not reversible, such as paragraph separation.
>
>Writer objects encapsulate device interfaces. Abstract devices, such as file formats, are supported as well as physical devices. The provided implementations all work with abstract devices. The interface makes available mechanisms for setting the properties which formatter objects manage and inserting data into the output.

Also check out this question and answers in Stack Overflow regarding exercise 8 in the book: "[formatter in python - Stack Overflow](http://stackoverflow.com/questions/15280004/formatter-in-python)". Some responses that help clarify `formatter`:

>The formatter acts as a template, each `%r` acting as a place holder for the values in the tuple on the right-hand side.

>That's the classic format for string formatting, `print "%r" % var` will print the raw value of var, four %r expects 4 variables to be passed after the %.

>formatter is a string. so, the first line is the same as: `"%r %r %r %r" % (1, 2, 3, 4)`

When using the ``\n`` syntax to create new lines, remember that using it with a `%r` formatter changes its behaviour:

>**Why do the \n newlines not work when I use %r?** That’s how %r formatting works; it prints it the way you wrote it (or close to it). It’s the ”raw” format for debugging.

### Escape sequences

From the book:

>This \ (backslash) character encodes difficult-to-type characters into a  string. There are various ”escape sequences” available for different characters you might want to use. We’ll try a few of these sequences so you can see what I mean.
>
>An important escape sequence is to escape a single-quote ’ or double-quote ”. Imagine you have a string that uses double-quotes and you want to put a double-quote inside the string. If you write ”I ”understand” joe.” then Python will get confused because it will think the ” around ”understand” actually ends the string. You need a way to tell Python that the ” inside the string isn’t a real doublequote.
>
>To solve this problem you escape double-quotes and single-quotes so Python knows to include in the string. Here’s an example:
```
” I am 6’2\” tall. ” # escape double-quote inside string
’ I am 6\’2” tall. ’ # escape single-quote inside string
```
>The second way is by using triple-quotes, which is just ””” and works like a string, but you also can put as many lines of text as you want until you type ””” again.

```
Escape    What it does.
\\        Backslash ()
\’        Single-quote (’)
\”        Double-quote (”)
\a        ASCII bell (BEL)
\b        ASCII backspace (BS)
\f        ASCII formfeed (FF)
\n        ASCII linefeed (LF)
\N{name}  Character named name in the Unicode database (Unicode only)
\r ASCII  Carriage Return (CR)
\t ASCII  Horizontal Tab (TAB)
\uxxxx    Character with 16-bit hex value xxxx (Unicode only)
\Uxxxxxxxx Character with 32-bit hex value xxxxxxxx (Unicode only)
\v        ASCII vertical tab (VT)
\ooo      Character with octal value ooo
\xhh      Character with hex value hh
```

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

## Commands

From the book (page 77):

>You give a file a command by using the . (dot or period), the name of the command, and parameters. Just like with open and raw_input. The difference is that txt.read() says, ”Hey txt! Do your read command with no parameters!”

Commands are also called ”functions” and ”methods".

## Code writing best practices

* Try keep lines to 80 characters in length (exercise 7 comments).
