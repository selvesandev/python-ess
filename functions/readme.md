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