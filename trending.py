from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getdata(driver):
    url = "https://x.com/explore/tabs/for-you"

    # Open the Twitter homepage
    driver.get(url)

    # Wait for the trending section to load (dynamic content)
    try:
        # Wait until the trending section is visible on the page
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-testid="trend"]'))
        )

        # Find all trending topic elements (hashtags or topics)
        trending_elements = driver.find_elements(By.XPATH, '//div[@data-testid="trend"]//span[@dir="ltr"]')

        # Ensure we capture 5 trends, if available
        trends_to_show = trending_elements[:5]  # Get only the first 5 trends

        # Loop through and print the first 5 trending elements
        for idx, trend in enumerate(trends_to_show, 1):
            try:
                # Extract the topic name (Hashtag or phrase)
                topic = trend.text

                # Print the trending topic
                print(f"Trending #{idx}: {topic}")
            except Exception as e:
                print(f"Error parsing trend #{idx}: {str(e)}")

        # If there are fewer than 5 trends, print a message indicating this
        if len(trends_to_show) < 5:
            print(f"Only {len(trends_to_show)} trending topics found.")

    except Exception as e:
        print(f"Error while fetching data: {str(e)}")
