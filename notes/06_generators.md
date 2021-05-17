# Python Bootcamp: Generators

<!-- omit in toc -->
## Table of Contents

1. [Generator concept](#generator-concept)

## Generator concept

* generate items on demand, especially when only a part of the data is used
* Example:

```Python
  # traditional approach:

  def gen_list():
    list = []
    for i in range(0,10):
        print("list: " + str(i))
        list.append(i)
    return list

  for elem in gen_list():
      print(elem)

  # list: 0
  # list: 1
  # list: 2
  # list: 3
  # list: 4
  # list: 5
  # list: 6
  # list: 7
  # list: 8
  # list: 9
  # 0
  # 1
  # 2
  # 3
  # 4
  # 5
  # 6
  # 7
  # 8
  # 9

  def gen_generator():
    for i in range(0,10):
        print("gen: " + str(i))
        yield i
        
  for elem in gen_generator():
      print(elem)

  # gen: 0
  # 0
  # gen: 1
  # 1
  # gen: 2
  # 2
  # gen: 3
  # 3
  # gen: 4
  # 4
  # gen: 5
  # 5
  # gen: 6
  # 6
  # gen: 7
  # 7
  # gen: 8
  # 8
  # gen: 9
  # 9
  
```

* yield in recursive calls : creates nested lists
  * flatten lists with list comprehension does not use the genarator --> use `()` instead of `[]`:
  
  ``` Python
    articles = (art for page in pages for art in page)    # flatten with generator support
    articles = [art for page in pages for art in page)]   # default list comprehension: ignores "inner" generator 
    
    for page in pages:
      for art in page: 
        ...                                               # also ignores inner generator 
  ```

**[⬆ back to top](#table-of-contents)**
___
