myStr = 'Hello'
myList = []

for letter in myStr:
    myList.append(letter)

print(myList)

myListCom = [letter for letter in myStr]
print(myListCom)

myNewList = [num ** 2 for num in range(0, 10)]  # Square root of every number in a range
print(myNewList)

myNewList = [x for x in range(0, 11) if x % 2 == 0]
print(myNewList)

celcius = [0, 10, 20, 35.43]
fahrenheit = [(9 / 5) * temp + 32 for temp in celcius]
print(fahrenheit)

results = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
print(results)

myList = []
for x in [2, 4, 6]:
    for y in [1, 10, 20]:
        myList.append(x * y)

print(myList)

myList = [x * y for x in [2, 4, 6] for y in [1, 10, 100]]
print(myList)
