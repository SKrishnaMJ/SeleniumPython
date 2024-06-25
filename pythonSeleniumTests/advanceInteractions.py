import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# This class provides the capability to perform advancend actions like double click, right click,
# drag and drop, hover etc etc
action = ActionChains(driver)
driver.implicitly_wait(5)
# This move_to_element is like hovering over an element and for any action we need to do a .perform()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()