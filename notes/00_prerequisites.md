# Python Bootcamp: Prerequisites

<!-- omit in toc -->
## Table of Contents

1. [Setup](#setup)
2. [Jupyter configuration](#jupyter-configuration)
3. [Jupyter Notebooks](#jupyter-notebooks)

## Setup

python installation: use ___Anaconda__ package

[Anaconda](https://www.anaconda.com/) : toolset incl. Jupyter etc..

Anaconda navigator: Launcher for all tools related to Python

Anaconda update via console (run anaconda bash as administrator):
(cf. [StackOverflow](https://stackoverflow.com/questions/55144561/anaconda-navigator-does-not-update-packages))

``` Bash
    conda update conda                      # updates anaconda
    conda update anaconda-navigator         # updates navigator
    conda update navigator-updater          # not necessary
    conda update --all -y                   # updates all other packages
```

**[⬆ back to top](#table-of-contents)**
___

## Jupyter configuration

* by default, jupyter notebooks start at the user directory (without the chance to navigate up !)
* to change this, generate a custom jupyter config:

    1. open command prompt
    2. run `jupyter notebook --generate-config`
    3. this generates a config file at `C:\Users\username\.jupyter\jupyter_notebook_config.py`
    4. look for the line: `#c.NotebookApp.notebook_dir = ''`
    5. set the new path (use forward slashes ! e.g. `D:/Programming/python/`) in this setting (replace the `#` at the beginning)

**[⬆ back to top](#table-of-contents)**
___

## Jupyter Notebooks

* every cell is an executable code block (like REPL)
* execute cell with `Shift+Enter`
* mix up code blocks, markdown, headings etc.

**[⬆ back to top](#table-of-contents)**
___
