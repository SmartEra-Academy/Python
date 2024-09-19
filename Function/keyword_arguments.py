# Keyword arguments allow you to specify values by the parameter name
# The order doesn't matter because you're explicitly stating which parameter each argument is for

def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

# Calling the function with keyword arguments
greet(last_name="Doe", first_name="John") 

