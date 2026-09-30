"""
function arguments & return values

functions can take parameters and return values

types of arguments:
"""


# 1)positional arguments

# def add(a,b):
#     x = a + b
#     return x
# c = add(3,5)
# print(c)

def sub(a, b):
    x = a - b
    return x
s = sub(4, 6)
print(s)


# # default argument
# def add(a, b, plus = 0):
#     x = a + b + plus
#     return x
# c = add(3,5,2)
# print(c)

def mul(a, b, m = 0):
    x = a * b * m
    return x
c = mul(3,1,2)
print(c)


# # keyword Arguments
# def student(name,age):
#     print(f"Name: {name}, Age: {age}")
# student(age=20,name="Bob")


def uday(age , name):
    print(f"my name is {name}, and my age is {age}")
uday(age = 76, name = "uday kumar")






