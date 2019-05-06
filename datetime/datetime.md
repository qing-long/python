# python standard library datetime


## python converting <class 'str'> to <class 'datetime'>


```python
from datetime import datetime

s = '2018-10-28 11:00:00'
date_obj = datetime.strptime('s', '%Y-%m-%d %H:%M:%S')
# datetime(2018, 12, 28, 11, 0)
```

## python datetime format symbol

| symbol | description |
|--------|-------------|
| %Y     | 年          |
| %m     | 月          |
| %d     | 天          |
| %H     | 小时        |
| %M     | 分钟        |
| %S     | 秒          |
