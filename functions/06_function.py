def sum(a,b):
    # a and b are local variables
    print(z)
    c = a + b
    # z = 1 # it is creates a local variable called z 
    return c
z = 8 # z is the global variable
print(sum(2,3))
print(z)




