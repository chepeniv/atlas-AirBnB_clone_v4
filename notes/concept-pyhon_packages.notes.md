# Python Packages

[6.4. Packages](https://docs.python.org/3.4/tutorial/modules.html#packages)

python files can define modules and folders containing python files can define packages

## Comparison to C
C:
`#include "example.h"`

Python:
```python
import example

example.func()
```
or 
```python
from example import func

func()
```

C:
`#include "path/to/example.h"`

Python:
```python
import path.to.example
```
or
```python
from path.to.example import func
```

## Dotted module names == Path
presume the given file organization:
```
script.py
math/
	__init__.py
	func.py
```
in order to be able to refer to the `func()` function defined in `func.py` from `script.py` in the prefered method `from math.func import func` the empty file `__init__.py` must exist in the directory to be considered a package

## `import *` is dangerous
using `import *` is considered bad practice and if it used used `__init__.py` shouldn't be empty; it should contain the list of modules to load in order to function:

`__all__ = ["module_a", "module_b", "module_c"]`

## Relative and Absolute Imports

assume the given file structure:
```
script.py
module/
	__init__.py
	func_a.py
	func_b.py
```
then `func_a.py` can use `func_b(n)` by impporting either wih a relative path :
`from func_b import func_b`
or importing with an absolute path :
`from module.func_b import func_b`

pyhon treats the current working directory as the root from which to interpret
absolute paths

## Dealing with circular imports
https://www.stefaanlippens.net/circular-imports-type-hints-python.html
