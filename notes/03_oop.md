# Python Bootcamp: OOP

<!-- omit in toc -->
## Table of Contents

1. [Basics](#basics)
2. [List Comprehensions](#list-comprehensions)
3. [Tuple](#tuple)
4. [Dictionaries](#dictionaries)

## Basics

* define class:
  
  ```Python

    class Student():

    # constructor
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_name(self):
        print(self.firstname + " " + self.lastname)

    erik = new Student("Erik", "Mustermann")

    erik.get_name()
    # Erik Mustermann

  ```

**[⬆ back to top](#table-of-contents)**
___
