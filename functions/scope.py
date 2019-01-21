x = 10  # Global Scope


def printer():
    print(x)  # Will print 10


printer()

print(x)  # Prints 10


def changeX():
    global x
    x = 200
    print('changed')


changeX()
print(x)  # The changeX Function won't change the value of a global X Unless `global` Keyword is useds
