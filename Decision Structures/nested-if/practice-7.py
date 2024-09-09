age = 22
has_ticket = False

if age >= 18:
    if has_ticket:
        print("You can enter the event.")
    else:
        print("You need a ticket to enter the event.")
else:
    print("You are not old enough to enter the event.")