import re

patterns = ['term1', 'term2']

text = 'this is a string with term1'

search = re.search('term1', text)
if (search):
    print('match was found')

print(search.start())
print(search.end())
