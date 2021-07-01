from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Imports for explicit waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains

import time

# Path to chrome driver
PATH = "/mnt/c/Users/zwang/OneDrive/Desktop/Apps/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=PATH,options=options)
driver.get("https://www.checkers.co.za/")

# Function to get all the main cartegories from the checkers website
def getCategories():
    # Getting the html tag that holds all the cartegories
    cartegoriesCarousel = driver.find_element_by_class_name("carousel__component-departments")

    cartegories = cartegoriesCarousel.find_elements_by_class_name("owl-item")
    driver.implicitly_wait(5)

    cartList = []
    # Looping through each cartegory item ("owl-item") in the whole list of items
    for cart in cartegories:
        departmentName = cart.find_element_by_class_name("department__title")
        # print("cartegories ",departmentName.get_attribute('textContent'))
        cartList.append(departmentName.get_attribute('textContent'))
    
    # Return a list that holds all the cartegories
    return cartList

# Clicking on the specific cartegory
testList = getCategories()
print(testList)
#rint(testList)
# link = driver.find_element_by_link_text(testList[0])
# link.click()
cartegoriesCarousel = driver.find_element_by_class_name("carousel__component-departments")

cartegories = cartegoriesCarousel.find_elements_by_class_name("owl-item")
driver.implicitly_wait(5)

cartList = []
action = ActionChains(driver)
# Looping through each cartegory item ("owl-item") in the whole list of items
for cart in cartegories:
    departmentName = cart.find_element_by_class_name("department__image")
    action.move_to_element(departmentName)
    action.click()
    action.perform()
    break
    driver.implicitly_wait(5)
    
    



time.sleep(3)
driver.quit() # Closes the browser tab

# with open('/mnt/c/Users/zwang/OneDrive/Desktop/Apps/tests.txt') as f:
#     print(f.readlines())