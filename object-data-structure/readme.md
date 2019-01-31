# Advanced object and data structure.


### Numbers
```
print(hex(12))

bin(128)

print(pow(2, 4))  # two to the power 4

print(pow(2, 4, 3))  # 2 to the power 4 modulus 3

print(round(3.8))

print(round(3.82827719, 2))

```

Also has a `Math` library if you want more match functions.


### Strings.

```
str = 'hello world'

print(str.capitalize())  # Hello world
print(str.upper())  # HELLO WORLD
print(str.lower())  # hello world
print(str.count('o'))  # How many 'o' are there in a string
print(str.find('o'))  # Find the first occurrence of 'o' in the string.

print(str.center(20, 'z'))  # center str between 'z' and the length should be 20

print('hello\thi'.expandtabs())  # tab

print('20'.isalnum())  # True
print('hello'.isalpha())  # True

print('checK'.islower())  # False
print('     '.isspace())  # True if all characters is a white space.
print('Check'.istitle())  # True
print('HELLO'.isupper())  # True
print('Hey'.endswith('y'))  # True  or you can (s[-1]=='y')
print('Hello'.split('e'))  # ['H', 'llo']
print('newmega'.partition('m'))  # ('new', 'm', 'ega') (head,split,food)

# Split and Partitions are regular expression 
```

### Sets.
```
s = {1, 2}
s.add(3) # Add Items to set
print(s)

------

s.clear() # remove all items in a set
print(s) 

--------
sc = s.copy() #  Creating a new copy
# Changing the value of copy won't effect the original


--------
diff = {1, 2, 3,4,5}.difference({1, 2, 3, 4})
print(diff) # 5

--------
s = {1, 2, 3}
s.difference_update({1, 4, 5})
print(s) # {2,3}


--------
s = {1, 2, 3, 4}
s.discard(2)
print(s)  # {1,3,4}  remove the element if it's a member


--------
s1 = {1, 2, 3}
s2 = {1, 2, 4}
print(s1.intersection(s2))  # {1,2}  # common to both of the set


--------
s1 = {1, 2, 3}
s2 = {1, 2, 4}
s1.intersection_update(s2)
print(s1) # updates s1 value with new set i.e the common between both 

--------
print({1, 2}.isdisjoint({3, 4})) # Returns true only if the set values does not match


--------
{1,2}.issubset({1,2,3}) # True


--------
# Returns the symmetric difference of two sets i.e the value which is on one of the set opposite of intersection
print({1, 2}.symmetric_difference({2, 4}))  # {1, 4}


--------
s1 = {1, 2, 3}
s2 = {1, 2, 4}
print(s1.union(s2))  # {1,2,3,4}



--------
s1 = {1, 2, 3}
s2 = {1, 2, 4}
s1.update(s2)
print(s1)  # {1,2,3,4}
```

### Dictionaries.
```
d = {
    'k1': 1,
    'k2': 2
}

xd = {x: x ** 2 for x in range(10)}
print(xd)

------

nxd = {k: v ** 2 for k, v in zip(['a', 'b', 'c'], range(3))}
print(nxd)

```

### Lists.
```
l = [1, 2, 3, 4, 5, 6, 7]
l.append(6) # append item to your list at last.

l.count() # count how many times a object occur in list
l.count(1) # what occurs how many times.

-----
l = [1, 2, 3, 4, 5, 6, 7]
l.append([2, 3]) # [1, 2, 3, 4, 5, 6, 7, [2, 3]]

l.extend([2, 3]) # [1, 2, 3, 4, 5, 6, 7, 2, 3]
# extend expects a iterable object.



l.index(2) # would return the index of whatever value is passed in it.
# will get error if the item is not in the list.


l.insert(2,'inserted') # put the object in the index supplied. takes two argument.
# inserted at 2 index 3rd place.

l.pop() # pop the last element and returns it and changes permanentry

l.pop(index) # pops from the given index

l.remove() # removes the first occurance of the value.
# removes only the first instance.

l.reverse() # reverse the list permanently

l.sort() # sorts the list.

```
