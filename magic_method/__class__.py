from pprint import pprint


class A:
    pass


a = A()
print(dir(A) == dir(A()) == dir(a))
pprint(dir(a))
"""
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__']
"""

pprint(a.__class__)


class B:
    b = 1


#  pprint(B.__class__.b) AttributeError

b = B()
print(b.__class__.b)


class C:
    c = 1

    def __init__(self):
        self.__class__.c = 2


#  pprint(C.__class__.b) AttributeError
c = C()
pprint(c.__class__.c)
