unique_numbers = {1, 2, 3, 4, 1, 2, 5}
print(f"Unique numbers set: {unique_numbers}")  # {1, 2, 3, 4, 5}

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Union: {set1 | set2}")  # {1, 2, 3, 4, 5, 6, 7, 8}
print(f"Intersection: {set1 & set2}")  # {4, 5}
print(f"Difference (set1 - set2): {set1 - set2}")  # {1, 2, 3}
print(f"Symmetric Difference: {set1 ^ set2}") # {1, 2, 3, 6, 7, 8}


