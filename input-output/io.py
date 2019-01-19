file = open('file.txt')
print(file.read())
file.seek(0)
print(file.read())
file.seek(0);

print(file.readlines())
file.close()

# No Need to close the file
with open('file.txt') as myNewFile:
    contents = myNewFile.read()
    print(contents)

with open('file.txt', mode='a') as myFileWrite:
    myFileWrite.write('Hello from python\n')

