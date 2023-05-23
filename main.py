import sqlalchemy
from sqlalchemy.orm import sessionmaker

DSN = 'postgres://postgres: @localhost;3452/somedb'
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

