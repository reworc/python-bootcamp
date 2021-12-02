# Python Bootcamp: DataScience

<!-- omit in toc -->
## Table of Contents

1. [Tools Overview](#tools-overview)
2. [Numpy Basics](#numpy-basics)
3. [Numpy Filtering](#numpy-filtering)
4. [Numpy - multidimensional arrays](#numpy-multidimensional-arrays)
5. [Pandas - Basics](#pandas-basics)
6. [Pandas - Excel and Plotting](#pandas-excel-and-plotting)
7. [References](#references)

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

## Pandas - Basics

``` python
   df = pd.read_csv("data.csv")         # read csv into data frame

   df["Name"]                           # return all values on column "Name"
   first = df.iloc[0]                   # returns first row (as Pandas.Series)

   first["Name"]                        # returns value of column Name in first row 

   df.iloc[-10:]                        # list slicing: returns the last 10 elements

   for row in df.iterrows():            # iterates through rows, 
                                        # row is tuple of index and row content
       pos, d = row                     # unpacking tuple into pos and d
   # for pos, d in df.iterrows():       # alternative notation: unpack directly in for loop

   filtered = df[df["Year"] < 1990]     # filter data frame by Year > 1990 (returns copy)

   # filter all null, NaN values in column "Missing"
   deaths = df[df["Missing"].isnull() == False]

    # combine filters syntax
   combined = df[(df["col1"] > x) & (df["col2"] == False)] 

    # sort data frame by column values descending
    df.sort_values("col", ascending=False)
```

* __Remarks__:
  * Pandas assumes, that the first row in the csv contains the column names
  * by default, the delimiter for csv is `,` - this can be changed by specifying the parameter delimiter in `read_csv` function, e.g.: `pd.read_csv("data.csv", delimiter=';')`
  * instead of combining filters, they can also applied subsequently (in case of and)

**[⬆ back to top](#table-of-contents)**
___

## Pandas - Excel and Plotting

``` python
    %matplotlib inline
    import matplotlib.pyplot as plt

    excel_df = pd.read_excel("data/data.xlsx")          # load excel sheet

    year = excel_df["Year"]
    sales = excel_df["Sales"]

    plt.plot(year, sales)
    plt.show()
```

**[⬆ back to top](#table-of-contents)**
___

## References

[Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/index.html)  
[Pandas - Read Excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html)  

**[⬆ back to top](#table-of-contents)**
___
