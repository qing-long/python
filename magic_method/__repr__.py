class Foo:
    def __str__(self):
        return 'foo'


foo = Foo()
print(repr(foo))


class Foo1:
    def __repr__(self):
        return 'foo'


foo1 = Foo1()
print(repr(foo1))
print(foo1)
