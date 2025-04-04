class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Meow Meow")

    def info(self):
        print(f"Cat name: {self.name}")
        print(f"Cat age: {self.age}")
        self.make_sound()

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Bark Bark")

    def info(self):
        print(f"Dog name: {self.name}")
        print(f"Dog age: {self.age}")
        self.make_sound()

def my_pet(pet):
    pet.info()

cat = Cat('Meow Meow Fuzzyface', 25)
dog = Dog('Mr Peanutbutter', 40)

my_pet(cat)
print("")
my_pet(dog)

