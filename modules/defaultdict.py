from collections import defaultdict

d = {'k1': 1}

d = defaultdict(object, d)
print(d['k2'])

print(d)

# d = defaultdict(lambda: 0)
# print(d['one'])
