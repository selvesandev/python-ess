## Input And Output with Basic Text File.


* Open file with `myFile=open('file')`
* Read from file.
```
file = open('file.txt')
print(file.read())
print(file.read()) // This line won't print anything since the cursor is pointed at the end of the file
```

* `file.seek(0)` to change the position of the cursor.

```
file = open('file.txt')
print(file.read())
file.seek(0) // re positioning the cursor position to 0 
print(file.read())
```
* Get each line separately on a list type `print(file.readlines())`

* **FILE LOCATION**

`WINDOWS`   >   `open("C:\\Users\\UserName\\Folder\file.txt")`


`MAC/LIN`   >   `open("/users/username/folder/file.txt")`


* Close the file with`myFile.close()` **Hey python is still using this file**   


* **SHORT HAND METHOD**
```
# No Need to close the file
with open('file.txt') as myNewFile:
    contents = myNewFile.read()
    print(contents)
```


* Write to file. `default mode is r (read)`
```
with open('file.txt', mode='w') as myFileWrite:
    myFileWrite.read() # You canot read from the file while the mode is w

```
* **modes**
```
mode=r      is read only
mode=w      is write only (will overwrite files or create new)
mode=a      append only
mode=r+     reading and writing
mode=w+     writing and reading (overwrites existing files or creates new one.)
```

* Append
```
with open('file.txt', mode='a') as myFileWrite:
    myFileWrite.write('Hello from python\n')
```
