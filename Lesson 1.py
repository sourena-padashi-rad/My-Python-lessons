"""
📘 LESSON 1: What the Hell is Python 🐍
---------------------------------------
Welcome to your first Python lesson!

This file serves as a structured, commented study guide to help you understand:
- What Python is and why it’s popular
- How syntax, expressions, and linters work
- What tools you can use (VS Code, PyCharm, etc.)
- How to run Python programs and use formatting tools
"""

# ================================================================
# 🧠 1. What is Python?
# ================================================================
# Python is a **multipurpose**, **high-level** programming language.
# It’s one of the most desirable languages due to its readability,
# versatility, and strong community support.
#
# You can use Python for:
# - Web development
# - Data science & AI
# - Automation & scripting
# - Game development
# - Scientific research (like molecular biomedicine 😉)

# ================================================================
# 🧩 2. Basic Programming Terms
# ================================================================

# 📝 Syntax:
# In programming, syntax is like grammar in human languages.
# It defines how code must be written to make sense to the interpreter.

# 🧮 Expression:
# An expression is any combination of values, variables, operators,
# and function calls that can be evaluated to produce a value.
# Example:
import math
x = 5 + 3   # This expression evaluates to 8

# 🧰 Linter:
# A linter is a tool that checks your code for:
# - Syntax errors
# - Bugs
# - Formatting issues
# - Violations of coding standards
# Example: autopep8 is one such linter/formatter for Python.


# ================================================================
# 🧭 3. Tools for Writing Python Code
# ================================================================

# There are two main kinds of tools when using Python:
# 1️⃣ IDEs (Integrated Development Environments)
# 2️⃣ Editors (Lightweight code editors)

# Examples:
# IDE: PyCharm
# Editors: Visual Studio Code (VS Code), Sublime Text, Atom

# 🔗 Download VS Code:
# https://code.visualstudio.com/download


# ================================================================
# 💻 4. Running Python Code in VS Code
# ================================================================

# When we "call" a function, we mean we execute it.
# Example:
print("Hello World")  # 👋 Calling the print() function

# ⚙️ In VS Code:
# - Open the integrated terminal:
#     Ctrl + ^   (or on German keyboards: Ctrl + Ö)
# - Then type:
#     python file_name.py
#
# ⚠️ Always save (Ctrl + S) before running, or your changes might not appear!


# ================================================================
# 🔁 5. Repetition Using the * Operator
# ================================================================
print('ABCD' * 10)  # Repeats the string 10 times


# ================================================================
# 🧩 6. Python Extensions for VS Code
# ================================================================
# Recommended Extensions:
# ✅ Python (by Microsoft)
# ✅ autopep8 (for automatic code formatting)

# To format your code:
# Ctrl + Shift + P → search “Format Document”
# 💡 TIP: Enable “Format on Save” so your code auto-formats every time you save.


# ================================================================
# 📜 7. Python Enhancement Proposals (PEPs)
# ================================================================
# Official PEP repository: http://www.python.org/dev/peps
# PEP 8 → Python’s official style guide.

# ✍️ PEP 8 Key Idea:
# "Code is read much more often than it is written."
# It focuses on **readability** and **consistency**, so all Python code looks familiar.


# ================================================================
# 🧱 8. Indentation Rules
# ================================================================
# Python uses **indentation** instead of braces {}.
# Always use **4 spaces per indentation level** (never tabs).
# Example:
def my_function():
    print("Hello")  # ✅ Proper indentation


# ================================================================
# 🧩 9. Imports
# ================================================================
# Imports should be placed at the top of your file (grouped logically).
# Example:
print(math.sqrt(16))  # Just a sample import usage


# ================================================================
# 🎨 10. Autopep8 & Keyboard Shortcuts
# ================================================================
# 👉 Format your code manually:
#     Ctrl + Shift + P → search “Formatting” → “Format Document”
#
# 👉 Assign or check shortcuts:
#     Ctrl + Shift + P → search “Keyboard Shortcuts”
#     You can customize or view all Python-related commands there.


# ================================================================
# 🏁 END OF LESSON 1
# ================================================================
