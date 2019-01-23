# Object Oriented Programming in Python.
Allows programmers to create their own object that have method
and attributes.

* For much larger scripts of python code functions by themselves are not enough for organizing and 
repeatability.

* Commonly repeated task and object can be defined with OOP to create code
that is more usable.

```
class NameOfClass():
    def __init__(self,param1,param2):
        self.param1=param1
        self.param2=param2s
    
    def some_mothods(self):
        print(self.param1)    
```


* Example

```
class Dog:
    # Called Whenever a instance of a class is created.
    def __init__(self, breed, name='', spots=True):
        self.breed = breed
        self.name = name
        self.spots = spots


my_dog = Dog('German Shepherd', name='Tommy', spots=False)
# my_dog = Dog(breed='German Shepherd')
print(my_dog.breed)

```

### Inheritance
Method of creating a new class using classes that have already been defined. They main purpose to re use code and reduce
the complexity of a program.

* The newly formed class may inherit the old class to use some of it's method or attributes.
```
class Animal:
    def __init__(self):
        print('Animal Created')
        

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')
        
```

```
class Animal:
    def __init__(self):
        print('Animal Created')

    def who_am_i(self):
        print('I am animal')

    def eat(self):
        print('I am eating')


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    def who_am_i(self): # Methods can be overwritten
        print('I am a dog')


dog = Dog()
dog.eat()

```

### Polymorphism
```
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

print(niko.speak())
```
* Both the class contains the same method name called `speak`.
```

niko = Dog('Niko')
felix = Cat('Felix')

for pet in [niko, felix]:
    print(pet.speak())
```

* Or

```
def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
```

* Since these two different class share a common method `speak`. So in the above both cases
we are able to pass object and we obtain object specific results from this mechanism.

* That is polymorphism basic idea is you have two separate classes that happens to share the same method allowing you call those same method names without needing you to worry about that
specific class that's being passed in.


## Don't Go Through This Needs more research.
### Abstract Classes.
A class that is never instantiated. It is designed to only serve as the base class
 
* **Abstract Method**
    In python you will have to create a abstract method by your own.
    
    ```
    class Animal:
        def __init__(self, name):
            self.name = name
    
        # Raising an Error.
        def speak(self):
            raise NotImplementedError('Sub class must implement this abstract method')
    
    
    my_animal = Animal('Tommy')
    my_animal.speak() # Will Generate a Error.
    ```
The `speak` function when called will generate a NotImplementedError. Therefore
```
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
```

### Magic (Special) Methods
Also know as `Dunder` method because they have double underscore.`__init__`



##### __str__ (print your object)
```
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


b = Book('Python', 'Selvesan')
print(b)
```
You cannot print the `b` object because the print function asks for the string representation of the object rather it gives a string report of the memory.
So Instead what we can do is us the special method `__str__`. So by using this is there is any function or code in your python class
that ask for your string representation your object you can return it from here.

```
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

b = Book('Python', 'Selvesan')
print(b)
```

##### __len__ (return value when asked from the len(object) function)
```
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return 100


b = Book('Python', 'Selvesan')
print(len(b)) ## Executes the __len__ prints 100
```


##### (If you want to report or print when deleting a object)
```
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __del__(self):
        print('You deleted Book object')


b = Book('Python', 'Selvesan')

del b; ## You delete Book object.

```
