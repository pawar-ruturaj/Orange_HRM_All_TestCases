# this file for parameterized test case where we pass parameters from conftest file.
# when we run this testcase and false parameter given to username and password and it should fail the condition but
# the status of test case is Passed

from pageObject.LoginPage import loginpage
from utilities.readproperties import Readconfig
from utilities.Logger import LogGenerator


class Test_Login_parameter:
    Url = Readconfig.geturl()
    # Username = Readconfig.getusername() we taken username and password from parameters.
    # Password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    def test_login_para_03(self, setup,getDataforlogin):
        self.driver = setup
        self.log.info("test_login_01 is started")
        self.log.info("Opening Browser")

        self.driver.get(self.Url)
        self.log.info("Go to this url-->"+self.Url)

        self.lp = loginpage(self.driver)

        self.lp.Enter_Username(getDataforlogin[0])  # in parameters at index 0 we define username.
        self.log.info("Entering username-->"+ getDataforlogin[0])
        self.lp.Enter_Password(getDataforlogin[1])  # in parameters at index 1 we define password.
        self.log.info("Entering password-->" + getDataforlogin[1])

        self.lp.Click_Login()
        self.log.info("Click on Login Button")

        if self.lp.Login_status() == True:
            if getDataforlogin[2] == "Pass":
                self.driver.save_screenshot("D:\\OrangeHRMrevision\\Screenshots\\LoginSuccess.png")
                self.lp.Click_MenuButton()
                self.log.info("Click on MenuButton Button")
                self.lp.Click_Logout()
                self.log.info("Click on Logout Button")
                self.log.info("test_login_01 is Passed")
                assert True
            else:
                self.log.info("test_login_01 is Failed")
                self.driver.save_screenshot("D:\\OrangeHRMrevision\\Screenshots\\LoginFail.png")
                assert False

        else:
            if getDataforlogin[2] == "Fail":
                assert True
            else:
                self.driver.save_screenshot("D:\\OrangeHRMrevision\\Screenshots\\LoginFail.png")
                self.log.info("test_login_01 is Failed")
                assert False

        self.driver.close()
        self.log.info("test_login_01 is completed")




