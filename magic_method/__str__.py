class Foo:
    def __str__(self):
        return 'foo'


foo = Foo()
print(foo)


class Foo1:
    def __repr__(self):
        return 'repr foo'


foo1 = Foo1()
print(foo1)


class Foo2:
    def __str__(self):
        return 'foo'

    def __repr__(self):
        return 'repr foo'


foo2 = Foo2()
print(foo2)
