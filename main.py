from trending import getdata
from dbConnection import connectDB
from login import login
from model import TrendData


from selenium import webdriver
import datetime
import time



driver = webdriver.Chrome( )

login(driver)

getdata(driver)

# Example of creating and saving an entry
trend_entry = TrendData(
    unique_id="abc123",
    trend1="Trend 1 Data",
    trend2="Trend 2 Data",
    trend3="Trend 3 Data",
    trend4="Trend 4 Data",
    trend5="Trend 5 Data",
    # end_time=datetime.now(),
    ip_address="192.168.1.1"
)

trend_entry.save()  # Save the document to MongoDB


driver.quit()