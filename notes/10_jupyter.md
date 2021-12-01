# Python Bootcamp: Jupyter

<!-- omit in toc -->
## Table of Contents

1. [Start Directory](#start-directory)
2. [Keyboard Shortcuts](#keyboard-shortcuts)
3. [Special Actions](#special-actions)
4. [Math formula](#math-formula)
5. [Jupyter widgets](#jupyter-widgets)
6. [References](#references)

## Start Directory

* start jupyter notebooks with specific directory as root path:

``` bash
jupyter notebook --notebook-dir="Q:\Programming\python-bootcamp"
```

**[⬆ back to top](#table-of-contents)**
___

## Keyboard Shortcuts

| Shortcut           | Action                                          |
| ------------------ | ----------------------------------------------- |
| `Esc`              | switch to Command Mode (cell border turns blue) |
| (Command Mode) `M` | change cell to markdwon                         |
| (Command Mode) `Y` | change cell to code                             |
| (Command Mode) `C` | copy cell                                       |
| (Command Mode) `X` | cut cell                                        |
| (Command Mode) `V` | paste cell                                      |
| (Command Mode) `B` | insert cell below                               |

**[⬆ back to top](#table-of-contents)**
___

## Special Actions

* Save and Checkpoint --> generates checkpoints
* Save as: md / pdf (LaTeX erfordert zusätzliche Tools) / html ...

**[⬆ back to top](#table-of-contents)**
___

## Math formula

* math formatting by surrounding formula with `$`:

``` md
    $ a^2 + b^2 = c^2 $ 
```

* enables use of LaTeX math notation (e.g. \sqrt{b} for square root)

* use `$$` for centering formula

**[⬆ back to top](#table-of-contents)**
___

## Jupyter widgets

``` python
    import ipywidgets as widgets
    widgets.Button(description="Hallo Welt")                        # button with "Hallo Welt" Label

    widgets.Text(description="Beschriftung:", value="Text")         # Text input with placeholder: Text
    widgets.IntText(description="Int-Value:", value="123")          # integer Input field
    widgets.FloatText(description="Float value:", value="123.5")    # float Input field


    widgets.Checkbox(description="Use Floats?", value=True)         # checkbox (pre-selected)

    widgets.RadioButtons(                                           # radio buttons
        options= ['München', 'Berlin', 'Köln'],
        description= "Welche Stadt ?",
        disabled=False
    )

    widgets.Dropdown(                                               # drop down
        options= ['München', 'Berlin', 'Köln'],
        description= "Welche Stadt ?",
        disabled=False
    )
```

* display widget with `display`:

``` python
    from IPython.display import display

    age = widgets.IntText(description="Alter:", value="23")         # define widget ans save it to variable
    display(age)                                                    # display widget
    print(age.value)                                                # show current value
```

### Interaction

``` python

    button = widgets.Button(description="OK")                       # define button
    display (button)                                                # show button

    def on_button_click(event):                                     # define event handler function
        button.description="Clicked!"
    
    button.on_click(on_button_click)                                # assign event-handler function

```

**[⬆ back to top](#table-of-contents)**
___

## References

[Wikibook: LaTeX Math](https://en.wikibooks.org/wiki/LaTeX/Mathematics)  
[List of LaTeX math symbols](http://oeis.org/wiki/List_of_LaTeX_mathematical_symbols)  
[IPyWidgets Documentation - List of Widgets](https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html#Complete-list)

**[⬆ back to top](#table-of-contents)**
___
