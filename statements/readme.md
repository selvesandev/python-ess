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
