# Variables and Data Types in Python

# What are Variables?
# Variables are used to store data that can be used and manipulated in a
# program.
# A variable is created when you assign a value to it using the = operator.
# Example:

# Variable Naming Rules
# Variable names can contain letters, numbers, and underscores.
# Variable names must start with a letter or underscore.
# Variable names are case-sensitive.
# Avoid using Python keywords as variable names (e.g., print , if , else ).

# Best Practices
# Use descriptive names that reflect the purpose of the variable.
# Use lowercase letters for variable names.
# Separate words using underscores for readability (e.g., first_name ,
# total_amount 
# name = "Alice"
# age = 25
# height = 5.6

# use the type() function to check the data type of a variabe.
print(type(10)) # Output: <class 'int'>
print(type("Hello")) # Output: <class 'str'>


# what is typecastin?
# typecasting is the process of converting one data type to another
# python provides build in functions for testing :
# int() : Converts to integer.
# float() : Converts to float.
# str() : Converts to string.
# bool() : Converts to boolean.

# Convert string to integer
num_str = "10"
num_int = int(num_str)
print(num_int) # Output: 10
# Convert integer to string
num = 25
num_str = str(num)
print(num_str) # Output: "25"
# Convert float to integer
pi = 3.14
pi_int = int(pi)
print(pi_int) # Output: 3


uday = 30
v = str(uday)
print(v)

chandu = "456"
c = int(chandu)
print(c)

