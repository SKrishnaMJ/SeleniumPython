import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CLASS_NAME,'search-keyword').send_keys('to')
time.sleep(3)
products = driver.find_elements(By.XPATH,'//div[@class="products"]/div')
assert len(products) > 0
for product in products:
    # This is the concept of chaining in selenium, we find element on an already found element
    product.find_element(By.XPATH,'div/button').click()
    time.sleep(3)






driver.close()