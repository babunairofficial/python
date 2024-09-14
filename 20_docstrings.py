# Docstrings
#used as comments to explain the code

def increment(n):
    """Increment a number"""
    return n + 1

class Dog:
    """A class representing a dog"""
    def __init__(self, name, age):
        """Initialize a new dog"""
        self.name = name
        self.age = age

    def bark(self):
        """Let the dog bark"""
        print('WOF!')

print(help(Dog)) #gives details of the code including docstrings