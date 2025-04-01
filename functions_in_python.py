def greet(name="Guest"):  # Default argument
    """This function greets the person passed in as a parameter.
    If no name is provided, it greets 'Guest'."""
    return f"Hello, {name}!"

message1 = greet("David")
message2 = greet()  # Using default argument
print(message1)
print(message2)

def calculate_area(length, width):
    """Calculates the area of a rectangle."""
    area = length * width
    return area

rectangle_area = calculate_area(5, 10)
print(f"Area: {rectangle_area}")

#Demonstrating local and global variables
global_variable = 20

def my_function():
    local_variable = 10
    print(f"Inside function: global_variable = {global_variable}")
    print(f"Inside function: local_variable = {local_variable}")

my_function()
print(f"Outside function: global_variable = {global_variable}")
# print(f"Outside function: local_variable = {local_variable}") #This will give an error


