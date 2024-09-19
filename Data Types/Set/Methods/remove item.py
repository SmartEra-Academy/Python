# remove(item):
# Removes the specified element from the set.
# Raises a KeyError if the element does not exist.

# discard(item):
#  Removes the specified element from the set,
#  but does not raise an error if the 

my_set = {14, 2, 3, 11, 12, 13, 44}

# Remove an element using remove 
my_set.remove(2)
print(my_set) 

my_set.discard(4)

# Pop an arbitrary element
popped_item = my_set.pop()
print(popped_item) 
print(my_set) 
