'''
in Python, variables are used to store data values. 
A variable is created the moment you first assign a value to it. 
Variables can hold different data types, such as integers, floats, strings, and lists.

>>> Key Points about Variables in Python:

>>> No declaration required: You don’t need to declare a variable before using it.

>>> Dynamic typing: You can assign a new value to a variable of any type.

>>> Naming conventions: Variable names can include letters, numbers, and underscores, 
but cannot start with a number. They are case-sensitive.

'''

# Variable assignments
name = "Alice"           # String
age = 25                 # Integer
height = 5.6             # Float
is_student = True        # Boolean
grades = [90, 85, 88]    # List

# Printing variable values
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)
print("Grades:", grades)

# Changing variable value
age = 26  # Updating age
print("Updated Age:", age)

# Combining variables in a string
introduction = f"My name is {name}, I am {age} years old and my height is {height}."
print(introduction)

'''
Explanation of the Code:
Variable Assignments:

name: Stores a string.
age: Stores an integer.
height: Stores a float.
is_student: Stores a boolean value.
grades: Stores a list of integers.
Printing Variables:

The print() function outputs the variable values.
Updating a Variable:

The variable age is updated to a new value.
Formatted Strings:

The f-string syntax (f"...") allows for easy variable interpolation within strings.

'''
