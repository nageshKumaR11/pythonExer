# for loop with a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# for loop with range
for i in range(2, 6):  # Numbers from 2 to 5
    print(f"Number: {i}")

# while loop
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

# while loop with break
number = 0
while number < 10:
    print(f"Number: {number}")
    if number == 5:
        break  # Exit the loop when number is 5
    number += 1

# for loop with continue
for i in range(10):
    if i % 2 == 0:
        continue # Skip even numbers
    print(f"Odd Number: {i}")

# while loop with continue
n = 0
while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)


