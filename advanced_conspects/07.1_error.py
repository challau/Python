while True:
    try:
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        print(f"The sum is {a + b}")
    except:
        print("some error occurred!")
