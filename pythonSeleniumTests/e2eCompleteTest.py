import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chromeOptions)
driver.implicitly_wait(6)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT, "Shop").click()
wait = WebDriverWait(driver,20)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.btn-primary')))
time.sleep(3)
items = driver.find_elements(By.CSS_SELECTOR, "app-card")

for item in items:
    item.find_element(By.CSS_SELECTOR,"div button").click()

driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
driver.find_element(By.CSS_SELECTOR, ".checkbox").click()

driver.find_element(By.ID, 'country').send_keys("ind")
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.suggestions ul li a')))
driver.find_element(By.LINK_TEXT, 'India').click()
driver.find_element(By.CSS_SELECTOR, "[value='Purchase']").click()
successMsg = driver.find_element(By.CSS_SELECTOR, ".alert").text
assert "Success! Thank you" in successMsg


time.sleep(3)
driver.close()