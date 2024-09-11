# Default arguments allow you to assign default values to parameters in the function definition.
# If no argument is provided for that parameter when calling the function, the default value will be used.

def greet(first_name, last_name="Smith"):
    print(f"Hello, {first_name} {last_name}!")

# Calling the function with one argument, default for 'last_name' is used
greet("John") 

# Calling the function with both arguments, default is overridden
greet("John", "Doe") 