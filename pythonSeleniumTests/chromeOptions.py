import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


chromeOptions = webdriver.ChromeOptions()

# All kinda options available and more
# options.add_argument("no-sandbox")
# options.add_argument("--disable-gpu")
# options.add_argument("--window-size=800,600")
# options.add_argument("--disable-dev-shm-usage")
# options.set_headless()

chromeOptions.add_argument("--ignore-certificate-errors")
chromeOptions.add_argument("--start-maximized")
# chromeOptions.add_argument("headless")

driver = webdriver.Chrome(options=chromeOptions)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

print(driver.title)

driver.close()
