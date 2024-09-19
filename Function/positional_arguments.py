# Positional arguments are the most common type of argument in Python.
# The order in which you pass them to the function matters, 
# and they are assigned to the parameters in the same order in which they are passed.

def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

# Calling the function with positional arguments
greet("John", "Doe")  