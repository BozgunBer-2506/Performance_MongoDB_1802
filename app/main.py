from datetime import datetime
from fastapi import FastAPI
from .mongodb import get_all_events 
from .database import get_db_users
from .mongodb import collection
from .database import SessionLocal, User

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Project is running!"}

@app.get("/events")
async def show_events():
    data = await get_all_events()
    return data

@app.get("/all-data")
async def show_all():
    mongo_data = await get_all_events()
    sql_data = get_db_users()
    
    return {
        "mongodb_events": mongo_data,
        "postgresql_users": sql_data
    }

@app.post("/add-event")
async def add_event(type: str, user: str):
    new_event = {"type": type, "user": user, "ts": datetime.utcnow().isoformat()}
    await collection.insert_one(new_event)
    return {"message": "MongoDB'ye eklendi!"}

@app.post("/add-user")
def add_user(name: str, email: str):
    db = SessionLocal()
    new_user = User(name=name, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()
    return {"message": "Postgres'e eklendi!"}