# sqlite
from sqlalchemy import create_engine
engine = create_engine('sqlite:///test.db', echo=True)

# mysql+pymysql
engine = create_engine('mysql+pymysql://root:root@localhost/blog')