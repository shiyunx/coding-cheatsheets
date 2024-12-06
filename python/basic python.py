#----------Print----------
# Print in table 
sep=';'
# Print with whitespace
sep='\t'
# Print a new line
sep='\n'
#---------Add two numbers--------
# Addition
10 + 10
20

# Add and print
print(10 + 10)
20

a = "North"
print(a)

# Printing values stored in variable
total = 10 + 10
(total)
20

# Update a variable must already store a value
+=, -=, *=, /=, **=

a = 10
a += 10
a = 10 + 10
print(a)
20

#---------Types--------
# Find type of variables
type("colour")
str

#---------Round up and round down--------
# Convert to round down
round(10.2)
10

# Convert to round up
round(10.88)
11

#---------Concatenate---------
# Concatenating two or more string
colours = "red" + " " + "green"
print(colours)
red green

#---------Length--------
# Find length of the locations
locations = ["North", "South", "East", "West"]
print (len(locations))
4

#----------Index and slice---------
# Find positive index of the locations
locations = ["North", "South", "East", "West"]
print(locations[2])
East

# Find negative index of the locations
locations = ["North", "South", "East", "West"]
print(locations[-1])
West

# List slicing of the locations
locations = ["North", "South", "East", "West"]
print(locations[1:3])
['South', 'East']

#----------Append--------
# Add append
locations = ["North", "South", "East", "West"]
locations.append("Central")
locations.append("Not Found")
print(locations)
['North', 'South', 'East', 'West', 'Central', 'Not Found']

#--------Remove--------
# Remove pop
locations = ["North", "South", "East", "West", "Central", "Not Found"]
locations.pop(-1)
print(locations)
['North', 'South', 'East', 'West', 'Central']

#----------Dictionaries--------
colours = dict(
    apple='red',
    pear='green',
    mango='yellow',
    berries='purple'
    )
    
colours['apple']
'red'

# Use d[key] to find values in dictionary
d = {"tom":111, "Fio":222, "Gin":333}
for key in d:
    print("key:",key,"values:",d[key])

#--------Input---------
name = input("Enter your name: ")
print(name)

number = input("Enter number: ")
#convert to integer
number = int(number)
#convert to float
number = float(number)

>>> Enter your name:
hello

h = input("Enter hours: ")
r = input("Enter rate: ")
p = float(h) * float(r)
print("Total: ", p)
# commas ',' means add spacing

>>> Enter hours: 2.2
>>> Enter rate: 2.1
Total:  4.620000000000001

#--------Sequential--------
x = 2
print(x)
x = x + 2
print(x)

2
4

#---------Conditional--------
x = 5
if x < 10: # If true or false
    print('Smaller')
if x > 20: # If true or false
    print('Bigger')
print('All')

Smaller
Biggest

#--------One-way decision--------
x = 5
print('Before 5')
if x == 5:
    print('Is 5')
    print('Is still 5')
    print('Third 5')
print('Afterwards 5')
print('Before 6')
if x == 6:
    print('Is 6')
    print('Is still 6')
    print('Third 6')
print('Afterwards 6')

Before 5
Is 5
Is still 5
Third 5
Afterwards 5
Before 6
Afterwards 6

#--------Two-way decision--------
x = 4
if x > 2:
    print('Bigger')
else:
    print('Smaller')
print ('All done')

Bigger
All done

#--------Nested decision---------
x = 42
if x > 1:
    print('More than one')
    if x < 100:
        print('Less than 100')
print('All done')

More than One
Less than 100
All done

#--------Multi-way---------
# only one will run
x = 0
if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
else: 
    print('Large')
print('All done')

Small 
All done

x = 5
if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
else: 
    print('Large')
print('All done')

Medium 
All done

x = 20
if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
else: 
    print('Large')
print('All done')

Large 
All done

#--------Conditional try except---------
# If the code in try works, except is skipped
# If the code in try fails, it jumps to the except 

astr = 'Hello'
try:
    istr = int(astr) # When the first conversion fails, it just drops into the except: clause and the program continues.
except:
    istr = -1
print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr) # When the second conversion succeeds, it just skips the except: clause and the program continues.

First -1
Second 123

#-------Functions--------
# A function is some stored code that we use. A function takes some input and produces an output.
# Stored and reused
def thing():
    print('Hi')
    print('Hello')

    thing()
    print('add')
    thing()

Hi
Hello
add
Hi
Hello

# Parameters in function
# A parameter is a variable which we use in the function definition.
It is a "handle" that allows the code in the function to access the arguments for a particular function invocation.
def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

greet('en')
Hello
greet('es')
Hola
greet('fr')
Bonjour

# Return values in function 
def greet():
    return "Hello"
print(greet(), "Green")
print(greet(), "White")

Hello Green
Hello White

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet ('en'), 'Green')
Hello Green
print(greet ('es'), 'White')
Hola White
print(greet ('fr'), 'Grey')
Bonjour Grey

#-------Multiple parameters and arguements--------
def addtwo(a, b): # parameter in function
    added = a + b
    return added 
x = addtwo(3, 5) # arguement in function
print(x)

8

#----------Loops---------
# Loops (repeated steps) have iteration variables (n) that change each time through a loop.
# For loop
fruits_list = ["Apple", "Orange", "Berries", "Mango", "Melon"]
for selected_fruit in fruits_list:
    print(selected_fruit)
Apple
Orange
Berries
Mango
Melon

# While loop descending
a = 3
while (a > 0):
    a = a-1
    print(a)
2
1
0

# While loop ascending
a = 0
while (a < 3):
    a = a+1
    print(a)
1
2
3

# repeated while steps
n = 5
if n > 0: #question of true or false
    print(n)
    n = n - 1 #print this code if true and back to while to recheck 
print('end') # else print this code
print(n)

5
4
3
2
1
end
0

# Definite loop (for loops) have clear iteration variables that change each time through a loop. These iteration variables move through the sequence or set. 
# Definite loop for list of numbers
for i in [5,4,3,2,1]:
    print(i)
print('end')

5
4
3
2
1
end

# Definite loop with strings
fruits = ['Apple', 'Orange', 'Mango']
for fruit in fruits:
    print('Healthy:' fruit)
print('Fresh!')

Healthy Apple
Healthy Orange
Healthy Mango
Fresh!

# Find largest number in a loop ##
# We make a variable that contains the largest value we have seen so far. If the current number we are looking at is larger, it is the new largest value we have seen so far.
largest_so_far = -1
print ('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print (largest_so_far, the_num)
print('After', largest_so_far)

Before -1
9 9
41 41
41 12
41 3
74 74
74 15
After 74

# Counting in a loop
# To count how many times we execute a loop, we introduce a counter variable that starts at 0 and we add one to it each time through the loop.
count = 0
print('Before', count)
for thing in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    print(count, thing)
print('After', count)

>> Before 0
1 9
2 41
3 12
4 3
5 74
6 15
After 6

# Summing in a loop 
# To add up a value we encounter in a loop, we introduce a sum variable that starts at 0 and we add the value to the sum each time through the loop.
count = 0
print('Before', count)
for thing in [9, 41, 12, 3, 74, 15]:
    count = count + thing
    print(count, thing)
print('After', count)

Before 0
9 9
50 41
62 12
65 3
139 74
154 15
After 154

# Find average in a loop
# An average just combines the counting and sum patterns and divides when the loop is done.
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + thing
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count)

Before 0 0
1 9 9
2 50 41
3 62 12
4 65 3
5 139 74
6 154 15
After 6 154 25

# Filtering in a loop
# We use an if statement in the loop to catch / filter the values we are looking for.
print ('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print 'Large number', value
print('After')

Before
Large number 41
Large number 74
After

# Search using a boolean variable
# If we just want to search and know of a value was found, we use a variable that starts at False and is set to True as soon as we find what we are looking for.
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value ==3:
        found = True
    print(found, value)
print('After', found)

Before False
False 9
False 41
False 12
True 3
True 74
True 15
After True

# Find smallest number in a loop
# We still have a variable that is the smallest so far. The first time through the loop smallest is None, so we take the first value to be the smallest. 
smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)

Before
9 9
9 41
9 12
3 3
3 74
3 15
After 3

#----------Break----------
# Break statement ends the current loop and jumps to the statement immediately following the loop.
# Break infinite loop
# Break execute means out of loop
while True:
    line = input('> ') # type something
    if line == 'done':
        break
    print(line)
    print('Done!') 

>>> hello
hello
>>> finished
finished
>>> done
Done!

#--------Continue--------
# Continue statement ends the current iteration and jumps to the top of the loop and starts the next iteration.
while True:
    line = input('> ') # type something
    if line[0]== '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!') 

>>> hello
hello
>>> # print
print
>>> done
Done!


