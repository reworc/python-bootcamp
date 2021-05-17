# Python Bootcamp: Crawler Project

<!-- omit in toc -->
## Table of Contents

1. [Basics](#basics)
2. [Folders as modules](#folders-as-modules)
3. [Python Module Index](#python-module-index)

## Basics

* Required Modules:
  * [requests-Module](https://docs.python-requests.org/en/master/)
  * [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  
* usually need to be installed manually, but is included with anaconda
  * [url-lib](https://docs.python.org/3/library/urllib.html)
  
  ```Python
    import requests
    from bs4 import BeautifulSoup

    response = requests.get(url)        # crawl url

    doc = BeautifulSoup(response.text, "html.parser")     # convert response content to bs4 document (using default python html parser)

    for p in doc.find_all("p"):        # get all <p> elements as list
      print(p.attrs)                   # get attributes of element

    for card in doc.select(".card"):   # select card elements using given css selector 
      print(card.select_one(".emoji")).text # select single element in result set and extract text content

      # card contains 2 spans inside the heading: emoji + text - select second one
      title = card.select(".card-title span")[1].text

      # card contains single img tag - access src-attribute
      img = card.select_one("img").attrs["src"]


  ```

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
  
**[⬆ back to top](#table-of-contents)**
___
