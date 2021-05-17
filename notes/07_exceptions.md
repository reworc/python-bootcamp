# Python Bootcamp: Exceptions

<!-- omit in toc -->
## Table of Contents

1. [Exceptions in Python](#exceptions-in-python)

## Exceptions in Python

* Example:

  ```Python
    x = 0

    try:
        print(5/x)                        # throws ZeroDivisionError
    except ZeroDivisionError:
        print("Cannot divide by zero!")     


    file_name = "datei.xyz"

    try: 
        with open(file_name, "r") as file:  # thorws FileNotFoundError
            print(file)
    except FileNotFoundError:
        print(f'Could not open {file_name}')
  ```

* Chained or nested exceptions:

  ```Python
    x = 0
    file_name = "datei.xyz"


    try:
        print(5/x)
        with open(file_name, "r") as file:
            print(file)
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except FileNotFoundError:
        print(f'Could not open {file_name}')
  ```

* define a custom Exception:  
  `class MyCustomException(Exception):`
* throw / raise an Exception:  
  `raise MyCustomException(errorMessage)`
* `finally` : specify actions that are __always__ executed no matter if an error occurs or not

```Python
  try:
    file = open("existiert.txt", "r")
  except FileNotFoundError:
      print("File Not Found")
  except Exception as e:
      print(f'other error: {e}') 
  finally:    
    file.close()
    print("close file")
```

**[⬆ back to top](#table-of-contents)**
___
