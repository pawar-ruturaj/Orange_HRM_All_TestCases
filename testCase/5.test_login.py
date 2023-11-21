# this file for common data.
# we can also save common and repeatedly used data in test cases.we create configuration folder. in that folder,
# we create config.ini file. we create another folder utility, and in that folder we create readproperties.py file.
# and create methods for common files. utilities folder created to store supporting files for your code.

# By using config.ini file and readproperties file rewrite the test case.


import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObject.LoginPage import loginpage
from utilities.readproperties import Readconfig


class Test_Login:
    Url = Readconfig.geturl()
    Username = Readconfig.getusername()
    Password = Readconfig.getpassword()

    def test_pagetitle(self, setup):
        self.driver = setup

        self.driver.get(self.Url)  # changes because of readproperties.

        if self.driver.title == "OrangeHRM":
            assert True
        else:
            assert False

    def test_login_01(self, setup):
        self.driver = setup

        self.driver.get(self.Url)  # changes because of readproperties.

        self.lp = loginpage(self.driver)

        self.lp.Enter_Username(self.Username)  # changes because of readproperties.
        self.lp.Enter_Password(self.Password)  # changes because of readproperties.
        self.lp.Click_Login()

        if self.lp.Login_status() == True:
            self.driver.save_screenshot("D:\\OrangeHRMrevision\\Screenshots\\LoginSuccess.png")
            self.lp.Click_MenuButton()
            self.lp.Click_Logout()
            assert True
        else:
            self.driver.save_screenshot("D:\\OrangeHRMrevision\\Screenshots\\LoginFail.png")
            assert False
