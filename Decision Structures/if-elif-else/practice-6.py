status = input("Enter your delivery status (shipped, in transit, delivered): ").lower()

if status == "shipped":
    print("Your order has been shipped.")
elif status == "in transit":
    print("Your order is on the way.")
elif status == "delivered":
    print("Your order has been delivered.")
else:
    print("Invalid status. Please enter shipped, in transit, or delivered.")