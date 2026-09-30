# def fac(n):
#     if n == 0 or n == 1:
#         return 1
#     return fac(n - 1) + fac(n - 2)
# print(fac(5))


def safe_divide(a,b):
    if b == 0:
        return "Cannot divide by zero"
    return a/b
print(safe_divide(3,4))
print(safe_divide(9,0))