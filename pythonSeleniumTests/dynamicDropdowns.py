import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)

# We use find_elements becuse there are mutliple values retuned in the dropdown when ind is typed and we need to iterate on each to check and find INDIA
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item']")

for country in countries:
    if country.text == "India":
        country.click()
        break

# Here the get_attribute() retrieves the dynamic value from the DOM. Text method cannot be used, only used when static text is present and visible when the website is loaded
assert "India" in driver.find_element(By.ID,"autosuggest").get_attribute("value")









time.sleep(3)
driver.close()