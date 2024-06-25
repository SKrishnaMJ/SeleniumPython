import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CLASS_NAME,'search-keyword').send_keys('to')

# sleep is added here even though implicit wait is defined because when a list is being returned,
# there might be an empty list returned as selenium implicit wait does not care about the list contents
# as long as list is returned
time.sleep(3)
actual_list = ["Tomato - 1 Kg", "Potato - 1 Kg"]
l=[]
products = driver.find_elements(By.XPATH,'//div[@class="products"]/div')
assert len(products) > 0
for product in products:

    # This is the concept of chaining in selenium, we find an element on an already found element
    l.append(product.find_element(By.CSS_SELECTOR,"div h4[class='product-name']").text)
    product.find_element(By.XPATH,'div/button').click()
print(l)
assert l == actual_list

driver.find_element(By.CSS_SELECTOR, 'img[alt="Cart"]').click()
driver.find_element(By.XPATH,'//button[text()="PROCEED TO CHECKOUT"]').click()

# sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum=0
for price in prices:
    sum=sum+int(price.text)
print(sum)
totalSum = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == totalSum


driver.find_element(By.CSS_SELECTOR, '.promoCode').send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, '.promoBtn').click()

# we are using the explicit wait by importing the class WebDriverWait() and creating its object
wait = WebDriverWait(driver, 10)

# Here we wait until the element is visible on the screen, be privy of brackets inside presence_of_element
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'.promoInfo')))
print(driver.find_element(By.CSS_SELECTOR,'.promoInfo').text)

disAmt = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print(disAmt)
assert disAmt < totalSum








driver.close()