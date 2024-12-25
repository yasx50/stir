from trending import getdata
from dbConnection import connectDB
from login import login
from model import TrendData


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service  
import datetime
import time



chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")  # Disable sandbox
chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues
chrome_options.add_argument("--disable-gpu")  # Disable GPU

# Initialize Chrome WebDriver
driver = webdriver.Chrome( options=chrome_options)


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

# trend_entry.save()  # Save the document to MongoDB


driver.quit()