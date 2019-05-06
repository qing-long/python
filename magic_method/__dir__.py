from pprint import pprint


class Foo:
    pass


f1 = Foo()
pprint(dir(f1))


class Foo1:
    def __dir__(self):
        return dir(Foo1) + ['a']


f2 = Foo1()
pprint(dir(f2))
