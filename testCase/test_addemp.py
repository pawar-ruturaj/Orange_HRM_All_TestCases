# this file for maintain logs.
import time

from selenium.webdriver.common.by import By

from pageObject import Add_Emp
from pageObject.Add_Emp import Addemp
from pageObject.LoginPage import loginpage
from utilities.readproperties import Readconfig
from utilities.Logger import LogGenerator


class Test_Addemp:
    Url = Readconfig.geturl()
    Username = Readconfig.getusername()
    Password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    def test_addemp_02(self, setup):
        self.driver = setup
        self.log.info("test_addemp_02 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this url-->"+self.Url)

        self.ae = Addemp(self.driver)
        self.lp = loginpage(self.driver)

        self.lp.Enter_Username(self.Username)
        self.log.info("Entering username-->" + self.Username)
        self.lp.Enter_Password(self.Password)
        self.log.info("Entering password-->" + self.Password)
        self.lp.Click_Login()
        self.log.info("Click on Login Button")

        self.ae.Click_PIM()
        self.log.info("Click on PIM Button")
        self.ae.Click_Add()
        self.log.info("Click on Add Button")
        self.ae.Enter_Firstname("Ruturaj")
        self.log.info("Entering Firstname")
        self.ae.Enter_Middlename("sadashiv")
        self.log.info("Entering Middlename")
        self.ae.Enter_Lastname("Pawar")
        self.log.info("Entering Lastname")
        time.sleep(1)
        self.ae.Click_Save_buttton()
        self.log.info("Click on Save Button")

        if self.ae.Addemp_success() == True:
            self.driver.save_screenshot("D:\\OrangeHRMrevision\\Screenshots\\AddEmpSuccess.png")
            self.lp.Click_MenuButton()
            self.log.info("Click on MenuButton Button")
            self.lp.Click_Logout()
            self.log.info("Click on Logout Button")
            self.log.info("test_addemp_02 is Passed")
            assert True

        else:
            self.driver.save_screenshot("D:\\OrangeHRMrevision\\Screenshots\\AddEmpFail.png")
            self.log.info("test_addemp_02 is Failed")
            assert False

        self.driver.close()
        self.log.info("test_addemp_02 is completed")
