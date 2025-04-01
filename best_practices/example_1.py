def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Division by zero!")
        return None
    else:
        print("Result is:", result)
        return result
    finally:
        print("Cleanup: This block always executes.")

a = 10
b = 2
divide(a, b)

a = 10
b = 0
divide(a, b)