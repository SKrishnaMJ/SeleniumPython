import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/iframe")

# Here we switch to a frame(a frame is a html code embedded onto the parent HTML)
driver.switch_to.frame('mce_0_ifr')
driver.find_element(By.ID,'tinymce').send_keys("I'm HIM, they call me HIMMY")
# Here we switch back to our parent HTML code
driver.switch_to.default_content()

print(driver.find_element(By.TAG_NAME,"h3").text)

driver.close()