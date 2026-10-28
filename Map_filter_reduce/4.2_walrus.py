# Without walrus operator
# data = input("Enter a value (or 'quit' to exit): ")
# while data != "quit":
#      print(f"You entered: {data}")
#      data = input("Enter a value (or 'quit' to exit): ")



# With walrus operator
while (data := input("Enter a value (or 'quit' to exit): ")) != "quit":
   print(f"You entered: {data}")

# In the “with walrus” example, the input is assigned to data and compared to
# “quit” in a single expression.