from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="chromedriver.exe")
driver= webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://practicetestautomation.com/practice-test-login/")

input_element =driver.find_element(By.ID, "username")
input_element.send_keys("student")
input_element =driver.find_element(By.ID, "password")
input_element.send_keys("Password123")
input_element =driver.find_element(By.ID, "submit")
input_element.click()

print("loggin successful")

time.sleep(100)
driver.quit()