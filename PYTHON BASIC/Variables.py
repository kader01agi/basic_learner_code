# Variables are containers for storing data values.
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _)
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

var = "This is my first ever Python video."

#  Multi Words Variable Names
"""
Camel Case: Each word, except the first, starts with a capital letter:
myVariableName = "John"

Pascal Case: Each word starts with a capital letter:
MyVariableName = "John"

Snake Case: Each word is separated by an underscore character:
my_variable_name = "John"
"""


# Assign values to multiple variables in one line:
x, y, z = "Apple", "Orane", "Cherry"
print(x, y, z)
print(x)

# Assign the same value to multiple variables in one line:
x = y = z = "Avocado"
print(x)

# To combine both text and a variable, Python uses the + character:
x = "nice"
print("Python is " + x)

# Use comma to print more than one string/variable:
x = "cute"
print("Python is", x)

# CAN ONLY CONCATENATE STR (NOT "int" to "str") TO STR



# https://www.w3schools.com/python/python_variables_global.asp
#Gobal vs Local variables
x = "breathtaking"  #Here x is GLOBAL Variable.
def myfunc():
  x = "inspiring" #Here x is LOCAL Variable.
  print("Python is " + x)
myfunc()
print("Python is " + x)

#If you use the "global" keyword, the variable belongs to the global scope:
x = "astounding"
def myfunc():
  global x
  x = "stunning"
myfunc()
print("Python is " + x)

#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
