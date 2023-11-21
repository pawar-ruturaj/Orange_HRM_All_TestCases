from selenium.common import NoSuchElementException as Ec
from selenium.webdriver.common.by import By


class loginpage:
    Text_username_XPATH = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]")
    Text_password_XPATH = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[2]/input[1]")
    Click_login_button_XPATH = (By.XPATH, "//button[@type='submit']")
    Click_Menu_button_XPATH = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    Click_logout_button_XPATH = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self,driver):
        self.driver = driver

    def Enter_Username(self,Username):
        self.driver.find_element(*loginpage.Text_username_XPATH).send_keys(Username)

    def Enter_Password(self,Password):
        self.driver.find_element(*loginpage.Text_password_XPATH).send_keys(Password)

    def Click_Login(self):
        self.driver.find_element(*loginpage.Click_login_button_XPATH).click()

    def Click_MenuButton(self):
        self.driver.find_element(*loginpage.Click_Menu_button_XPATH).click()

    def Click_Logout(self):
        self.driver.find_element(*loginpage.Click_logout_button_XPATH).click()

    def Login_status(self):
        try:
            self.driver.find_element(*loginpage.Click_Menu_button_XPATH)
            return True
        except Ec:
            return False
