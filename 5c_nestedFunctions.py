# nested functions
def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)

talk('I am going to buy the milk')


#example
def count():
    count = 0

    def increment():
        nonlocal count #allows us to access variable declared outside the function
        count = count + 1
        print(count)

    increment()

count()