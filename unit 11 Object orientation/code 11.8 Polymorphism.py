class Animal(object):

    def speak(self):
        print('Animal Speaking')

class Cat(Animal):

    def speak(self):
        print('Meow')

class Dog(Animal):

    def speak(self):
        print('Woof')
def speak(object):  # animal
    object.speak()

animal = Animal()

speak(animal)

kitty = Cat()
puppy = Dog()

speak(kitty)
speak(puppy)
