#Tuples - creates immutable group of items
names = ("Roger", "Syd", "Beau")
print(names[0])
print(names.index("Roger"))
print(len(names))
print("Roger" in names)
print("sorted tuple : ", sorted(names))
print("original tuple : ", names)
#hence tuples are immutable, ulike lists
new_tuple = names + ("Tina", "Quincy")
print(new_tuple)