from functools import total_ordering


class Integer:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        """addition operation +"""
        return self.num + other.num

    def __sub__(self, other):
        """subtraction operation -"""
        return self.num - other.num

    def __mul__(self, other):
        """multiplication operation *"""
        return self.num * other.num

    """
    # only in python 2.x
    def __div__(self, other):
        return self.num / other.num
    """

    def __truediv__(self, other):
        """true division operation /"""
        return self.num / other.num

    def __floordiv__(self, other):
        """exact operation //"""
        return self.num // other.num

    def __eq__(self, other):
        """operation =="""
        return self.num == other.num

    def __ne__(self, other):
        """operation !="""
        return self.num != other.num

    def __lt__(self, other):
        """operation <"""
        return self.num < other.num

    def __gt__(self, other):
        """operation >"""
        return self.num > other.num

    def __ge__(self, other):
        """operation >="""
        return self.num >= other.num

    def __le__(self, other):
        return self.num <= other.num

    """
    only in python2.x
    def __cmp__(self, other):
        pass
    """


# 可以使用functools 里面的 total_ording 装饰器


@total_ordering
class Integer2:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        """addition operation +"""
        return self.num + other.num

    def __sub__(self, other):
        """subtraction operation -"""
        return self.num - other.num

    def __mul__(self, other):
        """multiplication operation *"""
        return self.num * other.num

    """
    # only in python 2.x
    def __div__(self, other):
        return self.num / other.num
    """

    def __truediv__(self, other):
        """true division operation /"""
        return self.num / other.num

    def __floordiv__(self, other):
        """exact operation //"""
        return self.num // other.num

    def __eq__(self, other):
        """operation =="""
        return self.num == other.num

    def __le__(self, other):
        return self.num <= other.num


def test_magic_method_opertaion():
    i1 = Integer(1)
    i2 = Integer(2)

    assert i1 + i2 == 3
    assert i1 - i2 == -1
    assert i1 * i2 == 2
    assert i1 // i2 == 0
    assert i1 / i2
    assert not i1 == i2
    assert i1 != i2
    assert i1 < i2
    assert not i1 > i2
    assert not i1 >= i2
    assert i1 <= i2


def test_magic_method_opertaion_total_ording():
    """
    使用total_ordering 的话需要实现 == 以及 除了 != 的任意一个方法即可
    """
    i1 = Integer2(1)
    i2 = Integer2(2)

    assert i1 + i2 == 3
    assert i1 - i2 == -1
    assert i1 * i2 == 2
    assert i1 // i2 == 0
    assert i1 / i2
    assert not i1 == i2
    assert i1 != i2
    assert i1 < i2
    assert not i1 > i2
    assert not i1 >= i2
    assert i1 <= i2
