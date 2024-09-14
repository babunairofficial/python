# Annotations
#python is dynamically typed, that means there is no need to specifically mention the datatype
#Nonetheless this can be particularly done using annotations


def increment(n): #function without annotations
    return n+1

print(increment(5))

def decrement(x: int) -> int: #function with annotations
    return x-1

print(decrement(9))
