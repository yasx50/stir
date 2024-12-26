from mongoengine import connect, Document, StringField
from pymongo import MongoClient
import os

DB_NAME = "STIR"

# MongoDB Atlas URI
ATLAS_URI =os.getenv("ATLAS_URI")

# Connect to MongoDB using mongoengine
def connectDB():
    try:
        # Connect to the MongoDB Atlas instance
        connect(DB_NAME, host=ATLAS_URI)
        
        # Access the database using MongoClient (optional for verification)
        client = MongoClient(ATLAS_URI)
        db = client[DB_NAME]
        
        # Print the available collections in the database to verify connection
        print("Connected to the database:", db.name)
        print("Collections:", db.list_collection_names())

    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

# Call the function to connect to the database
connectDB()
