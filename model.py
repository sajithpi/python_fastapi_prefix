from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, create_engine, MetaData, exc ,desc
# from sqlalchemy.ext.declarative import declarative_base       
from sqlalchemy.orm import declarative_base,sessionmaker,relationship
from datetime import datetime
from main import PrefixerBase
# Table creation
class User(PrefixerBase):
    print("prefix",PrefixerBase._the_prefix)
    __incomplete_tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer(),primary_key=True)
    username = Column(String(25),nullable=False)
    email = Column(String(75),nullable=False)
    date_created = Column(DateTime(),default=datetime.utcnow)
    # child = relationship('Profile', back_populates = 'profile')

class Profile(PrefixerBase):

    __incomplete_tablename__ = 'profile'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer(),primary_key=True)
    user_id = Column('user_id', Integer, ForeignKey(f'{PrefixerBase._the_prefix}users.id'), primary_key=True)
    # user_id = Column(Integer(),ForeignKey('users.id'))
    sponser_id=Column(Integer(),nullable=False)
    address = Column(String(25),nullable=False)
    # profile = relationship('User', back_populates = 'child')
 

# class Account(PrefixerBase):
#     __incomplete_tablename__='account'
#     id = Column(Integer(),primary_key=True)
#     user_id = Column(Integer(),ForeignKey('users.id'))
#     balance = Column(Integer())
           
     