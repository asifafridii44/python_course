'''
Types of Variables
Variables can be categorized based on various criteria, such as scope, 
lifetime, and data type. Here are the primary types:

1. By Data Type
Integer: Represents whole numbers (e.g., 1, 42, -7).
Float: Represents decimal numbers (e.g., 3.14, 0.001, -2.5).
String: Represents a sequence of characters (e.g., "Hello", "123").
Boolean: Represents a truth value (e.g., True or False).

2. By Scope
Local Variables: Defined within a function or block and accessible only within that context.
Global Variables: Defined outside of any function and accessible from any part of the program.

3. By Lifetime
Static Variables: Retain their value between function calls and are initialized only once.
Dynamic Variables: Created and destroyed at runtime, often managed through heap memory allocation.

4. By Mutability
Mutable Variables: Can be changed after they are created (e.g., lists, dictionaries in Python).
Immutable Variables: Cannot be changed after they are created (e.g., strings, tuples in Python).

'''

# Integer
age = 25
print(age)
# Float
height = 5.9
print(height)

# String
name = "Alice"
print(name)

# Boolean
is_student = True
print(is_student)

# List (mutable)
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Tuple (immutable)
coordinates = (10.0, 20.0)
print(coordinates)


