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

driver2 = webdriver.Chrome(executable_path=PATH,options=options)
driver2.get("https://www.checkers.co.za/")

# # Function to get all the main cartegories from the checkers website
# def getCategories():
#     # Getting the html tag that holds all the cartegories
#     cartegoriesCarousel = driver.find_element_by_class_name("carousel__component-departments")

#     cartegories = cartegoriesCarousel.find_elements_by_class_name("owl-item")
#     driver.implicitly_wait(5)

#     cartList = []
#     # Looping through each cartegory item ("owl-item") in the whole list of items
#     for cart in cartegories:

#         # If any category times out restart search for cartegories
#         try:
#             departmentName = cart.find_element_by_class_name("department__title")
#             title = departmentName.get_attribute('textContent')
#             cartList.append(title)
#         except:
#             driver.implicitly_wait(0.5)

    
#     # Return a list that holds all the cartegories
#     return cartList

# # Checks whether pagination has reached last page
# def nextPage(drive):
#     output = drive.find_element_by_class_name("sort-refine-bar")
#     print("prettify")
#     soup = BeautifulSoup(output.get_attribute('innerHTML'), "html.parser")
#     next = soup.find(cslass_="pagination-next")
#     next_list = next.get('class')
   
#     if len(next_list) != 1:
#         return False
#     return True

# Clicking on the specific cartegory
productDataObject = ProductData()
shop = Checkers(driver,productDataObject)
shop.getProductInformation(driver)
loop = asyncio.get_event_loop()
testList = loop.run_until_complete(shop.getCategories(driver))
navigate = loop.run_until_complete(shop.gatherCategoryData(driver,testList[7]))
print(testList[0])

# # Define wait condition
# wait = WebDriverWait(driver, 20)

# # Link to go first category
# link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, testList[7])))
# link.click()


# # Link to move to next page in category
# while nextPage(driver):
#     paginationLink = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"pagination-next")))
#     output = driver.find_element_by_class_name("sort-refine-bar")
#     soup = BeautifulSoup(output.get_attribute('innerHTML'), "html.parser")
#     next = soup.find(class_="pagination-next")
#     print(nextPage(driver))
    
#     try:
#         output = driver.find_element_by_class_name("pagination-toolbar")
#     except NoSuchElementException:
#         print("not found "+str(i)) 

#     paginationLink.click()
  
# print("done")

time.sleep(1)
# cartegoriesCarousel = driver.find_element_by_id("gpt-ad-1")


# Define wait condition
# wait = WebDriverWait(driver, 20)

# Link to go first category

# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "row"))
#     )
#     print("element found")
# finally:
#     print("not found")
#     driver.quit()


# product_grid = driver.find_element_by_css_selector("body > main > div.main__inner-wrapper.wrap > div.row > div.col-sm-12.col-md-9 > div.yCmsContentSlot.product-grid-right-result-slot > div > div.product__listing.product__grid")
# products = product_grid.find_elements_by_class_name("item-product")
# # soup = BeautifulSoup(product_grid.get_attribute('innerHTML'), "html.parser")
# # link = soup.find(image_="pagination-next")
# #print(soup.prettify())

# for product in products:
#     image = product.find_element_by_class_name("item-product__image")
#     class_within = image.find_element_by_class_name("product-listening-click")
#     soup = BeautifulSoup(class_within.get_attribute('innerHTML'), "html.parser")
#     image_url = 'https://www.checkers.co.za' + soup.find('img')['src']
    
#     # Finding the name
#     print(image.get_attribute('innerHTML'))
#     print("")
    
  

# try:
#     title = driver.find_element_by_class_name("header js-mainHeader")
# except:
#     print("print")
driver.quit() # Closes the browser tab
driver2.quit()