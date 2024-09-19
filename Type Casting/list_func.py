# list() -> Converts an iterable (like a tuple or string) into a list.

# Converting a tuple to a list
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list, type(my_list)) 

# Converting a string to a list (each character becomes a list element)
my_string = "hello"
my_list_2 = list(my_string)
print(my_list_2, type(my_list_2)) 