my_info = {
    "name":"Danial",
    "age":23,
    "course":"Python"
}

# Retrieve the value for a key
print(my_info["name"])
# print(my_info["email"]) 

# Retrieve the value for a key, with an optional default value
print(my_info.get("name")) 
print(my_info.get("email", "Not Available"))