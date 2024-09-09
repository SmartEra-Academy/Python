num = int(input("Enter a number: "))
reversed_num = 0

while num > 0:
    remainder = num % 10
    reversed_num = reversed_num * 10 + remainder
    num //= 10

print("Reversed number:", reversed_num)