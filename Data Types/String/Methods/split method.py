# Split the string into a list

text = "apple banana cherry"
fruits_1 = text.split(" ")
print(fruits_1) 

text_2 = "apple banana cherry"
fruits_2 = text_2.split(" ", 1)
print(fruits_2) 

text_3 = "I'm a good boy. You are a good boy"
fruits_3 = text_3.split("a")
print(fruits_3) 

text_4 = "I'm a good boy. You are a good boy"
fruits_4 = text_4.split("a", 2)
print(fruits_4) 
