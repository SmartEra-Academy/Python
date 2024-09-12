try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = num1 / num2
    print(f"The result of the division is: {result}")
    
except Exception as e:
    print(f"Error occurred: {e}")

print("Hello, World!")