numbers = [1, 2, 3, 4, 5]
print(f"Original list: {numbers}")

# Indexing
print(f"First element: {numbers[0]}")  # 1
print(f"Last element: {numbers[-1]}") # 5

# Slicing
print(f"Slice [1:3]: {numbers[1:3]}")  # [2, 3]
print(f"Slice [:3]: {numbers[:3]}")  # [1, 2, 3]
print(f"Slice [2:]: {numbers[2:]}")  # [3, 4, 5]

# Methods
numbers.append(6)
print(f"Append 6: {numbers}")        # [1, 2, 3, 4, 5, 6]
numbers.insert(2, 10)
print(f"Insert 10 at index 2: {numbers}")  # [1, 2, 10, 3, 4, 5, 6]
numbers.remove(4)
print(f"Remove 4: {numbers}")           # [1, 2, 10, 3, 5, 6]
popped_element = numbers.pop(1)
print(f"Popped element at index 1: {popped_element}, List: {numbers}")  # 2, [1, 10, 3, 5, 6]


