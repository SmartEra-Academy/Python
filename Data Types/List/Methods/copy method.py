# Return a shallow copy of the list

fruits = ["apple", "banana", "cherry"]

fruits_copy = fruits
fruits_copy.append("apple")

print(fruits)
print(fruits_copy)



fruits = ["apple", "banana", "cherry"]

fruits_copy = fruits.copy()
fruits_copy.append("apple")

print(fruits)
print(fruits_copy)