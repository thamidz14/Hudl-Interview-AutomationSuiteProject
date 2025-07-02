from selenium.webdriver.common.by import By

class PasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.password_field = (By.ID, "password")
        self.continue_password_button = (By.XPATH, "//button[@class='ccbf5f810 c0a334fa0 c8f34b77b cec7560fc _button-login-password']")
        self.create_account_button = (By.XPATH, "//a[@class='c15c36395 c0e6110c2']")
        self.forgot_password_button = (By.XPATH, "//a[@class='c15c36395 c75090d76 c0e6110c2']")

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_create_account_button(self):
        self.driver.find_element(*self.create_account_button).click()

    def click_forgot_password_button(self):
        self.driver.find_element(*self.forgot_password_button).click()

    def click_continue_password(self):
        self.driver.find_element(*self.continue_password_button).click()
