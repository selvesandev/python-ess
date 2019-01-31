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
