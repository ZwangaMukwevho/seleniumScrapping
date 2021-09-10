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
        CategoryPageLink = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/main/div[4]/div/div[4]/div/div[3]/div/div/div")))
        soup = BeautifulSoup(CategoryPageLink.get_attribute('innerHTML'), "html.parser")
        #print(soup.prettify())
        categories = CategoryPageLink.find_elements_by_xpath("//div[@class='col-sm-2 col-xs-4 aisle-tile']")
        
        for category in categories:
            # print(category.get_attribute("innerHTML"))
            soup = BeautifulSoup(category.get_attribute("innerHTML"), "html.parser")
            title = category.find_element_by_xpath("//h4")
            print(title.get_attribute("textContent"))
            print("")

        #CategoryPageLink = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/main/header/div[2]/div/nav/ul[2]/li[1]/a")))
        # categoriesContainer = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/main/div[4]/div/div[4]/div/div[3]")))
        # categories = categoriesContainer.find_elements_by_class_name("col-sm-2 col-xs-4 aisle-tile")
        
        # soup = BeautifulSoup(categoriesContainer.get_attribute('innerHTML'), "html.parser")
        # containers = soup.find_all('div',class_='col-sm-2 col-xs-4 aisle-tile') # bs4
        
        # print(len(categories))
        # count = 0
        # for category in categories:
        #     print(count)
        #     count += 1
        #     soup = BeautifulSoup(category.get_attribute('innerHTML'), "html.parser")
        #     print(soup.prettify())

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
pnp.collectCategories(driver)

driver.quit()
