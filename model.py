from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import *
import numpy as np
import json


engine = create_engine(f"{engine}://{user}@{host}/{name}?", echo=False)
conn = engine.connect()
Base = declarative_base()


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    image_encodes = Column(String(16000))
    card_encodes = Column(String(200))


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def jsonSerialize(arr):
    arr = arr.tolist()
    arr = json.dumps(arr)
    return arr


def jsonDeserialize(jData):
    arr = json.loads(jData)
    arr = np.array(arr)
    return arr
