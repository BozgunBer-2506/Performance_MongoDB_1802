import os
import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_users():
    try:
        db_pass = os.getenv("DB_PASS") 
        
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "host.docker.internal"),
            database=os.getenv("DB_NAME", "practiceapp"),
            user=os.getenv("DB_USER", "postgres"),
            password=db_pass
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM users;")
        users = cur.fetchall()
        cur.close()
        conn.close()
        return users
    except Exception as e:
        return {"error": str(e)}