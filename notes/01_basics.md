# Python Bootcamp: Basics

## Base Data structures and Syntax

* define variable: `a = 2+3`
* strings +  number:  
  `print("my age is: " + 22)`  
  throws an error - number needs to be converted first using `str()`:  
  `print("my age is: " + str(22))`
* define list: `students = [ "Max", "Monika", "Erik", "Franziska" ]`
* `print(students)` outputs ['Max', 'Monika', 'Erik', 'Franziska']
* lists can contain mixed types: `mixed = ["Max", 1]`
* list length: `len(mixed)` (returns 2)
* `pop()` removes last element from the list (and returns the last element itself)
* `join()` insert strings as separators in lists: `(" & ").join(["Max", "Moritz", "Hexe"])` --> `Max & Moritz & Hexe`
* `split() `: split string at separator string : `"Max & Moritz & Hexe".split(" & ")` --> ["Max", "Moritz", "Hexe"]

## Conversions

* `str()`: converts to string
* `int()`: converts to integer
* `float`: converts to float
* `bool()`: converts to bool
  
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

## Loops

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

