def get_user_age():
    try:
        age = -10
        
        if age < 0:
            raise ValueError("Age cannot be negative")
        
        print(f"Your age is {age}")
    
    except ValueError as ve:
        print(f"Error: {ve}")    

# Run the function@!
get_user_age()
