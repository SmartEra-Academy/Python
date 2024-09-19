text = "this is a text and that is not a text!!"
emty_dict = {}

for char in text:
    if char not in emty_dict:
        emty_dict[char] = 1
    else:
        emty_dict[char] += 1 

print(emty_dict)