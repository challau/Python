while True:
    try:
        a = int(input("enter the number 1: "))
        b = int(input("enter the number 2: "))
        print(f"The division is : {a / b}")
    except ValueError:
        print("Please don't perform bad typecasts")
    except ZeroDivisionError:
        print("Hey don't divide by 0")
    except Exception as e:
        print("Unknown error occurred!", e)
