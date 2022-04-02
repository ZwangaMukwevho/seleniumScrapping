from test import ProductData
from Checkers import Checkers


from selenium import webdriver
from bs4 import BeautifulSoup
import time
PATH = "/mnt/c/Users/zwang/OneDrive/Desktop/Apps/chrome_driver/test/chromedriver.exe"
driver = webdriver.Chrome(PATH)
time.sleep(2)
# driver.get("https://www.checkers.co.za/c-2413/All-Departments/Food")
# objects = driver.find_element_by_xpath("/html/body/main/div[4]/div[1]/div[2]")
# product_grid = driver.find_element_by_css_selector("body > main > div.main__inner-wrapper.wrap > div.row > div.col-sm-12.col-md-9 > div.yCmsContentSlot.product-grid-right-result-slot > div > div.product__listing.product__grid")
# products = product_grid.find_elements_by_class_name("item-product")

newObj = ProductData()
info = newObj.gatherProducts()

shop = Checkers(driver)
