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


# Operator Overloading
#make classes comparable

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return True if self.age > other.age else False
    
handsome = Dog('Handsome', 5)
dora = Dog('Dora', 2)

print(handsome > dora)
 
#there are several other special functions or methods for operator overloading

#Creating instances in class
class Item:
    def calculate_total_price(self, x, y): #method
        return x * y
    

item1 = Item() #instance

#attributes
item1.name = "Phone" 
item1.price = 100
item1.quantity = 5

print(type(item1)) #this line prints a new datatype created different from the regular ones
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item() 
item2.name = "Laptop"
item2.price = 50000
item2.quantity = 2
print(item2.calculate_total_price(item2.price, item2.quantity))
