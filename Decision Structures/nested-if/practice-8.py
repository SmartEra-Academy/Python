membership = input("Are you a member? (yes/no): ").lower()
purchase_amount = float(input("Enter your purchase amount: "))

if membership == "yes":
    if purchase_amount >= 100:
        print("You are eligible for a 20% discount.")
    else:
        print("You are eligible for a 10% discount.")
else:
    if purchase_amount >= 100:
        print("You are eligible for a 5% discount.")
    else:
        print("You are not eligible for a discount.")