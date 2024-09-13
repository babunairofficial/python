#Lambda Functions

#also called anonymous function 
#they have no name and only have 1 expression as their body
#defined using lamda keyword

# argument : expression
lambda num : num * 2

multiply = lambda a, b : a * b

print(multiply(2,4))

#lambda functions work better when combined with other functions eg map, filter and reduce

# map, filter, reduce

#map()
numbers = [1, 2, 3]

"""
def double(a):
    return a * 2
"""
#same output can be achieved using a lambda function
double = lambda a: a * 2

result = map(double, numbers)
#result = map(lambda a: a * 2, numbers)

print(list(result))

#filter()
numbers2 = [4, 5, 6]

"""
def isEven(n):
    return n % 2 == 0

result2 = filter(isEven, numbers2)
"""

result2 = filter(lambda n: n % 2 == 0, numbers2)
print(list(result2))