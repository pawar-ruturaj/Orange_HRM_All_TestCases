# this file for maintain logs.

from pageObject.LoginPage import loginpage
from utilities.readproperties import Readconfig
from utilities.Logger import LogGenerator   # import for maintain log


class Test_Login:
    Url = Readconfig.geturl()
    Username = Readconfig.getusername()
    Password = Readconfig.getpassword()
    log = LogGenerator.loggen()    # to maintain logs.

    def test_pagetitle(self, setup):
        self.driver = setup
        self.log.info("test_pagetitle is started")
        self.log.info("Opening Browser")  # we track activity through logs.
        self.driver.get(self.Url)
        self.log.info("Go to this url-->"+self.Url)

        if self.driver.title == "OrangeHRM":
            self.log.info("Page title is-->"+self.driver.title)
            self.log.info("test_pagetitle is Passed")

            assert True
        else:
            self.log.info("test_pagetitle is Failed")
            assert False
        self.driver.close()
        self.log.info("test_pagetitle is Completed")

    def test_login_01(self, setup):
        self.driver = setup
        self.log.info("test_login_01 is started")
        self.log.info("Opening Browser")

        self.driver.get(self.Url)
        self.log.info("Go to this url-->"+self.Url)

        self.lp = loginpage(self.driver)

        self.lp.Enter_Username(self.Username)
        self.log.info("Entering username-->"+ self.Username)
        self.lp.Enter_Password(self.Password)
        self.log.info("Entering password-->" + self.Password)

        self.lp.Click_Login()
        self.log.info("Click on Login Button")

        if self.lp.Login_status() == True:
            self.driver.save_screenshot("D:\\OrangeHRMrevision\\Screenshots\\LoginSuccess.png")
            self.lp.Click_MenuButton()
            self.log.info("Click on MenuButton Button")
            self.lp.Click_Logout()
            self.log.info("Click on Logout Button")
            self.log.info("test_login_01 is Passed")
            assert True
        else:
            self.driver.save_screenshot("D:\\OrangeHRMrevision\\Screenshots\\LoginFail.png")
            self.log.info("test_login_01 is Failed")
            assert False

        self.driver.close()
        self.log.info("test_login_01 is completed")

        # self.log.debug("debug")
        # self.log.info("info")
        # self.log.warning("warning")
        # self.log.error("error")
        # self.log.critical("critical")

        # uncomment above code and run test case.


