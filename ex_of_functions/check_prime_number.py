
def is_prime(number):  # 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
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
        return True

    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            print(i, "times", number // i, "is", number)
            return False

    print(number, "is a prime number")
    return True




print(is_prime(7))  # True
print(is_prime(12)) # False
print(is_prime(29)) # True
print(is_prime(1))  # False
print(is_prime(0))  # False



