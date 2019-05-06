from sqlalchemy import Column, String, Integer, ForeignKey, create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

# OneToOne
e_f_table = Table('e_f', Base.metadata,
    Column('e_id', Integer, ForeignKey('e.id')),
    Column('f_id', Integer, ForeignKey('f.id'))
)

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


engine = create_engine('sqlite:///test.db', echo=False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

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

