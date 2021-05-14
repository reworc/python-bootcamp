# Python Bootcamp: Lists

<!-- omit in toc -->
## Table of Contents

1. [Basics](#basics)
2. [List Comprehensions](#list-comprehensions)
3. [Tuple](#tuple)
4. [Dictionaries](#dictionaries)

## Basics

* define list: `students = [ "Max", "Monika", "Erik", "Franziska" ]`
* `print(students)` outputs ['Max', 'Monika', 'Erik', 'Franziska']
* lists can contain mixed types: `mixed = ["Max", 1]`
* list length: `len(mixed)` (returns 2)
* concatenate lists using `+` operator = `full = [1, 2] + [3, 4, 5]`
* remove item at specific index: `del list[idx]`
* remove specific item (only first occurrence!): `list.remove(value)`
* `pop()` removes last element from the list (and returns the last element itself)
* `join()` insert strings as separators in lists: `(" & ").join(["Max", "Moritz", "Hexe"])` --> `Max & Moritz & Hexe`
* `sum()`: sum elements of a list
* __List-Slicing__: `first_elements = students[0:2]` return the first two elements (start-idx: 0, last-index: 2 (exclusive))
  * Examples:

  ```Python
    numbers = [1,1,2,3,4,5,5,7]
    part = numbers[2:5]             # [2, 3, 4]
    
    part = numbers[5: -1]           # [5, 5]
    
    part = numbers[-3: -1]          # [5, 5]
    
    part = numbers[: -1]            # [1, 1, 2, 3, 4, 5, 5]
    
    part = numbers[5:]              # [5, 5, 7] 
  ```

* negative index: get element from the end of the list:
  
  ```Python
    students = ["Max", "Monika", "Erik", "Franziska"]
    print(students[-1])
    # Franziska

  ```

**[⬆ back to top](#table-of-contents)**
___

## List Comprehensions

* creates a new list with converted values:
  `y = [v * v for v in x]` - creates a list containing the square of each element in x
* examples:

```Python
    xs = [1,2,3,4,5,6,7,8]
    ys = [v * v for v in xs]                # [1, 4, 9, 16, 25, 36, 49, 64]

    def transform(x):
    return x + 2

    ys2 = [transform(v) for v in xs]        # [3, 4, 5, 6, 7, 8, 9, 10]

    students = ["Max", "Monika", "Erik", "Franziska"]
    numbers = [len(v) for v in students]    # [3, 6, 4, 9]

    xs2 = [x / 10 for x in range(0,100)]    # [0.0, 0.1, .., 9.9]
    ys3 = [v * v for v in xs2]              # [0.0, 0.01, .., 98.01]

```

**[⬆ back to top](#table-of-contents)**
___

## Tuple

* Define dictionary: `tpl = (1, 2, 3)`
* (read) access elements: `data = tpl[idx]`
* difference to list: tuples are __immutable__:
  * content can't be changed
  * cannot add elements
* use tuples to return multiple / combined values in functions
* unpack elements in tuple:

  ```Python
    student = ("Max Müller", 22, "Informatik")
    
    name, age, subject = student    # --> equivalent to:
                                    # name = student[0]
                                    # age = student[1]
                                    # subject = student[2]

    # directly unpack in for loop:
    students = [
        ("Max Müller", 22),
        ("Monika Mustermann", 22)
    ]

    for name, age in students:
        print(name + " : " + str(age))

  ```

**[⬆ back to top](#table-of-contents)**
___

## Dictionaries

* Define dictionary: `dict = { "Key" : "Value", .. }`
* add element: `dict["newKey"] = "value"`
* access value: `dict["Key"]` or `d.get("Saigon")` (get() does not throw an error, if key does not exist !)
* remove value: `del d["Key"]`
* check if value is in dictionary: `if "Key" in dict):`
* duplicate keys are automatically replaced:
  `error = {1 : "Dresden", 1: "Berlin", 3: "Leipzig"}` --> `{1: 'Berlin', 3: 'Leipzig'}`
* access all elements as tuples with `d.items()`
  
  ``` Python
    for key in d:
        value = d[key]
        print(key + " : " + value)

    # better use with Tuples:
    for key, value in d.items():
        print(key + " : " + value)

  ```

**[⬆ back to top](#table-of-contents)**
___
