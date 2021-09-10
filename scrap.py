from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Imports for explicit waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains

# Import exceptions
from selenium.common.exceptions import NoSuchElementException

# Import async functions
import asyncio

import time
from bs4 import BeautifulSoup
from Checkers import Checkers
from test import ProductData


# Path to chrome driver
PATH = "/mnt/c/Users/zwang/OneDrive/Desktop/Apps/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=PATH,options=options)
driver.get("https://www.checkers.co.za/")


# Clicking on the specific cartegory
productDataObject = ProductData()
shop = Checkers(driver,productDataObject)
loop = asyncio.get_event_loop()

testList = loop.run_until_complete(shop.getCategories(driver))
print(testList[5])
navigate = loop.run_until_complete(shop.gatherCategoryData(driver,testList[5],"food.csv"))

driver.quit() # Closes the browser tab