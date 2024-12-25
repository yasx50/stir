
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 

def getdata(driver):
    

    url = "https://x.com/explore/tabs/for-you"

    driver.get(url)


    trending_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "react-root"))
    )

    
    trending_topics = trending_section.find_elements(By.CSS_SELECTOR, "div.css-1dbjc4n.r-18u37iz.r-thb0q2.r-1jgb49r.r-1v0dtai")
    
    # If there are at least 5 trending topics
    for idx, topic in enumerate(trending_topics[:5], 1):
     print(f"Trending #{idx}: {topic.text}")

    driver.quit()