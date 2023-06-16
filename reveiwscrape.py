import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from parsel import Selector

def search_food_near_location(food_type, location):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    query = f"{food_type}+near+{location}"
    driver.get(f"https://www.google.com/maps/search/{query}")

    
    ratings = []
    names = []
    prices = []
    while True:
        new_ratings = driver.find_elements(By.CLASS_NAME, "MW4etd")
        new_ratings = [rating.text for rating in new_ratings]
        ratings += new_ratings

        new_names = driver.find_elements(By.XPATH, "//div[@class='qBF1Pd fontHeadlineSmall ']")
        new_names = [name.text for name in new_names]
        names += new_names

        new_prices = driver.find_elements(By.XPATH, "//span[contains(@aria-label, 'Price: ')]")
        new_prices = [price.text for price in new_prices]
        prices += new_prices

        print(ratings)
        print(names)
        print(prices)

        if len(ratings) < 10 and len(names) < 10 and len(prices) < 10:  # not enough results, scroll down and wait
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        else:
            break

    driver.quit()
    


if __name__ == '__main__':
    print("Food search")
    print("Press 1 to exit at anytime")
    ch = "Y"
    while ch.upper() == 'Y':
        choice = input("Search by food type:")
        if choice != '1':
            location = input("Enter location: ")  # or use geopy to get location coordinates
            if location != "1":
                search_food_near_location(choice, location)
        ch = "N"
