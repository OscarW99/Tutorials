# TODO...
# add confidence level to the tuple
# Modify it to loop through countries and job titles.


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Path to your ChromeDriver executable
chromedriver_path = r'C:\Users\Oscar Wright\Downloads\chromedriver_win32\chromedriver.exe'
# URL of the Glassdoor page
url = "https://www.glassdoor.com/Salaries/us-bioinformatics-scientist-salary-SRCH_IL.0,2_IN1_KO3,27.htm"

# Configure ChromeDriver options
chrome_options = Options()
chrome_options.add_argument("--disable-popup-blocking")
# chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Set up ChromeDriver service
service = Service(chromedriver_path)

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.implicitly_wait(10)

# Navigate to the Glassdoor page
driver.get(url)

# Find the dropdown toggle element
toggle_element = driver.find_element("css selector", 'div[data-test="occ-median-filters-desktop-experience-dropdownContent"] .selectedLabel')
# Click on the toggle element to open the dropdown
toggle_element.click()
option_elements = driver.find_elements("css selector", 'div[data-test="occ-median-filters-desktop-experience-dropdownContent"] span')
years_of_experience_options = [option.text.strip() for option in option_elements]
years_of_experience_options = [option for option in years_of_experience_options if option != '']

data = []

for option in years_of_experience_options:
    # Find the dropdown menu element
    dropdown_element = driver.find_element("css selector", 'div[data-test="occ-median-filters-desktop-experience-dropdownContent"]')
    # Find the toggle element within the dropdown menu
    toggle_element = dropdown_element.find_element("css selector", '.selectedLabel')
    # Click on the toggle element to select it
    toggle_element.click()
    # Find the option element within the dropdown menu
    option_element = dropdown_element.find_element("xpath", f".//span[contains(., '{option}')]")
    # Use JavaScript to modify the dropdown's value directly
    driver.execute_script("arguments[0].setAttribute('aria-selected', 'true')", option_element)
    driver.execute_script("arguments[0].click()", option_element)
    time.sleep(2)  # Add a short delay to allow the page to update
    # Use JavaScript to retrieve the salary values
    salary_values = driver.execute_script(
        'return Array.from(document.querySelectorAll("span[data-test=\'formatted-pay\']")).map(el => el.innerText.trim())'
    )
    # Iterate over the salary values and print them
    for salary in salary_values:
        data.append((option, salary))
        print(salary)
    print("-" * 30)
    
