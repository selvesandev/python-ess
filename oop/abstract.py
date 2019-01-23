class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Sub class must implement this abstract method')


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def speak(self):
        print('Hello ' + self.name)


dog = Dog('Hunter')
dog.speak()
