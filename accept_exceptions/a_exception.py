#TypeError	
"""You used the wrong “type” of stuff together	
 eg : You tried to add a number and a word """

# print(1 + "hello")

# ValueError	
"""# You gave a value that doesn’t make sense	
You tried to turn "abc" into a number:""" 

# print(int("1")) 

# IndexError	
"""You looked for something that’s not in the list"""	
# my_list  = [5, 3, 1] 

# my_list[5] 

# KeyError	

"""You asked for a key that doesn’t exist in a dictionary"""	
# my_dict = {"x":1, "y":"hello", "w":True}
# my_dict["x"] 

# FileNotFoundError	
"""You tried to open a file that doesn’t exist"""	
# open("no_file.txt") 

























try:
    with open("some_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file 'no_file.txt' was not found.")
