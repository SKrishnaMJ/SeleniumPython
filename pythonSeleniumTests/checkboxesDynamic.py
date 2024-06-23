import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radioBtn = driver.find_elements(By.XPATH, "//input[@type='radio']")

for btn in radioBtn:
    if btn.get_attribute("value") == "radio3":
        btn.click()
        assert btn.is_selected()
        break

Select(driver.find_element(By.ID, "dropdown-class-example")).select_by_value("option3")


driver.find_element(By.ID,"autocomplete").send_keys("ind")
time.sleep(3)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] div")
for country in countries:
    if country.text == "India":
        print(country.text)
        country.click()
        break









time.sleep(3)
driver.close()