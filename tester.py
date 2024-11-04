import xlwings as xw
import pandas as pd
from multiprocessing import Pool

# Function to calculate a single sheet
def calculate_sheet(sheet_name, file_path="path_to_your_file.xlsx"):
    # Open Excel workbook
    wb = xw.Book(file_path)
    
    # Get the specific sheet
    sheet = wb.sheets[sheet_name]
    
    # Calculate the sheet
    sheet.calculate()
    
    # Optionally, read the data back into a DataFrame
    data = sheet.range("A1:B10").options(pd.DataFrame, header=1, index=False).value
    
    # Close workbook
    wb.close()
    
    print(f"Calculation done for {sheet_name}")
    return data

# Function to calculate multiple sheets using a process pool
def calculate_multiple_sheets_in_parallel(sheet_names, file_path="path_to_your_file.xlsx", num_processes=4):
    # Use a process pool to limit the number of parallel processes
    with Pool(processes=num_processes) as pool:
        # Each sheet calculation runs in a separate process
        pool.starmap(calculate_sheet, [(sheet, file_path) for sheet in sheet_names])

# List of sheet names to calculate
sheet_names = ["Sheet1", "Sheet2", "Sheet3"]

# Run the calculation in parallel
if __name__ == "__main__":
    calculate_multiple_sheets_in_parallel(sheet_names)
-----------




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
