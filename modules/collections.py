from collections import Counter

cnt = [1, 2, 3, 1, 1, 3, 4, 5, 6, 7, 8, 6, 7, 7]
print(Counter(cnt))

sent = 'ssslllmmmeeee'
print(Counter(sent))

s = 'hey this is repeating hey hey is'
c = Counter(s.split())
print(c.most_common())
