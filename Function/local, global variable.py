a = 5  # Global variable 'a'

def add():
    a = 3  # Local variable 'a', does not affect global 'a'
    b = 6  # Local variable 'b', exists only within the function
    sum_numbers = a + b  # Local variable 'sum_numbers', exists only within the function
    return sum_numbers  # Return the sum of local 'a' and 'b'

c = 7  # Global variable 'c'

print(a)  # Output: 5 (global 'a')
print(c)  # Output: 7 (global 'c')

result = add()  # Call the function and store the result in a global variable 'result'
print(result)  # Output: 9 (sum of local 'a' and 'b' from the function)

# print(b)  # This will raise an error because 'b' is a local variable, not accessible outside the function
