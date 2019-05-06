class Foo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        print('call __init__ with args({}, {}, {})'.format(
            self.a, self.b, self.c))

    def __call__(self, a, b):
        self.a = a
        self.b = b
        print('call __call__ with args({}, {})'.format(self.a, self.b))


f = Foo(1, 2, 3)
f(1, 2)
