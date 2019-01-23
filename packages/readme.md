
# Install a External Python Package.
```
pip install requests
pip install colorama
```

```
from colorama import Fore
print(Fore.RED+"some text here.")
```


### Writing your own module.
* Modules are just a `.py` scripts that you call in another `.py` script.
* Packages are collection of modules.


```
#module.py

def my_func():
    print('Hey I am a module')

``` 

```
#index.py

from module import my_func
my_func()

```

### Write your own package.
Create a `__init__.py` file in your package root directory. You don't need to write anything it is just there to let
python know that it's the root directory of your package.  
The `__init__.py` file and that tells python it's a directory which have bunch of modules in it which can be used with some syntax.

* **Package Directory Structure**
```
    mypack/__init__.py
    mypack/my_pack_script.py # You can have many more scripts here
    
    mypack/subpack/__init__.py
    mypack/subpack/my_sub_pack_script.py # You can have many more scripts here     
```
**You can call these packages by**
```
from mypack import my_pack_script
from mypack.subpack import my_sub_pack_script

my_pack_script.my_pack()
my_sub_pack_script.my_sub_pack()

```

**Or you can directly import a function**
```
from mypack.my_pack_script import my_pack
my_pack()
```

#### "__name__" and "__main__"
Often confusing part in python is a mysterious line of code:
```
if __name__ == "__main__":

```

* Sometimes when you are importing from a module, you would like to know whether a modules
function is being used as an import, of if you are using the original .py file of that module.

* In the background `__name__` variable is assigned `"__main__"` automatically if the file is running directory therefore you can
check it as shown below.

```
# one.py

# one.py

def one():
    print('The is a function in one.py')


if __name__ == "__main__":
    print('The File is running directory one.py')
else:
    print('The file is imported one.py')

```

```
#two.py

import one
one.one()
```

* This is generally done for better code management.