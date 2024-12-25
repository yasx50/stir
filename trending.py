from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getdata(driver):
    url = "https://x.com/explore/tabs/for-you"

    # Open the Twitter homepage
    driver.get(url)

    # Wait for the trending section to load (dynamic content)
    try:
        # Wait until the trending section is visible on the page
        trending_section = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Timeline: Trending now"]'))
        )

        # Find the trending topics inside the section
        trending_topics = trending_section.find_elements(By.XPATH, './/span[contains(@class, "css-901oao")]/span')

        # Print the top 5 trending topics
        # for idx, topic in enumerate(trending_topics[:5], 1):
        #     print(f"Trending #{idx}: {topic.text}")

    except Exception as e:
        print(f"Error while fetching data: {str(e)}")
