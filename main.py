from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  # Import Service class

# Replace with your credentials
USERNAME = "_yash_yadav__"
PASSWORD = "yash8055"

# Start the WebDriver
options = Options()
options.add_argument("--disable-extensions")

# Optionally, specify the path to your Chrome browser if it's not in the default location
options.binary_location = "C:\chrome-headless-shell-win64/chrome.exe"  # Adjust path if necessary

# Create a Service object
# service = Service(ChromeDriverManager().install())

# Use the ChromeDriverManager to automatically install the correct version of chromedriver
driver = webdriver.Chrome( options=options)
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

    # Navigate to the "Trending" page
    driver.get("https://x.com/explore/tabs/trending")

    # Wait for the trending section to load
    trending_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//section[@aria-labelledby='accessible-list-2']"))
    )

    # Find and print the top 5 trending topics using the correct CSS class
    trending_topics = trending_section.find_elements(By.CSS_SELECTOR, "div.css-1dbjc4n.r-18u37iz.r-thb0q2.r-1jgb49r.r-1v0dtai")
    
    # If there are at least 5 trending topics
    for idx, topic in enumerate(trending_topics[:5], 1):
        print(f"Trending #{idx}: {topic.text}")

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
