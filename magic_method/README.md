# Magic Methods


## about class

1. `__class__`: [instance's type](https://stackoverflow.com/questions/48066220/python-class)
2. `__all__`: `from foo import *` if foo define `__all__` and the * file only contain the package in __all__ list
3. `__dir__`: binding built-in dir()
4. `__dict__`: list property in class or instance and `__dict__` is a dict, save properties
5. `__str__`: binding built-in str()
6. `__repr__`: binding built-in repr(), and if class call str() and not exist `__str__`, str() will call `__repr__`
5. `__call__`: call class without init class
