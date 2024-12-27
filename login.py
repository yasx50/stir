from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
EMAIL = os.getenv("EMAIL")

def login(driver):
    driver.get("https://x.com/login")

    try:
        # Wait for username field to appear and enter the username
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text"))
        ).send_keys(USERNAME, Keys.RETURN)

        # Wait for password field to appear and enter the password
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        ).send_keys(PASSWORD, Keys.RETURN)

        # Check if Twitter asks for email verification
        try:
            email_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "text"))  # Assuming the email field uses "text" as the name
            )
            email_field.send_keys(EMAIL, Keys.RETURN)
        except Exception as email_exception:
            print("Email step not required or an error occurred during email entry.", email_exception)

        # Wait for login to complete and redirect to the homepage
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Home']"))
        )
        print("Login successful.")

    except Exception as e:
        print(f"Error while logging in: {e}")

