class Person:
    def __init__(self, age):
        self.__age = 0
        self.set_age(age)

    def get_age(self):
        return self.__age

    def set_age(self, age: int):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self.__age = age
person = Person(25)
print(person.get_age())
person.set_age(30)
print(person.get_age())



class Animal:
    def __init__(self, name: str):
        self.name = name
    def speak(self) -> str:
        return "I am an animal"
class Dog(Animal):
    def speak(self) -> str:
        return "Woof"
class Cat(Animal):
    def speak(self) -> str:
        return "Meow"
dog = Dog("pes")
cat = Cat("Kot")
print(dog.name, dog.speak())
print(cat.name, cat.speak())





class Vehicle:
    def move(self):
        return "Vehicle is moving"
class Car(Vehicle):
    def move(self):
        return "Car is driving"
class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"
def move(vehicle: Vehicle):
    return vehicle.move()
car = Car()
bike = Bicycle()
print(move(car))
print(move(bike))








from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return (22 / 7) * (self.radius ** 2)
rect = Rectangle(10, 5)
circle = Circle(7)
print(rect.area())
print(circle.area())












