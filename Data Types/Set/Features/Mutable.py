# Sets are mutable,
# meaning you can add and remove
# lements after the set is created.
# However, the elements themselves must be immutable
# (like numbers, strings, or tuples).

my_set = {1, 2, 3, (3, 4, 5), "ali"}
my_set.add(24)
my_set.add(20)
print(my_set) 
