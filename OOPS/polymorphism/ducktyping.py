def PetLover(pet):
    if hasattr(pet,'talk'):
        pet.talk()
    if hasattr(pet,'walk'):
        pet.walk()

class Duck:
    def talk(self):
        print('Duck is talking')

    def walk(self):
        print('Duck is walking')
class Dog:
    def talk(self):
        print('Dog is talking')

    def walk(self):
        print('Dog is walking')

duck = Duck()
dog = Dog()

PetLover(duck)
PetLover(dog)
