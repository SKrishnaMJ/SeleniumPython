import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client/")

# Using Link Text (we need to first check if there is an "a" tag with a "href" link and then we can use link text to locate an element
driver.find_element(By.LINK_TEXT, "Forgot password?").click()

#using xpath we can do a parent to child traversal to locate an element
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")

# using CSS we can do a parent to child traversal (use :nth-child(2), if there are many children in a tag) to locate an element
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("imlikedatboi12")

driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("imlikedatboi12")

# If an element just has a text and no tags or anything xapth can be written like this using //tagname[text()='text_onwebsite']
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()




time.sleep(4)
driver.close()