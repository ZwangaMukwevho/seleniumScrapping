from selenium import webdriver
from bs4 import BeautifulSoup
import time

class ProductData():
    def __init__(self):
        pass

    def findProductDetailsSoup(self,Product):
        '''
        returns beautifulSoup objects for product caption html section
        '''
        caption = Product.find_element_by_class_name("item-product__details")
        return BeautifulSoup(caption.get_attribute('innerHTML'), "html.parser")

    def findDueDate(self,soup):
        ''' Find the due date of the promotion
        '''
        valid_until = soup.find(class_="item-product__valid")

        dueDate = ""
        if valid_until != None:
            dueDate = str(valid_until.text).strip()
        return dueDate

    def findPromotionMessage(self,soup):
        '''
        Gets the type of promotion on the product 
        '''
        message_soup = soup.find(class_="js-item-product__message")
        if message_soup != None:
            message = message_soup.find(class_="item-product__message__text")
            return message.text.strip()
        return ""

    def productTitleandUrlObject(self,Product):
        '''
        Gets the selenium object to be used in findImageUrl(Product) function and findTile(Product) function
        '''
        image = Product.find_element_by_class_name("item-product__image")
        class_within = image.find_element_by_class_name("product-listening-click")
        return class_within

    def findImageUrl(self,Product):
        '''
        Gets the image Url from the product
        '''
        class_within = self.productTitleandUrlObject(Product)
        soup = BeautifulSoup(class_within.get_attribute('innerHTML'), "html.parser")
        image_url = 'https://www.checkers.co.za' + soup.find('img')['src']
        return image_url
            
    def findTitle(self,Product):
        '''
        Gets the product title
        '''
        class_within = self.productTitleandUrlObject(Product)
        title = class_within.get_attribute("title")
        return title

    def getPrices(self,Product):
        '''
        Get price of the product
        '''
        product_caption = Product.find_element_by_class_name("js-item-product-price") 
        soup = BeautifulSoup(product_caption.get_attribute('innerHTML'), "html.parser")

        # Current Price
        curr_price = soup.find(class_="now")
        current_price = curr_price.text

        previous_price_bool = soup.find(class_="before")
        
        sale_price = ""

        if previous_price_bool != None:
            # print("not true")
            sale_price = current_price
            current_price = previous_price_bool.text

        return [str(sale_price).strip(),str(current_price).strip()]
        
    def getSaleType(self,Product):
        '''
        Determines if ther's a sale promotion and gives type of sale
        '''
        savings_class = BeautifulSoup(Product.get_attribute('innerHTML'),"html.parser")
        saving_soup = savings_class.find(class_="item-product__options item-product__options--right")
        
        if saving_soup != None:
            extra_saving = saving_soup.find(class_="product-option product-option--xtra-savings")
            if extra_saving != None:
                return "Extra Savings"
            
            normal_saving = saving_soup.find(class_="product-option product-option--save")
            if normal_saving != None:
                return "Normal Sale"
        
        return "None"

    def gatherProducts(self):

        PATH = "/mnt/c/Users/zwang/OneDrive/Desktop/Apps/chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        time.sleep(2)
        driver.get("https://www.checkers.co.za/c-2413/All-Departments/Food")
        objects = driver.find_element_by_xpath("/html/body/main/div[4]/div[1]/div[2]")
        product_grid = driver.find_element_by_css_selector("body > main > div.main__inner-wrapper.wrap > div.row > div.col-sm-12.col-md-9 > div.yCmsContentSlot.product-grid-right-result-slot > div > div.product__listing.product__grid")
        products = product_grid.find_elements_by_class_name("item-product")

        count = 1
        for product in products:
            print("product "+str(count))
            count += 1  
            imageUrl = self.findImageUrl(product)
            title = self.findTitle(product)
            
            print("title: "+title)
            priceList = self.getPrices(product)
            print("Sale prices: "+priceList[0])
            print("Current price: "+priceList[1])

            saleType = self.getSaleType(product)
            print("Sale Type: "+saleType)

            captionSoup = self.findProductDetailsSoup(product)
            DueDate = self.findDueDate(captionSoup)
            promotionMessage = self.findPromotionMessage(captionSoup)
            print("Due date: "+str(DueDate))
            print("promotionMessage: "+str(promotionMessage))
            print("")

        driver.quit()

