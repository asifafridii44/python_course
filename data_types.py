''''
In Python, data types define the kind of value that a variable can hold and determine the operations 
that can be performed on that value. Python is a dynamically typed language, which means you don’t need 
to explicitly declare the data type of a variable; the interpreter infers it based on the value assigned 
to the variable.

>>> Basic Data Types in Python

1) Numeric Types
int: Represents integers (whole numbers), e.g., 5, -10, 42.
float: Represents floating-point numbers (decimal numbers), e.g., 3.14, -0.001, 2.0.
complex: Represents complex numbers with a real and imaginary part, e.g., 3 + 4j.


2) Sequence Types
str: Represents strings (text), e.g., "Hello", "Python".
list: An ordered collection of items (mutable), e.g., [1, 2, 3], ["apple", "banana"].
tuple: An ordered collection of items (immutable), e.g., (1, 2, 3), ("apple", "banana").

3) Mapping Type
dict: Represents a collection of key-value pairs, e.g., {"name": "Alice", "age": 25}.

4) Set Types
set: An unordered collection of unique items, e.g., {1, 2, 3}.
frozenset: An immutable version of a set, e.g., frozenset([1, 2, 3]).

5) Boolean Type
bool: Represents truth values, True or False.

Type Checking and Conversion
You can check the type of a variable using the type() function:
x = 5
print(type(x))  # Output: <class 'int'>

'''

# Numeric Types
# Integer
age = 25
# Float
height = 5.9
# Complex
complex_number = 3 + 4j

print("Numeric Types:")
print(f"Age (int): {age}, Height (float): {height}, Complex Number: {complex_number}")

# Sequence Types
# String
name = "Alice"
# List
fruits = ["apple", "banana", "cherry"]
# Tuple
coordinates = (10, 20)

print("\nSequence Types:")
print(f"Name (str): {name}")
print(f"Fruits (list): {fruits}")
print(f"Coordinates (tuple): {coordinates}")

# Mapping Type
# Dictionary
person = {"name": name, "age": age}

print("\nMapping Type:")
print(f"Person (dict): {person}")

# Set Types
# Set
unique_numbers = {1, 2, 3, 4, 5}
# Frozenset
immutable_numbers = frozenset([1, 2, 2, 3, 4])

print("\nSet Types:")
print(f"Unique Numbers (set): {unique_numbers}")
print(f"Immutable Numbers (frozenset): {immutable_numbers}")

# Boolean Type
# Boolean
is_student = True

print("\nBoolean Type:")
print(f"Is Student (bool): {is_student}")

# Demonstrating type conversion
num_str = "10"
num_int = int(num_str)  # Converts string to integer
num_float = float(num_str)  # Converts string to float

print("\nType Conversion:")
print(f"String '10' to Integer: {num_int}, String '10' to Float: {num_float}")

# Example operations
# List Operations
fruits.append("orange")  # Adding an item to the list
print(f"\nUpdated Fruits (list after append): {fruits}")

# Dictionary Operations
person["city"] = "Wonderland"  # Adding a new key-value pair
print(f"Updated Person (dict after adding city): {person}")

# Set Operations
unique_numbers.add(6)  # Adding an item to the set
print(f"Updated Unique Numbers (set after adding 6): {unique_numbers}")

'''
STEP BY STEP EXPLANATION

>>> 1. Numeric Types
code...

# Numeric Types
# Integer
age = 25
# Float
height = 5.9
# Complex
complex_number = 3 + 4j
print("Numeric Types:")
print(f"Age (int): {age}, Height (float): {height}, Complex Number: {complex_number}")

>>> Explanation:
Integer (int): The variable age is assigned the value 25, which is an integer.
Float (float): The variable height is assigned the value 5.9, which is a floating-point number (decimal).
Complex (complex): The variable complex_number is assigned a complex number 3 + 4j, where j denotes the imaginary unit.
The print() function outputs the values of these variables, formatted in a string.

>>> 2. Sequence Types
code...

# Sequence Types
# String
name = "Alice"
# List
fruits = ["apple", "banana", "cherry"]
# Tuple
coordinates = (10, 20)
print("\nSequence Types:")
print(f"Name (str): {name}")
print(f"Fruits (list): {fruits}")
print(f"Coordinates (tuple): {coordinates}")

>>> Explanation:
String (str): The variable name is assigned the value "Alice", which is a string.
List (list): The variable fruits is assigned a list containing three elements: ["apple", "banana", "cherry"]. Lists are mutable, meaning they can be changed after creation.
Tuple (tuple): The variable coordinates is assigned a tuple (10, 20). Tuples are immutable, meaning their values cannot be changed once defined.
The print() function outputs the values of these variables in a formatted string.

>>> 3. Mapping Type
code...

# Mapping Type
# Dictionary
person = {"name": name, "age": age}
print("\nMapping Type:")
print(f"Person (dict): {person}")

>>> Explanation:
Dictionary (dict): The variable person is a dictionary that maps keys to values. Here, "name" maps to the variable name, and "age" maps to the variable age. The dictionary is defined using curly braces {}.
The print() function outputs the dictionary in a formatted string.

>>> 4. Set Types
code...

# Set Types
# Set
unique_numbers = {1, 2, 3, 4, 5}
# Frozenset
immutable_numbers = frozenset([1, 2, 2, 3, 4])
print("\nSet Types:")
print(f"Unique Numbers (set): {unique_numbers}")
print(f"Immutable Numbers (frozenset): {immutable_numbers}")

>>> Explanation:
Set (set): The variable unique_numbers is a set that contains unique values {1, 2, 3, 4, 5}. Sets automatically discard duplicate values.
Frozenset: The variable immutable_numbers is a frozenset created from a list that had duplicates. Frozensets are immutable versions of sets, meaning they cannot be changed after creation.
The print() function outputs the set and frozenset values in a formatted string.

>>> 5. Boolean Type
code...

# Boolean Type
# Boolean
is_student = True
print("\nBoolean Type:")
print(f"Is Student (bool): {is_student}")

>>> Explanation:
Boolean (bool): The variable is_student is a boolean value assigned True. Booleans represent truth values, which can either be True or False.
The print() function outputs the boolean value in a formatted string.

>>> 6. Type Conversion
code...

# Demonstrating type conversion
num_str = "10"
num_int = int(num_str)  # Converts string to integer
num_float = float(num_str)  # Converts string to float
print("\nType Conversion:")
print(f"String '10' to Integer: {num_int}, String '10' to Float: {num_float}")

>>> Explanation:
Type Conversion: The variable num_str is a string containing "10".
int(num_str) converts the string to an integer (10).
float(num_str) converts the string to a floating-point number (10.0).
The print() function outputs the converted values in a formatted string.

>>> 7. Example Operations
code...

# Example operations
# List Operations
fruits.append("orange")  # Adding an item to the list
print(f"\nUpdated Fruits (list after append): {fruits}")
# Dictionary Operations
person["city"] = "Wonderland"  # Adding a new key-value pair
print(f"Updated Person (dict after adding city): {person}")
# Set Operations
unique_numbers.add(6)  # Adding an item to the set
print(f"Updated Unique Numbers (set after adding 6): {unique_numbers}")

>>> Explanation:
List Operations: The append() method adds "orange" to the end of the fruits list. The updated list is printed.
Dictionary Operations: A new key-value pair "city": "Wonderland" is added to the person dictionary. The updated dictionary is printed.
Set Operations: The add() method adds 6 to the unique_numbers set. The updated set is printed.

'''