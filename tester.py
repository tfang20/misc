import xlwings as xw
from concurrent.futures import ThreadPoolExecutor, as_completed

# Function to perform calculations on a single sheet
def calculate_sheet(sheet):
    sheet.api.Calculate()  # Perform calculation on the sheet
    return f"Calculated sheet: {sheet.name}"

# Main function to process sheets in increments of 4
def concurrent_calculations(sheets):
    results = []
    
    # Process sheets in chunks of 4
    for i in range(0, len(sheets), 4):
        # Get the next batch of 4 sheets (or less if fewer remain)
        batch = sheets[i:i+4]
        
        # Use ThreadPoolExecutor to manage concurrent calculations for each batch
        with ThreadPoolExecutor(max_workers=4) as executor:
            # Submit tasks for each sheet in the batch
            future_to_sheet = {executor.submit(calculate_sheet, sheet): sheet for sheet in batch}
            
            # Collect results as they complete
            for future in as_completed(future_to_sheet):
                sheet = future_to_sheet[future]
                try:
                    result = future.result()
                    results.append(result)
                    print(result)
                except Exception as exc:
                    print(f"{sheet.name} generated an exception: {exc}")

    return results

# Assuming we have a workbook and an array of Sheet objects
if __name__ == "__main__":
    # Open your workbook
    wb = xw.Book('your_workbook.xlsx')
    sheets = wb.sheets  # This gets all sheets in the workbook as Sheet objects
    
    # Call the concurrent calculation function
    concurrent_calculations(sheets)


-----
import xlwings as xw
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Function to perform calculations on a single sheet
def calculate_sheet(sheet_name, workbook):
    sheet = workbook.sheets[sheet_name]
    sheet.api.Calculate()
    return f"Calculated sheet: {sheet_name}"

# Main function to process sheets in increments of 4
def concurrent_calculations(sheet_names, workbook_path):
    # Open the Excel workbook
    wb = xw.Book(workbook_path)

    results = []
    # Process sheets in chunks of 4
    for i in range(0, len(sheet_names), 4):
        # Get the next batch of 4 sheets (or less if fewer remain)
        batch = sheet_names[i:i+4]
        
        # Use ThreadPoolExecutor to manage concurrent calculations for each batch
        with ThreadPoolExecutor(max_workers=4) as executor:
            # Submit tasks for each sheet in the batch
            future_to_sheet = {executor.submit(calculate_sheet, sheet, wb): sheet for sheet in batch}
            
            # Collect results as they complete
            for future in as_completed(future_to_sheet):
                sheet_name = future_to_sheet[future]
                try:
                    result = future.result()
                    results.append(result)
                    print(result)
                except Exception as exc:
                    print(f"{sheet_name} generated an exception: {exc}")

    # Close the workbook if needed
    # wb.close()

    return results

# List of sheet names
sheet_names = [f"Sheet{i+1}" for i in range(33)]  # Example sheet names "Sheet1" to "Sheet33"

# Execute concurrent calculations in increments of 4
if __name__ == "__main__":
    workbook_path = 'your_workbook.xlsx'  # Replace with your actual workbook path
    concurrent_calculations(sheet_names, workbook_path)



--1---

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
