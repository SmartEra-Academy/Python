while True:
    print("Menu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("You selected Option 1.")
    elif choice == "2":
        print("You selected Option 2.")
    elif choice == "3":
        print("Exiting...")
        break  # Exit the loop when the user chooses 3
    else:
        print("Invalid choice, please try again.")