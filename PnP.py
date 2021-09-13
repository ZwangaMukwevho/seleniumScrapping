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

PATH = "/mnt/c/Users/zwang/OneDrive/Desktop/Apps/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=PATH,options=options)
driver.get("https://www.pnp.co.za/pnpstorefront/pnp/en/All-Products/c/pnpbase")

class PnP:
    productDataObject = None
    #def __init__(self,driver,productDataObject):
    def __init__(self):
        pass
        #self.productDatObject = productDataObject
    
    def AcceptCookies(self,driver):
        """Accepts cookies from the promt that shows

        :param driver: [description]
        :type driver: [type]
        """
        try:
            wait = WebDriverWait(driver, 10)
            CategoryPageLink = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"myModal\"]/div/div/div[3]/button[2]")))
            CategoryPageLink.click()
            return False
        except :
            return True

    def collectCategories(self,driver):
        """Collects all the categories that in the Pick n Pay website

        :param driver: Driver 
        :type driver: Selenium object
        """

        wait = WebDriverWait(driver, 10)

        # Get HTML segment with h4 category tags embedded
        CategoryPageLink = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/main/div[4]/div/div[4]/div/div[3]/div/div/div")))
        categories = CategoryPageLink.find_elements_by_xpath("//div[@class='col-sm-2 col-xs-4 aisle-tile']")
        
        categoriesList = []

        # Loop through all the cartegories
        for category in categories:
        
            soup = BeautifulSoup(category.get_attribute("innerHTML"), "html.parser")
            title =  category.find_element_by_css_selector("h4")
        
            # Check using beautiful soup to check if the category htlm tags are done
            try:   
                check = soup.find('img')['class'] #b4
            except KeyError:
                break
                
            categoriesList.append(title.text)
            
        return categoriesList

    def pressAccept(self,driver):
        """Presses the accept cookies when occurs

        :param driver: [description]
        :type driver: [type]
        """
        checkBool = True
        while(checkBool):
            try:
                checkBool = self.AcceptCookies(driver)
            except :
                pass


pnp = PnP()
pnp.AcceptCookies(driver)
categories_list = pnp.collectCategories(driver)
print(categories_list)

driver.quit()
