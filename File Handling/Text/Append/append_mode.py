# "a" - Opens a file for appending,
#  creates the file if it does not exist

file = open(r"Python\File Handling\Text\Append\append_text.txt", 'a')

file.write('this is a new thing\n')

file.close()