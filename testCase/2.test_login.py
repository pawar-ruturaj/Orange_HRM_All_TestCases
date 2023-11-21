
# in above test cases, we observed that some functionality like login functionality we use repeatedly in each test
#  case, so to hande such condition we create new python file conftest where we store common files, if we change in
# conftest that changes apply on all file/testcase.

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Login:

    def test_pagetitle(self,setup):
        self.driver = setup

        if self.driver.title=="OrangeHRM":
            assert True
        else:
            assert False

    def test_login_01(self,setup):
        self.driver = setup

        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

        try:
            self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
            print("test_login_01 is passed")
            self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
            self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
            print("test_login_01 is Completed")
            assert True
        except:
            print("test_login_01 is Failed")
            print("test_login_01 is Completed")
            assert False

    def test_addemp_02(self,setup):
        self.driver = setup

        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Ruturaj")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys("Sadashiv")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Pawar")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        try:
            self.driver.find_element(By.XPATH,
                                "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']")
            self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
            self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
            print("test_addemp_02 is Passed")
            print("test_addemp_02 is Completed")
            addemp = True
        except:
            print("test_addemp_02 is Failed")
            print("test_addemp_02 is Completed")
            addemp = False

        if addemp == True:
            assert True
        else:
            assert False