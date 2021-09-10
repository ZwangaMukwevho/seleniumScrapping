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
import csv

class Checkers:
    productDataObject = None
    def __init__(self,driver,productDatObject):
        self.driver = driver
        self.productDatObject = productDatObject

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

    async def gatherCategoryData(self,driver,category,name):
        '''Gathers all data from a given category page'''
        wait = WebDriverWait(driver, 13)

        # Link to go first category
        try:
            link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, category)))
            link.click()
        except:
            self.findCategory(driver,category)

        

        csv_file = open(name,"w")
        csv_writer = csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(['title','imageUrl','Sale Price','Normal Price','sale Type','Promo message','Due date'])

        # Getting the data from individual products using the productData object
        #self.productDatObject.gatherProducts(driver)
        self.productDatObject.gatherProducts(driver,csv_writer)

        # Link to move to next page in category
        while await self.nextPage(driver):
            paginationLink = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"pagination-next")))
            paginationLink.click()
    

            #self.productDatObject.gatherProducts(driver)
            self.productDatObject.gatherProducts(driver,csv_writer)
        
        print("done")
        csv_file.close()

    def getProductInformation(self,driver):
        wait = WebDriverWait(driver, 20)
        products = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/main/div[6]/div[4]/div")))
        items = products.find_elements_by_class_name("owl-item")
        for item in items:
            print(item.get_attribute('textContent'))
    
    def findCategory(self, driver, category):
        """Clicks the pagination next button if category item is not in current page view

        :param driver: selenium driver nativagating the page
        :type driver: Selenium object
        :param category: Category to be searched for
        :type category: String
        """
        wait = WebDriverWait(driver, 5)
        not_found = True
        while(not_found):
            try:
                # Scroll to next cartegories
                paginationLink = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/main/div[6]/div[4]/div/div[1]/div/div[2]/div[3]/i")))
                paginationLink.click()

                # Click link
                link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, category)))
                link.click() 
                return True
            except:
                pass

        return False