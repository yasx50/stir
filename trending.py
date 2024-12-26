from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from model import TrendData
import requests
import random
import string
from datetime import datetime


# Function to get external IP address
def get_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        ip_address = response.json().get("ip")
        return ip_address
    except Exception as e:
        print(f"Error fetching IP address: {e}")
        return "Unknown"


# Function to generate a unique ID
def generate_unique_id():
    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return f"{timestamp}_{random_string}"


# Main function to get trending topics and save them to the database
def getdata(driver):
    url = "https://x.com/explore/tabs/for-you"

    # Open the Twitter homepage
    driver.get(url)

    try:
        # Wait for the trending section to load (increased wait time)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-testid="trend"]'))
        )

        # Wait for all trend elements to be present (not just the first trend)
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@data-testid="trend"]//span[@dir="ltr"]'))
        )

        # Find all trending topic elements (hashtags or topics)
        trending_elements = driver.find_elements(By.XPATH, '//div[@data-testid="trend"]//span[@dir="ltr"]')

        # Ensure we capture 5 trends, if available
        trends_to_show = trending_elements[:5]  # Get only the first 5 trends

        if len(trends_to_show) < 5:
            print(f"Only {len(trends_to_show)} trending topics found.")
        else:
            print(f"Found 5 trends.")

        # Extract the trending topics
        trend_data = [trend.text for trend in trends_to_show]

        # Get IP address and generate a unique ID
        ip_address = get_ip()
        unique_id = generate_unique_id()

        # Store the trend data in the database
        trend_record = TrendData(
            trend1=trend_data[0],
            trend2=trend_data[1],
            trend3=trend_data[2],
            trend4=trend_data[3],
            trend5=trend_data[4],
            ip_address=ip_address,
            unique_id=unique_id
        )
        trend_record.save()  # Save the record to the database

        # Print the trending topics
        for idx, topic in enumerate(trend_data, 1):
            print(f"Trending #{idx}: {topic}")

    except Exception as e:
        print(f"Error while fetching data: {str(e)}")

