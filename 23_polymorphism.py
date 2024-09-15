# Polymorphism

class Dog:
    def eat(self):
        print('eating dog food')
    
class Cat:
    def eat(self):
        print('Eating cat food')

#different classes having the same method

animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()
