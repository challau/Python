
'''
while True:
    try:
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        print(f"The sum is { a + b }")
    except Exception as e:
        print("Some error occurred!", e)

'''
# Enter number 1: 4
# Enter number 2: uday
# Some error occurred! invalid literal for int() with base 10: 'uday'
# Enter number 1: 


# while True:
#     try:
#         a = int(input("Enter number 1: "))
#         b = int(input("Enter number 2: "))
#         print(f"The division is { a / b }")
#     except ValueError:
#         print("Please don't perform bad typecasts")
#     except ZeroDivisionError:
#         print("Hey dont divide by 0")
#     except Exception as e:
#         print("Unknown error occurred!",e)


a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

if b == 0:
    raise ValueError("Please dont divide by 0")
print(f"The division is { a / b }")


# Enter number 1: 4
# Enter number 2: 0
# Traceback (most recent call last):
#   File "/Users/challaudaykumar/Desktop/Python/advanced_conspects/07.2_error.py", line 35, in <module>
#     raise ValueError("Please dont divide by 0")
# ValueError: Please dont divide by 0


