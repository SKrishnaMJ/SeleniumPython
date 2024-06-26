import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()

# .window_handles retrieves all the names of the windows(tabs) opened an returns the list with 0th
# index having the name of the window we are currently on
opened = driver.window_handles

# .switch_to.window() here switches to the new window that has the name got from the opened list from the above step
driver.switch_to.window(opened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()

# switching back to the parent window from where we started our automation
driver.switch_to.window(opened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text

driver.close()