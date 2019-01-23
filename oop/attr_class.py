class Dog:
    # Called Whenever a instance of a class is created.
    def __init__(self, breed, name='', spots=True):
        self.breed = breed
        self.name = name
        self.spots = spots


my_dog = Dog('German Shepherd', name='Tommy', spots=False)
# my_dog = Dog(breed='German Shepherd')
print(my_dog.breed)
