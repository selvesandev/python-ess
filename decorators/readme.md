# Decorators
Decorator allows you to `decorate` your function with some extra code.  
Python has `decorators` that allows you to tack on extra functionaliy to an already
existing function.  
They use the `@` operator and are then placed on the top of the original function.
```
    @some_decorator_func # This is a decorator that connects to some extra code.
    def my_func():
        //do some stuff 
        return something;
```

### Steps

* You define a function that takes function as a argument
```
# We will treat this function as a decorator.
def new_decorator(original_func):
```

* Now this function will have another function inside it. Inside which we will call the original funciton.
```
def new_decorator(original_func):
    def wrap_func():
        original_func()
```


* You can do things before and after calling the original function now.
```
def new_decorator(original_func):
    def wrap_func():
        print('Some extra code before the original function')
        original_func()
        print('Some extra code after the original function')

    return wrap_func;
```
* Finally return the inside function i.e `wrap_func`


* The above code done is our decorator which allows you to `decorate` our function which is passed to this function with some extra code.

* Now you can use the above decorator as
```
@new_decorator
def func_needs_decorator():
    print('I want to be decorated')

func_needs_decorator()
```
* By This way we are passing our function `func_needs_decorator` to the `new_decorator` function which is our decorator by using the decorator syntax `@new_decorator`

