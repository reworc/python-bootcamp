# Python Bootcamp: Data Structures

<!-- omit in toc -->
## Table of Contents

1. [Overview](#overview)
2. [Sets](#sets)
3. [Queue](#queue)
4. [PriorityQueue](#priorityqueue)

## Overview

| Name           | Description                               | Example                                                            |
| -------------- | ----------------------------------------- | ------------------------------------------------------------------ |
| __Tuple__      | *immutable* data container                | `t = ( 1,2,3 )`                                                    |
| __List__       | ordered list of elements                  | `list = [ 1,2,3 ]`                                                 |
| __Dictionary__ | assignment: value to *unique* key         | `dict = { "Berlin" : "BER", "Helsinki" : "HEL", "Saigon" : "SG" }` |
| __Set__        | unordered collection of *unique* elements | `set = { 1, 2, 3}`                                                 |
| __Queue__      | automatic output of elements              | `q = queue.Queue()`                                                |
| __PriorityQueue__ | automatically sorted queue             | `q = queue.PriorityQueue()`                                        |

## Sets

* define empty set: `set = set()`
* add elements: `set.add(element)`
* optimized for quick lookup of elements (esp. `if elem in set`)

``` Python
  s = { 1, 7, 5, 9 }
  print(s)              # {1, 5, 9, 7}

  s.add(5)  
  print(s)              # {1, 5, 9, 7}

  text = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
  words = set()
  for word in text.split(" "):
      words.add(word)
      
  print(words)
  # {'tempor', 'takimata', 'eirmod', 'sea', 'amet,', 'voluptua.', 'sit', 'magna', 'clita', 'justo', 'erat,', 'diam', 'Stet', 'ipsum', 'ea', 'vero', 'dolores', 'consetetur', 'duo', 'accusam', 'kasd', 'est', 'amet.', 'no', 'dolor', 'At', 'invidunt', 'dolore', 'aliquyam', 'eos', 'et', 'sanctus', 'sadipscing', 'ut', 'sed', 'Lorem', 'labore', 'elitr,', 'gubergren,', 'nonumy', 'rebum.'}
  print(len(words))
  # 41
```

**[⬆ back to top](#table-of-contents)**
___

## Queue

* [Reference](https://docs.python.org/3/library/queue.html)
* add Elements (at the end): `q.put(elem)`
* remove (from the beginning): `elem = q.get()`

```Python
  import queue
  q = queue.Queue()

  q.put("Hallo")
  q.put("Welt")
  q.put("Hallo")
  q.put("Mars")
  q.put("Pluto")

  while not q.empty():
    print(q.get())

  # Hallo
  # Welt
  # Hallo
  # Mars
  # Pluto
```

**[⬆ back to top](#table-of-contents)**
___

## PriorityQueue

* [Reference](https://docs.python.org/3/library/queue.html#queue.PriorityQueue)
* add Elements (at the end): `q.put((priority, elem))`
* remove (from the beginning): `elem = q.get()` ordered by the priority ascending (__lowest priority is returned first!__)

```Python
  import queue

  text = "A A A A A B B B C C C C C D D D D D D D D E E E E E E E"
  d = {}
  # generate dictionary with word entries, counting the occurrences of an element  
  for word in text.split(" "):
      if word in d:
          d[word] = d[word] + 1
      else:
          d[word] = 1
          
  # for getting the sorted number of occurrences: put into priority queue . get the occurrence descending: simply negate count (priority queue does not order by the absolute value)
  pq = queue.PriorityQueue()
  for word, prio in d.items():
      pq.put((-prio, word))
      
  # retrieve elements ordered
  while not pq.empty():
      print(pq.get())
```

**[⬆ back to top](#table-of-contents)**
___
