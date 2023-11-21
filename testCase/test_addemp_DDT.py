# this file for gets data from Excel.
import time

from selenium.webdriver.common.by import By

from pageObject import Add_Emp
from pageObject.Add_Emp import Addemp
from pageObject.LoginPage import loginpage
from utilities import XLutils
from utilities.readproperties import Readconfig
from utilities.Logger import LogGenerator


class Test_Addemp_DDT:
    Url = Readconfig.geturl()
    Username = Readconfig.getusername()
    Password = Readconfig.getpassword()
    log = LogGenerator.loggen()
    path = "D:\\OrangeHRMrevision\\testCase\\TestData\\EmployeeList.xlsx"  # we create variable for excel file path.

    def test_addemp_ddt_05(self, setup):
        self.driver = setup
        self.log.info("test_addemp_ddt_05 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this url-->" + self.Url)

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

        self.rows = XLutils.getrowCount(self.path, "Sheet1")
        status_list = []
        for r in range(2, self.rows + 1):
            self.rows = XLutils.getrowCount(self.path, "Sheet1")  # here we give a path of Excel file and sheetname.
            self.FirstName = XLutils.readData(self.path, "Sheet1", r, 2) # get the first name from Excel.
            self.MiddleName = XLutils.readData(self.path, "Sheet1", r, 3) # get middle name from Excel.
            self.LastName = XLutils.readData(self.path, "Sheet1", r, 4) # get the last name from Excel.
            time.sleep(2)
            self.ae.Enter_Firstname(self.FirstName)
            self.log.info("Entering Firstname-->" + self.FirstName)
            self.ae.Enter_Middlename(self.MiddleName)
            self.log.info("Entering Middlename-->" + self.MiddleName)
            self.ae.Enter_Lastname(self.LastName)
            self.log.info("Entering Lastname-->" + self.LastName)
            time.sleep(2)
            self.ae.Click_Save_buttton()
            self.log.info("Click on Save Button")

            if self.ae.Addemp_success() == True:
                self.ae.Click_Add_Employee()
                status_list.append("Pass")
                XLutils.writeData(self.path, "Sheet1", r, 5,"Pass") # to write data in Excel
                self.driver.save_screenshot("D:\\OrangeHRMrevision\\Screenshots\\AddEmpSuccess.png")

                self.log.info("test_addemp_ddt_05 is Passed")


            else:
                status_list.append("Fail")
                XLutils.writeData(self.path, "Sheet1", r, 5, "Fail")
                self.driver.save_screenshot("D:\\OrangeHRMrevision\\Screenshots\\AddEmpFail.png")
                self.log.info("test_addemp_ddt_05 is Failed")

        print(status_list)
        self.lp.Click_MenuButton()
        self.log.info("Click on MenuButton Button")
        self.lp.Click_Logout()
        self.log.info("Click on Logout Button")

        if "Fail" not in status_list:
            assert True
        else:
            assert False
        self.driver.close()
        self.log.info("test_addemp_ddt_05 is completed")
