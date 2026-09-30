
# num = int(input("enter a number: \n"))
# match num:
#     case 1:
#         print("sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thuesday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operation = input("choose operation: ")
match operation:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    case "//":
        print(num1 // num2)
    case "**":
        print(num1 ** num2)
        