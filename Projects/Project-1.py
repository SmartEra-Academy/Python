def add(x, y):
    return x + y 

def sub(x, y):
    return x - y 

def mul(x, y):
    return x * y 

def div(x, y):
    if y != 0:
        return x / y
    else:
        return "Invalid"

print("\nChoose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Which one (1/2/3/4/exit) ? ")

    if choice == "exit":
        break

    try:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
    except Exception as e:
        print(f"Error: {e}")

    if choice == "1":
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == "2":
        print(f"{num1} - {num2} = {sub(num1, num2)}")
    elif choice == "3":
        print(f"{num1} * {num2} = {mul(num1, num2)}")
    elif choice == "4":
        print(f"{num1} / {num2} = {div(num1, num2)}")
    else:
        print("Wrong input, try again!")