
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Login:

    def test_pagetitle(self):
        drver = webdriver.Chrome()
        drver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        if drver.title=="OrangeHRM":
            assert True
        else:
            assert False
    #
    def test_login_01(self):
        driver=webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # time.sleep(3)
        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

        try:
            driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
            print("test_login_01 is passed")
            driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
            driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
            print("test_login_01 is Completed")
            assert True
        except:
            print("test_login_01 is Failed")
            print("test_login_01 is Completed")
            assert False

    # def test_addemp_02(self):
    #     driver=webdriver.Chrome()
    #     driver.implicitly_wait(3)
    #     driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #     # time.sleep(3)
    #     driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    #     driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
    #     driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #
    #     driver.find_element(By.XPATH,"//span[normalize-space()='PIM']").click()
    #     driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()
    #     driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Ruturaj")
    #     driver.find_element(By.XPATH,"//input[@placeholder='Middle Name']").send_keys("Sadashiv")
    #     driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Pawar")
    #     driver.find_element(By.XPATH,"//button[@type='submit']").click()
    #
    #     print(driver.find_element(By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']").text)
    #
    #     try:
    #         driver.find_element(By.XPATH,
    #                             "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']")
    #         driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
    #         driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
    #         print("test_addemp_02 is Passed")
    #         print("test_addemp_02 is Completed")
    #         assert True
    #     except:
    #         print("test_addemp_02 is Failed")
    #         print("test_addemp_02 is Completed")
    #         assert False

    def test_addemp_02(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # time.sleep(3)
        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
        driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Ruturaj")
        driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys("Sadashiv")
        # driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Pawar")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        try:
            driver.find_element(By.XPATH,
                                "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']")
            driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
            driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
            print("test_addemp_02 is Passed")
            print("test_addemp_02 is Completed")
            addemp = True
        except:
            print("test_addemp_02 is Failed")
            print("test_addemp_02 is Completed")
            addemp = False

        if addemp == True:
            assert True
        else:
            assert False

        # we can addemp=True and addemp=False instead of assert true and false.in assert, if the first assert
        # condition is satisfied it will stop execution of the remaining code of that test case, means it not check
        # assert false condition, but in addemp=True and addemp=false case it will execute both conditions. but we
        # use tag in try and except and use assert in if else condition for good practice because it checks both true
        # and false condition in try and except, and after that we use assert.
