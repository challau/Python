a = int(input("Enter the number: "))


match a:
    case 122:
        print("the value is 122")
    case 3:
        print("The value is 3")
    case 6:
        print("The value is 6")
    case _:
        print("Better luck next time")