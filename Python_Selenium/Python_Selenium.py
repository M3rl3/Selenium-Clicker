import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

# Counter for number of iterations
count = 0

# Set a custom chrome browser executable
binary_location = "C:\\Program Files\\Chromium\\chrome.exe"

# Set a custom chrome-driver executable
chrome_driver_location = "./chromedriver.exe"

# Create a new options variable
options = Options()

# Set initial conditions
options.binary_location = binary_location
driver = webdriver.Chrome(options=options)
driver.get("https://hiring.amazon.ca/app#/login")

# Set flags
options.add_argument("--remote-debugging-port=9515")
# options.add_argument("--enable-chrome-browser-cloud-management")
# options.add_argument("--no-sandbox")

# Give the user some time to login to Amazon Jobs and deal with pop-ups (in secs)
time.sleep(60.0)

# Main loop that clicks && reloads
while (True):
    
    # Counter that increments per iteration
    count += 1
    
    # Try to click the button
    try:
        print("\n\nTest Iteration: ", count)
        
        # Check if the current URL is the same as required
        if (driver.current_url != "https://hiring.amazon.ca/jobDetail/en-CA/Amazon-Fulfilment-Centre-Warehouse-Associate/Barrhaven/a0R4U00000FSE2gUAH#/jobDetail?jobId=a0R4U00000FSE2gUAH&locale=en-CA&seoIndex=1"):
            driver.get("https://hiring.amazon.ca/jobDetail/en-CA/Amazon-Fulfilment-Centre-Warehouse-Associate/Barrhaven/a0R4U00000FSE2gUAH#/jobDetail?jobId=a0R4U00000FSE2gUAH&locale=en-CA&seoIndex=1")
            
        button = WebDriverWait(driver, 10).until(Ec.element_to_be_clickable((By.XPATH, "//*[@id='pageRouter']/div/div[2]/div[1]/div[3]/button[2]")))
        button.click()
        
        # Check if the button was clicked
        # try:    
            
        #     # Wait for the new element to appear
        #     new_element = WebDriverWait(driver, 10).until(Ec.visibility_of_element_located((By.XPATH, "//div[@id='new-element']")))
        #     print("Button clicked successfully.")
        
        # finally:
            
        #     # Button wasn't clicked
        #     print("Button click failed.")
    
    # Rinse && repeat
    except Exception as Ex:
        
         # Print stack trace
        print("\nButton click failed.\nContinuing...\n")
        print(Ex)
        
        # Refresh the page
        driver.refresh()
         
    # finally:
    #     driver.quit()    