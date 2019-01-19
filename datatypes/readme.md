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
Ordered sequence of objects [10,'hello',200] that can hold a variety of object types.
* They use [] brackets and commas to separate object types.
* List support indexing and slicing just as string.
```
myList = [1, 2, 3]

myList2 = ['string', 100, 22.3]

```
* Use len() function to get the size of length.
* Use `myList[0]` to get the value from the list.
* You can add lists
```
print(myList2 + myList) // ['string', 100, 22.3, 1, 2, 3]

```
* Lists value can be overriden `myList[0]='newvalue'`
* Add value to the end of the list by `myList.append(6)` 
* Get and remove the last value from the list `myList.pop()`
* Pass the index position of the list to remove the value at desired position `myList.pop(2)`
* Order List by `myList.sort()` won't return anything.
* `myList.reverse()` for reverse sort.
* Just like in string we can perform indexing and slicing in the list `mylist[:2]`



#### Dictionaries (dict)
Unordered mapping of objects Key:Value pairs 
```
{
    "myKey":"value",
    "name":"Frankie"
}
```
They cannot be sorted.


#### Tuples (tup)
Ordered immutable sequence of object (10,'hello',200.3)


#### Sets (set)
Unordered collection of unique objects {"a":"b"}


#### Booleans (bool)
Logical Value indicating `TRUE` or `FALSE`


#### None
