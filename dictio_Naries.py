student = {"name": "Charlie", "grade": "A", "age": 20}
print(f"Student dictionary: {student}")

# Accessing values
print(f"Student name: {student['name']}")
print(f"Student grade: {student.get('grade')}") #using get

# Adding/Updating
student["age"] = 22  # Update existing key
student["major"] = "Physics"  # Add new key-value pair
print(f"Updated student: {student}")

# Removing
removed_value = student.pop("age")
print(f"Removed value (age): {removed_value}, Updated dictionary: {student}")
del student["grade"]
print(f"Dictionary after deleting 'grade': {student}")


