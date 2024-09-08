# set() -> Converts an iterable into a set.

# Converting a list with duplicates to a set
my_list = [1, 2, 2, 3, 3, 4]
my_set = set(my_list)
print(my_set, type(my_set))  

# Converting a string to a set (duplicates are removed)
my_string = "hello"
my_set_2 = set(my_string)
print(my_set_2, type(my_set_2))  