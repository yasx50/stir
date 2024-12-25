from mongoengine import Document, StringField, DateTimeField
from datetime import datetime

class TrendData(Document):
    # Defining the fields for the model
    trend1 = StringField(required=True)
    trend2 = StringField(required=True)
    trend3 = StringField(required=True)
    trend4 = StringField(required=True)
    trend5 = StringField(required=True)
    end_time = DateTimeField(default=datetime.utcnow)  # Date and time when the script ends
    ip_address = StringField(required=True)  # IP address used
    unique_id = StringField(unique=True, required=True)  # Unique ID for each entry

    meta = {
        'indexes': [
            'unique_id',  # This ensures a unique index is created for 'unique_id'
        ]
    }

    def __str__(self):
        return f"Trend Data {self.unique_id}: {self.trend1}, {self.trend2}, {self.trend3}, {self.trend4}, {self.trend5}"
