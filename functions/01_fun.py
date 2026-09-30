# # a = 4
# # b = 2
# # c = 1
# # average = (a+b+c)/3
# # print(average)

# def average(a,b,c):
#     d = (a + b + c)/3.0
#     print(d)

# average(3, 5, 1)

# """
# function and modules 
# defining functions in Python
# functions help in reusability and modularity in python

# syntax:
# """
# def greet(name):
#     return f"Hello, {name}!"
# print(greet("Alice"))


# """
# key points:

# define using def keyword

# function names should be meaningful

# use return to send a value back

# """


# def name(s):
#     return s
# print(name(2))


# def name_a(y):
#     return y + 3
# print(name_a(3))


# def name_y(y):
#     return y
# print(name_y("uday"))


# def name_u(u):
#     return u
# print(name_u(4.5555555))




# def nameI(y,e,r,t,i):
#     if(y < e):
#         return e
#     elif(e < t):
#         return t
#     elif(r < i):
#         return i
#     else:
#         return r
# print(nameI(3,1,4,5,6))


# def nameu(y,e,r,t):
#     return y,e,r,t
# print(nameu(3,4,5,6))

# def nameu(y, e, r, t):
#     return y, e, r, t

# a, b, c, d = nameu(3, 4, 5, 6)

# print(a)
# print(b)
# print(c)
# print(d)


def average(a,b,c):
    d = (a + b + c)/3.0
    # print(d)
    return d
o1 = average(3,5,6)
o2 = average(4,2,1)

print(o1)
print(o2)