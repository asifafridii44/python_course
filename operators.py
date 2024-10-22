'''
In programming, operators are special symbols or keywords that perform operations 
on one or more operands(variables or values). Operators are used to manipulate data and variables, 
enabling a wide range of functionalities in a program. Python supports several types of operators, 
each serving different purposes.

>>> Types of Operators in Python

>>> 1) Arithmetic Operators
Used for performing mathematical operations.
>>> Examples:
+ : Addition
- : Subtraction
* : Multiplication
/ : Division (returns a float)
// : Floor Division (returns the largest integer less than or equal to the division result)
% : Modulus (returns the remainder of the division)
** : Exponentiation (raises the left operand to the power of the right operand)

code...
a = 10
b = 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.3333
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000

>>> 2) Comparison Operators
Used for comparing values.
>>> Examples:
== : Equal to
!= : Not equal to
> : Greater than
< : Less than
>= : Greater than or equal to
<= : Less than or equal to

code...
x = 5
y = 10
print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
print(x >= y)  # False
print(x <= y)  # True

>>> 3)Logical Operators
Used to combine conditional statements.
>>> Examples:
and : Returns True if both statements are true
or : Returns True if at least one statement is true
not : Reverses the result (True becomes False

code...
a = True
b = False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False

>>> 4)Bitwise Operators
Operate on bits and perform bit-level operations.
>>> Examples:
& : Bitwise AND
| : Bitwise OR
^ : Bitwise XOR
~ : Bitwise NOT
<< : Left shift
>> : Right shift

>>> code...
x = 5   # (binary: 0101)
y = 3   # (binary: 0011)
print(x & y)  # 1  (binary: 0001)
print(x | y)  # 7  (binary: 0111)
print(x ^ y)  # 6  (binary: 0110)
print(~x)     # -6 (binary: 1010, inverts the bits)
print(x << 1) # 10 (binary: 1010, shifts left)
print(x >> 1) # 2  (binary: 0010, shifts right)

>>> 5)Assignment Operators
Used to assign values to variables.
>>> Examples:
= : Assigns the value
+= : Adds and assigns
-= : Subtracts and assigns
*= : Multiplies and assigns
/= : Divides and assigns
%= : Modulus and assigns
**=: Exponentiation and assigns
//=: Floor division and assigns

code...
a = 5
a += 2  # a = a + 2
print(a)  # 7
a *= 3  # a = a * 3
print(a)  # 21

>>> 6) Identity Operators
Used to check if two variables point to the same object in memory.
>>> Examples:
is : Returns True if both variables are the same object
is not : Returns True if both variables are not the same object

code...
a = [1, 2, 3]
b = a
c = a[:]
print(a is b)    # True (same object)
print(a is c)    # False (different object)
print(a is not c) # True

>>> 7)Membership Operators
Used to test if a value or variable is in a sequence (like a string, list, or tuple).
>>> Examples:
in : Returns True if the value is found
not in : Returns True if the value is not found

code...
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)   # True
print("grape" not in fruits) # True

'''
# Arithmetic Operators
print("Arithmetic Operators:")
a = 10
b = 3
print(f"Addition: {a} + {b} = {a + b}")        # 10 + 3 = 13
print(f"Subtraction: {a} - {b} = {a - b}")     # 10 - 3 = 7
print(f"Multiplication: {a} * {b} = {a * b}")  # 10 * 3 = 30
print(f"Division: {a} / {b} = {a / b}")        # 10 / 3 = 3.3333
print(f"Floor Division: {a} // {b} = {a // b}") # 10 // 3 = 3
print(f"Modulus: {a} % {b} = {a % b}")          # 10 % 3 = 1
print(f"Exponentiation: {a} ** {b} = {a ** b}") # 10 ** 3 = 1000

# Comparison Operators
print("\nComparison Operators:")
x = 5
y = 10
print(f"{x} == {y}: {x == y}")  # False
print(f"{x} != {y}: {x != y}")  # True
print(f"{x} > {y}: {x > y}")    # False
print(f"{x} < {y}: {x < y}")    # True
print(f"{x} >= {y}: {x >= y}")  # False
print(f"{x} <= {y}: {x <= y}")  # True

# Logical Operators
print("\nLogical Operators:")
a = True
b = False
print(f"a and b: {a and b}")   # False
print(f"a or b: {a or b}")     # True
print(f"not a: {not a}")        # False

# Bitwise Operators
print("\nBitwise Operators:")
x = 5   # (binary: 0101)
y = 3   # (binary: 0011)
print(f"x & y: {x & y}")  # 1  (binary: 0001)
print(f"x | y: {x | y}")  # 7  (binary: 0111)
print(f"x ^ y: {x ^ y}")  # 6  (binary: 0110)
print(f"~x: {~x}")         # -6 (binary: 1010, inverts the bits)
print(f"x << 1: {x << 1}") # 10 (binary: 1010, shifts left)
print(f"x >> 1: {x >> 1}") # 2  (binary: 0010, shifts right)

# Assignment Operators
print("\nAssignment Operators:")
c = 5
print(f"Initial value of c: {c}")  # 5
c += 2  # c = c + 2
print(f"After c += 2: {c}")  # 7
c *= 3  # c = c * 3
print(f"After c *= 3: {c}")  # 21

# Identity Operators
print("\nIdentity Operators:")
a = [1, 2, 3]
b = a
c = a[:]
print(f"a is b: {a is b}")     # True (same object)
print(f"a is c: {a is c}")     # False (different object)
print(f"a is not c: {a is not c}") # True

# Membership Operators
print("\nMembership Operators:")
fruits = ["apple", "banana", "cherry"]
print(f"'banana' in fruits: {'banana' in fruits}")   # True
print(f"'grape' not in fruits: {'grape' not in fruits}") # True


'''
>>> Explanation

>>> Arithmetic Operators: Demonstrates addition, subtraction, multiplication, division, 
floor division, modulus, and exponentiation.

>>> Comparison Operators: Compares two values using equality, inequality, greater than, less than, etc.

>>> Logical Operators: Combines boolean values using logical operations (AND, OR, NOT).

>>> Bitwise Operators: Performs bit-level operations on integers.

>>> Assignment Operators: Shows how to assign and modify values using shorthand assignments.

>>> Identity Operators: Checks if two variables refer to the same object in memory.

>>> Membership Operators: Tests for membership in a sequence like a list.

'''