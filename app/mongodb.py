import os
from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB connection string
MONGO_URL = "mongodb://host.docker.internal:27017"
client = AsyncIOMotorClient(os.getenv("MONGO_URL", "mongodb://host.docker.internal:27017"))
db = client.practiceapp

async def get_all_events():
    events = []
    # Fetch all data from events collection
    cursor = db.events.find()
    async for document in cursor:
        # Convert MongoDB ObjectId to string for JSON compatibility
        document["_id"] = str(document["_id"])
        events.append(document)
    return events