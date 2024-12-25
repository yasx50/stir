from mongoengine import connect, Document, StringField
from pymongo import MongoClient

DB_NAME = "STIR"

# Connect to MongoDB using mongoengine
def connectDB():
    try:
        # Connect to the local MongoDB instance
        connect(DB_NAME, host="mongodb://localhost:27017/")
        
        # Access the database using MongoClient (optional for verification)
        client = MongoClient("mongodb://localhost:27017/")
        db = client[DB_NAME]
        
        # Print the available collections in the database to verify connection
        print("Connected to the database:", db.name)
        print("Collections:", db.list_collection_names())

    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

# Call the function to connect to the database
connectDB()
