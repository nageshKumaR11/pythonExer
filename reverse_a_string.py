def reverse_string(text):
    """
    Reverses a string.

    Args:
        text: The string to reverse.

    Returns:
        The reversed string.
    """
    if not isinstance(text, str):
        return "Invalid input. Please provide a string."
    return text[::-1]  # Using slicing

print(reverse_string("hello"))  # "olleh"
print(reverse_string("world"))  # "dlrow"
print(reverse_string(""))     # ""
print(reverse_string(123)) # Invalid input


