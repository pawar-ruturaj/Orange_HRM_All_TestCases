# we create new folder pageObject.
# here we create page objects. files in pageobject also start with prefix test_.
# if test_ not taken, test case directly run but not run in the terminal.
# we can use pageobject class and its methods in our test cases. any changes in pageobject reflect in test cases.
# because of pageobject test code is minimized, and any changes in code can be done through a page object.

# for good practice, perform logout after each test case execution.

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObject.LoginPage import loginpage  # we are importing loginpage class from pageObject LoginPage.


class Test_Login:

    def test_pagetitle(self, setup):
        self.driver = setup

        if self.driver.title == "OrangeHRM":
            assert True
        else:
            assert False

    def test_login_01(self, setup):
        self.driver = setup

        self.lp = loginpage(self.driver)  # we are using loginpage class from pageobject.

        self.lp.Enter_Username("Admin")
        self.lp.Enter_Password("admin123")
        self.lp.Click_Login()
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        if self.lp.Login_status() == True:
            self.lp.Click_MenuButton()
            self.lp.Click_Logout()
            assert True
        else:
            assert False

    # def test_addemp_02(self, setup):
    #     self.driver = setup
    #
    #     self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    #     self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #
    #     self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
    #     self.driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
    #     self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Ruturaj")
    #     self.driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys("Sadashiv")
    #     self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Pawar")
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #
    #     try:
    #         self.driver.find_element(By.XPATH,
    #                                  "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']")
    #         self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
    #         self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
    #         print("test_addemp_02 is Passed")
    #         print("test_addemp_02 is Completed")
    #         addemp = True
    #     except:
    #         print("test_addemp_02 is Failed")
    #         print("test_addemp_02 is Completed")
    #         addemp = False
    #
    #     if addemp == True:
    #         assert True
    #     else:
    #         assert False

# we create a separate test case for add emp in test_addemp file.by creating pageobject and conftest file.
