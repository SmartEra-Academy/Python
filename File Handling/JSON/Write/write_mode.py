import json

# Data to be written
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Opening a JSON file in write mode
with open(r'Python\File Handling\JSON\Write\write_json.json', 'w') as json_file:
    json.dump(data, json_file)  