'''
Decorators in python

decorates in python are a powerful and expressive feature that allows you to modify or enhance functions and methods in a clean and readable way. they provide a way to wrap additional functionality around an existing function without permanently modifying it
'''
def decorator(func): # decorator is a function that takes a function, it creates a new function indside its body (wrapper). then it return that new function
    def wrapper():
        print("I am about to print hello...")
        func()
        print("I have executed this function...")
    return wrapper
@decorator
def say_hello():
    print("Hello!")

say_hello()

'''
f will look something like this 
def f():
   print("I am about to execute a function... ")
   print("Hello")
   print("I have executed this function....")

'''

# f = decorator(say_hello)
# f()




