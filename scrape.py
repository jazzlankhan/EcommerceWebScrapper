import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode

# Set up Chrome service
selenium_service = Service('C:\chromedriver-win64\chromedriver.exe')  # Replace with the path to your chromedriver executable

# Set up Chrome driver
driver = webdriver.Chrome(service=selenium_service, options=chrome_options)

def scrape_and_extract(url):
    try:
        driver.get(url)
        time.sleep(2)  # Wait for the page to load, adjust the delay as needed

        # Find review elements using different patterns
        review_elements = []
        patterns = [
            "//div[contains(@class, 'review')]",
            "//p[contains(@class, 'review')]",
            "//span[contains(@class, 'review')]"
        ]
        for pattern in patterns:
            elements = driver.find_elements(By.XPATH, pattern)
            review_elements.extend(elements)

        reviews = []
        if review_elements:
            for element in review_elements:
                review_text = element.get_attribute("innerText").strip()
                if review_text:
                    reviews.append(review_text)

        return reviews

    except Exception as e:
        print(f"Error occurred during the request: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    url = input("Enter the URL: ")
    extracted_reviews = scrape_and_extract(url)
    if extracted_reviews:
        print("Reviews found:")
        for idx, review_text in enumerate(extracted_reviews, start=1):
            print(f"{idx}. {review_text}")
    else:
        print("No reviews found on the page.")