# this is for creating a test case using pageObject

from selenium.webdriver.common.by import By

from pageObject import Add_Emp
from pageObject.Add_Emp import Addemp
from pageObject.LoginPage import loginpage


class Test_Addemp:

    def test_addemp_02(self, setup):
        self.driver = setup

        self.ae = Addemp(self.driver)
        self.lp = loginpage(self.driver)

        self.lp.Enter_Username("Admin")
        self.lp.Enter_Password("admin123")
        self.lp.Click_Login()

        self.ae.Click_PIM()
        self.ae.Click_Add()
        self.ae.Enter_Firstname("Ruturaj")
        self.ae.Enter_Middlename("sadashiv")
        self.ae.Enter_Lastname("Pawar")
        self.ae.Click_Save_buttton()

        if self.ae.Addemp_success() == True:
            self.driver.save_screenshot("D:\\OrangeHRMrevision\\Screenshots\\AddEmpSuccess.png")
            self.lp.Click_MenuButton()
            self.lp.Click_Logout()
            assert True

        else:
            self.driver.save_screenshot("D:\\OrangeHRMrevision\\Screenshots\\AddEmpFail.png")
            assert False
