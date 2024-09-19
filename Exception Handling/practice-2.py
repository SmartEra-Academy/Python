user_input = ""
sum_numbers = 0

while user_input != 0:
    try:
        user_input = int(input("Enter a number: "))
        print("No Problems")    

    except ValueError:
        print("Invalid input, Please enter a valid number")

    else:
        sum_numbers += user_input
        print("Operation Done")

print("Sum of numbers:", sum_numbers)
