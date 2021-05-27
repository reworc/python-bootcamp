# Python Bootcamp: Basics

<!-- omit in toc -->
## Table of Contents

1. [Base Data structures and Syntax](#base-data-structures-and-syntax)
2. [Strings](#strings)
3. [Conversions](#conversions)
4. [Operators](#operators)
5. [Control structures](#control-structures)
6. [Functions](#functions)
7. [File Handling](#file-handling)

## Base Data structures and Syntax

* define variable: `a = 2+3`
* x ^ y: `x ** y`
* Comments:  
  `#` for single line comments
  `"""` for comment blocks
* strings + number:  
  `print("my age is: " + 22)`  
  throws an error - number needs to be converted first using `str()`:  
  `print("my age is: " + str(22))`

**[⬆ back to top](#table-of-contents)**
___

## Strings

* `split()`: split string at separator string : `"Max & Moritz & Hexe".split(" & ")` --> ["Max", "Moritz", "Hexe"]
* `strip()`: removes whitespace and control characters (e.g. `\n` from string)  
  it is also possible to specify additional characters that should be removed from start and end:

  ``` Python

    string ="____?Hallo._"

    print(string.strip("_ .?"))         # Hallo
                                        # removes "_", " ", "." and "?" from start/beginning
    print(string.lstrip("_ .?"))        # Hallo._ 
                                        # strip only on left side
    print(string.rstrip("_ .?"))        # ____?Hallo
                                        # strip only on right side
  ```

* `upper()`: converts string to uppercase
* `lower()`: converts string to lowercase
* `startswith()`, `endswith()`: starts / ends string with the given string ?
* contains: either use regular expressions or `"word" in string`:
  
  ``` Python
    sentence = "Ist das Wetter heute gut ?"
    print("das" in sentence)                  # True
    print("dat" in sentence)                  # False
  ```

* `find(search)`: find search in string  
  returns -1 if search was not found
* `replace(src,dst)` replace dst in string by src

**[⬆ back to top](#table-of-contents)**
___

## Conversions

* `str()`: converts to string
* `int()`: converts to integer
* `float`: converts to float
* `bool()`: converts to bool
* `complex()`: converts to a complex number
  
  ``` Python
    result = bool(0)        # False
    result = bool(1)        # True
    result = bool(2)        # True
    result = bool("")       # False !
    result = bool("a")      # True !
    result = bool("abc")    # True !
    result = bool()         # False
  ```

* __CAUTION:__ python does not automatically do type conversions:
  * `f = float("5") + int("6")` - works
  * `f = float("5") + int("6.5")` - does not work !
  * `f = float("5") + int(float("6.5"))` - works !
  * floats can be converted to ints and vice versa, but string parsing is rather tedious!

**[⬆ back to top](#table-of-contents)**
___

## Operators

### Equality

``` Python

  result = 5 == 5               # True
  n = "5"
  result = 5 == n               # False
  result = 5 == int(n)          # True
  result = 5 == float(n)        # True !
  result = 5 == 5.0             # True !
  result = str(5) == str(5.0)   # False
```

``` Python
  age = 35
  if age >= 30 and age < 40:
      print("age is between 30 and 40")
  
  if age < 30 or age > 40:
      print("age is not between 30 and 40")
```

* `in` checks if list contains a given element: 
  
  ``` Python
    students = ["Max", "Monika", "Erik", "Franziska"]
    print("Monika" in students) # prints "true"
  ```

  __Remark:__ works on strings, too : `"i" in "Monika"` returns `True`

* `not`: Equivalent to `!` Operators in oth languages - negates boolean Expressions
``

**[⬆ back to top](#table-of-contents)**
___

## Control structures

__important!__ code blocks rely on indents!

### if / else

``` Python
if n < 42:
    print("inside if")
    print("also inside if")`
print("outside if")
```

``` Python
  country = "US"
  age = 20

  if (country == "US" and age >= 21) or (country != "US" and age >= 18):
      print("darf Akohol trinken")
  else:
      print("darf keinen Alkohol trinken")
```

``` Python

  currency = "€"

  if currency == "$":
      print("US-Dollar")
  else:
      if currency == "¥":
          print("Yen")
      else:
          if currency == "€":
              print("Euro")
          else:
              print("invalid")
```

* no nested else with `elif`

``` Python

  currency = "€"

  if currency == "$":
      print("US-Dollar")
  elif currency == "¥":
      print("Yen")
  elif currency == "€":
      print("Euro")
  else:
    print("invalid")
```

* __Ternary operator:__
  
  ``` python
    # Syntax :
    # [on_true] if [expression] else [on_false]

    def maximum(a,b):
      return b if a < b else a 

    # equivalent to:
    def maximum_if_else(a, b):
      if a < b:
        return b
      else:
        return a
  ```

### Loops

* __while__: as long as a condition is satisfied
  
``` Python
  counter = 0

  while counter < 10:
      print(counter)      # prints 0..9
      counter += 1  

  print("counter after loop: " + str(counter))      # prints "counter after loop: 10"      
```

* __for__: for a given number of iterations

``` Python
  for counter in range(0,10):
      print(counter)      # prints 0..9      
      
  print("counter after loop: " + str(counter))      # prints "counter after loop: 9"
```

* __foreach__: for every element in a sequence

``` Python
  list = [1, 5, 6]
  for elem in list:
    print(elem)      # prints 1, 5, 6      
      
  print("elem after loop: " + str(elem))      # prints "elem after loop: 6"
```

* __CAUTION__ : foreach **copies** - within the loop you can not modify the element itself - you have to assign it via list index:

```Python
  i = 0
  for elem in list:    
    if elem == "value to be changed":
      elem = "new value"                    # only the copy is modified, the original is still in list
      list[i] = "new value"                 # change value at index (or use for in range(0, len(list)) - loop)
    i += 1
```

* Output only uneven numbers:

``` Python
  for i in range(0,10):
    if i % 2 == 0:
        continue
    print(i)
```

* break loop execution:

``` Python
  for i in range(0,10):
    if i == 5:
        break
    print(i)
```

**[⬆ back to top](#table-of-contents)**
___

## Functions

``` Python
  def multi_print(p1, p2, p3 = "Ende" ):
    print(str(p1))
    print(str(p2))
    print(str(p3))

  multi_print("Hallo Welt", 25)
    # Hallo Welt
    # 25
    # Ende
  multi_print("Hallo Welt", 25, "Stop")
    # Hallo Welt
    # 25
    # Stop
```

**[⬆ back to top](#table-of-contents)**
___

## File Handling

* `file = open("example.txt", "r")`: opens file example.txt for read access
* `file = open("example.txt", "w")`: opens file example.txt for write access (creates if not existing)
* `file = open("example.txt", "a")` appends data to opened file
* `file.close()`: close file after it is used
* __with__ Operator (cf. `using` in __C#__):
  * closes/releases resources when they get out of scope
  
  ``` Python

    with open("schreiben.txt", "r") as file:
      for line in file:
          str = line.strip()
          print(str)

    print(file) # throws error: file is already closed

  ```

**[⬆ back to top](#table-of-contents)**
___
