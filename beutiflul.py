from bs4 import BeautifulSoup
import requests
import csv
import database
import mysql.connector

#with open(r'C:\Users\zwang\OneDrive\Desktop\code\New folder\sample.html') as html_File:

# Function to scrap data from the internet from the pick n pay website
def scrap(link):
    source = requests.get(link).text
    soup = BeautifulSoup(source,'lxml')

    return soup

    


def pinknpay(url,name):
    scrapObject = scrap(url)
    
    article = scrapObject.find('main')
    product = article.find('div',class_='product-price')
    
    #name = name+".csv"
    sqlobject = database.mysqlConnect("localhost","root",'v4469ZWA5569MUK#',"test")

    mycursor = sqlobject.cursor()
    #csv_file = open(name,"w")
    #csv_writer = csv.writer(csv_file,delimiter=',')
    #csv_writer.writerow(['title','Current Price','Previous Price','image url'])
    
    # For loop to go through all the Products and extract the title, current and previous price of the product
    for productContainer in article.find_all('div',class_='productCarouselItem js-product-carousel-item'):

        # Exctracting data from the scrapObject
        currentPrice = productContainer.find('div',class_="currentPrice hasSavings").text.strip()
        previousPrice = productContainer.find('div',class_="oldPrice").text.strip()
        imageurl = productContainer.find('div',class_="thumb")
        imageurl = productContainer.find('img')['src']
        title = productContainer.find('div',class_='item-name').text
    
        # Formatting the price
        currentPrice = currentPrice[:-2:]+"."+currentPrice[len(currentPrice)-2::]
        previousPrice = previousPrice[:-2:]+"."+previousPrice[len(previousPrice)-2::]

        #csv_writer.writerow([title,currentPrice,previousPrice,imageurl])
        #print(imageurl)

        # Writing to the database
      

        # SQL insert query
        query  = "insert into frozenfood(title,currentprice,previousprice,imageurl) values(%s,%s,%s,%s)"
        val = (title,currentPrice,previousPrice,imageurl)

        mycursor.execute(query,val)

    sqlobject.commit()
    
    #csv_file.close()

# PicknPay links
freshFoodurl = 'https://www.pnp.co.za/pnpstorefront/pnp/en/All-Products/Fresh-Food/c/fresh-food-423144840?q=%3Arelevance%3AisOnPromotion%3AOn+Promotion&text=&pageSize=18#'
cupboardUrl = 'https://www.pnp.co.za/pnpstorefront/pnp/en/All-Products/Food-Cupboard/c/food-cupboard-423144840?q=%3Arelevance%3AisOnPromotion%3AOn+Promotion&text=&pageSize=18#'
healthAndBeauryUrl = 'https://www.pnp.co.za/pnpstorefront/pnp/en/All-Products/Health-%26-Beauty/c/health-and-beauty-423144840?q=%3Arelevance%3AisOnPromotion%3AOn+Promotion&text=&pageSize=18#'
petsUrl = 'https://www.pnp.co.za/pnpstorefront/pnp/en/All-Products/Home-%26-Outdoor/Pets/c/pets-517886608?q=%3Arelevance%3AisOnPromotion%3AOn+Promotion&text=&pageSize=18#'
electronicsAndOfficeUrl = 'https://www.pnp.co.za/pnpstorefront/pnp/en/All-Products/Electronics-%26-Office/c/electronics-and-office-423144840?q=%3Arelevance%3AisOnPromotion%3AOn+Promotion&text=&pageSize=18#'
frozenFoodUrl = 'https://www.pnp.co.za/pnpstorefront/pnp/en/All-Products/Frozen-Food/c/frozen-food-423144840?q=%3Arelevance%3AisOnPromotion%3AOn+Promotion&text=&pageSize=18#'

name1 = "picknpayFrozenFood"
pinknpay(frozenFoodUrl,name1)