##########################################################################################
#                       Inheritance – Like Parent, Like Child
##########################################################################################

class Robot:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name} .")  

class CleanerBot(Robot):
    def clean(self):
        print(f"{self.name} is cleaning.")

class SecurityBot(Robot):
    def patrol(self):
        print(f"{self.name} is patrolling the area.")  

cleaner = CleanerBot("Dusty")
cleaner.greet()
cleaner.clean()


security = SecurityBot("Guardian")
security.greet()
security.patrol()

