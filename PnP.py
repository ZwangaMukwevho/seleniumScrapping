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
# driver.get("https://www.pnp.co.za/pnpstorefront/pnp/en/All-Products/Bakery/c/bakery-423144840?q=%3Arelevance&pageSize=72&page=0")

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
        wait = WebDriverWait(driver, 10)
        try:
            wait = WebDriverWait(driver, 10)
            CategoryPageLink = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"myModal\"]/div/div/div[3]/button[2]")))
            CategoryPageLink.click()
         

            return True
        except :
            return False

    def collectCategories(self,driver):
        """Collects all the categories that in the Pick n Pay website

        :param driver: Driver 
        :type driver: Selenium object
        """

        wait = WebDriverWait(driver, 20)

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
        checkBool = False
        while(not checkBool):
            try:
                checkBool = self.AcceptCookies(driver)
            except :
                pass    
    
    def goToCategory(self,driver,category,wait):
        """
        Clicks the category name given from the category page
        """
        link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, category)))
        link.click()
    
    def changeView(self,driver,wait):
        """
        Viewing more products

        :param driver: [description]
        :type driver: [type]
        """
        self.changeWindowWidth(driver, 1284)
        more = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"sortFormPagination\"]/div/div[2]/div/div[1]/div/div[2]/b")))
        more.click()
        show72 = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"sortFormPagination\"]/div/div[2]/div/div[1]/div/div[3]/div[1]/ul/li[4]")))
        show72.click()

    
    def changeWindowWidth(self,driver,width):
        """Changes the window width

        :param driver: Driver 
        :type driver: Selenium object
        """
        size = driver.get_window_size()
        driver.set_window_size(width, size['height'])
    
    def getProductsData(self,driver):
        """Collects the data from an individual product

        :param driver: [description]
        :type driver: [type]
        """
        return False
    
    def browseProducts(self,driver):
        """Browse through all the products in a single page

        :param driver: Driver 
        :type driver: Selenium object
        """
        wait = WebDriverWait(driver, 10)
        productsContainer = driver.find_element_by_xpath("/html/body/main/div[4]/div[2]/div/div[1]/div[3]/div[2]/div[2]/div/div[1]/ul")
        # products = productsContainer.find_elements_by_id("productCarouselItemContainer_000000000000672899_EA")
        
        # print(productsContainer.get_attribute("innerHTML"))
        # products = productsContainer.find_elements_by_xpath("//div[@class='productCarouselItemContainer']//div[@class='productCarouselItem js-product-carousel-item']//")
        products = productsContainer.find_elements_by_xpath("//div[@class='productCarouselItemContainer']//div[@class='productCarouselItem js-product-carousel-item']//div[@class='item js-product-card-item  product-card-grid']")
        print(len(products))
        # Looping through the 
        count = 0
        for product in products:
            print("product "+str(count))
            ProductimageUrl = self.findImageUrl(product)
            ProductTitle =  self.findImageTitle(product)
            productPrice =  self.findProductPrice(product)
            productPromotion = self.getProductPromotion(product)
            print("product title: "+str(ProductTitle))
            print("Product price: "+str(productPrice))
            print("product image url: "+str(ProductimageUrl))
            print("product promotion"+str(productPromotion))
            print("")
            count = count + 1
            
            # if count == 5:
            #     print("product "+str(count))
            #     ProductimageUrl = self.findImageUrl(product)           
            # #     ProductimageUrl = self.findImageUrl(product)
            # #     ProductTitle =  self.findImageTitle(product)
            # #     productPrice =  self.findProductPrice(product)
            # #     # print(product.get_attribute('innerHTML'))
            # #     productPromotion = self.getProductPromotion(product)
            #     break
        # self.paginationNext(driver)

    def getProductName(self,driver,product):
        """Returns name of product

        :param driver: [description]
        :type driver: [type]
        """
        name = product.find_elements_by_class("item-name")
        # print(name)
        return name
    
    def findImageUrl(self,productElement):
        """Finds the image URL for the product

        :param productElement: [Product element passed in from browseProducts function]
        :type productElement: [Selenium element]
        :return: [Image URL of the product]
        :rtype: [String]
        """
        imageClass = productElement.find_element_by_class_name("thumb")
        # Using beautiful soup
        soup = BeautifulSoup(imageClass.get_attribute('innerHTML'), "html.parser")
        imageUrl = soup.find('img')['src']
        return imageUrl
    
    def findImageTitle(self,productElement):
        titleClass = productElement.find_element_by_class_name("item-name")
        # print(titleClass.text)
        return titleClass.text
        # print(titleClass.get_attribute('innerHTML'))
    
    def findProductPrice(self,productElement):
        priceClass = productElement.find_element_by_class_name("product-price")
        priceSubClass = priceClass.find_element_by_class_name("item-price")
        currentPriceClass = priceSubClass.find_element_by_class_name("currentPrice  ")
        
        currentPrice = str(currentPriceClass.text)
        currentPrice = currentPrice[:-2]+"."+currentPrice[-2:]
        # print(currentPrice)
        return currentPrice
    
    def getProductPromotion(self,productElement):
        promotionClass = productElement.find_element_by_id("promotionContainer")
        # print(promotionClass.text)
        return promotionClass.text
    
    def paginationNext(self,driver):
        next = driver.find_element_by_xpath("/html/body/main/div[4]/div[2]/div/div[1]/div[3]/div[2]/div[2]/div/div[1]/div[4]/div/div[2]/div[2]")
        nextButton = next.find_element_by_class_name('pagination-next')
        nextButton.click()
        
    
    def paginationNextt(self,driver):
        next = driver.find_element_by_xpath("/html/body/main/div[4]/div[2]/div/div[1]/div[3]/div[2]/div[2]/div/div[1]/div[4]/div/div[2]/div[2]")
        paginationClass = next.find_element_by_class_name('pagination')
        uClass = paginationClass.find_element_by_xpath("//li[4]")

        soup = BeautifulSoup(paginationClass.get_attribute('innerHTML'), "html.parser")
        lastPage = soup.find("li",class_="pagination-next disabled")
        print(lastPage)
        if lastPage != None:
            print("retruened true")
            return False
        print("returned false")
        return True  
    
    def collectData(self,driver):
        count = 0
        self.browseProducts(driver)
        while(self.paginationNextt(driver)):
            self.paginationNext(driver)
            self.browseProducts(driver)

pnp = PnP()
time.sleep(4)
pnp.AcceptCookies(driver)
categories_list = pnp.collectCategories(driver)
wait = WebDriverWait(driver, 10)
pnp.goToCategory(driver,categories_list[1],wait)
pnp.changeView(driver,wait)
pnp.collectData(driver)



time.sleep(2)

driver.quit()
