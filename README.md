# Python学习之路

> 这是本人在python学习上的总结, 包含大量自我感悟, 并不是相关的教程(当然也可用作学习), 且有许多未知bug


## python 起步

- ### 第一章: python相关介绍
    - 1.1 [起源](1-1-1.md)
    - 1.2 [优点和缺点](1-1-2.md)


- ### 第二章: 安装python
    - 2.1 [在linux上安装python](2-2-1.md)
    - 2.2 [在windows上安装python](2-2-2.md)
    - 2.3 [在mac上安装python](2-2-3.md)
    - 2.4 [源码编译安装](2-2-4.md)
    - 2.5 [配置PATH和PYTHONPATN环境变量](2-2-5.md)

- ### 第三章: 集成开发环境和编辑器
    - 3.1 [编辑器](3-3-1.md)
    - 3.2 [IDE](3-3-2.md)

## python 基础

- ### 第四章 变量和数据类型
    - 变量
    - 基本数据类型
- ### 第五章 控制结构
    - if
    - while
    - for
    - break/contiune
- ### 函数
    - 内置函数
- ### 高级特性
    - 生成式
    - lambda
    - yield
    - 闭包
    - 装饰器
        - [简单装饰器](./simple_decorator.py)
        - [不改变元信息的装饰器](./decorator_with_wraps.py)
        - [带参数的装饰器](./decorator_with_parameter.py)
        - [带可选参数的装饰器](./decorator_with_bracket.py)
        - [类装饰器](./decorator_with_class.py)
        - [装饰器装饰类]()
- ### 模块
- ### 面向对象
    - class
    - module
- ### 魔术方法
    - [magic_method](./magic_method.md)
- ### 标准库
    - [base64](./base64.md)
    - [datetime](./datetime/datetime.md)
    - [re](./re.md)
    - os
    - urllib
    - sys
    - logging
    - io
    - argparse
    - functools(./functools.py)
        - [wraps的作用](./decorator_with_wraps.py)
- ### 虚拟环境
    - pyvenv
    - virtualenv
    - [pipenv](./pipenv.md)
    - conda

## python 进阶

- ### 正则表达式
- ### 单元测试
    - unittest
    - pytest(./pytest.md)
- ### type hint
    - mypy
- ### 第三方模块
    - requests
    - lxml
    - beautifulsoup4
- ### 数据库
    - sqlite3
    - mysql
    - redis
    - pymysql[./pymysql.md]
    - nosql
- ### web开发
    - [flask](flask/flask.md)
    - [django](django/django.md)
    - tornado
- ### orm
    - [sqlalchemy](sqlalchemy/sqlalchemy.md)
    - peewee
- ### 多线程/多进程
    - threading
- ### 异步
    - asyncio
    - aiohttp
- ### 网络编程
    - socket
- ### Gui开发
    - turtle
    - tkinter
    - [pyqt5](pyqt5/pyqt5.md)
- ### 发布
- ### 元类
    - [metaclass](./metaclass.md)

## python 实例

### python 爬虫
    - [爬虫 - 异步爬取妹子图]()

### python web开发

### python shell脚本

### python ML


## 附录

- [关键字](./keyword.md)
- [python 奇淫技巧](./magic_python.md)
- [python 神坑](./what_fuck_python.md)
