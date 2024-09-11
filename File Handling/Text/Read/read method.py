# "r" - Default value. 
# Opens a file for reading, 
# error if the file does not exist

file = open(r"Python\File Handling\Text\Read\read_text.txt", "rt")

str_contents = file.read()

print(str_contents)
print("\n" in str_contents)
print(len(str_contents))

file.close()


with open(r"Python\File Handling\Text\Read\read_text.txt", "rt") as file:
    str_contents = file.read()

print(str_contents)