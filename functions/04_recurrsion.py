# what is recursion in python 

# A function calling itself to solve a problem

# ex:

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))


"""

0 1 1 2 3 5 8 13
0 1 2 3 4 5 6 ......
fib(0) = 0
fib(1) = 1
fib(2) = fib(0) + fib(1)
fib(3) = fib(1) + fib(2)
fib(4) = fib(2) + fib(3)
fib(n) = fib(n-2) + fib(n-1)
"""

def fib(n):
    # base case of recursion
    if(n == 0 or n == 1):
        return n
    return fib(n - 2) + fib(n - 1)

print(fib(5))

    