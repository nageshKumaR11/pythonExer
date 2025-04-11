"""Blue print of a robot"""

class Robot:            #class Robot => defines a class (blueprint)
    def __init__(self, name, task):     #__init__ = constructor method, runs when you create an object
        self.name = name                #self     = refers to the current object
        self.task = task 

    def introduce(self):   
        print(f"Hi I am {self.name}, and I {self.task} !")

#instances of the class Robot
robot_1 = Robot("Robo_cleaner", "clean floor")
robot_2 = Robot("Chef_bot", "cook food")


robot_1.introduce()

robot_2.introduce()


