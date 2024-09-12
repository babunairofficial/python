#classes

# object is an instance of a class
# a class is the type of an object

class Tiger:
    def roar(self):
        print("roar!")

sher = Tiger()

print(type(sher))

#constructor = a special type of method
class Monkey:
    def __init__(self, name, age): #init is a contstructor
        self.name = name
        self.age = age

    def chatter(self):
        print("chatter")

bandar = Monkey("chipu", 8)

print(bandar.name)
print(bandar.age)

bandar.chatter()

#inheritance
class Animal:
    def walk(self):
        print("Walking...")

class Cat(Animal):
    def __init__(self, name, age): #init is a contstructor
        self.name = name
        self.age = age

    def meow(self):
        print("meow")

billa = Cat("Meena", 3)

print(billa.name)
print(billa.age)

billa.meow()
billa.walk()
