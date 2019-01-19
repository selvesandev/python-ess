mySet = set()
mySet.add(1)
mySet.add('hello')
mySet.add('hello')  # won't repeat it can't add hello again

print(mySet) #{1, 'hello'}

myList = [1, 2, 2, 3, 4, 5, 1, 1, 1, 3, 4, 5]
print(set(myList)) # {1, 2, 3, 4, 5}
