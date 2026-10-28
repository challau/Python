# Walrus Operator (:=)

# Introduction
# The walrus operator ( := ), introduced in Python 3.8, is an assignment expression
# operator. It allows you to assign a value to a variable within an expression. This can
# make your code more concise and, in some cases, more efficient by avoiding
# repeated calculations or function calls. The name “walrus operator” comes from the
# operator’s resemblance to the eyes and tusks of a walrus.

# Use Cases
# Conditional Expressions: The most common use case is within if
# statements, while loops, and list comprehensions, where you need to both
# test a condition and use the value that was tested.


def very_slow_func():
    print("Something...")
    print("Something..")
    print("Something..")
    print("Something...")
    return 70

# if(very_slow_func() > 10):
#     print(very_slow_func())
# else:
#     print("Its not greater than 10")


while(data:=input("enter the value: ")):
    print(data)
    if data == "q":
        break