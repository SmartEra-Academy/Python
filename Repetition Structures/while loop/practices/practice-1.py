password = input("Enter the correct password: ")

while password != "secret":

    print("Password is wrong")
    password = input("Enter the correct password: ")

print("Access granted!")