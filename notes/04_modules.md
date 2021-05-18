# Python Bootcamp: Modules

<!-- omit in toc -->
## Table of Contents

1. [Basics](#basics)
2. [Folders as modules](#folders-as-modules)
3. [Python Module Index](#python-module-index)

## Basics

``` Python
# hallo.py

def welt(): 
    print("Hallo Welt")
    
def mars(): 
    print("Hallo Mars")
```

* other python scripts can simply be referenced by filename and imported: `import hallo` (loads script `hallo.py`)
* execute by `module.method` : `hallo.welt()` --> `"Hallo Welt"`

* import only specific functions:

``` Python
  from hallo import welt, mars
  welt() # "Hallo Welt"
```

* renaming: `import mathplotlib.pyplot as plt`

* print all variables and function of an imported module: `print(dir(mymodule))`

* __remark regarding Jupyter Notebooks__: imports are only executed once, if script changes, kernel needs to be restarted to reimport module

**[⬆ back to top](#table-of-contents)**
___

## Folders as modules

* place `__init__.py` inside folder: python recognizes folder content as module
* all other scripts can be imported like:
  
  ```Python

    # folder/__init__.py (empty file)

    # folder/file.py
    def f():
        ...

    # ./script.py
    from folder import file

    file.f()
  ```

* if __all__ scripts should be imported:

   ```Python

    # folder/__init__.py
    __all__ = ["file"]        # list with all script files in folder

    # folder/file.py
    def f():
        ...

    # ./script.py
    from folder import *

    file.f()
  ```

  __OR__

  ```Python

    # folder/__init__.py
    from . import file      # import file from current module

    # folder/file.py
    def f():
        ...

    # ./script.py
    import folder

    file.f()
  ```

**[⬆ back to top](#table-of-contents)**
___

## Python Module Index

* [List of included python modules](https://docs.python.org/3/py-modindex.html)
* online-documentation of available python modules for current python version
* find currently used python version:
  
  ```Python
  import sys
  print(sys.version)
  ```
