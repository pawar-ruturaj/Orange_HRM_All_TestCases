# this file for maintain screenshots.
# we can also take screenshots of our test cases for proof of testing (POT). we create new directory Screenshots to
# store screenshots.


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
            self.driver.save_screenshot("D:\\OrangeHRMrevision\\Screenshots\\LoginSuccess.png")
            self.lp.Click_MenuButton()
            self.lp.Click_Logout()
            assert True
        else:
            self.driver.save_screenshot("D:\\OrangeHRMrevision\\Screenshots\\LoginFail.png")
            assert False