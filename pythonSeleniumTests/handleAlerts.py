import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID, "name").send_keys("CR7")
driver.find_element(By.ID, "alertbtn").click()
time.sleep(3)


# to handle a javascript or java popup/alert that cant be inspected we need to switch to alert mode from driver
alert = driver.switch_to.alert
assert "CR7" in alert.text
alert.accept()

driver.find_element(By.ID, "confirmbtn").click()
time.sleep(2)
confirm = driver.switch_to.alert
confirm.dismiss()




time.sleep(3)
driver.close()