# Python Bootcamp: OOP

<!-- omit in toc -->
## Table of Contents

1. [Basics](#basics)
2. [Special methods](#special-methods)
3. [Inheritance](#inheritance)
4. [Type checking](#type-checking)
5. [Static variables](#static-variables)
6. [Naming Conventions](#naming-conventions)
7. [Type Annotations](#type-annotations)

## Basics

* define class:
  
  ```Python

    class Student():        
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname        
        self.__term = 1                # private variable
        
    def increase_term(self):
        if self.__term >= 9:
            return
        self.__term += 1
    
    def get_name(self):
        print(self.firstname + " " + self.lastname + "(" + str(self.get_term()) + ")")
        
    def get_term(self):
        return self.__term
    
    def __do_something(self):       # private method
        print("something private")

  ```

* private methods: everything that start with `__` is treated as private.
* private by convention, but not enforced by the language: variables that are starting with a single `_` should not be changed, but in fact this si not enforced by the language, just a developer hint !
* even floats are objects:

``` Python
  a = 12.5
  a.__add__(5) # return 17.5
```

**[⬆ back to top](#table-of-contents)**
___

## Special methods

* constructor: `__init__`
* toString: `__str__`
* string representation of object in console (not via str()) : `__repr__`
* overwrite `len()` for object: `__len__`
* `__dict__`: returns all properties with values of a python object

``` Python
  class Phonebook:
  
    def __init__(self):
        self.__entries = {}
        
    def add(self, name, phone_number):
        self.__entries[name] = phone_number
        
    def get(self, name):
        if name in self.__entries:
            return self.__entries[name]
        else:
            return None
        
    def __str__(self):
        return "Phonebook(" + str(self.__entries) + ")"
    
    def __repr__(self):
        return self.__str__()
    
    def __len__(self):
        return len(self.__entries)
```

**[⬆ back to top](#table-of-contents)**
___

## Inheritance

``` Python
  class Student():        
    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname
    
    def name(self):
        return self.firstname + " " + self.surname
    
  class WorkingStudent(Student):
    def __init__(self, firstname, surname, company):
        super().__init__(firstname, surname)
        self.company = company
        
    def name(self):
        return super().name() + " - " + self.company
```

**[⬆ back to top](#table-of-contents)**
___

## Type checking

``` Python
  w_student = WorkingStudent("Max", "Müller", "Fantastico GmbH")
  student = Student("Monika", "Mustermann")
```

* `type(obj)` returns exact type, e.g:  
 `type(w_student)` returns `WorkingStudent`  
 `type(student)` returns `Student`
* `isInstance(obj, type)` checks if obj is of specified type or any deriving type:
  `isinstance(w_student, WorkingStudent):`  returns `true`  
  `isinstance(w_student, Student):`  returns `true`

**[⬆ back to top](#table-of-contents)**
___

## Static variables

``` Python
  class Car:
    price = "expensive" # STATIC VARIABLE
        
    c1 = Car()        
    c2 = Car()

    print(c1.price)       # expensive  
    print(c2.price)       # expensive

    Car.price = "cheap"

    print(c1.price)       # cheap
    print(c2.price)       # cheap

    c1.price = "moderate" # !!! don't do this - creates a new instance variable overwriting the static variable 

    print(c1.price)       # moderate
    print(c2.price)       # cheap

    c3 = Car()
    print(c3.price)       # cheap

    Car.price = "mäh"
    print(c1.price)       # mäh
    print(c2.price)       # moderate
    print(c3.price)       # mäh
```

**[⬆ back to top](#table-of-contents)**
___

## Naming Conventions

* PascalCase(`AVeryLongName`)
* camelCase(`aVeryLongName`)  --> __not used in Python__
* sneak_case(`a_very_long_name`)

| Typ           | Case       | Example                              |
| ------------- | ---------- | ------------------------------------ |
| Class Name    | PascalCase | `class AVeryLongClassName`           |
| Variable Name | sneak_case | `a_very_long_variable_name = []`     |
| Method Name   | sneak_case | `def a_very_long_method_name(self):` |

**[⬆ back to top](#table-of-contents)**
___

## Type Annotations

``` Python
  from typing import Optional, Iterator                         # typings package

  class Example:

    # You can optionally declare instance variables in the class body
    attr: int
    # This is an instance variable with a default value
    charge_percent: int = 100

    # The "__init__" method doesn't return anything, so it gets return
    # type "None" just like any other method that doesn't return anything
    def __init__(self) -> None:
      ...

    # Decorator: static method
    # returns an array of Crawled articles, argument type is string
    @staticmethod                                                 
    def read_from_file(file_name: str) -> list[CrawledArticle]:   
        result = []
        ...
        return result

    # 'void' return type: None
    def write_to_file(self, file_name: str, num_articles: int) -> None:

    # generators return iterators
    def __fetch(doc: BeautifulSoup, page_url: str) -> Iterator[CrawledArticle]:

    # a method that may return None returns an Optional
    def __get_next_page_url(page_url: str, doc: BeautifulSoup) -> Optional[str]:
        ...
        if len(elem) == 1:
            return "..."
        else:
            return None


```

* Reference: [Python3 Type Annotations Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

**[⬆ back to top](#table-of-contents)**
___
