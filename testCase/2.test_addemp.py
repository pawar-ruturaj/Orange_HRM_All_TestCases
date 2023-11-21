# this is for creating a test case using common data by using ini file and readproperties.

from selenium.webdriver.common.by import By

from pageObject import Add_Emp
from pageObject.Add_Emp import Addemp
from pageObject.LoginPage import loginpage
from utilities.readproperties import Readconfig


class Test_Addemp:
    Url = Readconfig.geturl()
    Username = Readconfig.getusername()
    Password = Readconfig.getpassword()

    def test_addemp_02(self, setup):
        self.driver = setup
        self.driver.get(self.Url)

        self.ae = Addemp(self.driver)
        self.lp = loginpage(self.driver)

        self.lp.Enter_Username(self.Username)
        self.lp.Enter_Password(self.Password)
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
