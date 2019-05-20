
class Foo:
    def __str__(self):
        return 'Foo'

    def __repr__(self):
        return 'repr Foo'

if __name__ == "__main__":
    print(Foo)
    print(str(Foo))

    foo = Foo()
    print(foo)

    print(repr(Foo))
    print(repr(foo))