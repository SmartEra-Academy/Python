my_info = {
    "name": "Danial", 
    "age": 23,       
    "course": "Python" 
}
print(my_info)


# update age value
my_info["age"] = 22
print(my_info)


# update name value using update() method
update_name = {"name": "reza"}  
my_info.update(update_name)  
print(my_info)