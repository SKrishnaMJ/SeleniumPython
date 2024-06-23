import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# locate elements on webpage using id, name, xpath, class and CSS
driver.find_element(By.NAME,"name").send_keys("Sai Krishna M J")
driver.find_element(By.NAME, "email").send_keys("saik@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID, "exampleCheck1").click()

# Select class to handle static dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")


driver.find_element(By.ID,"inlineRadio2").click()

# Xpath Syntax - //tagname[@attribute_name='value'] --> //input[@type='submit']
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

# to pass or fail tests we use assert class
assert "Success" in message

driver.find_element(By.XPATH,"(//input[@name='name'])[2]").clear()

# CSS selectors can also be used to identify #id_name, .class_name



time.sleep(5)
driver.close()