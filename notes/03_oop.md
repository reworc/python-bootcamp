# Python Bootcamp: OOP

<!-- omit in toc -->
## Table of Contents

1. [Basics](#basics)
2. [Inheritance](#inheritance)

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

## Special methods

* constructor: `__init__`
* toString: `__str__`
* string representation of object in console (not via str()) : `__repr__`
* overwrite `len()` for object: ``__len__`

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
