# Python Bootcamp: Specials

<!-- omit in toc -->
## Table of Contents

1. [Optional Parameters](#optional-parameters)
2. [Variable Parameters](#variable-parameters)
3. [Value types and References in Python](#value-types-and-references-in-python)
4. [Dates in Python](#dates-in-python)
5. [Time and Time Differences](#time-and-time-differences)
6. [Lambda Functions](#lambda-functions)
7. [Sorting](#sorting)
8. [Format Strings](#format-strings)

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

## Dates in Python

**[⬆ back to top](#table-of-contents)**
___

## Time and Time Differences

**[⬆ back to top](#table-of-contents)**
___

## Lambda Functions

**[⬆ back to top](#table-of-contents)**
___

## Sorting

**[⬆ back to top](#table-of-contents)**
___

## Format Strings

**[⬆ back to top](#table-of-contents)**
___
