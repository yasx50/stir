from mongoengine import connect
DB = "STIR"
# Connect to MongoDB (adjust the URI as needed)
def connectDB():
    connect(DB, host='localhost', port=27017)
    print("database connected successfully")
