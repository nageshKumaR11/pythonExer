def factorial(n):
    """Calculates the factorial of a non-negative integer n."""
    if not isinstance(n, int) or n < 0:
        return "Invalid input.  Please provide a non-negative integer."
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

print(factorial(5))  # 120
print(factorial(0))  # 1
print(factorial(-1)) # Invalid input
print(factorial(5.5)) # Invalid input



