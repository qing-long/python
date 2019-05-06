# Sqlalchemy

## 基本操作

### Version Check / 版本检查


```python
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.1.15'
```

### Connecting / 连接数据库

- [连接数据库](connecting-databases.py)


### create models / 创建模型

```python
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __str__(self):
        return "<User {}>".format(self.name)
```

### creare database / 创建数据库

```python
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __str__(self):
        return "<User {}>".format(self.name)

engine = create_engine('sqlite:///test.db', echo=True)
Base.metadata.create_all(engine)
```

### create a session / 创建会话

```python
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()
```

### add & update / 添加, 修改数据

```python
# add
user = User(name='buglan')
session.add(user)
session.commit()
# update
user = session.query(User).filter_by(name='admin').first()
user.name = 'admin1'
session.add(user)
session.commit()
```

### query / 查询数据

```python
users = session.query(User).all()

"""
[<sqlalchemy_models.User object at 0x000002962F879898>, <sqlalchemy_models.User object at 0x000002962F879908>, <sqlalchemy_models.User object at 0x000002962F8799B0>, <sqlalchemy_models.User object at 0x000002962F879A58>, <sqlalchemy_models.User object at 0x000002962F879B00>, <sqlalchemy_models.User object at 0x000002962F879BA8>]
"""
```

### order_by / 排序数据

```python
users = session.query(User).order_by(User.id.desc()).all()

for user in users:
    print(user)
# 倒序排列
```

### filter_by / 过滤数据

```python
users = session.query(User).filter_by(name='buglan').all()

for user in users:
    print(user)
```

### filter / 过滤数据

```python
users = session.query(User).filter(User.name == 'buglan').all()

for user in users:
    print(user)
# and_
users = session.query(User).filter(and_(User.name == 'buglan', User.id == 2)).all()
# or_
users = session.query(User).filter(or_(User.name=='admin1', User.name=='buglan')).all()
# like
users = session.query(User).filter(User.name.like('%ug%'))
# in_
users = session.query(User).filter(User.name.in_(['buglan', 'admin'])).all()
# ~ in_ (not in)
users = session.query(User).filter(~User.name.in_(['buglan', 'admin'])).all()

```

### returning lists and sclars / 返回列表

- all()
- one()
- first()
- one_or_none()
- scalar()

### count / 计数

```python
users = session.query(User).count()
```

### Basic RelationShip Patterns

- #### OneToMany
```python
class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))

    def __str__(self):
        return "<Teacher {}>".format(self.name)


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    teacher_id = Column(Integer, ForeignKey('teacher.id'))

    def __str__(self):
        return "<Student {}>".format(self.name)
```

```python
# back_populates
class Parent(Base):
    """
    if we use back_populates
    the Child and Parent also need parents and childern
    other thing is:
    lazy='dynamci' is not allowed use in OneToMany or ManyToOne 
    """
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    children = relationship('Child', back_populates='parents')
    
    def __str__(self):
        return "<Parent {}>".format(self.name)


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parents = relationship('Parent', back_populates='children')
    
    def __str__(self):
        return "<Child {}>".format(self.name)
```

```python
#  backref
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    products = relationship('Product', backref='users')

    def __str__(self):
        return "<User {}>".format(self.name)


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    user_id = Column(Integer, ForeignKey('user.id'))

    def __str__(self):
        return "<Product {}>".format(self.name)


# backref
user = session.query(User).get(1)
print(user)
for p in user.products:
    print(p)

p1 = session.query(Product).get(1)
print(p1)
print(p1.users)

"""
<User admin>
<Product qwe>
<Product asd>
<Product zxc>
<Product qwe>
<User admin>
"""
```

- #### OneToOne / 一对一关系

```python
# back_populates
class A(Base):
    __tablename__ = 'a'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    b = relationship('B', uselist=False, back_populates='a')
    def __str__(self):
        return "<A {}>".format(self.name)


class B(Base):
    __tablename__ = 'b'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    a = relationship('A', back_populates='b')
    a_id = Column(Integer, ForeignKey('a.id'))
    
    def __str__(self):
        return "<B {}>".format(self.name)

a1 = session.query(A).get(1)
print(a1)
print(a1.b)
# 对于数据库中有多的a_id=a1.id 的 只返回最先的一个
```

```python
# backref
class C(Base):
    __tablename__ = 'c'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    d_id = Column(Integer, ForeignKey('d.id'))

    def __str__(self):
        return "<C {}>".format(self.name)


class D(Base):
    __tablename__ = 'd'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    c = relationship('C', uselist=False, backref='d')

    def __str__(self):
        return "<D {}>".format(self.name)

d1 = session.query(D).get(1)
print(d1.c)
c1 = session.query(C).get(2)
print(c1.d)
"""
<C qwe>
<D 456>
"""

# or 
from sqlalchemy.orm import backref
class C(Base):
    __tablename__ = 'c'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    d_id = Column(Integer, ForeignKey('d.id'))
    d = relationship('D', backref=backref('c', uselist=False))
    def __str__(self):
        return "<C {}>".format(self.name)

class D(Base):
    __tablename__ = 'd'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))

    def __str__(self):
        return "<D {}>".format(self.name)

d1 = session.query(D).get(1)
print(d1.c)

c1 = session.query(C).get(2)
print(c1.d)

"""
# a SAWarning
D:\python35\lib\site-packages\sqlalchemy\orm\strategies.py:645: SAWarning: Multiple rows returned with uselist=False for lazily-loaded attribute 'D.c'  % self.parent_property)
<C qwe>
<D 456>
"""
```

- ##### ManyToMany / 多对多

Many to Many adds an association table between two classes.

```python
class E(Base):
    __tablename__ = 'e'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    f = relationship('F', secondary='e_f')
    def __str__(self):
        return "<E {}>".format(self.name)


class F(Base):
    __tablename__ = 'f'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))

    def __str__(self):
        return "<F {}>".format(self.name)

# operation

# add
"""
e = E()
e.name = 'a'
session.add(e)
e = E()
e.name = 'b'
session.add(e)
session.commit()
"""

"""
f = F()
f.name = 'c'
session.add(f)
f = F()
f.name = 'd'
session.add(f)

session.commit()
"""

e = session.query(E).filter_by(name='a').first()

f = session.query(F).filter_by(name='c').first()

print([x for x in e.f])
e.f.remove(f)

print([x for x in e.f])
```

```
ManyToMany is also can use backref that is the same operations
```

## 实例
