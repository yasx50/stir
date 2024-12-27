from mongoengine import Document, StringField, DateTimeField
from datetime import datetime

class TrendData(Document):
    trend1 = StringField(required=True)
    trend2 = StringField(required=True)
    trend3 = StringField(required=True)
    trend4 = StringField(required=True)
    trend5 = StringField(required=True)
    end_time = DateTimeField(default=datetime.now())
    ip_address = StringField(required=True)
    unique_id = StringField(unique=True, required=True)

    meta = {
        'indexes': ['unique_id']
    }

    def __str__(self):
        return (f"Trend Data {self.unique_id}: {self.trend1}, {self.trend2}, {self.trend3}, "
                f"{self.trend4}, {self.trend5} (IP: {self.ip_address})")
