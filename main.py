import db
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import models
import schema
from db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
db = SessionLocal()

app = FastAPI(title="user registration")


@app.get('/get_user')
def  get_user(id:str):
     receive_user = db.query(models.user_register).filter(models.user_register.id==id).first()
     return receive_user

@app.post('/user_register')
def user_register(data:schema.Base):
    receive_data = db.query(models.user_register).filter(models.user_register.mobile_no==data.mobile_no).first()
    

    if receive_data:

        return {'phone number already in db'}
    
    receive_data1 = db.query(models.user_register).filter(models.user_register.email==data.email).first()
    if receive_data1:
        return {'phone email already in db'}

        
    try:
        user_details = models.user_register(**data.dict())
        db.add( user_details)
        db.commit()
    except:
         return{'db error'}
    return data