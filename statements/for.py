myListItems = [1, 2, 3, 3, 4, 5]

for myListItem in myListItems:
    print(myListItem)

print('\n')

for num in myListItems:
    if num % 2 == 0:
        print(f'EVEN {num}')

for letter in 'Hello world':
    print(letter)

myTupList = [(1, 2), (3, 2), (5, 6)]
for (a, b) in myTupList:
    print(a)
    print(b)

myDict = {
    'k1': 1,
    'k2': 2,
    'k3': 3
}

print(myDict.items())  # Returns the dictionary items in tuple.

print('\n')
for key, value in myDict.items():
    print(key, value)
