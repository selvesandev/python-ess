## Control Flow

### IF .. EL
```
    if some_condition:
        #execute
    elif other_codition:
        # do something    
    else:
        #do something else.    
```


### For Loops
**Iterate** over the object. eg: every single char in a string, over the item
in a list, every key in a dictionary etc.

```
    myList=[1,2,3,5,4]
    for itemName in myList:
        print(itemName)
```

```
for num in myListItems:
    if num % 2 == 0:
        print(f'EVEN {num}')
```

```
for letter in 'Hello world':
    print(letter)
```


```
myTupList = [(1, 2), (3, 4), (5, 6)]
for item in myTupList:
    print(item)

```



```
myTupList = [(1, 2), (3, 4), (5, 6)]
for (a,b) in myTupList:
    print(a)
```

```

myDict = {
    'k1': 1,
    'k2': 2,
    'k3': 3
}

print(myDict.items())  # Returns the dictionary items in tuple.
print(myDict.values()) # Returs only values in list
print('\n')
for key, value in myDict.items():
    print(key, value)
```

### While

```
while someBooleanCondition:
    # Execute.

//While my dog is still hungry keep feeding.
```


```
x = 0
while x <= 5:
    print(x)
    x += 1
else:
    print(f'While ended X {x} is not less than 5')

```

##### Break, Continue and Pass
* Break out of the current loop
* Goes to the top of the loop
* Pass does nothing.


You cannot use a empty loop so use pass.
```

x = [1, 2, 3]
for item in x:
    # Empty Loop
    pass
```

```
    for letter in 'Spring'
        if letter == 'a'
            continue
        print(letter)    
```


### Use full Operators.
##### Range function.
```
list(range(10)) # Generate a list 
```

```
for num in range(10):  # Will generate number from 0 to 9
    print(num) # 0,1,2,3....9
```

* From 3 to 9
```
for num in range(3, 10):  # Will generate number from 0 to 9
    print(num) #3,4,5,6..9
```

* From 0 to 10 escaping every second.
* From 3 to 9
```
for num in range(0, 10, 2):  # Will generate number from 0 to 9
    print(num) #0,2,4,6..10
```

##### Enumerate Function
```
indexCount = 0
word = 'letter'
for letter in word:
    print(word[indexCount])
    indexCount += 1
```

This can be made easy with enumerate
```
for item in enumerate(word):
    print(item) # item is now a tuple
    
for (key, item) in enumerate(word):
    print(item)    
```

##### Zip Function
Like the zipper in a jacket the zip function combine two or more list and pair up the items they match together.  

```
myL1 = [1, 2, 3]
myL2 = ['a', 'b', 'c']

print('\n')
print(list(zip(myL2, myL1)))
```

```
myL1 = [1, 2, 3]
myL2 = ['a', 'b', 'c']

for item in zip(myL1, myL2):
    print(item)  # Returns tuple combining the both List (1,'a') (2,'b')
```

* If the list items are uneven the zip function will zip together with the shortest list will ignore the rest.


##### Check if a item is in the list. (IN)

```
2 in [1,2,3] # True Boolean
```

```
'a' in 'a world' # True
```

```
'myKey' in {'myKey':345} # True
```


```
'myKey' in {'myKey':345} # True
```

```
d = {'a': 'apple'}

print('apple' in d) # False
```


##### More functions.
```
min([10,20,30])

max([10,20,30])

```
##### Random Lib
```
from random import shuffle,randint

myList = [1, 2, 3, 4, 5, 6, 7]
shuffle(myList) # Suffle in a inplace function show the variable value will permanently change.
print(myList)


print(randint(0, 100)) # Random Number
```

##### INPUT  FROM USER
```
myNum = int(input('Enter a number here.'))
print(myNum) # IS ALWAYS A STRING

```