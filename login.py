from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv
import os


USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

def login(driver):
    
    driver.get("https://x.com/login")

# Wait for the page to load and log in
    try:
        # Wait for username field to appear and enter the username
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text"))
        ).send_keys(USERNAME, Keys.RETURN)

        # Wait for password field to appear and enter the password
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        ).send_keys(PASSWORD, Keys.RETURN)

        # Wait for login to complete and redirect to the homepage
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Home']"))
        )
    except Exception as e:
        print(f"error while login {e}")
