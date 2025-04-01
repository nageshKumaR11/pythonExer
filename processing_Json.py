import json

# Sample JSON string
json_string = '{"name": "Alice", "age": 30, "city": "New York"}'

# Deserialize JSON string to Python dictionary
python_dict = json.loads(json_string)
print(f"Python dictionary: {python_dict}")
print(f"Type of python_dict: {type(python_dict)}")

# Accessing data
print(f"Name: {python_dict['name']}")
print(f"Age: {python_dict['age']}")
print(f"City: {python_dict['city']}")

# Modifying data
python_dict['age'] = 32
python_dict['occupation'] = 'Engineer'
print(f"Modified dictionary: {python_dict}")

# Serialize Python dictionary to JSON string
new_json_string = json.dumps(python_dict, indent=4)  # indent for pretty printing
print(f"New JSON string:\n{new_json_string}")
print(f"Type of new_json_string: {type(new_json_string)}")

# Create a Python dictionary
data = {
    "name": "Bob",
    "age": 25,
    "is_student": True,
    "hobbies": ["reading", "coding", "traveling"],
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "zip": "12345"
    }
}

# Serialize the dictionary to a JSON formatted string with indent
json_data = json.dumps(data, indent=4)
print(json_data)

# Writing JSON to a file
with open("data.json", "w") as outfile:
    json.dump(data, outfile, indent=4)

# Reading JSON from a file
with open("data.json", "r") as infile:
    loaded_data = json.load(infile)
print(loaded_data)
