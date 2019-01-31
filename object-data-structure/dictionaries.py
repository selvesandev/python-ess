d = {
    'k1': 1,
    'k2': 2
}

xd = {x: x ** 2 for x in range(10)}
print(xd)

x = range(2)
print(x)

for i in range(10):
    print(i)

for k, v in zip(['a', 'b'], range(2)):
    pass
    # print(v)

nxd = {k: v ** 2 for k, v in zip(['a', 'b', 'c'], range(3))}
print(nxd)

