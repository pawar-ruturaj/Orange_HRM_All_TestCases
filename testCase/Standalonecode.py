import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# time.sleep(3)
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

driver.find_element(By.XPATH,"//p[@class='oxd-userdropdown-name']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()
