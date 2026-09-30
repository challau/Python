password = "Y2k123"

entered_pass = input("enter Password: ")

while(entered_pass != password):
    entered_pass = input("wrong Password! Try again enter password: ")
print("Success! You are logged in")