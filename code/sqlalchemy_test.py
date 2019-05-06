# 脚本
from sqlalchemy003 import Parent, Child, session

for i, text in enumerate(range(1, 101)):
    par = Parent(
        id=i,
        name=str(text) + 'Parent'
    )
    chi = Child(
        id=i,
        name=str(text) + 'Child',
        parent_id=i
    )
    session.add(par)
    session.add(chi)

session.commit()
