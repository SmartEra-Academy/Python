age = int(input("How old are you? "))

if 0 < age and age <= 6:
    print("You are child")
elif 6 < age and age <= 13:
    print("You are teenager")
elif  13 < age and age <= 18:
    print("You are young")
elif 18 < age and age <= 30:
    print("You are adult")
elif 30 < age <= 120:
    print("You are more than 30")
else:
    print("Wrong age!")