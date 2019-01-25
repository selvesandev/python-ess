# Errors and Exception Handling.

Currently if there is any type of error in your code, the entire script will stop. We
can use `Error Handling` to let the script continue with other code, even if there is an error.

* We use three keywords for this.

**try** This is the block of code attempted.

**except** If there is a the error in try block the except block will execute.

**finally** A Final block of code executed whether or not there is a error.
```
#This will generate a TypeError

def my_func(a, b):
    return a + b


my_func(2, '2')
print('Check') # This line is never going to execute
```

**With Exception Handling**
```
try:
    result = my_func(2, 2)
except:
    print('Error')
else:
    # Would get executed when the try block was successful.
    print(result)
    print('Function executed successfully')
    

```

**Error Types**
You will find more error types in python official doc.
```
try:
    f = open('test.txt', 'r')
    f.write('Write a test line')
except TypeError:
    print('The was a Type Error')
except OSError:
    print('hey you have an OS Error')
else:
    # Would get executed when the try block was successful.
    print('Written successfully')
finally:
    print('I always run..')
```

**Example 2**

```
def ask_for_int():
    try:
        result = int(input('Please provide num 1')) + int(input('Please provide num 2'))
    except ValueError:
        print('You should provide only number')
    else:
        print(f'The result is {result}')
    finally:
        print('Program completed')


ask_for_int()

```