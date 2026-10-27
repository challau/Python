# def is_greater_than_9(x):
#     if x > 9:
#         return True
#     else:
#         return False

# a = [1,3,4,56,75,7,68,89,4]
# new = list(filter(is_greater_than_9, a))
# print(new)



a = [1,3,5,65,7,8,5,7,98,0,7,3,423,45,42,67,54,54]

new = list(filter(lambda x: x < 9, a))
uday = list(filter(lambda x: x > 9, a))
print(new)
print(uday)
