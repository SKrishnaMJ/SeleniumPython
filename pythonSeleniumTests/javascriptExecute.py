import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chromeOptions)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# this below command is used to execute a javscript command on the browser
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

# takes a screenshot and saves as a .png file in the current project folder
driver.get_screenshot_as_file("screenshot1.png")


driver.close()

