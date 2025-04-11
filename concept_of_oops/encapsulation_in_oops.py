#########################################################################################
#                    Encapsulation – Keeping Things Private                        
#########################################################################################

"""Let’s say some data inside the robot should not be tampered with directly 
(eg - like its battery level in the following example. )
This is where encapsulation helps us.
"""

class Robot:
    def __init__(self, name, task):
        self.name = name
        self.task = task
        self.__battery_level = 100      #Private variable 
        
    def introduce(self):
        print(f"Hi, I am {self.name}, I {self.task}. Battery : {self.__battery_level}%") 

    def charge(self):
        self.__battery_level = 100
        print(f"{self.name} is fully charged.")

    def work(self):
        if self.__battery_level > 0:
            self.__battery_level -= 10
            print(f"{self.name} is working .... battery level is {self.__battery_level}%") 
        else:
            print(f"{self.name} needs chaarging.")

    def battery_level(self):
        print(f"{self.name} has {self.__battery_level}% battery left.")


my_bot = Robot("Helper_bot", "assist humans")

my_bot.introduce()
my_bot.work()
my_bot.work()
my_bot.battery_level()
my_bot.charge()
my_bot.battery_level()


#################################################################################################
#                           Why use encapsulation ?
#################################################################################################

"""
Prevents bugs: No one can change important values accidentally.

Makes your code easier to manage and update.

Keeps logic in one place—safe and secure.

Encapsulation = hiding the internals + controlling access.

"""