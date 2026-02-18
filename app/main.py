from fastapi import FastAPI
from .mongodb import get_all_events 
from .database import get_db_users

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