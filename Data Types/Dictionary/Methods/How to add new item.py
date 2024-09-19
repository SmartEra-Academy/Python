my_info = {
    "name": "Danial", 
    "age": 23,       
    "course": "Python" 
}
print(my_info)


# Add new item
my_info["course_2"] = "ML"  
print(my_info)


# Add new item using update() method
new_info = {"email": "Danial@gmail.com"}  
my_info.update(new_info)
print(my_info)