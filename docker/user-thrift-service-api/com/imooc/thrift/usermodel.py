"""
user orm
"""

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = sa.Column(sa.String(20), primary_key=True)
    username = sa.Column(sa.String(20), nullable=False)
    password = sa.Column(sa.String(60), nullable=False)
    real_name = sa.Column(sa.String(20), nullable=False)
    mobile = sa.Column(sa.String(20), nullable=False, default="")
    email = sa.Column(sa.String(30), nullable=False, default="")


engine = sa.create_engine('mysql+mysqlconnector://root:123@localhost:3306/test')
DBSession = sessionmaker(bind=engine)
session = DBSession()
