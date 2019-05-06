# celery 小记

### 安装

```python
pip install celery
```



### 最小实例

```python
from celery import Celery

# 需要先安装redis 数据库
# 安装redis连接库 pip install redis
app = Celery('tasks', backend='redis', broker='redis://localhost//')


@app.task
def add(x, y):
    return x + y
```



#### 启动celery

linux:

```python
celery -A tasks worker --loglevel=info
# 其中 是tasks.py
```



```python
celery -A flask_celery.celery worker --loglevel=info -P eventlet
# celery 4 不支持windows 
# 需要安装 eventlet pip install eventlet 
# 并用以上命令开启
```

```python
# 开启python控制台
>>> from tasks import add
>>> result = add.delay(1, 1)
>>> result.status
'SUCCESS'
```

### 定时任务

```python
# flask_celery.py
from flask import Flask, render_template
from celery import Celery
from datetime import timedelta
from pixiv_spider import get_urls
from flask_sqlalchemy import SQLAlchemy
import requests
import os
from random import randint

app = Flask(__name__)
basedir = os.getcwd()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'celery.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

celery = Celery(app.import_name, backend='redis', broker='redis://localhost')
celery.conf.update(
    beat_schedule={
        'add-every-30-seconds': {
            'task': 'flask_celery.insert',
            'schedule': timedelta(seconds=30),  # 每 30 秒执行一次
            'args': (randint(0, 24), )}}
)


class Image(db.Model):
    __tablename__ = 'image'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(56))
    path = db.Column(db.String(128))


@app.route('/')
def index():
    try:
        img = Image.query.all()[-1]
    except IndexError as e:
        print(e)
        return render_template('index.html', img='1.jpg')
    else:
        return render_template('index.html', img=os.path.basename(img.path))


@celery.task
def insert(n):
    print('insert %d' % n)
    urls = get_urls()
    url = urls[n]
    name = os.path.basename(url)
    img = Image()
    img.name = name
    img.path = url
    db.session.add(img)
    db.session.commit()
    r = requests.get(img.path, headers={'user-agent': 'Mozilla/5.0 '
                                                      '(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Ge'
                                                      'cko) Chrome/65.0.3325.181 Safari/537.36',
                                        'referer': 'https://www.pixiv.net/'})
    with open('./static/' + os.path.basename(url), 'wb') as f:
        f.write(r.content)
    return 'success'


if __name__ == '__main__':
    app.run(debug=True)

```

```python
# pixiv_spider.py
import re
import json
import requests

from functools import wraps


def repeat(n=3):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                result = f(*args, **kwargs)
            except Exception as e:
                nonlocal n
                n -= 1
                if n < 0:
                    return None
                else:
                    print(e)
                    return wrapper(*args, **kwargs)
            else:
                return result

        return wrapper

    return decorator


@repeat(5)
def handle(url='https://www.pixiv.net/'):
    r = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'
                                                 '537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
    url_json = re.search(r'class="json-data" value=\'(.*?)\'>', r.text).group(1)
    return json.loads(url_json)


def get_json(url_json):
    urls = []
    for items in url_json['pixivBackgroundSlideshow.illusts']['landscape']:
        urls.append(items['url']['1200x1200'])
    return urls


def get_urls():
    url_json = handle()
    return get_json(url_json)


```

```python
# windows下
1.
celery -A flask_celery.celery worker --loglevel=info -P eventlet
2.
celery -A flask_celery.celery beat
```

```python
# linux下
celery -A flask_celery.celery --loglevel=info beat
# 应为windows下不支持 -B 参数
```

> 注意randint(0, 24) 一单确定就不会再改变

### 解决

```python
# flask_celery.py
from flask import Flask, render_template
from celery import Celery
from datetime import timedelta
from pixiv_spider import get_urls
from flask_sqlalchemy import SQLAlchemy
import requests
import os
from random import randint

app = Flask(__name__)
basedir = os.getcwd()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'celery.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

celery = Celery(app.import_name, backend='redis', broker='redis://localhost')
celery.conf.update(
    beat_schedule={
        'add-every-30-seconds': {
            'task': 'flask_celery.insert',
            'schedule': timedelta(seconds=30),  # 每 30 秒执行一次
            # args': (0,)'
        }}
)
i = 0


class Image(db.Model):
    __tablename__ = 'image'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(56))
    path = db.Column(db.String(128))


@app.route('/')
def index():
    try:
        img = Image.query.all()[-1]
    except IndexError as e:
        print(e)
        return render_template('index.html', img='1.jpg')
    else:
        return render_template('index.html', img=os.path.basename(img.path))


@celery.task
def insert():
    # 定义全局变量i
    # 在flask_celery.py 中改变变量
    # celery 每次获取的时候i值都不同
    global i
    urls = get_urls()
    i += 1
    if i == 25:
        i = 0
    url = urls[i]
    name = os.path.basename(url)
    img = Image()
    img.name = name
    img.path = url
    db.session.add(img)
    db.session.commit()
    r = requests.get(img.path, headers={'user-agent': 'Mozilla/5.0 '
                                                      '(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Ge'
                                                      'cko) Chrome/65.0.3325.181 Safari/537.36',
                                        'referer': 'https://www.pixiv.net/'})
    with open('./static/' + os.path.basename(url), 'wb') as f:
        f.write(r.content)

    return 'success'


if __name__ == '__main__':
    app.run(debug=True)
```

### 扩展

[动态创建celery任务](https://segmentfault.com/a/1190000010112848)