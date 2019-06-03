# What The Fuck Python


## python 循环漏删

```python
In [1]: a = [0,0,1]

In [2]: for n in a:
   ...:     if n == 0:
   ...:         a.remove(0)
   ...:

In [3]: a
Out[3]: [0, 1]
```

## Flask request.args['name'] 当键值不存在时, 不报错而是报400(bad request)

```python
@app.route('/hello')
def hello():
    name = request.args['name']
    # files form
    pass

```

应使用`request.args.get('name', None) 来避免这种错误
```python
@app.route('/hello')
def hello():
    name = request.args['name']
    pass

```

## 使用next时的url安全性

> 假设我们的应用是一个银行业务系统（下面简称网站A），某个攻
> 击者模仿我们的网站外观做了一个几乎一模一样的网站（下面简称网站
> B）。接着，攻击者伪造了一封电子邮件，告诉用户网站A账户信息需
> 要更新，然后向用户提供一个指向网站A登录页面的链接，但链接中包
> 含一个重定向到网站B的next变量，比如：http://exampleA.com/login?
> next=http://maliciousB.com。当用户在A网站登录后，如果A网站重定向
> 到next对应的URL，那么就会导致重定向到攻击者编写的B网站。因为B
> 网站完全模仿A网站的外观，攻击者就可以在重定向后的B网站诱导用
> 户输入敏感信息，比如银行卡号及密码,

## python tutple `1,`

```python
In [1]: a = 1,

In [2]: a

Out[2]: (1,)
```
元组定义就是用逗号分隔的一组元素，跟括号根本没有关系好吧。只是因为大多情况下在表达式中需要用括号做定界符。a=1, a=1,2,3 a 就是元组了，根本不用括号。括号的主要作用是用来提升运算符优先级.


## 设置了`SQLALCHEMY_DATABASE_URI` 却依旧出现警告
app.config 要在 db = SQLAlchemy(app) 之前
