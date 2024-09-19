# "x" - Creates the specified file,
#  returns an error if the file exists

file = open(r"Python\File Handling\Text\Create\create_text.txt", 'x')

file.write('new file created')

file.close()