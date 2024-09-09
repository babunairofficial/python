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