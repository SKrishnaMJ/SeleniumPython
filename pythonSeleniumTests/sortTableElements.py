import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

originalList=[]

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chromeOptions)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.LINK_TEXT,"Top Deals").click()
opened = driver.window_handles
driver.switch_to.window(opened[1])
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
veggieItems = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(1)")
for items in veggieItems:
    originalList.append(items.text)
print(originalList)
sortedList = originalList
print(sortedList)
originalList.sort()
assert sortedList == originalList

driver.close()