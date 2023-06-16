import time
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def searchforfood(food_type, location):
    # maybe headless browsing to increase performance?
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # format maps/search/word+word+word/coordinates
    query = f"{food_type}+near+{location}"
    driver.get(f"https://www.google.com/maps/search/{query}")

    
    
    names = []
    ratings = []
    prices = []
    num_ratings = []
    while True:
        new_names = driver.find_elements(By.XPATH, "//div[@class='qBF1Pd fontHeadlineSmall ']")
        new_names = [name.text for name in new_names]
        names += new_names

        new_ratings = driver.find_elements(By.CLASS_NAME, "MW4etd")
        new_ratings = [rating.text for rating in new_ratings]
        ratings += new_ratings

        new_prices = driver.find_elements(By.XPATH, "//span[contains(@aria-label, 'Price: ')]")
        new_prices = [len(price.text) for price in new_prices]
        prices += new_prices

        new_num_ratings = driver.find_elements(By.CLASS_NAME, "UY7F9")
        new_num_ratings = [num_rating.text[1:-1] for num_rating in new_num_ratings]
        num_ratings += new_num_ratings

        # print(ratings)
        # print(names)
        # print(prices)

        if len(ratings) < 10 and len(names) < 10 and len(prices) < 10:  # not enough results, scroll down and wait
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        else:
            break

    driver.quit()
    return names, ratings, prices, num_ratings
    
def write_to_csv(names, ratings, prices):
    with open('./scrape_results.csv', mode='w', newline='', encoding='utf-8') as xcel:
        writer = csv.writer(xcel)
        writer.writerow(['Name', 'Rating', 'Price', 'Num_Ratings'])
        for i in range(len(names)):
            writer.writerow([names[i], ratings[i], prices[i], num_ratings[i]])

if __name__ == '__main__':
    print("Food search")
    print("Press 1 to exit at anytime")
    choice = input("Search by food type:")
    if choice != '1':
        location = input("Enter location: ") 
        if location != "1":
            names, ratings, prices, num_ratings = searchforfood(choice, location)
    write_to_csv(names, ratings, prices)
