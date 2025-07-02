from selenium.webdriver.common.by import By

class ResetPasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.ID, "email")
        self.continue_button = (By.CLASS_NAME, "ccbf5f810 c0a334fa0 c8f34b77b cec7560fc c8aea3181")
        self.go_back_button = (By.CLASS_NAME, "c07ad2e24")

    def enter_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def click_go_back(self):
        self.driver.find_element(*self.go_back_button).click()
