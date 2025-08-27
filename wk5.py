#Assignment 1: Design Your Own Class! 🏗️
#Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
#Add attributes and methods to bring the class to life!
#Use constructors to initialize each object with unique values.
#Add an inheritance layer to explore polymorphism or encapsulation.


# Parent class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f"{self.name} is eating")

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def bark(self):
        print("Woof! Woof!")

# Create object
my_dog = Dog("Buddy", 3, "Golden Retriever")
print(f"{my_dog.name} is a {my_dog.breed}")
my_dog.eat()
my_dog.bark()






#Activity 2: Polymorphism Challenge! 🎭

#Create a program that includes animals or vehicles with the same action (like move()). 
# However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Boat:
    def move(self):
        print("Sailing ⛵")

# Create objects
car = Car()
plane = Plane()
boat = Boat()

# Call move() on each object directly
car.move()
plane.move()
boat.move()