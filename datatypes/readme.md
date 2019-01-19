## Variables
A name that represent the data.
* Cannot start with number
* No Spaces between
* '":,<>/?!~-+ etc can't be used 



* Better if your var name is in lowercase
* Avoid keywords (reserved words that have special meaning in python) should not be used.

#### Python is dynamic Typing
* This means that you can reassign variables to different data types in runtime.
```
myDoc=2; // int
myDoc=['ram','shyam'] // 
```



## Python Datatypes

Check the data types of any variable with `type` function 
```
a=10
type(a) // <class 'int'>
print(type(a) == int) // true

```

### Strings (str)
* Sequence of characters in 'single' or "double" quote.
* They are ordered sequences which can be used for indexing or slicing to grab sub-sections.
```
myStr = 'hello'
print(myStr[0]) // h

len('hello')//5
```
* use `\n` for new line `\t` for tab.
* Also supports reverse indexing.
```
//Supports reverse indexing.
myStr = 'hello'
print(myStr[-1])

myVar='my cat'
print(myVar[3:])//cat
print(myVar[:1])//my

print(myVar[3:4])//ca

print(myVar[::]) // print all string
print(myVar[::2])//print all string jumping every 2nd char.

print(myVar[::-1])//tac ym (reverse your string)
```
* String is immutable. You cannot change a part of a string.
```
name='Sam'
name[0]='P'// would result TypeError

newName=name[1:];
newName='P'+newName;//Pam
```

* String supports multiplication
```
print('hello world '*10)
```
* **String Functions**
```
x='Hello World'
x.upper()
x.lower()
x.split() //splic the string in to array based on whitespace or by the string that is passed.
```

* **Formatting strings**
```
print('I am {} years old'.format(10))
print('My name is {} {}'.format('Selvesan','Malakar'))
print('Then {2} {1} {0}'.format('fox','brown','quick')) // this is quick brown fox
print('Then {q} {b} {f}'.format(f='fox',b='brown',q='quick')) // this is quick brown fox
```
* Float formatting follows "{value:width.precision f}"
```
result = 100 / 777
print(result)  # 0.1287001287001287
print('The result is {r:1.3f}'.format(r=result))  # The result is 0.129
```
* String literals
```
name = 'Jose'
age=3
print(f'Hello my name is {name}. I am {age} years old')
```

### Integers (int)


#### Floating Points (float)



#### Lists (list)
Ordered sequence of objects [10,'hello',200]

#### Dictionaries (dict)
Unordered Key:Value pairs {"myKey":"value","name":"Frankie"}


#### Tuples (tup)
Ordered immutable sequence of object (10,'hello',200.3)


#### Sets (set)
Unordered collection of unique objects {"a":"b"}


#### Booleans (bool)
Logical Value indicating `TRUE` or `FALSE`