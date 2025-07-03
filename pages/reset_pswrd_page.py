from selenium.webdriver.common.by import By

class ResetPasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.ID, "email")
        self.continue_button = (By.XPATH, "//button[@class='ccbf5f810 c0a334fa0 c8f34b77b cec7560fc c8aea3181']")
        self.go_back_button = (By.XPATH, "//button[@class='c07ad2e24 _link-back-to-login c0e6110c2']")

    def enter_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def click_continue(self):
        continueBtn = self.driver.find_element(*self.continue_button)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", continueBtn)
        continueBtn.click()

    def click_go_back(self):
        backBtn = self.driver.find_element(*self.go_back_button)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", backBtn)
        backBtn.click()
