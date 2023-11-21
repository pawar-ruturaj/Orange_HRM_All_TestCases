from selenium.webdriver.common.by import By


# here we create seperate test case for add employee


class Addemp:

    Click_PIM_Button_XPATH = (By.XPATH,"//span[normalize-space()='PIM']")
    Click_Add_Button_XPATH = (By.XPATH,"//button[normalize-space()='Add']")
    Text_Firstname_XPATH = (By.XPATH,"//input[@placeholder='First Name']")
    Text_Middlename_XPATH = (By.XPATH, "//input[@placeholder='Middle Name']")
    Text_Lastname_XPATH = (By.XPATH, "//input[@placeholder='Last Name']")
    Click_Save_Button_XPATH = (By.XPATH, "//button[@type='submit']")
    Success_confirm_XPATH = (By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']")
    Click_AddEmployee_Button_XPATH = (By.XPATH,"//a[normalize-space()='Add Employee']")

    def __init__(self, driver):
        self.driver= driver


    def Click_PIM(self):
        self.driver.find_element(*Addemp.Click_PIM_Button_XPATH).click()

    def Click_Add(self):
        self.driver.find_element(*Addemp.Click_Add_Button_XPATH).click()

    def Enter_Firstname(self,firstname):
        self.driver.find_element(*Addemp.Text_Firstname_XPATH).send_keys(firstname)

    def Enter_Middlename(self,middlename):
        self.driver.find_element(*Addemp.Text_Middlename_XPATH).send_keys(middlename)

    def Enter_Lastname(self,lastname):
        self.driver.find_element(*Addemp.Text_Lastname_XPATH).send_keys(lastname)

    def Click_Save_buttton(self):
        self.driver.find_element(*Addemp.Click_Save_Button_XPATH).click()

    def Addemp_success(self):
        try:
            self.driver.find_element(*Addemp.Success_confirm_XPATH)
            return True
        except:
            return False

    def Click_Add_Employee(self):
        self.driver.find_element(*Addemp.Click_AddEmployee_Button_XPATH).click()