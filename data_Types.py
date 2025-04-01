# Integer
age = 25
print(f"Age: {age}, Type: {type(age)}")  # Using f-string

# Float
price = 19.99
print(f"Price: {price}, Type: {type(price)}")

# String
name = "Alice"
print(f"Name: {name}, Type: {type(name)}")

# Boolean
is_adult = age >= 18
print(f"Is Adult: {is_adult}, Type: {type(is_adult)}")

# List (mutable, ordered)
numbers = [1, 2, 3, "hello", 5.0]
print(f"Numbers: {numbers}, Type: {type(numbers)}")
print(f"First element: {numbers[0]}")  # Indexing
numbers[1] = 20  # Modification
numbers.append(6)  # Append
print(f"Modified list: {numbers}")

# Tuple (immutable, ordered)
coordinates = (10, 20)
print(f"Coordinates: {coordinates}, Type: {type(coordinates)}")
print(f"First coordinate: {coordinates[0]}")

# Dictionary (mutable, unordered, key-value pairs)
student = {"name": "Bob", "city": "New York", "age": 20}
print(f"Student: {student}, Type: {type(student)}")
print(f"Student Name: {student['name']}")  # Accessing value by key
student["age"] = 22  # Updating value
student["major"] = "Computer Science"  # Adding key-value pair
print(f"Updated student: {student}")

# Set (mutable, unordered, unique elements)
unique_numbers = {1, 2, 3, 4, 1, 2, 5}  # Duplicates are removed
print(f"Unique Numbers: {unique_numbers}, Type: {type(unique_numbers)}")


