from sqlalchemy_models import Base, User, MetaData, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_


# link sqlite
engine = create_engine('sqlite:///test.db', echo=False)

# create sqlite
Base.metadata.create_all(engine)

Session = sessionmaker()
session = Session(bind=engine)


"""
# add
user = User(name='buglan')
session.add(user)
session.commit()       
"""


"""
# update
user = session.query(User).filter_by(name='admin').first()
user.name = 'admin1'
session.add(user)
session.commit()
"""

"""
# query
users = session.query(User).all()
"""

"""
# order_by
users = session.query(User).order_by(User.id.desc()).all()
for user in users:
    print(user)
"""

"""
# filter_by
users = session.query(User).filter_by(name='buglan').all()
for user in users:
    print(user)
"""

"""
# filter
users = session.query(User).filter(User.name == 'buglan').all()

for user in users:
    print(user)

user = session.query(User).filter(User.name == 'buglan' and User.id == 2).first()
print(user)  
"""

"""
# like
users = session.query(User).filter(User.name.like('%ug%'))
"""

"""
# and_
users = session.query(User).filter(and_(User.name == 'buglan', User.id == 2)).all()
"""

"""
# or_
users = session.query(User).filter(or_(User.name=='admin1', User.name=='buglan')).all()
"""

"""
# in_
users = session.query(User).filter(User.name.in_(['buglan', 'admin'])).all()users = session.query(User).filter(User.name.in_(['buglan', 'admin'])).all()
"""
"""
~ in_
users = session.query(User).filter(~User.name.in_(['buglan', 'admin'])).all()
"""

"""
count
users = session.query(User).count()
"""



