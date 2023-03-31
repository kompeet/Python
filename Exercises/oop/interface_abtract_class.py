from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def say_hi(self):
        print("HI!")

class Dog(Animal):

    def make_sound(self):
        print("WOFF!!")

    def say_hi(self):
        print("Hiya!!!")

class Cat(Animal):

    def make_sound(self):
        print("MEOW!!")

class Turtle(Animal):
    def say_hi(self):
        print("SSS!")


dog1 = Dog()
cat1 = Cat()
turtle1 = Turtle()

dog1.make_sound()
dog1.say_hi()
cat1.make_sound()
turtle1.say_hi()