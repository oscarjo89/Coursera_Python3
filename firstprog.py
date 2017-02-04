#firstprog.py

# Coursera: Programming for Everybody (Getting Started with Python)
###########################################################################
# Week 2: Windows 8: Installing Python and writing a program

# Learning how to use Python on Windows with Notepad++
# Download Notepad++ and Python
# Write code in Notepad++, save it and open command promt: Start > cdm
# dir
# cd Desktop
# cd Coursera Python
# firstprog.py
# To write python code in cdm directly type: c:\python27\python
# get the chevron promt: >>> 
# here you can write python code directly

print "Hello world"
print "more stuff to show that I can print more stuff"

###########################################################################
# Week 3
# Lecture 1.4 Writing Paragraphs of Code

# writing a Python script, add ".py" 

# Program steps: 
# Sequential steps
x = 2
print x
x = x + 2
print x

# Conditional steps
x = 5
if x < 10:
	print 'Smaller'
if x > 20:
	print 'Bigger'
print 'Finis'

# Repeated steps, Loops have iteration variables that change each time through a loop
n = 5
while n > 0:
	print n
	n = n - 1
print 'Blastoff'

# Lecture 1.5 An animated programming story
# Exercises to observe how our brain tackles problems. Compare to how computers solve problems

'''
# Get the name of the file and open it
name = raw_input('Enter file:')
name = raw_input('Enter file:')
handle = open(name, 'r')
text = handle.read()
words = text.split()

# Count word frequency
counts = dict()
for word in words:
	counts[word] = counts.get(word,0) + 1

# Find the most common word
bigcount = None
bigword = None
for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count

# All done
print bigword, bigcount
'''

#############################################################################
# Week 4 
# Lecture 2.1 Expressions

# Constants: numeric, string
print 123
print 98.6
print 'Hello world'

# Variables: name and content
x = 12.2
print x
y = 14
print y
x = 100 # now x has 100 as value, not 12.2 anymore, sequential
print x

'''
Python variable name rules:
must start with letter or underscore
must consist of letters and numbers and underscores
case sensitive
'''

# Reserved words
'''
and
del
for
is
raise
assert
elif
from
lambda
return
break
else
global
not
try
class
except
if
or
while
continue
exec
import
pass
yield
def
finally
in
print
'''
# variable, operator, constant, reserved word
x = 2
x = x + 2
print x 

# Assignment statement. x and = not like in math...
x = 0.6
x = 3.9 * x * (1 - x)
print x 

# numeric expressions, +, -, *, /, ** power, % remainder
xx = 2
xx = xx + 2
print xx

yy = 440 * 12
print yy

# integer division
zz = yy / 1000
print zz

# remainder
jj = 23
kk = jj % 5
print kk

print 4 ** 3

# order of evaluation
'''
Parenthesis
Power
Multiplication & division 
Addition
Left to right
'''

x = 1 + 2 ** 3 / 4 *5
print x

# Operator precedence
x = 1 + (2*3) - (4/5)

# Python integer division is weird! Truncating division 
print '10/2 ='
print 10/2
print 9/2
print 99/100
# Floating point number
print 10.0/2.0
print 99.0/100.0

# Mixing integer and floating
print 1 + 2*3 / 4.0 - 5


# Lecture 2.2 Types
# What does a "Type" mean? Variables, literals and constants have a "type"
ddd = 1 + 4   # addition
print ddd

# string
eee = 'hello ' + 'there'   # concatenate = put together
print eee

# eee = eee + 1
'''
Traceback (most recent call last):
  File "C:\Users\oscar.haavardsholm\Desktop\Coursera Python\firstprog.py", line 194, in <module>
    eee = eee + 1
TypeError: cannot concatenate 'str' and 'int' objects
'''
type(eee)
type('Hello')
type(1)

xx = 1 
type(xx)
temp = 98.6
type(temp)
type(1)
type(1.0)

#Type conversion
print float(99)/100

i = 42
type(i)
f = float(i)
print f
type(f)

print 1 + 2 * float(3) / 4 - 5

# String conversion
sval = '123'
type(sval)
# print sval + 1

ival = int(sval)
type(ival)
print ival + 1
nsv = 'hello bob'
# niv = int(nsv)

'''
# User input
nam = raw_input('Who are you?')
print 'Welcome', nam 

# Converting user input
inp = raw_input('Europe floor?')
usf = int(inp) + 1
print "US floor", usf
'''

# Comments in Python, describe what is going to happen, documentation, turn on and off line of code

# String operations, + implies concatenation, * implies multiple concatenation
print 'abc' + '123'

print 'Hi' * 5

# Mnemonic variable names (memory aid), best practice
hours = 35.0
rate = 12.50
pay = hours * rate
print pay

# assignment raw - input, string, float(), * , print 
# summary type, reserved words, variables (mnemonic), operators, operator precedence, integer division, conversion between types, user input, comments (#)
'''
hours = raw_input('Enter hours worked')
fhours = float(hours)

rate = raw_input('Enter pay rate')
frate = float(rate)

pay = fhours * frate
print 'Pay', pay
'''

# Temperature conversion program, celsius to farenheit
'''
celsius = raw_input('Write temperature in celsius that you would like converted into farenheit')
fcelsius = float(celsius)

farenheit = fcelsius * 9/5 + 32

print 'Temperature in farneheit', farenheit
'''

'''
inp = raw_input('Enter Fahrenheit Temperature:')
fahr = float(inp)
cel = (fahr - 32.0) * 5.0 / 9.0
print cel
'''

#############################################################################
# Week 5
# Lecture 3.1 Conditional statements

# Conditional steps
x = 5
if x < 10:
	print 'Smaller'

if x > 20:
	print 'Bigger'

print 'Finis'

# Comparison operators, <, <=, ==, >=, >, !=
x = 5
if x == 5:
	print 'Equal 5'

# Indentation is sintaxicly important, blank lines and comments are ignored
x = 5
if x > 2:
    print 'Bigger than 2'
    print 'Still bigger'
print 'Done with 2'

for i in range(5):
    print i
    if i > 2:
        print 'Bigger than 2'
    print 'Done with i', i

# Mental begin/end squares

# Lecture 3.2 Examples of conditional statements
# Nested decisions
x = 42

if x > 1:
    print 'More than one'
    if x < 100: 
        print 'Less than 100'

print 'All done'

# Two way decision
x = 4

if x > 2:
    print 'Bigger'
else:
    print 'Smaller'

print 'All done'

# Multi way if
x = 20 
if x < 2:
    print 'Small'
elif x < 10:
    print 'Medium'
else:
    print 'LARGE'
print 'All done'
# can have multiway without else
# can have many elif
if x < 2:
    print 'Small'
elif x < 10:
    print 'Medium'
elif x < 20:
    print 'Medium2'
elif x < 30:
    print 'Medium3'

# multiway puzzel, order matters. second to last line will never print
x = 5

if x < 2:
    print 'Below 2'
elif x < 20:
    print 'Below 20'
elif x < 10:             # error , will never print this, if x less than 10 it is also less than 20 and will have printed Below 20 and finished if-thingy
    print 'Below 10' 
else:
    print 'Something else'
    
    
# Lecture 3.3 Try and except

# the try / except structure
# insurance, test one thing, safty net, do another if it doesnt work
astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
    
print 'First',istr

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
    
print 'Second',istr

# Sample try/except
'''
rawstr = raw_input('Enter a number:')

try:
    ival = int(rawstr)
except:
    ival = -1
    
if ival > 0:
    print 'Nice work'
else:
    print 'Not a number'
'''

# rewrite pay computation. more than 40 hours, 1,5 pay for those hours. 
# Give out error if not number. NO LOOP! just quit, one prompt => quit

# Excercise 3.1 and 3.2
'''
try:
    hours = raw_input('Enter hours worked: ')
    fhours = float(hours)
    rate = raw_input('Enter pay rate: ')
    frate = float(rate)
except:
    print 'Error, please enter numeric input'
    exit()
    
if fhours > 40:
    pay = 40 * frate + (fhours-40) * (frate * 1.5)
else:
    pay = fhours * frate
print 'Pay', pay
'''

'''
inp = raw_input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print cel
except:
    print 'Please enter a number'
'''

# excercise 3.3
'''
iscore = raw_input('Enter score between 0.0 and 1.0: ')
try:
    score = float(iscore)
    if score < 0.6:
        print 'F'
    elif score < 0.7:
        print 'D'
    elif score < 0.8:
        print 'C'
    elif score < 0.9:
        print 'B'
    elif score <= 1.0:
        print 'A'
    else:
        print 'Bad score, number has to be between 0.0 and 1.0'
except:
    print 'Bad score'
'''

#############################################################################
# Week 6
# Lecture 4.1 Functions

# Stored (and reused) steps. Reusable pieces of code "functions". def: define
def hello():
    print 'Hello'
    print 'Fun'

hello()
print 'Zip'
hello()

# Two kinds of functions: built-in and the kind we define and name ourselvs
# def: call it, use/invoke 

# Built in functions: print, float, int, type, max, min, ....

# Max/min functions
big = max('Hello world')
print big

tiny = min('Helloworld')
print tiny

x = len('Hello world')
print x

# Building our own functions
def print_lyrics():
    print "I'm a lumberjack, and I'm okay"
    print 'I sleep all night and I work all day'
    
print_lyrics()

# Arguments, inside the parenthesis
def greet(lang):
    if lang == 'es':
        print 'Hola'
    elif lang == 'fr':
        print 'Bonjour'
    else:
        print 'Hello'

greet('en')
greet('es')
greet('fr')

# Return values
def greet():
    return "Hello"

print greet(), "Glenn"
print greet(), "Sally"

# Fruitful functions (return value) others void

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print greet('en'),'Glenn'
print greet('es'),'Sally'
print greet('fr'),'Michael'

# Arguments, parameters and results
# Multiple parameters / arguments

def addtwo(a,b):
    added = a + b
    return added
    
x = addtwo(3,5)
print x

# problem, def: computepay

import random
for i in range (10):
    x = random.random()
    print x

random.randint(5,10)
x = random.randint(5,10)
print x

t = [1, 2, 3]
random.choice(t)
x = random.choice(t)
print x

import math
print math

signal_power = 10
noise_power = 5
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
print decibels

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print 'I sleep all night and I work all day.'
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
repeat_lyrics()

def print_twice(bruce):
    print bruce
    print bruce
    
print_twice('Oscar' *4)

# Exercise 4.6
'''
try:
    hours = raw_input('Enter hours worked: ')
    fhours = float(hours)
    rate = raw_input('Enter pay rate: ')
    frate = float(rate)
except:
    print 'Error, please enter numeric input'
    exit()
    
def computepay(fhours, frate):
    if fhours > 40:
        pay = 40 * frate + (fhours-40) * (frate * 1.5)
    else:
        pay = fhours * frate
    return pay
    
print computepay(fhours, frate)
'''

# Exercise 4.7
'''
iscore = raw_input('Enter score between 0.0 and 1.0: ')
try:
    score = float(iscore)
    if score < 0.6:
        print 'F'
    elif score < 0.7:
        print 'D'
    elif score < 0.8:
        print 'C'
    elif score < 0.9:
        print 'B'
    elif score <= 1.0:
        print 'A'
    else:
        print 'Bad score, number has to be between 0.0 and 1.0'
except:
    print 'Bad score'
'''

'''
iscore = raw_input('Enter score between 0.0 and 1.0: ')
try:
    score = float(iscore)
    def computegrade(score):
        if score < 0.6:
            print 'F'
        elif score < 0.7:
            print 'D'
        elif score < 0.8:
            print 'C'
        elif score < 0.9:
            print 'B'
        elif score <= 1.0:
            print 'A'
        else:
            print 'Bad score, number has to be between 0.0 and 1.0'
except:
    print 'Bad score'
    
print computegrade(score)
'''

#############################################################################
# Week 7

# Lecture 5.1 Loops and iterations
# Foundations: sequential, conditional, functions and loops

# Repeated steps
n = 5
while n > 0:
    print n
    n = n - 1
print 'Blastoff!'
print n
# Iteration variables, changing in the loop: here it is n

# Infinite loop or zero trip loop
'''
n = 5
 while n > 0:
    print 'Lather'
    print 'Rinse'

print 'Dry off'
'''


'''
# Breaking out of a loop, way of controling execution of loop
while True:
    line = raw_input('>')
    if line == 'done':
        break
    print line
print 'Done'

# Finishing an iteration with continue
while True:
    line = raw_input('>')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print line
print 'Done'
'''
# indefinite loops
# definite loops

for i in [5, 4, 3, 2, 1]:
    print i
print 'Blastoff!'

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print 'Happy New Year:', friend
print 'Done!'


# Lecture 5.2 Loops Idioms
# making smart loops 
'''
Set some variable to initial value

for thing in data:
Look for something or do something to each entry seperately, updating a variable.

Look at the variables.
'''

largest_so_far = -1
print 'Before', largest_so_far
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print largest_so_far, the_num    

print 'After', largest_so_far

zork = 0
print 'Before', zork
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print zork, thing
print 'After', zork

# Running total
zork = 0
print 'Before', zork
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print zork, thing
print 'After', zork

# Finding average
count = 0 
sum = 0
print 'Before', count, sum
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print count, sum, value
print 'After', count, sum, sum/count

# Filtering in a loop
print 'Before'
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print 'Large number', value
print 'After'

# Search using a boolean variable (true/false)
found = False
print 'Before', found
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
        break
    print found, value
    
print 'After', found



# Lecture 5.3 Smallest and Largest

#finding the smallest
smallest_so_far = 100
print 'Before', smallest_so_far
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print smallest_so_far, the_num    

print 'After', smallest_so_far

smallest = None
print 'Before'
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:       # First iteration
        smallest = value
    elif value < smallest:
        smallest = value
    print smallest, value
print 'After', smallest

# Summary: while loops (indefinite), infinite, using break, continue, for loops (definite), iteration variables, counting, sumin, averaging, searching, detecting, largest/smallest

# Exercise 5.1
count = 0
total = 0
while True:
    line = raw_input('Enter numbers to add, one at the time, then enter "done" to get result ')
    
    # Handle edge cases
    if line == 'done': break
    if len(line) < 1 : break   # Check for empty line
    
    # Do the work
    try:
        num = float(line)
    except:
        print "invalid input"
        continue
            
    count = count + 1
    total = total + num
    print num, total, count

print 'Count = ', count
print 'Total = ', total   
print 'Average = ', total / count

''' 
largest = None
smallest = None
while True:
    line = raw_input("Enter a number: ")
    
    # handle edge cases
    if line == "done":
        break
        
    # Do work
    try:
        num = int(line)
    except:
        print 'Invalid input'
        continue
    
    if largest is None:
    	largest = num
    elif num > largest:
        largest = num
    
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num

print "Maximum is", largest
print "Minimum is", smallest
'''