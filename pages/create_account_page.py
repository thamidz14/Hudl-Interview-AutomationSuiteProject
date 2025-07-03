from selenium.webdriver.common.by import By

class CreateAccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.email_field = (By.ID, "email")
        self.password_field = (By.ID, "password")
        self.create_account_button = (By.XPATH, "//button[@class='ccbf5f810 c0a334fa0 c8f34b77b cec7560fc _button-signup-id']")
        self.continue_account_button = (By.XPATH, "//button[@class='ccbf5f810 c0a334fa0 c8f34b77b cec7560fc cf43f3ba3']")
        
    def open(self, url):
        self.driver.get(url)

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.first_name_field).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name_field).send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_create_account(self):
        createAcctBtn = self.driver.find_element(*self.create_account_button)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", createAcctBtn)
        createAcctBtn.click()

    def click_continue_account(self):
        continueBtn = self.driver.find_element(*self.continue_account_button)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", continueBtn)
        continueBtn.click()
        