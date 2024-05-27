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
