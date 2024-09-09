#Dictionaries - key value pairs
dog = {"name": "Roger", "age": 8, "color": "green"}
print(dog)
print(dog["name"])

dog["name"] = "Syd" #change values stored at specific index
print(dog)
print(dog.get("name")) #to get a specific element
print(dog.get("color"))
print(dog.get("color", "brown")) #color default value is brown, incase it cannot find the color value
print(dog.pop("name")) #pop returns the value of the key and removes it from the dictionary
print(dog)

print(dog.popitem()) #pops the last item from the dictionary
print(dog)
print("color" in dog)
print(dog.keys())
print(list(dog.keys()))
print(dog.values())
print(list(dog.values()))
print(list(dog.items()))
print(len(dog))
dog["favorite food"] = "Meat" #add new key value pair
print(dog)
del dog["age"] #delete a key value pair
print(dog)
dogCopy = dog.copy() #copy the dictionary
print("copy ", dogCopy)