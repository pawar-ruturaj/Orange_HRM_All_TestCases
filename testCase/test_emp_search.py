import time

from pageObject.Add_Emp import Addemp
from pageObject.Emp_search import EmployeeSearch
from pageObject.LoginPage import loginpage
from utilities.Logger import LogGenerator
from utilities.readproperties import Readconfig


class Test_emp_Search:
    Url = Readconfig.geturl()
    Username = Readconfig.getusername()
    Password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    def test_emp_search_04(self, setup):
        self.driver = setup
        self.log.info("test_emp_search_04 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this url-->" + self.Url)
        self.lp = loginpage(self.driver)

        self.lp.Enter_Username(self.Username)
        self.log.info("Entering username-->" + self.Username)
        self.lp.Enter_Password(self.Password)
        self.log.info("Entering password-->" + self.Password)
        self.lp.Click_Login()
        self.log.info("Click on Login Button")
        self.ae = Addemp(self.driver)
        self.ae.Click_PIM()
        self.log.info("Click on PIM Button")

        self.se = EmployeeSearch(self.driver)
        self.se.Enter_emp_name("David")
        time.sleep(2)
        self.se.Click_Search()

        if self.se.Search_Result() == True:
            self.log.info("Search Found")
            self.log.info("test_emp_search_04 is Passed")
            self.lp.Click_MenuButton()
            self.log.info("click on Menu button")
            self.lp.Click_Logout()
            self.log.info("click on Logout button")
            assert True

        else:
            self.log.info("No Search Found")
            self.lp.Click_MenuButton()
            self.log.info("click on Menu button")
            self.lp.Click_Logout()
            self.log.info("click on Logout button")
            self.log.info("test_emp_search_04 is Failed")
            assert False
        self.driver.close()
        self.log.info("test_emp_search_04 is completed")