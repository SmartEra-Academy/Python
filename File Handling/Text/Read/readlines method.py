file = open(r"Python\File Handling\Text\Read\read_text.txt")

list_contents = file.readlines()
print(list_contents)

file.close()