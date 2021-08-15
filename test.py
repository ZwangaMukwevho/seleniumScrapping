from selenium import webdriver
import time

PATH = "/mnt/c/Users/zwang/OneDrive/Desktop/Apps/chromedriver.exe"
driver = webdriver.Chrome(PATH)
time.sleep(5)
driver.get("https://www.checkers.co.za/c-2413/All-Departments/Food")
# objects = driver.find_element_by_xpath("/html/body/main/div[4]/div[1]/div[2]")
product_grid = driver.find_element_by_css_selector("body > main > div.main__inner-wrapper.wrap > div.row > div.col-sm-12.col-md-9 > div.yCmsContentSlot.product-grid-right-result-slot > div > div.product__listing.product__grid")
products = product_grid.find_elements_by_class_name("item-product")
for product in products:
    image_url = product.find_element_by_class_name("item-product__image")
    print(image_url.get_attribute('textContent'))
    #print(product.text)
#
driver.quit()