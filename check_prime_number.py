def is_prime(number):
    """
    Checks if a number is prime.

    Args:
        number: The number to check.

    Returns:
        True if the number is prime, False otherwise.
    """
    if not isinstance(number, int) or number <= 1:
        return False  # 1 and numbers less than 1 are not prime
    if number <= 3:
        return True  # 2 and 3 are prime
    if number % 2 == 0 or number % 3 == 0:
        return False  # Numbers divisible by 2 or 3 are not prime

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

print(is_prime(7))  # True
print(is_prime(12)) # False
print(is_prime(29)) # True
print(is_prime(1))  # False
print(is_prime(0))  # False



