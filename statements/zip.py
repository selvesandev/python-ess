myL1 = [1, 2, 3]
myL2 = ['a', 'b', 'c']

for item in zip(myL1, myL2):
    print(item)  # Returns tuple combining the both List (1,'a') (2,'b')

print('\n')
print(list(zip(myL2, myL1)))
