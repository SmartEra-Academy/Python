# *args allows a function to accept any number of positional arguments.
def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3) 

# **kwargs allows a function to accept any number of keyword arguments 
# (arguments passed as key=value pairs)

def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(name="John", age=25, city="New York")
