from functools import reduce

numbers = [1,2,3,4,5,6]
#.         [3,3,4,5,6]
#          [6,4,5,6]
#          [10,5,6]
#           [15,6]
#            [21]

def sum(a,b):
    return a + b

c = reduce(sum,numbers)
print(c)



numbers = [1, 2, 3, 4, 5]
# Calculate the sum of all numbers using reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers) # Output: 15

# Calculate the product of all numbers using reduce
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print(product_of_numbers) # Output: 120


#reduce with initializer
empty_list_sum = reduce(lambda x,y: x+y, [], 0)
print(empty_list_sum) # 0


# Without the initializer:
# empty_list_sum = reduce(lambda x,y: x+y, []) # raises TypeError
# Equivalent using a loop (for sum):
total = 0
for x in numbers:
    total += x
print(total) # 15