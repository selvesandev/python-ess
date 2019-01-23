class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' Says woof!!'


class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' Says meow!!'


niko = Dog('Niko')
felix = Cat('Felix')

for pet in [niko, felix]:
    print(pet.speak())



def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)