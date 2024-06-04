#datatypes
name = "babu"
age = 33
marks = float(98)
number = "16"
jersey_no = int(number)

print(type(name))
print(type(age))

print(type(name) == str)

print(isinstance(name,str))

print(isinstance(marks, float))

print(isinstance(number, int))
print(isinstance(jersey_no, int))

def is_adult(age):
  return True if age>18 else False

name += " is a boy"
print(name)

print("""hello friends

welcome to 

my channel""")

print("BeAu".lower())
print("BeAu".upper())
print("BeAu person".title())
print("BeAu person".islower())

print(name.upper())
print(name) #string does not change
print(len(name)) #length of string
print("bu" in name) #check if 'bu' is contained in name

#escaping characters
name2 = "Ba\"bu"
name3 = 'Ba"bu'
name4 = "Ba\nbu"
name5 = "Ba\\bu"

print(name2)
print(name3)
print(name4)
print(name5)

#strings and slicing
print(name[1])
print(name[-1])

print(name[1:3]) #slicing
print(name[:7])
print(name[2:])

#booleans
done = True 
not_done = False

print(type(done) == bool)

if done: #yes should print
  print("yes")
else:
  print("no")

if not_done: # no should print
  print("yes")
else:
  print ("no")
#strings are false only when empty, otherwise its true

book_1_read = True
book_2_read = False
read_any_book = any([book_1_read, book_2_read])
print(read_any_book) #it is enough to have any of the above to be true , it will return true

ingredients_purchased = True
meal_cooked = False
ready_to_serve = all([ingredients_purchased, meal_cooked])
print(ready_to_serve) #all of it has to be true, only then true would be returned

#number data types
num1 = 2+3j
num2 = complex(2,3) #complex object
print(num1.real, num2.imag)

#built in functions
print(abs(-5.5))
print(round(5.49))
print(round(5.49, 2)) #rounding to 2nd decimal place


#Enums
from enum import Enum

class State(Enum): #State word can be any word we use
  INACTIVE = 0
  ACTIVE = 1

print(State.ACTIVE)
print(State.ACTIVE.value)
print(State(1))
print(State['ACTIVE'])

print(list(State)) #list the values of the State

print(len(State))

#user input
age = input("What is your age? ")
print("Your age is " + age)

#control statements
condition = True
if condition == True:
  print("The condition")
  print("was true")
else:
  print("The condition")
  print("was false")

print("outside if")

#Lists
dogs = ["Roger", "Syd", 1, True, "Quincy", 7]
print("Roger" in dogs)
print("Beau" in dogs)
print(dogs[0])
print(dogs[2])

dogs[2] = "Ray"  #updated item at index 2
print(dogs)

print(dogs[2:4])  #slice from index 2 to 4
print(dogs[2:])  #slice from index 2 to end
print(dogs[:3])  #slice from start to index 3

print(len(dogs))
dogs.append("Judah")  #add item at the end of the list
print(dogs)
print(len(dogs))

dogs.extend(["Judah", 5])  #add multiple items at the end of the list
print(dogs)
print(len(dogs))

dogs += ["Joshua", 2]  #add multiple items at the end of the list
print(dogs)
print(len(dogs))

dogs.remove("Joshua")  #remove item from the list
print(dogs)
print(len(dogs))

print(dogs.pop())  #remove and return last item from the list
print(dogs)
print(len(dogs))

dogs.insert(2, "Test")  #insert item at index 2
print(dogs)
print(len(dogs))
dogs[1:1] = ["Test1", "Test2"] #add multiple items at index 1
print(dogs)

#sorting lists
items = ["Roger", "Syd", "Quincy", "Beau", "bob"]  #all strings
itemscopy = items[:] #creating a copy of the list 'items'
print("the list before sorting")
print(items)
items.sort()
print("the list after sorting")
print(items) #sorting upper case first then lower case
items.sort(key=str.lower) #sorts irrespective of upper case or lower case
print(items)
#sorting modifies the contents of list
print("the original list was as follows:")
print(itemscopy)