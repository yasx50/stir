from trending import getdata
from dbConnection import connectDB
from login import login


from selenium import webdriver
import time



driver = webdriver.Chrome( )
connectDB()
login(driver)
time.sleep(5)
getdata(driver)
time.sleep(5)

driver.quit()