# Exceptions

#example 1
try:
    result = 2 / 0
except ZeroDivisionError:
    print('Cannot divide by zero')
finally:
    result = 1

print(result)


#example 2
try:
    raise Exception('An error!') #raise an exception
except Exception as error:
    print(error)


#example 3
class DogNotFoundException(Exception):
    print('inside')
    pass

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print('Dog not found!')