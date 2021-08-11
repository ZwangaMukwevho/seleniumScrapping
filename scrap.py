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

import time
from bs4 import BeautifulSoup
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

        # If any category times out restart search for cartegories
        try:
            departmentName = cart.find_element_by_class_name("department__title")
            title = departmentName.get_attribute('textContent')
            cartList.append(title)
        except:
            driver.implicitly_wait(0.5)

    
    # Return a list that holds all the cartegories
    return cartList

# Checks whether pagination has reached last page
def nextPage(drive):
    output = drive.find_element_by_class_name("sort-refine-bar")
    print("prettify")
    soup = BeautifulSoup(output.get_attribute('innerHTML'), "html.parser")
    next = soup.find(class_="pagination-next")
    next_list = next.get('class')
   
    if len(next_list) != 1:
        return False
    return True

# Clicking on the specific cartegory
testList = getCategories()

print(testList[0])

# Define wait condition
wait = WebDriverWait(driver, 20)

# Link to go first category
link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, testList[7])))
link.click()


# Link to move to next page in category
while nextPage(driver):
    paginationLink = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"pagination-next")))
    output = driver.find_element_by_class_name("sort-refine-bar")
    soup = BeautifulSoup(output.get_attribute('innerHTML'), "html.parser")
    next = soup.find(class_="pagination-next")
    print(nextPage(driver))
    
    try:
        output = driver.find_element_by_class_name("pagination-toolbar")
        # output2 = output.find_element_by_class_name("col-xs-12 col-sm-6 col-md-7")
        # print(output)
        # print(output2)
        # print(innerOutput.get_attribute('innerHTML'))
    except NoSuchElementException:
        print("not found "+str(i))

    paginationLink.click()
  
   


# cartegories = cartegoriesCarousel.find_elements_by_class_name("owl-item")
# driver.implicitly_wait(5)

# cartList = []
# action = ActionChains(driver)
# # Looping through each cartegory item ("owl-item") in the whole list of items
# for cart in cartegories:
#     departmentName = cart.find_element_by_class_name("department__image")
#     action.move_to_element(departmentName)
#     action.click()
#     action.perform()
#     break
#     driver.implicitly_wait(5)
    
    



time.sleep(3)
driver.quit() # Closes the browser tab
