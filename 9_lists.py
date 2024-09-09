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