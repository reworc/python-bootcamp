# Python Bootcamp: DataScience

<!-- omit in toc -->
## Table of Contents

1. [Tools Overview](#tools-overview)
2. [Numpy Basics](#numpy-basics)
3. [Numpy Filtering](#numpy-filtering)
4. [Numpy - multidimensional arrays](#numpy-multidimensional-arrays)
5. [References](#references)

## Tools Overview

* __NumPy__: filter / sort arrays/matrices, execute function on data
* __MatPlotLib__: create diagrams / plots
* __Pandas__: load / save Excel/CSV files, working with table-organized data
* __SymPy__: working with mathematic formulas
* __scikit learn__: machine learning on data
* __PyTables__: work with large scale table data
* __Apache spark__: large-scale data computation on clusters

**[⬆ back to top](#table-of-contents)**
___

## Numpy Basics

``` python

    # vanilla python:
    xs = []
    for x in range (0,10):
        xs.append(x)
    
    ys = []
    for x in xs:
        ys.append(x ** 2)

    # with numpy:
    import numpy as np

    xs = np.arange(10)          # creates array of number 0..9
    ys = xs ** 2                # creates list with x^2 values

```

* `arange(n)`: creates list with *n* values, starting with 0

``` python

    xs = np.arange(10)          # [ 0, 1, .., 9 ]
    xs = np.arange(10) + 3      # [ 3, 4, .., 12 ] 
    xs = np.arange(10) * 3      # [ 0, 3, .., 27 ]
    xs = np.arange(10) ** 2     # [ 0, 1, .., 81 ]
```

* `array(list)`: converts *list* into numpy array
* `zeros(num)`: creates array with *num* zero values
* `array.mean()`: compute mean value of *array*
* `array.min()`: compute min value of *array*
* `array.max()`: compute max value of *array*
* `array.std()`: compute standard deviation value of *array*

**[⬆ back to top](#table-of-contents)**
___

## Numpy Filtering

``` python
    a = np.array([1,2,3,4])
    b = np.array([False, True, True, False])

    a[b]                        # filter a with values of b = [2, 3]
    a >=3                       # returns array with given predicate: [ False, False, True, True ]
    a[a >= 3]                   # [3, 4]

```

**[⬆ back to top](#table-of-contents)**
___

## Numpy - multidimensional arrays

``` python
    a = np.arange(8) + 1                # a = [ 1, 2, ..., 8 ]
    reshaped = a.reshape(2,4)           # 4 columns, 2 rows:  reshaped = [ [1, 2, 3, 4] [5,6,7,8] ]
    reshaped = a.reshape[-1,4]          # 4 columns, fit rows   

    b = np.array([[1,2,3], [4,5,6]])    # creates 2-dim array
    c1 = b.reshape(-1)                  # reduce to 1 dim: c1 = [ 1, 2, ..., 6 ]
```

* __Remarks__:
  * only one dimension can be undefined (`reshape(-1, -1) does not work!`)
  * reshape can only work on "filled" data:
    * `np.array([1,2,3,4,5]).reshape(2,3)` does not work
    * `np.array([1,2,3,4,5]).reshape(4)` does not work
* `shape`: returns tuple containing array dimensions:

``` python
    b = np.array([[1,2,3], [4,5,6]])    # creates 2-dim array
    b.shape                             # returns (2,3)

```


**[⬆ back to top](#table-of-contents)**
___

## References

[Wikibook: LaTeX Math](https://en.wikibooks.org/wiki/LaTeX/Mathematics)  
[List of LaTeX math symbols](http://oeis.org/wiki/List_of_LaTeX_mathematical_symbols)  
[IPyWidgets Documentation - List of Widgets](https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html#Complete-list)

**[⬆ back to top](#table-of-contents)**
___
