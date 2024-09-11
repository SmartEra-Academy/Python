import json

# Opening a JSON file in read mode
with open(r'Python\File Handling\JSON\Write\write_json.json', 'r') as json_file:
    data = json.load(json_file)  

print(data)