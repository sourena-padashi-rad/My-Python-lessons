# comparison Operators:
10 > 5  # Greater than
10 < 5  # Less than
10 >= 5  # Greater than or equal to
10 <= 5  # Less than or equal to
10 == 5  # Equal to
10 != 5  # Not equal to

"bsg" > "apple"  # since bag comes after apple alphabetically
# each charachter has a corresponding number based on unicode values
# b=98, a=97 so bsg>apple
ord("b")  # gives 98
ord("a")  # gives 97
ord("A")  # gives 65

# =======================================================

# Conditional Statements:
# there times when we need to make decisions in our code
# here we use conditional statements like if, elif and else
temperature = 35
if temperature > 30:  # boolean expression
    print("It's a hot day")  # code block
    print("Drink plenty of water")
    # to add another condition we use elif
elif temperature > 20:
    print("It's a nice day")
    # if none of the above conditions are true we use else
else:  # no boolean expression needed
    print("It's a cold day")
print("Enjoy your day")  # this line is outside the if block

# ======================================================
# Ternary Operator:
# a shorthand way of writing an if-else statement
# instead of writing the following line:
age = 22
if age >= 18:
    print("eligible to participate")
else:
    print("not eligible to participate")
# there was nothing wrong with the above code and it also can be written like this:
age = 22
if age >= 18:
    message = "eligible to participate"
else:
    message = "not eligible to participate"
print(message)
# but we can write it in a single line using the ternary operator
age = 22
message = "eligibale to particiapate " if age >= 18 else "not eligible to participate"
print(message)
# =======================================================
# Logical Operators:
# in python we have three logical operators: and, or, not
high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
# please dont write this high_income= True
# the previous code needs both to be true
# if only one condition is enough we use or:
high_income = True
good_credit = False

if high_income or good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# not operator is used to reverse the result
high_income = True
good_credit = False
criminal_record = True

if not criminal_record:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# lets combine all the logical operators
high_income = True
good_credit = True
criminal_record = False

if (hiogh_income and good_credit) and not criminal_record:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")
# in python logocal operators are short-circuited
# meaning that if we have multiple conditions:
# if they are with "and" if only one condition is false the rest will not be evaluated
# if they are with "or" if only one condition is true the rest will not be evaluated
# this is done to optimize the code and make it faster
# =======================================================
# chaining comparison operators:
# age should be between 18 and 65
age = 25
if age >= 18 and age <= 65:
    print("Eligible")

# in math we write it like this and we can do it here too!!!
if 18 <= age <= 65:
    print("Eligible")
# this is called chaining comparison operators
# =======================================================
# Membership Operators:
# in and not in are membership operators
# they are used to check if a value is present in a sequence (like a list, tuple, string, etc)
numbers = [1, 2, 3, 4, 5]
print(1 in numbers)  # True
print(10 in numbers)  # False
print(10 not in numbers)  # True
print(1 not in numbers)  # False
# =======================================================
# Loops:there are times we want to repeat a task multiple times
# instead of writing the same code again and again we use loops

# so imagine we want to print a message 5 times
print("Looping is fun!")
print("Looping is fun!")
print("Looping is fun!")
print("Looping is fun!")
print("Looping is fun!")
# this is not efficient and ugly as my grandma using a vibrator :)

# instead we use a for loop
for number in range(5):  # range(5) generates numbers from 0 to 4
    # this line is indented to show it's inside the loop
    print("Looping is fun!")

# now look at this
for number in range(5):
    print("This is line number", number)
# this happens because range(5) generates numbers from 0 to 4
# if we want to start from 1 to 5 we can do this:
for number in range(1, 6):  # range(start, end)
    print("This is line number", number)

# also we can do this:
for number in range(5):
    print("This is line number", number + 1)
# but the first method is more efficient

# this is also a neat trick:
for number in range(5):
    print("looping is fun ", number + 1, (number + 1)*"A")
# it multiplies the string "A" by the current number +1

# we can also add a step value like this:
for number in range(1, 5, 2):  # range(start, end, step)
    print(number)

# ======================================================
# For else loop:
# to jump out of a loop:
IHC_stain_result = True
for number in range(3):
    if IHC_stain_result:
        print("Cancer detected")
        break
else:
    print("Attemted 3 times but no cancer detected")
# the else block will be executed only if the loop is not terminated by a break statement
# ======================================================
# Nested loops:
# we can also have loops inside loops
for x in range(5):
    for y in range(3):
        print(f"({x},{y})")
      #  print (x,y)

# why did we here write {} ?
# this is called f-strings (formatted string literals)
# it allows us to embed expressions inside string literals, using curly braces {}

# ======================================================
# Iterables
print(type(5))  # this will return <class 'int'>
print(type(range(5)))  # this will return <class 'range'>

# intragers, booleans, floats are primitive data types and not iterables
# range is one of the complex data types

# range is also an iterable meaning we can loop over it
for x in range(5):
    print(x)

# another iterable is a string
for x in "Python":
    print(x)  # this will print each charachter

# Lists are also iterables
for x in [1, 2, 3, 4, 5]:
    print(x)  # this will return each object

# we can also convert custom objects to iterables by implementing the __iter__ method
# and after doing that we can use it like this:
for markers in MHCII_stains:
    print(markers)

# ======================================================
# While loop:
# another type of loop is the while loop
# they are used to repeat sth until a condition is met
number = 100
while number > 0:
    print(number)
    number //= 2

# interesting fact:
# python uses a while loop to reply to our inputs in an interactive shell
# it keeps asking for input until we exit the shell
# thi can be terminated by pressing ctrl + c or ctrl + d

# another example of while loop:
command = ""
while command != "quit":
    command = input(">")
    print("ECHO", command)

# here only the command "quit" will stop the loop
# we can make it case insensitive like this:
command = ""
while command.lower() != "quit":
    command = input("<")
    print("ECHO", command)

# ======================================================
# Infinite loops:
# a loop that never ends
command = ""
while True:
    command = input(">")
    print("ECHO", command)
    # to stop the loop we can use a break statement
    if command.lower() == "quit":
        break
# ======================================================
# exercise: write a program that displays all the even numbers from 1 to 10
# after this it should print out we have 4 even numbers
for x in range(1, 10):
    while x // 2 == (int):
        print(x, "we have 4 even numbers")
