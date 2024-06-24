import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

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

driver.find_element(By.CSS_SELECTOR, 'img[alt="Cart"]').click()
driver.find_element(By.XPATH,'//button[text()="PROCEED TO CHECKOUT"]').click()
driver.find_element(By.CSS_SELECTOR, '.promoCode').send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, '.promoBtn').click()

# we are using the explicit wait by importing the class WebDriverWait() and creating its object
wait = WebDriverWait(driver, 10)

# Here we wait until the element is visible on the screen, be privy of brackets inside presence_of_element
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'.promoInfo')))
print(driver.find_element(By.CSS_SELECTOR,'.promoInfo').text)






driver.close()