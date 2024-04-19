from cProfile import label
import time

from sys import executable
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

binary_location = "C:/Program Files/Chromium/"
chrome_driver_location = "./chromedriver.exe"

options = Options()
options.binary_location = binary_location
options.add_argument("--enable-chrome-browser-cloud-management")
options.add_argument("--remote-debugging-port=9515")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)
driver.get("https://hiring.amazon.ca/jobDetail/en-CA/Amazon-Fulfilment-Centre-Warehouse-Associate/Barrhaven/a0R4U00000FSE2gUAH#/jobDetail?jobId=a0R4U00000FSE2gUAH&locale=en-CA&seoIndex=1")

# button = driver.find_element(By.XPATH, "//*[@id='596738822']/span")
# button = driver.find_element(By.XPATH, "//*[@id='pageRouter']/div/div[2]/div[1]/div[3]/button[2]")
# button = driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[1]/div/div[2]/header/div/div/div[2]/button/div")
# button.click()

count = 0
str = ""
time.sleep(5.0)

while (count < 1):
    count+=1
    try:
        button = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[@id='pageRouter']/div/div[2]/div[1]/div[3]/button[2]")))
        button.click()
    except Exception as Ex:
        driver.refresh()
        print(Ex)
else:
    while (1):
        print("Continue? Y/n")
        str = input().lower()
        if str == "n":
            exit()
        elif str == "y" or str == "":
            count = 0
            break
        else:
            print("Invalid Response")    
            continue

driver.quit()

str = "\nYou either die a buddy or you live long enough to see yourself become the retard."
print(str)
