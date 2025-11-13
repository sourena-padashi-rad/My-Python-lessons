"""
📘 LESSON 2: Variables, Strings, and Numbers in Python 🧠
---------------------------------------------------------
In this lesson, you’ll learn:
- What variables are and how to name them properly
- The main data types (float, boolean, string)
- How to work with and format strings
- String methods and operations
- How to use numbers, arithmetic operations, and type conversion
- Basic coding style rules from PEP 8
"""

# ================================================================
# 🧩 1. Variables — What Are They?
# ================================================================
# Variables are used to **store data** in a computer’s memory.
# Think of them as boxes that hold information you want to use later.

import math
students_count = 1000  # Example variable


# ================================================================
# 🔢 2. Types of Variables
# ================================================================

# 🧮 Floating Numbers (floats):
pi = 3.141592653
temperature = 1.5

# 🔘 Boolean (True / False):
# Used mostly in making decisions and conditional statements.
is_sunny = True
is_raining = False

# ⚠️ NOTE:
# Boolean values must be written with capitalized first letters:
# ✅ True, False   ❌ not true, false

# 🔤 Strings:
# Strings are sequences of characters — usually text.
# They are written within quotes (" " or ' ').
name = "Sourena"
city = 'Oldenburg'


# ================================================================
# 🧭 3. Variable Naming Rules (PEP 8 Style)
# ================================================================
# ✅ DO:
# 1️⃣ Use descriptive, clear names
# 2️⃣ Use lowercase letters
# 3️⃣ Use underscores (_) instead of spaces
# 4️⃣ Leave a space around the equal sign (=)
# 5️⃣ Follow PEP 8 for clean, readable code

# Example:
student_name = "Maryam"
average_grade = 1.3

# ❌ BAD EXAMPLES:
# StudentName = "Maryam"
# averageGrade=1.3
# student name = "Maryam"  (spaces not allowed)


# ================================================================
# 🔤 4. Strings in Python
# ================================================================
# Strings can be created using:
# - Single quotes: 'Hello'
# - Double quotes: "Hello"
# - Triple quotes: """Hello"""  ← for multi-line text

course = "Python for beginners"
print(course)  # prints: Python for beginners

# You can check the number of characters in a string using len():
print(len(course))  # returns 21

# Accessing characters:
print(course[0])     # First character (P)
print(course[0:3])   # First 3 characters (Pyt)


# ================================================================
# 🧙‍♂️ 5. Escape Sequences
# ================================================================
# Escape characters let you include special symbols or formatting inside strings.

course = "Python \"Programming\""
print(course)
# Output: Python "Programming"

# Common Escape Sequences:
# \n  → New line
# \t  → Tab space
# \\  → Backslash itself
# \"  → Double quote inside string

print("Hello\nWorld")
# Output:
# Hello
# World


# ================================================================
# 💬 6. Comments
# ================================================================
# Comments start with #
# They are ignored by Python and used to explain your code.

# Example:
# This prints the user’s name
print("Sourena")


# ================================================================
# 🧩 7. Formatting Strings (f-strings)
# ================================================================
# f-strings allow combining variables into one readable string.
# Introduced in Python 3.6 → very popular and clean!

first = "Sourena"
last = "Padashirad"
full = f"{first} {last}"

print(full)  # Output: Sourena Padashirad

# You can even embed expressions inside f-strings:
age = 26
info = f"{first} is {age} years old."
print(info)


# ================================================================
# 🧰 8. String Methods
# ================================================================
course = "python for beginners"

# (.) can be used to see all the methods available for strings
print(course.upper())       # 'PYTHON FOR BEGINNERS'
print(course.lower())       # 'python for beginners'
print(course.title())       # 'Python For Beginners'
# Replace part of string
print(course.replace("beginners", "absolute beginners"))

# Whitespace handling:
print(course.strip())       # Removes leading & trailing whitespace
print(course.lstrip())      # Removes leading whitespace
print(course.rstrip())      # Removes trailing whitespace

# Searching within strings:
print(course.find("for"))       # returns 7
print(course.find("advanced"))  # returns -1 (not found)

# Checking for substrings:
print("pro" in course)          # True
print("adv" not in course)      # True


# ================================================================
# 🔢 9. Numbers
# ================================================================
# There are 3 types of numbers in Python:
# 1️⃣ Integers
# 2️⃣ Floating-point numbers
# 3️⃣ Complex numbers

X = 10          # integer
Y = 3.14        # float
Z = 2 + 3j      # complex number

# Basic arithmetic operations
addition = X + Y
subtraction = X - Y
multiplication = X * Y
division = X / Y
floor_division = X // Y   # returns an integer
modulus = X % Y
exponentiation = X ** 2

# Shorthand assignment
x = 10
x = x + 3      # Regular addition
x += 3         # Shorthand for same operation


# ================================================================
# 🧮 10. Useful Number Functions
# ================================================================
print(round(3.141592653))  # returns 3
print(abs(-7))             # returns 7 (absolute value)

# Using the math module for advanced math functions:
print(math.sqrt(16))       # Square root
print(math.ceil(3.14))     # Round up
print(math.floor(3.99))    # Round down


# ================================================================
# 🔄 11. Type Conversion
# ================================================================
# The input() function always returns a string.
# To perform arithmetic, convert it to a number first.

x = input("x: ")   # e.g. user enters "5"
# y = x + 1  → ❌ Error (string + int not allowed)
y = int(x) + 1     # ✅ Convert x to integer before adding
print(f"x: {x}, y: {y}")

# Checking the type of a variable:
print(type(x))  # <class 'str'>

# Falsy values in Python:
# ""
# 0
# None

print(bool(0))       # False
print(bool(1))       # True
print(bool(""))      # False
print(bool("Hello"))  # True


# ================================================================
# 🏁 END OF LESSON 2
# ================================================================
# ✔️ You learned:
# - Variables, naming rules, and types
# - Strings, escape sequences, and f-strings
# - String methods
# - Numbers and basic math functions
# - Type conversion and truthy/falsy values
# ================================================================
