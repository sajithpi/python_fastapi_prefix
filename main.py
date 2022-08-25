from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, create_engine, MetaData, exc ,desc
# from sqlalchemy.ext.declarative import declarative_base       
from sqlalchemy.orm import declarative_base,sessionmaker,relationship,exc
from datetime import datetime

from fastapi import FastAPI, status, Request
from schema import user_data
import os
import sys
app = FastAPI()







Session = sessionmaker()

from sqlalchemy.ext.declarative import declared_attr


metadata_obj = MetaData()
Base = declarative_base(metadata=metadata_obj)

class PrefixerBase(Base):

    __abstract__ = True

    _the_prefix = 'myprefix'
    extend_existing=True

    @declared_attr
    def __tablename__(cls):
        
        return cls._the_prefix + cls.__incomplete_tablename__

# Specifying database connection url
engine = create_engine("mysql+pymysql://root:password@localhost/python_db",echo=False)

@app.get("/")
def home():
    return {'message':'hello from fastapi'}                                          
@app.post('/add_user', status_code = status.HTTP_201_CREATED)
def add_user(request:Request, payload:user_data):

    PrefixerBase._the_prefix = request.headers.get('prefix')
    if 'model' in sys.modules.keys():
        del sys.modules['model']
        print("main deleted, cache cleared")
    else:
        print("main not exists in cache")
    from model import User
    # Base.metadata.create_all(engine)
    try:

        local_session = Session(bind = engine)
        user_data = User(username=payload.username, email=payload.email)
        local_session.add(user_data)
        local_session.commit()
        print("payload data:",payload.username)
        local_session.close()
        return {'message':'success'}
    except Exception as e:
        print(e)