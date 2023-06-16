import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def search_food_near_location(food_type, location):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    query = f"{food_type}+near+{location}"
    driver.get(f"https://www.google.com/maps/search/{query}")

    ratings = []
    names = []
    while True:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        new_ratings = soup.find_all('div', {'class': 'MW4etd'})
        new_ratings = [rating.text for rating in new_ratings]
        ratings += new_ratings

        new_names = soup.find_all('div', {'class': 'qBF1Pd fontHeadlineSmall '})
        new_names = [name.text for name in new_names]
        names += new_names

        print(ratings)
        print(names)

        if len(ratings) < 10 and len(names) < 10:  # not enough results, scroll down and wait
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
