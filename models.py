from enum import unique
from sqlalchemy import  Column, Integer, String
from db import Base


class user_register(Base):
   
    __tablename__ = "user_register_table"
    id          = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    name        = Column(String(255), index=True, nullable=False)
    email       = Column(String(100), index=True, nullable=False,unique=True)
    mobile_no   = Column(String(100), index=True, nullable=False,unique=True)
