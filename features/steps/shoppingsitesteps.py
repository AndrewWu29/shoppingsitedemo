import time

from behave import *
from selenium import webdriver

@given('I add four different products to my wish list')
def addFourDiffItemsToWishList(context):
   context.driver = webdriver.Chrome(executable_path="D:/chromedriver_win32/chromedriver.exe")
   context.driver.get("https://testscriptdemo.com/")
   context.driver.find_element_by_xpath("//*[@id='cc-window']/div[5]/a[1]").click()
   time.sleep(2)
   context.driver.find_element_by_link_text("Shop").click()
   time.sleep(2)
   context.driver.find_element_by_xpath("//*[@id='site-content']/div/div/article/ul/li[1]/div/div[2]/div/div/a").click()
   time.sleep(2)
   context.driver.find_element_by_xpath("//*[@id='site-content']/div/div/article/ul/li[2]/div/div[2]/div/div/a").click()
   time.sleep(2)
   context.driver.find_element_by_xpath("//*[@id='site-content']/div/div/article/ul/li[3]/div/div[2]/div/div/a").click()
   time.sleep(2)
   context.driver.find_element_by_xpath("//*[@id='site-content']/div/div/article/ul/li[4]/div/div[2]/div/div/a").click()
   time.sleep(2)

@when('I view my wishlist table')
def viewWishlist(context):
   context.driver.find_element_by_xpath("//*[@id='blog']/div[3]/div[1]/div/div/div[3]/div[3]/a").click()
   time.sleep(2)

@then('I find total selected items in my Wishlist')
def checkWishlistItems(context):
    context.driver.find_elements_by_partial_link_text("Evening trousers")
    context.driver.find_elements_by_partial_link_text("Black trousers")
    context.driver.find_elements_by_partial_link_text("Black pants")
    context.driver.find_elements_by_partial_link_text("Bikini")
    time.sleep(2)

@when('I search for lowest price product')
def searchForLowestPriceProduct(context):
    context.driver.find_element_by_link_text("Shop").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//*[@id='site-content']/div/div/article/ul/li[1]/a[1]/span[2]/ins/span/bdi/span").click()
    time.sleep(2)

@when('I am able to add the lowest price item to my cart')
def addTheLowestPriceItemToMyCart(context):
    context.driver.find_element_by_xpath("//*[@id='product-22']/div[2]/form/button[3]").click()
    time.sleep(2)


@then('I am able to verify the item in my cart')
def verifyItemInMyCart(context):
    context.driver.get("https://testscriptdemo.com/?page_id=299")
    time.sleep(2)
    verifyitemname = "Bikini"
    itemname = context.driver.find_element_by_xpath("//*[@id='site-content']/div/div/article/div/div/div[1]/div/form/table/tbody/tr[1]/td[3]/a")
    print(itemname.text)
    assert verifyitemname == itemname.text
    context.driver.close()


