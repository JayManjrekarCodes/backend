from fastapi import FastAPI
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("/Users/mihirsampath/Downloads/fitness-tracker-database-cb3c4-firebase-adminsdk-gbub8-6547081832.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://fitness-tracker-database-cb3c4-default-rtdb.firebaseio.com/'
})

app = FastAPI()

class User:
    key: str
    value: dict
    
@app.post('/new')
def add_user(user: User):
    main = db.reference("/")
    main.update({User.name: User.stats})

@app.get('/users')
def get_users():
    ref = db.reference("/").get()
    return ref