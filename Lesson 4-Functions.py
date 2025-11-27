# Functions
# there are some built-in functions in Python like print(), input(), len(), etc.
print("print is a built-in function. It prints things. Shocking, I know.")
round  # round is also built-in. It rounds numbers, not your life's problems.
len  # len tells you how long something is — unlike my attention span.


# In this section we are going to learn how to write our own functions in Python.
# Yes, YOU will become the creator. Absolute power. No responsibility.


# Custom Functions:
def customfunction():
    print("This is my custom function!")
    print("PEP 8 recommends two blank lines after this...")
    print("...but PEP 8 also expects me to have my life together, so we ignore it.")


###
customfunction()  # calling the function like summoning a demon, but friendlier
###

# =======================================================
# In print() we give input to print.
# How do we give input to OUR functions?
# By sacrificing parameters and arguments.


# Parameters = names in function definition
# Arguments = values we sacrifice to the function when calling it
def greet(first_name, last_name):
    print("Hello " + first_name + " " + last_name +
          " — glad you survived long enough to run this function.")


greet("Arthur", "Morgen")  # “Arthur” and “Morgen” are arguments. RIP cowboy !


# Using f-strings because we're not living in 2005
def greet2(first_name, last_name):
    print(
        f"Hello {first_name} {last_name}! If this was Red Dead, you'd be dead by now.")


# the person you must hire if you are here to check my Git_Hub :)
greet2("Sourena", "Padashirad")


# The second version is cleaner AND makes you feel like a pro.


# ======================================================
# Types of Functions:
# 1- Functions that perform a task (like print)
# 2- Functions that calculate and return a value (like round)
# One prints. One thinks. Choose wisely.


def print_message(food):
    print(f"Germans love {food}! They love it so much they might marry it.")


print_message("Potatoe")


# ======================================================
# Type 2 functions: functions that return a value
def get_message(drink):
    return f"Germans love to drink {drink}! Especially after dealing with paperwork."


get_message("sprüdel Wasser")
message = get_message("Beer")
# file.write(message)  # pretend we wrote it. We didn’t. Responsibility is overrated.


# ======================================================
# Keyword Arguments:
def lunch(food, drink):
    print(f"I eat my {food} with {drink}. Because life is chaos.")


lunch("sassages", "ketchup")  # positional arguments
lunch(drink="mustard", food="sassages")  # keyword arguments
# mix both, like mixing mental stability with caffeine
lunch("sassages", drink="curry sauce")


# ======================================================
# Default Arguments:
def dinner(food, drink="nothing else"):
    print(f"For dinner I eat {food} with {drink}. Yes, I'm suffering.")


dinner("Soup")


def math_operation(a, b, c=1, d=1):
    return (a + b) * c / d


result = math_operation(2, 3, d=2)
print(result)  # Output: 2.5


# ======================================================
# *args — infinite arguments, infinite pain
def multiply(x, y):
    return x * y

# multiply(2, 3, 4, 5)  # this explodes — like my hopes.


def multi(*numbers):
    print(numbers)  # prints a tuple of numbers AND your bad decisions


multi(2, 3, 4, 5)


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


math_operation = multiply(2, 3, 4, 5)
print(math_operation)  # Output: 120, stronger than your willpower


# ======================================================
# **kwargs — keyword arguments, or as doctors call it: "patient_data"
def patient_data(**data):
    print(data)


patient_data(name="John Wick", age=45, pet="dog", favorite_object="pencil")
# NOTE: DO NOT TRY TO ERASE THE PET FROM THIS DICTIONARY OTHERWISE YOU SEE PENCIL

# ======================================================
# Local vs Global Scope:
x = 10  # global variable (king of the code)


def function():
    y = 5  # local variable (peasant)
    return y


print(x)         # global works
print(function())  # local only works when summoned


# global overwrite:
a = 5
a = 10  # overwritten like your dreams


def func1():
    a = 3
    return a


def func2():
    a = 7
    return a


print(func1() + func2())  # 10 — finally something that adds up in life


# ======================================================
# FizzBuzz — the ancient ritual of programming interviews
def FB(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    else:
        return str(input)


def FizzBuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)

# Python logic: check conditions one line at time, like a German border officer checking each document
# =====================================================
