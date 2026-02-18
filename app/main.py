import os
import psycopg2
from datetime import datetime
from fastapi import FastAPI
from .mongodb import get_all_events, collection
from .database import get_db_users

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Project is running!"}

@app.get("/all-data")
async def show_all():
    mongo_data = await get_all_events()
    sql_data = get_db_users()
    return {
        "mongodb_events": mongo_data,
        "postgresql_users": sql_data
    }

@app.post("/add-event")
async def add_event(event_type: str, user: str):
    new_event = {
        "type": event_type, 
        "user": user, 
        "ts": datetime.utcnow().isoformat()
    }
    await collection.insert_one(new_event)
    return {"message": "Successfully added to MongoDB"}

@app.post("/add-user")
def add_user(name: str, email: str):
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "host.docker.internal"),
            database=os.getenv("DB_NAME", "practiceapp"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASS")
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, email) VALUES (%s, %s);", (name, email))
        conn.commit()
        cur.close()
        conn.close()
        return {"message": "Successfully added to PostgreSQL"}
    except Exception as e:
        return {"error": str(e)}