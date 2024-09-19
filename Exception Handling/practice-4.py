try:
    num = int(input("Enter a number: "))
except ValueError as e:
    print("Error: Invalid input, please enter a valid number.")
else:
    num += 2
    print(f"Number after adding 2: {num}")
finally:
    print("Done.")