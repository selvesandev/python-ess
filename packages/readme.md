
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
