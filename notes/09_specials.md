# Python Bootcamp: Specials

<!-- omit in toc -->
## Table of Contents

1. [Optional Parameters](#optional-parameters)
2. [Variable Parameters](#variable-parameters)
3. [Value types and References in Python](#value-types-and-references-in-python)
4. [Regular Expressions](#regular-expressions)
5. [Dates in Python](#dates-in-python)
6. [Time Delta](#time-delta)
7. [Lambda Functions](#lambda-functions)
8. [Sorting](#sorting)
9. [Format Strings](#format-strings)

## Optional Parameters

* parameters can be made optional by specifying a default value:  
  `def multi_print(number = 3, word = "Hello"):`
* different from other programming languages, every single optional parameter can be set!
* this is done by using the name in the function call:

  ``` Python
    def multi_print(number = 3, word = "Hello"):
      for i in range(0, number):
          print(word)
    
    multi_print(word = "World")     # prints 3x "World"
    # World
    # World
    # World        
  ```

**[⬆ back to top](#table-of-contents)**
___

## Variable Parameters

* use case 1: provide a list of function parameters and specify, that elements should be used as parameters in their order in the list

  ``` Python
    def f(a,b,c):
      print(a)
      print(b)
      print(c)
    
    l = [1,2,3]

    f(*l)     # equivalent to: f(l[0], l[1], l[2])
              # throws an error, if len(l) != 3 !
  ```

* use case 2: provide an unspecified number of arguments:

```Python
  def calculate_max(*params):       
    result = params[0]
    for p in params:
        if p > result: 
            result = p
    
    return result
         
    calculate_max(1,2,3,4)
    # 4
```

* Parameters as Dictionary:
  
``` Python
  def f(**args):
      print(args)
    
  f(key="value", key2="value2")
  # {'key': 'value', 'key2': 'value2'}

  def g(key, param2):
      print(key)
      print(param2)
    
  d = {"key" : "Ich in der Schlüssel", "param2" : "Ich bin der Parameter" }

  g(**d)                            # equivalent to: g(key=d["key"], param2=d["param2"])
```

* use case: pass style parameters as dictionary:

``` Python

    %matplotlib inline
    import matplotlib.pyplot as plt

    def create_plot(**plot_params):
        # calculate something ...        
        plt.plot([1,2,3], [5,6,5], **plot_params)         # plt.plot([1,2,3], [5,6,5], color= "r", linewidth=5, linestyle="dashed")
        plt.show()
            
    create_plot(color="r", linewidth=5, linestyle="dashed")
    # alternative:
    # plot_cfg = { "color" : "r", "linewidth" : 5, "linestyle" : "dashed" }
    # create_plot(**plot_cfg)
```

**[⬆ back to top](#table-of-contents)**
___

## Value types and References in Python

* primitive type: numbers, strings, booleans, tuples
* primitive types are value types when passed as function parameters
* data structures and objects are reference types and are passed as reference

**[⬆ back to top](#table-of-contents)**
___

## Regular Expressions

* [Test regular expressions with __pythex__ online tool](https://pythex.org/)
* [RegExr Tool with explanation of regex-syntax](https://regexr.com)
* use `re` package to work with regular expressions: `import re`

``` Python
  import re
  sentence = "Ich habe 30 Hunde, die jeweils 4 Liter Wasser brauchen und 2 kg Nahrung"

  re.findall("[0-9]+", sentence)
  # ['30', '4', '2']

  re.search("[0-9]+", sentence)           # returns the first match with exact position
  # <re.Match object; span=(9, 11), match='30'>
```

* Examples:
  * `der?` find "de and "der" (r = optional)
  * `der*` find "de and "der", "derr", ... (r = optional and with arbitrary count) (count r = [0..n])
  * `der+` find "der", "derr", ... (r = with arbitrary count) (count r = [1..n])
  * `[0123456789]` or `[0-9]` - grouping (any of the symbols given)
  * `[0-9]+` find a group of characters with minimum one occurrences of number , but with as many as possible numbers following:  
    `re.search("[0,9]", "123")` returns `1`  
    `re.search("[0,9]+", "123")` returns `123`

**[⬆ back to top](#table-of-contents)**
___

## Dates in Python

### datetime

``` Python
  from datetime import datetime

  now = datetime.now()
  print(now)                          # 2021-05-18 18:42:55.996775

  day = datetime(2017,8,20,20,0,0)
  print(day)                          # 2017-08-20 20:00:00

  print(day.year)                     # 2017
  print(day.month)                    # 8
  print(day.day)                      # 20
  print(day.hour)                     # 20
  print(day.minute)                   # 0
  print(day.second)                   # 0

  print(day.date())                   # 2017-08-20
  print(day.time())                   # 20:00:00

  print(day.timestamp())              # 1503252000.0

  print(datetime.now() - day)         # 1366 days, 22:48:16.923331
```

### time and date

``` Python
  from datetime import date, time

  d = date(2017,8,21)
  print(d)                            # 2017-08-21
  t = time (20,15,32)
  print(t)                            # 20:15:32

  print(date(2017, 8, 20) < date(2017, 9, 15)) # True

  print(dt = datetime.combine(d,t))   # 2017-08-21 20:15:32
```

### format and parse dates

* `datetime.now().strftime("%d.%m.%Y")` --> 18.05.2021
* `datetime.now().strftime("%A, %dth of %B")` --> Tuesday, 18th of May
* [Format Codes](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)
* convert from string:

``` Python
  d = "18.05.2021"
  dt = datetime.strptime(d, "%d.%m.%Y")
  print(dt)                             # 2021-05-18 00:00:00
```

**[⬆ back to top](#table-of-contents)**
___

## Time Delta

``` Python
  from datetime import datetime, timedelta

  now = datetime.now()                    # 2021-05-18 19:06:57.732681
  
  delta = timedelta(days = 20)
  print(now + delta)                      # 2021-06-07 19:06:57.732681

  delta = timedelta(days =20, hours = 4, minutes = 3, seconds = 1)
  print(now + delta)                      # 2021-06-07 23:09:58.732681

  day = datetime(2017,8,20,20,0,0)
  delta = datetime.now() - day            

  print(delta)                            # 1366 days, 23:11:23.861662
  print(delta.days)                       # 1366
  print(delta.seconds)                    # 83483
  print(delta.total_seconds())            # 118105883.861662
```

**[⬆ back to top](#table-of-contents)**
___

## Lambda Functions

* syntax: `lambda argument: expr`
* lambdas must be in a single line

```Python
  students = [
    ("Max", 3),
    ("Monika", 2),
    ("Erik", 3),
    ("Franziska", 1)
]

students.sort(key = lambda student: student[1])

print(students)
# [('Franziska', 1), ('Monika', 2), ('Max', 3), ('Erik', 3)]

# equivalent to:
def students_sort_by_term(tpl_student):
    return tpl_student[1]

students.sort(key = students_sort_by_term)
```

* lambdas can be called like functions:
  
  ```Python
    max = lambda a,b: a if (a > b) else b
    max(3,4)                                  # returns 4
  ```

**[⬆ back to top](#table-of-contents)**
___

## Sorting

* `list.sort()` - sorts list ascending
* `list.sort(reverse = True)` - sorts in revers order (descending)
* custom sort function:
  
``` Python
  # sort by length of str
  def custom_sort(item):
      return len(item)
  
  l = ["Max", "Monika", "Erik", "Franziska" ]
  l.sort(key = custom_sort)
  # l.sort(key = len)       # equivalent to line before

  # ['Max', 'Erik', 'Monika', 'Franziska']
```

* sorting Dictionaries:
* `sorted(d)` returns keys in sorted order
* in general: `sorted()` returns a copy of with sorted values, `list.sort()` applies an in place sort (albeit, changing the indices) !
* key-function and reverse parameters are also possible

**[⬆ back to top](#table-of-contents)**
___

## Format Strings

**[⬆ back to top](#table-of-contents)**
___
