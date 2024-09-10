def hello():
    print("hi everyone")

hello()
hello()

def hi(name='no name'): #function with parameters (default value can be set too)
    print('hello ' + name)

hi('sachin') #calling function with arguments
hi()

def change(value):
    value["name"] = "Syd" #changes the dictionary

val = {"name":"beau"}

change(val) #calling the function with argument val

print(val)

def hello(name):
    print('Hello ' +name+' !')
    return name, "Beau", 8

print(hello("Syd"))