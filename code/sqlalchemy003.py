from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, MetaData
from sqlalchemy.orm import relationship, sessionmaker, backref


Base = declarative_base()
# declarative the base

# one to many
# techer and student

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

# 指定关系: 可以互相使用


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

# OneToMany change to OneToOne
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


"""
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
"""
# or



engine = create_engine('sqlite:///test.db', echo=False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Operation

# p1 = session.query(Parent).first()
"""
print(p1.children)
[<__main__.Child object at 0x0000012E7A2A10B8>]
may Parents has some children 
so back a list object

for i in p1.children:
    print(i)

<Child 1Child> 
"""

           

# c1 = session.query(Child).first()
"""
print(c1.parents)
<Parent 1Parent>
Childern just have a Parent
so just back an object 
"""

# backref
"""
user = session.query(User).get(1)
print(user)
for p in user.products:
    print(p)

p1 = session.query(Product).get(1)
print(p1)
print(p1.users)
"""

# back_populates
"""
a1 = session.query(A).get(1)
print(a1)
print(a1.b)
# 对于数据库中有多的a_id=a1.id 的 只返回最先的一个
"""

# backref

d1 = session.query(D).get(1)
print(d1.c)

c1 = session.query(C).get(2)
print(c1.d)