class Dog:
    """Represents a dog with name and breed attributes.  Can bark."""
    def __init__(self, name, breed, age):
        """Constructor for the Dog class."""
        self.name = name
        self.breed = breed
        self.age = age #added age
        self.is_hungry = True

    def bark(self):
        """Prints the dog's bark."""
        if self.is_hungry:
          print("Woof! I want food!")
        else:
          print("Woof!")

    def describe(self):
        """Describes the dog."""
        print(f"{self.name} is a {self.breed} and is {self.age} years old.")

    def feed(self):
        """Feeds the dog"""
        self.is_hungry = False
        print(f"{self.name} is fed.")

my_dog = Dog("Buddy", "Golden Retriever", 3)
my_dog.bark()
my_dog.describe()

your_dog = Dog("Charlie", "Labrador", 2)
your_dog.bark()
your_dog.feed()
your_dog.bark()
your_dog.describe()


