import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()

opened = driver.window_handles

driver.switch_to.window(opened[1])
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of(driver.find_element(By.XPATH,"(//div[@class='login-btn'])[1]")))
email = driver.find_element(By.LINK_TEXT,"mentor@rahulshettyacademy.com").text
print(email)
driver.close()

driver.switch_to.window(opened[0])
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys('yessir')
driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "signInBtn").click()

wait.until(expected_conditions.visibility_of(driver.find_element(By.CLASS_NAME,"alert-danger")))
message = driver.find_element(By.CLASS_NAME, "alert-danger").text
print(message)






driver.close()