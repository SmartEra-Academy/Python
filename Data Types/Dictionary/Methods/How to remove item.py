my_info = {
    "name": "Danial", 
    "age": 23,       
    "course": "Python" 
}

# Remove and return the value for a key
age = my_info.pop("age", "not exist")

print("age key removed ->", age) 
print(my_info) 

# Remove and return the last key-value pair (in Python 3.7+)
last_item = my_info.popitem()
print("last item ->", (last_item)) 
print(my_info)  

my_info.clear()
print(my_info)  

