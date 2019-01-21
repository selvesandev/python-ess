# Methods and Functions

Find the build in methods and their doc here. 
Get help about build in function with the `help` function
```
help(myList.insert) # Will print the short doc.
```
Or Get help from the python documentation.

<https://docs.python.org/3/>


#### Built In.

```
myList = [1, 2, 3]
myList.append(4)# Add to list

myList.pop() # Remove last from list
```

### Functions.
Allows us to create block of code that can be executed many times
without needing to constantly rewrite the entire block of code.  
**SYNTAX**
```
def name_of_func():
    """
        Doc string explaing the function.   
    """
    print('Hello')
    
name_of_func() #Hello    
```

* Parameters
```
def name_of_func(name):
    print('Hello '+name)
    
name_of_func('James')    
```
* Return
```
def name_of_func(a,b):
    return a+b
    
print(name_of_func(1,1))    
```

* Example.
```
def my_func(a, b):
    """
    DOCSTRING : Information about this function
    :param a:
    :param b:
    :return:
    """
    return a + b


print(my_func(1, 2))


help(my_func) # This will pring the Doc String.
```


* Default Argument `def say_hello(name='John')`

#### Functional Parameters (*args && **kwargs)
They stand for `Arguments` and `KeyWord Arguments` 
You cannot pass arguments more that the function accepts. eg:
```
def myFunc(a,b,c)

myFunc(2,3,4,5)
```
The above code would result TypeError. Therefore you should be using the `*args`

```
def calc(*a):
    print(a) # Here a is a tuple of values.
    return sum(a) * 0.5

print(calc(2, 4, 5, 6, 7))
```


```
def calc(*a):
    for item in a:
        print(item)
```

Python also provides a way to handle a number of keyword arguments. So instead of collecting tuple of values we use `**kwargs` which is `keyword arguments`.
So basically the `**kwargs` returns a dictionary instead of tuple.
```

def my_func_2(**kwargs):
    if 'fruit' in kwargs:
        print('My Fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')


my_func_2(fruit='apple', veggie='lettuce')

```

* **(\*args) && (\*\*kwargs)** in combination.
```
def my_func_3(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))

my_func_3(20, 30, 40, fruit='orange', food='eggs')
```

### Lambda Expression or Anonymous Functions (Map and Filters)
One time use function you use it once and never refer it again.```
```
    lambda arg:arg++
```
To explore and understand why do we use this we will use `map` and `filter` functions built in python.


* **MAP**
Is used to update the value of all the items in a list
```
my_nums = [1, 2, 3, 4, 5]

for item in map(my_func, my_nums):
    print(item)

OR

print(list(map(my_func, my_nums)))
```

* **FILTER**
Is used to filter the value from the list which meets the condition in a function.
```

my_nums = [1, 2, 3, 4, 5]

def check_event(num):
    return num % 2 == 0

print(list(filter(check_event, my_nums)))

or

for n in filter(check_event,my_nums):
    print(n)

```

* Now Converting These to a `lambda` functions
```
    for item in map(lambda num: num ** 2, [2,3,4,5]):
        print(item)
```


### Nested Statements and Scope (Local & Global).
When you create a variable in python that name is stored in a what is called as namespace. The variable name also has a scope which determines the visibility of that variable name on the other part of
your code.

```
x = 10  # Global Scope


def printer():
    print(x)  # Will print 10


printer()

print(x)  # Prints 10

``` 

#### LEGB RULE
* `LOCAL` Names assigned in any way within function and not declared global in that function.
* `Enclosing ` Names in a local scope of any and all enclosing functions (def or lambda), from inner our outer.
* `Global` Names assigned at the top level of a module file, or declared global in a def within the file.
* `Built In` Names preassigned in the built in names module : open, range, SyntaxError

* **Change the global variable inside a function**
Use `global` keyword to fetch the global variable inside the function and update it.
```
def changeX():
    global x
    x = 200
    print('changed')

changeX()
print(x)  # The changeX Function won't change the value of a global X Unless `global` Keyword is useds

```

Using the `global` keyword you can reach out to a global namespace and your local assignment can do affect.
