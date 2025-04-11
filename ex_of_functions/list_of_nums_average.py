def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.

    Args:
        numbers: A list of numbers.

    Returns:
        The average of the numbers, or 0 if the list is empty.
    """
    if not isinstance(numbers, list):
        return "Invalid input. Please provide a list."
    if not numbers:  # Check for empty list
        return 0.0
    total = sum(numbers)
    return total / len(numbers)

print(calculate_average([1, 2, 3, 4, 5]))  # 3.0
print(calculate_average([10, 20, 30]))     # 20.0
print(calculate_average([]))             # 0.0
print(calculate_average([2.5, 7.5, 10])) # 6.666666666666667
print(calculate_average("abc")) # Invalid input


