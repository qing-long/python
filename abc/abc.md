# abc


## abstractmethod

子类中如果不存在该装饰器的方法, 子类实例化的时候会出错


```python
import abc
from abc import abstractmethod


class BetterStrategy2(metaclass=abc.ABCMeta):
    @abstractmethod
    def bet(self):
        return 1

    def record_win(self):
        pass

    def record_loss(self):
        pass


class BetterStrategy3(BetterStrategy2):
    def bet2(self):
        return 2

    def record_win(self):
        pass

    def record_loss(self):
        pass


b = BetterStrategy3()

"""
Traceback (most recent call last):
  File "002.py", line 28, in <module>
    b = BetterStrategy3()
TypeError: Can't instantiate abstract class BetterStrategy3 with abstract methods bet
"""
```