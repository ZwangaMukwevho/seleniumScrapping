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

class Checkers:

    def __init__(self,driver):
        self.driver = driver

    # Function to get all the main cartegories from the checkers website
    async def getCategories(self,driver):
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
                await driver.implicitly_wait(0.5)
        
        # Return a list that holds all the cartegories
        return cartList

    # Checks whether pagination has reached last page
    async def nextPage(self,driver):
        output = driver.find_element_by_class_name("sort-refine-bar")
        soup = BeautifulSoup(output.get_attribute('innerHTML'), "html.parser")
        next = soup.find(class_="pagination-next")
        next_list = next.get('class')
    
        if len(next_list) != 1:
            return False
        return True

    async def gatherCategoryData(self,driver,category):
        '''Gathers all data from a given category page'''
        wait = WebDriverWait(driver, 20)

        # Link to go first category
        link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, category)))
        link.click()


        # Link to move to next page in category
        while await self.nextPage(driver):
            paginationLink = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"pagination-next")))
            paginationLink.click()
        
        print("done")

    def getProductInformation(self,driver):
        time.sleep(10)
        products = driver.find_element_by_class_name("yCmsComponent product__list--wrapper yComponentWrapper product-grid-right-result-component")
        items = products.find_elements_by_class_name("owl-item")
        for item in items:
            
            print(item.get_attribute('textContent'))