#Loops

condition = True
while condition == True:
    print("The condition is True")
    condition = False

count = 0
while count < 10:
    print("The conditon is True")
    count += 1

print("After the loop")

items = [1, 2, 3, 4]
for item in items:
    print(item)

for x in range(15):
    print(x)

nums = [1, 2, 3, 4, 5]
for index, num in enumerate(nums):
    print(index, num)