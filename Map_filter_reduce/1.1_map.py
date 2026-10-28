# map , filter , and reduce are higher-order functions in Python (and many other
# programming languages) that operate on iterables (lists, tuples, etc.). They provide
# a concise and functional way to perform common operations on sequences of data
# without using explicit loops. While they were more central to Python’s functional
# programming style in earlier versions, list comprehensions and generator
# expressions often provide a more readable alternative in modern Python.


# Map
# The map() function applies a given function to each item of an iterable and
# returns an iterator that yields the results.
# Syntax: map(function, iterable, ...)
# function : The function to apply to each item.
# iterable : The iterable (e.g., list, tuple) whose items will be processed.
# ... : map can take multiple iterables. The function must take the same
# number of arguments
numbers = [1,2,3,45,4,21]

def square(x):
    return x * x
new = list(map(square, numbers))
print(new)


print('\n')

#Example with multiple iterables
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
summed = map(lambda x, y: x + y, numbers1, numbers2)
print(list(summed)) # Output: [5, 7, 9]



print('\n')


# Equivalent list comprehension:
squared_numbers_lc = [x**2 for x in numbers]
print(squared_numbers_lc) # Output: [1, 4, 9, 16, 25]