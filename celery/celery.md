# celery

> celery 是强大的分布式处理异步框架


## install

注意建议在linux上使用celery, windows上仅能使用旧版

```bash
pip install celery --user
```

## get-start


```bash
from celery import Celery


app = Celery('task', broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y
```

## 使用celery 配置文件

### 文件树:

```bash
daemon
├── __init__.py
├── cronjob.py
├── customer.py
├── settings.py
└── tasks.py
```

- `__init__.py` 包声明
- `cronjob.py`  定时任务
- `customer.py` 消费者
- `settings.py` celery 配置
- `tasks.py`    异步任务

### 文件一览

- `__init__`

```py
from celery import Celery
from config.const import RabbitMqConst

app = Celery(__name__, broker=RabbitMqConst.RABBITMQ_BROKER_URL)
app.config_from_object('daemon.settings')

```

- `setting`

```py
from celery.schedules import crontab
from kombu import Queue

# backend
# CELERY_RESULT_BACKEND = RabbitMqConst.RABBITMQ_BROKER_URL

# 时区
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = True

# task_serializer = 'json'
# result_serializer = 'json'
# accept_content = ['json']


CELERYD_LOG_FORMAT = '%(message)s'

CELERYD_TASK_LOG_FORMAT = '%(message)s'

# 指定导入的任务模块
CELERY_IMPORTS = (
    'daemon.tasks',
    'daemon.cronjob'
)

# 指定celery队列
CELERY_QUEUES = (
    # 路由键以'default.task.'开头的都进default队列
    Queue('default', routing_key='default.task.#'),
    Queue('customer', routing_key='customer.task.#'),
)

# 默认交换机的名称为 oxygen.daemon.cronjob
CELERY_DEFAULT_EXCHANGE = 'daemon.cronjob'

# 交换机的类型
CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'

# 默认交换价的key
CELERY_DEFAULT_ROUTING_KEY = 'default.task.default'

# celery 消息调度设置
# daemon.cronjob.sync_user的消息会进入default队列
CELERY_ROUTES = {
    'daemon.cronjob.task': {
        'queue': 'default',
        'routing_key': 'default.task.user',
    },
}

# 定时任务配置
CELERYBEAT_SCHEDULE = {
    "default_task": {
        "task": "daemon.cronjob.task",
        "schedule": crontab(minute='*/30'),
    },
}
```

- `cronjob`

```python
@app.task
def something():
    default_task()
```

- `customer`

```python
// todo
```

- `tasks`

```bash
@app.task
def something():
    async_task()

```

## celery 注意事项

1. 加入exchange, queue, routing_key是为了保证celery 任务不被同一队列其他celery进程消费掉(如果部署多个不同celery | celery默认队列为`celery`)

2. celery官方推荐rabbitmq, 在实际使用过程中我也觉得使用rabbitmq比较好