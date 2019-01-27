# Build In Modules.


## collection

### Counter
```
from collections import Counter
```
* Counter counts the number of repeatation in a list and returns a Dictionary.
```
from collections import Counter

cnt = [1, 2, 3, 1, 1, 3, 4, 5, 6, 7, 8, 6, 7, 7]
print(Counter(cnt))

# Counter({1: 3, 7: 3, 3: 2, 6: 2, 2: 1, 4: 1, 5: 1, 8: 1})
```
* Or number of repeating character in a string

```
sent = 'ssslllmmmeeee'
print(Counter(sent))
# Counter({'e': 4, 's': 3, 'l': 3, 'm': 3})

```

* Or Words in a sentence.
```
s = 'hey this is repeating hey hey is'
print(Counter(s.split()))

```

**NOTE** You can also called methods in the counter returned values.
```
s = 'hey this is repeating hey hey is'
c = Counter(s.split())
print(c.most_common())

# [('hey', 3), ('is', 2), ('this', 1), ('repeating', 1)]

```

### defaultdict
Is a dictionary that provides all the methods that come from dictionary and also takes
the first argument as default data type for the dictionary.
```
from collection import defaultdict
```
**A defaultdict will never raise a KeyError. Any key that does not exists gets the value returned by the default by the default factory.**
```
d = {'k1': 1}
print(d['k2'])
# This will result key error
```
* Now lets create a default dict.
```

d = {'k1': 1}
d = defaultdict(object, d)
print(d['k2']) # Key named k2 will be created and assigned a object the object is passed as the first argument.
print(d)
```

* Pass a lambda function in a `defaultdict` to receive the returned value always even if there is no assigned key.
```
d = defaultdict(lambda: 0)
print(d['one']) # print 0 since the 'one' is not defined.

```

### OrderedDict
An orderedDict is a dictionary sub class that remembers the order in with it contents are added.

The dictionary by default is a mappings and they did not retain any order as to how you added keys or values to it. But in `orderdict` 
you will retain the order.

* A normal Dictionary.



### namedtuple
```
t = (1, 2, 3)
print(t[0]) # 1
print(t[1)) # 2
```
A named tuple assigns a name as well as numerical index to each member in the tuple.

A named tuple is like normal tuple it creates a basic object type and it allows name for the various fields. 

It is almost like creating a class very quickly by using the namedtuple factory function.


```
Dog = namedtuple('Dog', 'age breed name')
sammy = Dog(age=2, breed='german sh', name='tommy')
print(sammy) #Dog(age=2, breed='german sh', name='tommy')
print(sammy.name)  # 'tommy'

```
Or you can also use indexing.
```
print(sammy[2]) # tommy
```

* Namedtuples are very nice quick way to assign variables and field name to a situation where a normal tuple might get confusing or you might loose track.


## Datetime.
Helps to deal with timestamp in your code.
```
import datetime
```

## Python Debugger.
Known as `pdb` implements a interacting debugging in your python programing includes features to 
pause your program look at the values of variable and watch the execution step by step to understand what 
your program actually doing to find the bug in the logic.  
```
import pdb
x = [2, 3, 4]
y = 2
z = 3
result = y + z
print(result)
pdb.set_trace()
result2 = y + x
print(result2)
```
This opens a interacting debugger tool in the terminal of jetbrains where you can input to see your values.

## timeit.
