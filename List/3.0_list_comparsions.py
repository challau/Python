# create a list containing the table of 5

# a = 5 
# table = []

# for i in range(1,11):
#     table.append(5*i)

table = [5 * i for i in range(1,11)]

print(table)

# list comprehensions efficient list creation

squared = [x ** 2 for x in range(5)]
print(squared)

